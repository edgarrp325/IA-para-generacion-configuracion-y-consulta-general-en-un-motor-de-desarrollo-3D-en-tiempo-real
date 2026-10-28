---
title: "The Progressive Lightmapper"
category: "General"
source_file: "progressive-lightmapper.html"
doc_type: "manual"
---

# The Progressive Lightmapper

The Progressive Lightmapper is a fast path-tracing-based lightmapper system that provides baked **lightmaps** and **Light Probes** and **Light Probes** with progressive updates in the Editor. It requires non-overlapping UVs with small area and angle errors, and sufficient padding between the charts.

The Progressive Lightmapper takes a short preparation step to process geometry and instance updates, and generates the G-buffer and chart masks. It then produces the output immediately and progressively refines it over time for a much-improved interactive lighting workflow. Additionally, baking times are much more predictable because the Progressive Lightmapper provides an estimated time while it bakes.

The Progressive Lightmapper also bakes **global illumination** (GI) at the lightmap resolution for each texel individually, without upsampling schemes or relying on any irradiance caches or other global data structures. This makes it robust and allows you to bake selected portions of lightmaps, which makes it faster for you to test and iterate on your **Scene** (GI) at the lightmap resolution for each texel individually, without upsampling schemes or relying on any irradiance caches or other global data structures. This makes it robust and allows you to bake selected portions of lightmaps, which makes it faster for you to test and iterate on your **Scene**.

For an in-depth video showing the interactive workflow, see Unity’s video walkthrough: In Development - Progressive Lightmapper (YouTube).

## The Progressive CPU Lightmapper and the Progressive GPU Lightmapper (preview)

You can choose between two backends for the Progressive Lightmapper. The Progressive CPU Lightmapper backend is a backend for the Progressive Lightmapper that uses your computer’s CPU and system RAM. The Progressive GPU Lightmapper is a backend for the Progressive Lightmapper that uses your computer’s GPU and VRAM.

Note that the Progressive GPU Lightmapper is a preview feature in active development, and is subject to change. For information on the Progressive GPU Lightmapper backend, see the Progressive GPU Lightmapper (preview).

## Render pipeline support

See render pipeline feature comparison for more information about support for the Progressive Lightmapper across **render pipelines**

## Platform compatibility

The Apple silicon version of the Unity Editor is not compatible with the CPU Progressive Lightmapper. However, it is compatible with the Progressive GPU Lightmapper.

## Using the Progressive Lightmapper

To use the Progressive Lightmapper:

  1. Go to **Window** > **Rendering** > **Lighting**
  2. Navigate to **Lightmapping Settings**
  3. Set **Lightmapper** to **Progressive CPU** or **Progressive GPU**

You can perform many of the functions available in this window via **scripts** , using the LightmapEditorSettings and Lightmapping APIs.

## Settings

This page lists settings specific to the Progressive Lightmapper. See Lightmapping using Enlighten for settings specific to **Enlighten**

**Setting** | **Description**  
---|---  
**Lightmapper** | Use this to specify which internal lighting calculation software to use to calculate lightmaps in the Scene. The options visible in the user interface by default are:  
  

  * Progressive CPU
  * Progressive GPU

The default value is **Progressive CPU**. See Lightmapping using Enlighten Baked Global Illumination to find out how to make Enlighten Baked Global Illumination (deprecated in 2022.2 and absent in 2023.1) available for light baking.  
**Progressive Updates** | Enable this to make the Progressive Lightmapper apply changes to the texels that are currently visible in the **Scene View** , then apply changes to the out-of-view texels.  
**Multiple Importance Sampling** | Enable this to use multiple importance sampling for sampling the environment. This generally leads to faster convergence when generating lightmaps, but can lead to noisier results in certain low frequency environments. This is disabled by default.  
**Direct Samples** | The number of samples (paths) shot from each texel. This setting controls the number of samples Progressive Lightmapper uses for direct lighting calculations. Increasing this value can improve the quality of lightmaps, but increases the baking time.  
**Indirect Samples** | The number of samples (paths) shot from each texel. This setting controls the number of samples Progressive Lightmapper uses for indirect lighting calculations. For some Scenes, especially outdoor Scenes, 100 samples should be enough. For indoor Scenes with emissive geometry, increase the value until you see the result you want.  
**Environment Samples** | The Environment Samples property determines the total number of environment rays that Unity fires toward the skybox to gather light directly. Unity fires these rays from the lightmap texel or light probe position depending on the context. The default value is 500. Higher values might yield smoother results, but at the cost of increased bake times.  
  
In Scenes with HDR skyboxes, more samples are often needed to reduce noise in the final lightmap or probe. Scenes with skyboxes that include bright singularities (such as the sun) or high-frequency details with significant contrast (such as backlit clouds) also benefit from a higher number of samples.  
**Light Probe Sample Multiplier** | Controls how many samples are used for Light Probes as a multiplier of the sample values above. Higher values improve the quality of Light Probes, but they will take longer to bake. To enable this feature, go to **Project Settings > Editor** and disable **Use legacy Light Probe sample counts.** The default value is 4.  
**Bounces** | Use this value to specify the number of indirect bounces to do when tracing paths. For most Scenes, two bounces is enough. For some indoor Scenes, more bounces might be necessary.  
**Max Bounces** | The maximum number of bounces you want the Progressive Lightmapper to include in indirect lighting calculations.   
  
Default value: 2. Range: 0–100.   
  
