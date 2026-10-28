---
title: "XR SDK Display subsystem"
category: "General"
source_file: "xrsdk-display.html"
doc_type: "manual"
---

# XR SDK Display subsystem

The **XR** SDK Display subsystem provides an interface for texture allocation, frame lifecycle, and blocking for cadence.

**Note:** The Unity XR SDK is no longer available as we have focused our investments towards OpenXR.

## Texture allocation

Several device SDKs require that a texture is allocated through the SDK itself rather than the usual graphics APIs. If you use the XR SDK Display subsystem, you no longer need to rely on external **plug-ins** to **blit** or copy into the SDK texture.

The Display subsystem enables a plug-in provider to allocate the texture. Where possible, Unity renders directly to the texture to avoid unnecessary copies. Unity can also allocate the texture for you if needed.

In the following cases, Unity can’t render directly to the texture and instead renders to intermediate textures and then blits or copies to your texture:

  * If image effects are in use, your texture will be last in the chain.
  * On PC with MSAA, Unity renders to a multisampled texture and then resolves into your texture at the end of the **camera** stack.
  * On mobile, with the multisample auto resolve extension, the texture will be implicitly resolved when the texture is flushed or used as a source or destination for any operation other than drawing to it. See `EXT_multisampled_render_to_texture` extension.
  * Deferred rendering, **HDR** , and command buffers cause Unity to render to intermediate textures.
  * If rendering to a subset of the screen, Unity renders to intermediate textures.
  * If the “texture layout” doesn’t match what Unity is rendering to (for example, Unity is rendering each eye to separate textures, but the RenderPass is configured to render to a texture array or a single texture).
  * If the `kUnityXRRenderTextureFlagsLockedWidthHeight` flag is set and renderScale is not 1.0.
  * If the `kUnityXRRenderTextureFlagsWriteOnly` flag is set and Unity needs to read back from the texture.

### MSAA

On both PC and mobile, the engine always resolves to the provider’s texture. The engine performs implicit resolve (on mobiles with multi-sample render to texture extension) or explicit resolve.

On mobile, providers should enable the `kUnityXRRenderTextureFlagsAutoResolve` flag and create their textures with 1 sample.

### sRGB

Use `UnityXRFrameSetupHints.appSetup.sRGB` to check if Unity expects to render to sRGB texture formats. The provider ultimately selects the output **texture format** from the `colorFormat` field of `UnityXRRenderTextureDesc`. If the format is an sRGB type, Unity turns sRGB writes on or off depending on the color space that the active project selects. You should always sample from any sRGB textures with sRGB to linear conversion in your compositor.

### Depth textures

If your SDK needs depth information, you can obtain the **depth buffer** in the same way as the color buffer above. The `nativeDepthTex` value on the `UnityXRRenderTextureDesc` specifies the native resource. By default, Unity tries to share the depth buffer between textures with a similar desc if `nativeDepthTex` is set to `kUnityXRRenderTextureIdDontCare`.

If your SDK does not need depth information, you should set `UnityXRRenderTextureDesc::depthFormat` to `kUnityXRDepthTextureFormatNone` to avoid unnecessary resolves.

### Handling double and triple buffering

During submission (see the Submitting frames in-flight section below), you can specify a different texture ID each frame in order to handle the case where the SDK needs to double- or triple-buffer images that Unity is rendering to. The provider plug-in is responsible for managing the collection of `UnityXRRenderTextureId`s.

## Frame lifecycle

There are two methods responsible for the lifecycle of a frame: `PopulateNextFrameDesc`, which happens right before rendering begins, and `SubmitCurrentFrame`, which happens immediately after rendering has completed. Both methods are called on the graphics thread.

During `PopulateNextFrameDesc`, the display provider is expected to do the following:

  * Wait for cadence (wait until Unity should start submitting rendering commands again). Alternatively, this can be done in `SubmitCurrentFrame`.
  * Acquire the next image and tell Unity what texture IDs to render to next via the `nextFrame` parameter.

During the `SubmitCurrentFrame` method, the display provider is expected to do the following:

  * Submit the last frame in-flight (for example, eye textures or depth textures) to display on the screen.
  * Wait for cadence, as an alternative to waiting during `PopulateNextFrameDesc`.

### Blocking for cadence

To maintain the lowest possible latency and maximal throughput when rendering to an HMD display, you need to ensure precise timing when you obtain poses and submit textures. Each HMD has a native refresh rate that their compositor runs at. Rendering any faster than that rate results in a sub-optimal experience because of mismatched timing or redundant work.

Unity expects the display provider to block, or wait for frame cadence, during the frame lifecycle. Unity starts submitting rendering commands shortly after ‘waking up’ from the blocking call. You should synchronize the wake-up time to your compositor within a particular window. Some SDKs provide a floating wake-up time window based on heuristics. Meta/Oculus calls this the “queue ahead” (see Oculus developer documentation for more information). Valve calls it “running start” (see slides 18 and 19 of this presentation).

