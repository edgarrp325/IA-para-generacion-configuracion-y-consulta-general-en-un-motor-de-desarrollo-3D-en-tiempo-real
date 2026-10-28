---
title: "Graphics"
category: "General"
source_file: "class-GraphicsSettings.html"
doc_type: "manual"
---

# Graphics

Use the **Graphics** settings (main menu: **Edit** > **Project Settings** , then select the **Graphics** category) to apply global settings for Graphics.

This section provides documentation on the following groups of properties:

  * Scriptable Render Pipeline Settings
  * Camera Settings
  * Tier Settings
  * Built-in shader settings
  * Always-included Shaders
  * Shader stripping
  * Shader loading
  * Culling settings

## Scriptable Render Pipeline Settings

Allows you to set the default **render pipeline** that Unity uses to render your project. To set a render pipeline based on the Scriptable Render Pipeline, assign the desired Render Pipeline Asset here.

For more information, see How to get, set, and configure the active render pipeline.

## Camera Settings

These properties control various rendering settings.

**Property** | **Function**  
---|---  
**Transparency Sort Mode** | Define the order for rendering objects by their distance along a specific axis. Renderers in Unity are sorted by several criteria, such as their layer number or their distance from the **camera**. This is generally only useful in 2D development: for example, sorting **Sprites**. This is generally only useful in 2D development: for example, sorting **Sprites** by height or along the Y-axis.  
| _Default_ | Sort objects based on the Camera mode.  
| _Perspective_ | Sort objects based on perspective view.  
| _Orthographic_ | Sort objects based on orthographic view.  
| _Custom Axis_ | Sort objects based on the sort mode defined with the **Transparency Sort Axis**.  
**Transparency Sort Axis** | Define a custom **Transparency Sort Mode**.  
  
## Tier Settings

Tier Settings as displayed in the Player settings

In the Built-in Render Pipeline, you can use **Tier settings** to change rendering and shader compilation settings for different types of hardware. For more information, see Graphics tiers.

**Property** | **Function**  
---|---  
**Standard Shader Quality** | Set the quality of the Standard Shader to _High_ , _Medium_ , or _Low_.  
**Reflection Probes Box Projection** | Enable projection for reflection UV mappings on Reflection Probes.  
**Reflection Probes Blending** | Enable blending on Reflection Probes.  
**Detail Normal Map** | Enable Detail Normal Map sampling, if assigned.  
**Enable Semitransparent Shadows** | Enable Semitransparent Shadows.   
This adds or removes the UNITY_USE_DITHER_MASK_FOR_ALPHABLENDED_SHADOWS shader compiler define.  
**Enable Light Probe Proxy Volume** | Enable rendering a 3D grid of interpolated Light Probes.  
**Cascaded Shadows** | Enable using cascaded shadow maps.   
This adds or removes the UNITY_NO_SCREENSPACE_SHADOWS shader compiler define.  
**Prefer 32 bit shadow maps** | Enable 32-bit float shadow map when you are targeting platforms that use DX11 or DX12.  
Most platforms have a fixed shadow map format that you can’t adjust. These vary in format, and can be 16-bit, 24-bit, or 32-bit, and can also be either float- or integer-based. 32-bit shadow maps give higher quality shadows than 16-bit, but use increased memory and bandwidth on the GPU.  
**Note:** To use 32-bit shadow maps, make sure the depth buffer is also set to 32-bit.  
**Use HDR** | Enable High Dynamic Range rendering for this tier.  
**HDR Mode** | Select the format to use for the HDR buffer when **HDR** is enabled for the current Graphics Tier. By default, this is set to _FP16_.  
| _FP16_ | Color **render texture** format, 16-bit floating point per channel.  
| _R11G11B10_ | Color render **texture format**. R and G channels are 11-bit floating point, B channel is 10-bit floating point.  
**Rendering Path** | Choose how Unity should render graphics. Different rendering paths affect the performance of your game, and how lighting and shading are calculated. Some paths are more suited to different platforms and hardware than others.  
_Deferred_ rendering is not supported when using Orthographic projection. If the camera’s projection mode is set to Orthographic, these values are overridden, and the camera always uses _Forward_ rendering. For more information, see Rendering Paths.  
| _Forward_ | The traditional rendering path. This supports all the typical Unity graphics features (normal maps, per-pixel lights, shadows etc.). However under default settings, only a small number of the brightest lights are rendered in per-pixel lighting mode. The rest of the lights are calculated at object vertices or per-object.  
| _Deferred_ | Deferred shading has the most lighting and shadow fidelity, and is best suited if you have many real-time lights. It requires a certain level of hardware support.  
| _Legacy Vertex Lit_ |  Legacy Vertex Lit is the rendering path with the lowest lighting fidelity and no support for real-time shadows. It is a subset of _Forward_ rendering path.  
**Realtime Global Illumination CPU Usage** | The CPU budget you allow Enlighten Realtime Global Illumination to use for lighting calculations at runtime. Increasing this makes the system react faster to changes in lighting at a cost of using more CPU time.  
**Note:** Some platforms allow all CPUs to be occupied by worker threads whereas some enforce maximums. For example, some gaming consoles allow a maximum of 4 CPU cores. For Android devices, if it is a bigLittle architecture, only the little CPUs are used; otherwise the maximum is one less than the total number of CPUs.  
If you use the URP or HDRP render pipelines, you can configure this property in the quality settings.  
| _Low_ | 25% of the allowed CPU threads are used as worker threads.  
| _Medium_ | 50% of the allowed CPU threads are used as worker threads.  
| _High_ | 75% of the allowed CPU threads are used as worker threads.  
| _Unlimited_ | 100% of the allowed CPU threads are used as worker threads.  
  
