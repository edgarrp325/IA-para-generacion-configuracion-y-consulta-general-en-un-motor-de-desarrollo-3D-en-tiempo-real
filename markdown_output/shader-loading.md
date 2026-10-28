---
title: "How Unity loads and uses shaders"
category: "General"
source_file: "shader-loading.html"
doc_type: "manual"
---

# How Unity loads and uses shaders

Unity loads compiled shaders from your built application in the following way:

  1. When Unity loads a **scene** or a runtime resource, it loads all the compiled **shader** or a runtime resource, it loads all the compiled **shader** variants for the scene or resource into CPU memory.
  2. By default, Unity decompresses all the shader variants into another area of CPU memory. You can control how much memory shaders use on different platforms.
  3. The first time Unity needs to render geometry using a shader variant, Unity passes the shader variant and its data to the graphics API and the graphics driver.
  4. The graphics driver creates a GPU-specific version of the shader variant and uploads it to the GPU.

This approach ensures that Unity and the graphics driver avoid processing and storing all the shader variants on the GPU before Unity needs them. But there might be a visible stall when the graphics driver creates a GPU-specific shader variant for the first time.

Unity caches each GPU-specific shader variant, to avoid another stall when Unity needs the shader variant again.

Unity removes the shader variant completely from CPU and GPU memory when there are no longer any objects that reference the shader variant. 

## Which shaders Unity loads 

Unity only loads compiled shaders that are compatible with the platform’s graphics API, hardware and graphics tier.

If Unity can’t find the shader variant it needs because you or Unity stripped the shader variant from your built application, Unity tries to select a similar shader variant. If Unity can’t find a similar shader variant, it uses the magenta error shader.

You can enable strict shader variant matching to stop Unity trying to select a similar shader variant.

##  How Unity selects a subshader

If a shader variant contains multiple subshaders, Unity tries to select and use a single subshader that’s compatible with all of the following:

  * The platform’s hardware.
  * The current ShaderLab level of detail (LOD).
  * The active **render pipeline**.

Unity searches for the first compatible subshader among the following elements in the following order:

  1. The subshaders in the order they appear in the shader.
  2. The subshaders in any fallback **shader objects** , in the order they appear in the shader objects.

If Unity can’t find a compatible subshader, it uses the magenta error shader.

You can set which subshaders are compatible with which hardware using **ShaderLab** tags. See ShaderLab: assigning tags to a SubShader.

## Prewarming shader variants

To avoid visible stalls at performance-intensive times, Unity can ask the graphics driver to create GPU representations of shader variants before they’re first needed. This is called prewarming.

You can prewarm in the following ways:

  * Prewarm a Shader object or shader variant collection using the Experimental.Rendering.ShaderWarmup API.
  * Prewarm a shader variant collection by using the ShaderVariantCollection.WarmUp API.
  * Prewarm all variants of all Shader objects currently in memory using the Shader.WarmupAllShaders API.

You can also add shader variant collections to the Preloaded shaders section of the Graphics Settings window. Unity uses the `ShaderVariantCollection.WarmUp` API to load and prewarm the shader variant collections when your built application starts.

### Prewarm on DirectX 12, Metal or Vulkan

If you build for DirectX 12, Metal or Vulkan, the graphics driver can only create an accurate GPU representation of a shader variant if it knows the exact vertex data layout and render state. If a prewarmed GPU representation is inaccurate, Unity might still stall when it needs to create the accurate representation.

To create accurate variants and avoid stalling, you should prewarm by rendering Materials off-screen.

You can also:

  * Prewarm a Shader object or shader variant collection using `Experimental.Rendering.ShaderWarmup`, but only if you can provide the vertex data layout and set the render state accurately.
  * Use `ShaderVariantCollection.Warmup` or `Shader.WarmupAllShaders`, which may create inaccurate prewarmed GPU representations because you can’t provide a vertex data layout or render state.

## Control how much memory shaders use

In your built application, Unity stores several ‘chunks’ of compressed shader variant data. Each chunk contains multiple shader variants. When Unity loads a scene at runtime, it loads all the scene’s chunks into CPU memory and decompresses them.

To reduce memory usage on platforms that have limited memory, you can limit the size of chunks and how many decompressed chunks Unity keeps in memory.

To do this, in Player settings, select **Other Settings** > **Shader Variant Loading** and adjust the following settings:

  * Use **Default chunk size (MB)** to set the maximum size of compressed chunks Unity stores in your built application.
  * Use **Default chunk count** to limit how many decompressed chunks Unity keeps in memory. The default is `0`, which means there’s no limit.

See PlayerSettings.SetDefaultShaderChunkCount for more information.

You can use **Override** to override the values for each platform individually. See PlayerSettings.SetShaderChunkCountForPlatform for more information.

You can also use Shader.maximumChunksOverride to override **Default chunk count** at runtime.

## Profiler markers for shader loading

You can use the following **profiler markers** to see shader loading in the Profiler to see shader loading in the Profiler:

  * `Shader.ParseThreaded` and `Shader.ParseMainThread` for Unity loading the shader object from serialized data.
  * `Shader.CreateGPUProgram` for Unity creating a GPU-specific version of a shader variant.

To check when a shader unloads shader variants, search for the `Shader.MainThreadCleanup` profiler marker.