Unity waits on the frame lifecycle to complete before it starts submitting pose-dependent graphics commands.

#### Where to wait for cadence

Providers can wait for cadence in either `PopulateNextFrameDesc` or in `SubmitCurrentFrame`.

While Unity submits graphics commands for a frame on the graphics thread, the next frame’s simulation loop is running on the main thread. It contains physics, script logic, etc. `PopulateNextFrameDesc` is called on the graphics thread after all rendering commands have been submitted, and only after the simulation of the next frame and all graphics jobs scheduled on it are complete. One of the graphics job that `PopulateNextFrameDesc` waits for is `SubmitCurrentFrame` for the current frame. This is why it’s valid to wait for cadence in `SubmitCurrentFrame`. Furthermore, Unity doesn’t start rendering until `PopulateNextFrameDesc` is complete.

With these details in mind, there are some trade-offs to waiting for cadence in `SubmitCurrentFrame` as opposed to `PopulateNextFrameDesc`. For example, waiting for cadence in `SubmitCurrentFrame` can cause performance issues if the application schedules expensive graphics jobs during simulation. Because `SubmitCurrentFrame` is scheduled to run after rendering, the graphics jobs that the application scheduled will run after `SubmitCurrentFrame`, but before `PopulateNextFrameDesc`. In this case, the provider is waiting in `SubmitCurrentFrame`, then it wakes up expecting Unity to begin rendering. However, Unity processes the graphics jobs the application scheduled before it calls `PopulateNextFrameDesc`, which in turn allows Unity to start rendering. This delay between waking up for rendering and processing the graphics jobs scheduled in the update method could cause latency. Developers can optimize this by scheduling their graphics jobs after rendering to ensure the graphics jobs are scheduled before `SubmitCurrentFrame`.

While the Provider waiting for cadence in `SubmitCurrentFrame` allows computing graphics jobs to run in parallel to the main thread, waiting for cadence in `PopulateNextFrameDesc` blocks the Unity main thread entirely. This is acceptable because simulation and other graphics jobs have already completed. Problems might occur when the simulation or graphics thread take up far too much time and exceed the device’s target frame rate. This can cause frame rates to be cut in half while `PopulateNextFrameDesc` waits for the next cycle in the cadence.

### Submitting frames in-flight

When Unity calls `SubmitCurrentFrame`, the textures that you’ve set up last frame have been rendered to, or Unity has submitted render commands to the graphics driver to render them. Unity is now done with them and you can pass them on to your compositor.

### Filling out next frame descriptor

After blocking or acquiring the next frame to render to, you must tell Unity which textures to render to in the next frame, and what’s the layout of the render passes (see Render Passes below).

#### Render passes

A `UnityXRRenderPass` can involve a culling pass and a **scene** graph traversal. This is a resource-intensive operation, and you should try to limit the number of times Unity performs it via tricks like single-pass rendering.

Each `UnityXRRenderPass` contains an output texture (which can be a texture array), and output `UnityXRRenderParams` such as view, projection matrices, and the rect to render to or the texture array slice.

For each frame, the display Provider sets up a `UnityXRRenderPass` and fills out the `UnityXRRenderTextureId`s that Unity will render to the next frame.

Use cases for `UnityXRRenderPass` include the following:

  * Two-pass stereo rendering (2 RenderPass x 1 RenderParams)
  * Single-pass stereo rendering (1 RenderPass x 2 RenderParams)

The API supports these additional cases (but Unity might not react correctly right now):

  * **Quad** pass wide FOV stereo rendering (4 RenderPass x 1 RenderParams)
  * Single-pass + wide FOV stereo rendering (1 RenderPass x 2 RenderParams + 2 RenderPass x 1 RenderParams)
  * Foveated rendering: 
    * Two separate textures for each eye (inner and outer)
    * One texture, UV fitting
  * External view scenario (HoloLens BEV, Mayo 3rd eye) (extra RenderPass)
  * Near / far rendering for compositing objects or people in scene (2 RenderPass, different projections, different targets)

It’s safe to make these assumptions:

  * One texture per pass (singlepass is a one texture-array)
  * If single-pass, two pose / projections per pass (or foveated rendering)

**Note:** The Unity project and XR SDK must use the same setting (enabled/disabled) for single-pass rendering, because this setting affects user **shaders**. To check if single-pass rendering is enabled, use `UnityXRFrameSetupHints.appSetup.singlePassRendering`.

#### Culling passes

Two rendering passes can share a culling pass if their `cullingPassIndex`es are set to the same value. The `cullingPassIndex` selects which `UnityXRCullingPass` to use. Culling passes must be filled out in `UnityXRNextFrameDesc`.