## Built-in shader settings

Use these settings to specify which shader to use for each of the listed features in the Built-in Render Pipeline.

**Rendering path** | **Shader to use**  
---|---  
**Deferred** | Use with Deferred shading.  
**Deferred Reflection** | Use with Reflection Probes in deferred shading.  
**Screen Space shadows** | Use with cascaded shadow maps for directional lights on PC/console platforms.  
**Motion vectors** | Use for object-based motion vector calculations.  
**Lens Flare** | Use with Lens Flares.  
**Light Halo** | Use with Light Halos.  
  
For each of these features, you can choose which type of Shader to use:

  * **No Support** disables this calculation. Use this setting if you are not using deferred shading. This will save some space in the built game data files.
  * **Built-in Shader** uses Unity’s built-in Shaders to do the calculation. This is the default.
  * **Custom Shader** uses your own compatible Shader to do the calculation. This enables you to do deep customization of deferred rendering.

When you choose **Custom shader** , a **Shader** reference property appears below the feature property where you can set a reference to the Shader you want to use.

## Always Included Shaders

This is a list of shaders for which Unity includes all possible variants in every build. This can be useful if you want to use shaders or variants at runtime that would not otherwise be included in the build; for example, if you use AssetBundles or Addressables that rely on those shaders or variants, or if you use shader keywords to change variants at runtime.

**Warning:** This feature is not recommended for shaders that have a large number of variants, such as the Standard Shader; it can lead to significant runtime and build time performance problems. You should instead create shader variant collections that contain only the variants you need, and include those in your build.

**Note:** This setting overrides shader keyword declaration settings. For each shader in the list, Unity includes all sets of all keywords, even if you use the “shader feature” declaration type.

To add a shader to the list, increase the value in the **Size** property. To remove the last shader in the list, decrease the **Size** property. To remove a shader which is not the last one in the list, you can set the value to **None**.

## Shader stripping

These properties allow you to configure shader variant stripping in your build.

By default, Unity examines the **scenes** in the build and automatically strips shader variants in the build and automatically strips shader variants that are not used in those scenes. However, this can cause problems if you want to use shaders or variants at runtime that would not otherwise be included in the build; for example, if you use AssetBundles or Addressables that rely on those shaders or variants, or if you use shader keywords to change variants at runtime.

