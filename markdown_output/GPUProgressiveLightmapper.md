---
title: "The Progressive GPU Lightmapper (preview)"
category: "General"
source_file: "GPUProgressiveLightmapper.html"
doc_type: "manual"
---

# The Progressive GPU Lightmapper (preview)

**Note:** This is a preview feature and is subject to change. If you have **Scenes** that use this feature, you might need to update them in a future release. Do not rely on this feature for full-scale production until it is officially released.

The **Progressive GPU**Lightmapper**** is a backend for the Progressive Lightmapper which uses your computer’s GPU and Dedicated Video Ram (VRAM) to generate baked **lightmaps** is a backend for the Progressive Lightmapper which uses your computer’s GPU and Dedicated Video Ram (VRAM) to generate baked **lightmaps** and **Light Probes** and **Light Probes**.

## Hardware and software requirements

In order to use the Progressive GPU Lightmapper, your computer must meet these minimum specifications:

  * At least one GPU with OpenCL 1.2 support
  * At least 4GB of VRAM dedicated to that GPU
  * A CPU that supports SSE4.1 instructions

If the Scene you are baking requires more VRAM than is available on the designated GPU, bake times can significantly increase. See Performance for information to help you reduce the time it takes to bake your Scene.

The Progressive GPU Lightmapper does not support CPU OpenCL devices.

## Performance

The Progressive GPU Lightmapper bakes faster than the Progressive CPU Lightmapper, unless lightmapper tiling is active.

However, the specifications of the GPU you use to bake and the amount of VRAM dedicated to that GPU both influence your experience of the lightmapper’s performance.

Other applications competing for GPU resources also have an impact on baking performance. Depending on your hardware vendor, reductions in the amount of VRAM available to Unity can slow down the bake, cause it to fail, or even result in the Progressive GPU Lightmapper falling back to the CPU if the GPU cannot meet minimum memory requirements. Closing other applications while you are working with this functionality can improve stability and performance.

In order to achieve results of the same quality as the Progressive CPU Lightmapper, the Progressive GPU Lightmapper needs up to four times more indirect light samples. The Progressive CPU Lightmapper uses an approach called branched path tracing, which launches more light rays at each bounce. The branched path tracing approach is not suitable for GPUs.

Unity provides a spreadsheet to help you determine how much memory the Progressive GPU Lightmapper needs to bake your scene. For more information see the Progressive GPU Lightmapper Memory Spreadsheet .

## Preventing baking speed slowdowns caused by lightmapper tiling

The Progressive GPU Lightmapper includes a feature called lightmapper tiling. Lightmapper tiling prevents the Progressive GPU Lightmapper from falling back to the Progressive CPU Lightmapper when Unity has used up its GPU memory allocation. Instead, Unity allocates some temporary memory on the CPU, then bakes your lighting in tiles that are sized to match the amount of GPU memory available. Lightmapper tiling is active only when Unity can’t access enough GPU memory to bake the entire lightmap. The Progressive CPU Lightmapper does not include a tiling feature.

When lightmapper tiling is active, progressive updates cease in the **Scene view** and the baking process. However, the **Progressive updates** setting in the Lighting window does not visibly deactivate. Baking a scene when lightmapper tiling is active is slower than baking the same scene without tiling.

It is not possible to disable tiling. However, you can reduce the likelihood of its activation by using the following strategies:

  * Increase the amount of GPU memory available for Unity to use.

  * Disable ambient occlusion. Open the Lighting window (menu: **Window > Rendering > Lighting**). In the Lightmapping Settings interface, disable **Ambient Occlusion**.

  * Bake only indirect light. Set all your light sources to **Realtime** or **Mixed**. Make sure that no light sources are set to **Baked**. If you use the mixed approach, set **Lighting > Mixed Lighting > Lighting mode** to **Baked Indirect**.

  * Reduce the level of anti-aliasing in your project. Navigate to **Project Settings** > **Quality** and choose an option that takes fewer samples. For example, you might switch from **8x Multi Sampling** to **2x Multi Sampling**.

  * Reduce the quality of your lightmaps in your Lightmap Parameters Asset. Open the Lighting window, expand **Lightmapping settings** , and select a lower-resolution option for **Lightmap parameters**.

  * Reduce your lightmap resolution.

  * Use a CPU-based denoiser. To choose a denoiser, open the Lighting window, expand **Lightmapping settings** , set **Filtering** to **Advanced** and then select the denoiser for each type of lightmap target (**Direct** and **Indirect**). Only **OpenImageDenoise** is CPU-based. **RadeonPro** and **Optix** are GPU-based, but **RadeonPro** uses a lot more GPU memory.

## Platform-specific limitations

On macOS it is more difficult to determine how much memory is available. As a result, fallback to CPU is more likely on this platform and it is a best practice to follow instructions for optimizing your bake speed.

## How to optimize your bake speed

There are several ways you can reduce bake times and avoid situations where bakes exceed the VRAM available to the GPU designated for baking.

  * Close other GPU-accelerated applications. GPU-accelerated 2D image editing and 3D modelling software uses VRAM. Turn off accelerated graphics functionality or quit these applications.

  * Switch to a CPU-based denoiser. GPU-based denoisers also use VRAM capacity. Switch to a CPU-based option, like Intel Open Image, which uses system RAM instead.

  * Use Light Probes for smaller **GameObjects**. GameObjects such as debris or small props use up space in lightmaps but might not contribute significantly to the look of a scene. To optimize bake speed, disable **Contribute Global Illumination** for these GameObjects’ Mesh Renderers and light them with Light Probes instead.

  * Designate separate GPUs for rendering and baking. If your computer has more than one GPU, you can designate one for rendering and one for baking. See Configure GPU selection below.

  * Use a lower number of **Anti-aliasing samples**. The default value for this setting in the Lightmap Parameters Asset is 8. When you increase it, Unity uses more VRAM. When you are using a lightmap size of 4096 or above, this can quickly exceed the memory of many consumer GPUs.

## Configure GPU selection 

If you have at least two GPUs, you can specify one GPU for rendering the Scene and another for baking lighting. This might be desirable in cases where there is insufficient VRAM available for the default GPU to both render your scene and bake it using the Progressive GPU Lightmapper.   
To change which GPU Unity uses for baking:   
1\. Open the **Lighting** window (menu: **Window > Rendering > Lighting**).  
2\. Navigate to the **Workflow Settings** section.  
3\. Use the **GPU Baking Device** drop-down menu to select a GPU.