Values of up to 10 are suitable for most Scenes. Values higher than 10 might lead to significantly longer bake times.  
  
Each bounce increases the computational resources needed to bake your scene. Use higher bounce values for indoor Scenes, and lower bounce values for outdoor Scenes and those with many bright surfaces.  
  
  
**Filtering** | Configure the way the Progressive Lightmapper applies post-processing to lightmaps to limit noise. For lightmap post-processing, the lightmap is split into **Direct** , **Indirect** and **Ambient Occlusion** targets that Unity applies post-processing to individually, before it composites them together into a single lightmap.  
  
\- **Direct** : Any light that arrives directly from a Light to a sensor (usually the Camera).  
\- **Indirect** : Any light that arrives indirectly from a Light to a sensor. This most commonly applies to light that reflects off other GameObjects.  
\- **Ambient Occlusion** : Any ambient light that the lighting system calculates.  
| **None** | Select this to use no filter or denoising for the lightmap.  
| **Auto** | Select this to use a platform-dependent preset for post-processing the lightmap.   
**If your development machine fulfils the requirements to run OptiX** (the NVIDIA OptiX AI-Accelerated Denoiser), the Progressive Lightmapper uses the denoiser with a Gaussian filter that has a 1-texel radius for all targets.  
**If your development machine cannot run OptiX** , the Progressive Lightmapper falls back to **OpenImageDenoise**.  
| **Advanced** | Select **Advanced** to manually configure options for each type of lightmap target. The targets types are **Direct** , **Indirect** and ****Ambient Occlusion****. For more information, see Advanced Filtering settings, below.  
  
## Advanced Filtering settings

Set **Filtering** to **Advanced** to manually configure options for each type of lightmap target. The target types are:

  * **Direct** : Any light that arrives directly from a Light to a sensor (usually the Camera).
  * **Indirect** : Any light that arrives indirectly from a Light to a sensor. This most commonly applies to light that reflects off other **GameObjects**.
  * **Ambient Occlusion** : Any **ambient light** that the lighting system calculates.

**Setting** | **Description**  
---|---  
**Denoiser** | Select a denoiser to use for the lightmap target. The options are:  
  
**Optix** : The NVIDIA Optix denoiser is an AI accelerated denoiser that reduces noise in baked lightmaps. It requires an NVIDIA GeForce, Quadro, or Tesla GPU with Maxwell or newer generation architecture, using driver version R495.89 or above. Optix is only supported on Windows.  
**RadeonPro** : The RadeonPro denoiser is an AI accelerated denoiser that reduces noise in baked lightmaps. It requires an OpenCL capable GPU with 4GB+ VRAM.  
\- **OpenImageDenoise** : The Intel Open Image denoiser is an AI accelerated denoiser that reduces noise in baked lightmaps.  
\- **None** : Do not use a denoiser.  
**Filter** | Select a filter to use for the lightmap target:  
\- **Gaussian:** Select this to use a Gaussian filter for the lightmap target. The Gaussian filter applies a bilateral Gaussian filter on the lightmap. This blurs the lightmap and reduces the visible noise.  
\- **A-Trous:** Select this to use an A-Trous filter for the lightmap target. The A-Trous filter minimizes the amount of blur while it removes visible noise in the lightmap.  
\- **None** _:_ Select this to disable all filtering for the lightmap target.  
**Radius** | This option is only available when **Filter** is set to **Gaussian**. Use the **Radius** value to set the radius of the Gaussian filter kernel in texels. A higher **Radius** increases the blur strength and reduces the perceptible noise, but might cause detail to be lost in the lighting.  
**Sigma** | This option is only available when **Filter** is set to **A-Trous**. Use the **Sigma** value to adjust how much to preserve detail or blur the lighting. A higher **Sigma** increases the blur strength and reduces the perceptible noise, but might cause detail to be lost in the lighting.  
  
## Statistics

The panel below the **Auto Generate** and **Generate Lighting** options shows statistics about the lightmapping, including:

  * The number of lightmaps that Unity has created
  * **Memory Usage:** The amount of memory required for the current lightmapping.
  * **Occupied Texels** : The number of texels that are occupied in lightmap UV space.
  * **Lightmaps in view** : The number of lightmaps in the Scene view.
  * **Lightmaps not in view** : The number of lightmaps that are out of view. 
    * **Converged** : All calculations for these lightmaps are complete.
    * **Not Converged** : Baking is still in progress for these lightmaps.
  * **Bake Performance** : The number of rays per second. If this is low (that is, less than 2) you should adjust your settings or your hardware to process more light rays at a time.

## During baking

Progressive Lightmapper provides options to monitor and stop the bake while it is in progress, if you need to.

### ETA

The progress bar that appears while Unity is baking the lightmap provides an “estimated time of arrival” (displayed as **ETA**). This is the estimated time in seconds for the current bake to complete. This allows for much more predictable baking times, and allows you to quickly learn how much time baking takes with your current lighting settings.

### Force Stop

During manual baking, click **Force Stop** at any time to halt the baking process. This allows you to stop the process as soon as you see results that look good.

## Disabling the default environment contribution

Unity automatically generates an ambient probe and a default Reflection Probe to ensure that environment lighting affects your scene and the GameObjects in it by default.

To disable the environment contribution in the lighting result for a scene or GameObject that does not have manually created light maps and Light Probes, disable the default **Reflection Probe** and the ambient probe. For more information, see Disabling the SkyManager.