**Property** | **Function**  
---|---  
**Lightmap Modes** | Determine the shader variant stripping behavior for lightmap-related shaders.  
| _Automatic_ | Unity examines the scenes in the build and automatically strips variants that are not used in those scenes. This is the default setting.  
| _Custom_ | Choose to manually include or exclude variants for the following lightmap modes:  
  
* **Baked Non-Directional**  
* **Baked Directional**  
* **Realtime Non-Directional**  
* **Realtime Directional**  
* **Baked Shadowmask**  
* **Baked Subtractive**  
**Fog Modes** | Determine the shader variant stripping behavior for shaders that relate to Unity’s built-in fog effect.  
| _Automatic_ | Unity examines the scenes in the build and automatically strips variants that are not used in those scenes. This is the default setting.  
| _Custom_ | Choose to manually include or exclude variants for the following fog modes:  
  
* **Linear**  
* **Exponential**  
* **Exponential Squared**  
**Instancing Variants** | Determine the shader variant stripping behavior for shaders that relate to GPU instancing.  
| _Strip Unused_ | Unity only includes variants for GPU instancing for a given shader if at least one material that uses that shader has **Enable instancing** enabled. This is the default setting.  
| _Strip All_ | Strip all variants for GPU instancing, even if they are being used.  
| _Keep All_ | Include all variants for GPU instancing, even if they are being used.  
  
## Shader loading

These properties allow you to configure how Unity “prewarms” shader variant collections in your application.

For information on prewarming, including important information about graphics API support, see Shader loading: Prewarming shader variants.

**Property** | **Function**  
---|---  
**Renderer Light Probe Selection** | Choose the type of probe Unity uses when a Renderer receives global illumination from Light Probes but is not within the volume of influence (the tetrahedron) of any group of Light Probes. The default, **Find closest Light Probe** , means Unity searches for the nearest Light Probe, which consumes significant system resources. **Renderer Light Probe Selection** provides an alternative. Select **Use Ambient Probe** to make Unity fall back to the Ambient Probe in these situations, which conserves system resources.   
Options: 

  * **Find closest Light Probe**
  * **Use Ambient Probe**

  
**Preloaded shaders** | The shader variant collections to prewarm on application start.  
**Preload shaders after showing first scene** | When Unity prewarms the shader variants specified in **Preloaded shaders**.  
  
If enabled, Unity loads and prewarms them after the first scene has fully loaded. Otherwise, Unity loads and prewarms them before showing the first scene.  
**Preloaded time limit per frame (ms)** | This property determines how Unity prewarms the shader variants specified in **Preloaded shaders** if **Preload shaders after showing first scene** is enabled.  
  
If the value is 0, Unity preloads all shader variants on the next frame after it shows the first scene.  
  
Otherwise, Unity preloads new shader variants over multiple frames after it shows the first scene. In a given frame, Unity prewarms shader variants until it reaches the time limit set in this property. After that, it does not begin prewarming new shader variants until the next frame.  
  
### Tracked shader variants

The Unity Editor can track which shader variants your application uses when it runs. You can use this information to build shader variant collections.

**Control** | **Function**  
---|---  
**Create asset** | Creates a new shader variant collection asset using the currently tracked shader variants.  
**Clear** | Clear tracked shader variants.  
  
## Culling settings

**Property** | **Function**  
---|---  
**Camera-Relative Culling** | Determines whether Unity uses the camera position as the reference point for culling.  
| **Lights** | Use the camera position as the reference point to cull lights instead of the world space origin. Enable **Lights** to reduce flickering if lights are far away from the camera. Refer to Understanding the View Frustum for more information.  
| **Shadows** | Use the camera position as the reference point to cull shadows instead of the world space origin. Enable **Shadows** to reduce flickering if shadows are far away from the camera. Refer to Understanding the View Frustum for more information.  
  
GraphicsSettings