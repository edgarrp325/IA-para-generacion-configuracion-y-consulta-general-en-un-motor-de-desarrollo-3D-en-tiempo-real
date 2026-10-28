---
title: "Post-processing and full-screen effects"
category: "General"
source_file: "PostProcessingOverview.html"
doc_type: "manual"
---

# Post-processing and full-screen effects

Unity provides a number of ****post-processing**** effects and full-screen effects that can greatly improve the appearance of your application with little set-up time. You can use these effects to simulate physical **camera** and film properties, or to create stylised visuals.

This page contains the following information:

  * Render pipeline compatibility
  * Effect availability and location

The images below demonstrate a **Scene** with and without post-processing.

Scene with no post-processing Scene with post-processing

## Render pipeline compatibility

Which post-processing effects are available and how you apply them depend on which render pipeline you are using. A post-processing solution from one render pipeline is not compatible with other render pipelines.

This table contains information about which of Unity’s post-processing solutions are compatible with each of Unity’s render pipelines.

**Render pipeline** | **Post-processing support**  
---|---  
**Built-in Render Pipeline** | The Built-in Render Pipeline does not include a post-processing solution by default. To use post-processing effects with the Built-in Render Pipeline, download the Post-Processing Version 2 package. For information on using post-processing effects in the Built-in Render Pipeline, see the Post-Processing Version 2 documentation.  
**Universal Render Pipeline (URP)** | URP includes its own post-processing solution, which Unity installs when you create a Project using a URP Template. For information on using post-processing effects in URP, see the URP post-processing documentation.  
**High Definition Render Pipeline (HDRP)** | HDRP includes its own post-processing solution, which Unity installs when you create a Project using an HDRP Template. For information on using post-processing effects in HDRP, see the HDRP post-processing documentation.  
  
**Note:** Post processing stack version 1 is now deprecated and should not be used.

## Effect availability and location

This table contains information on which post-processing effects and full-screen effects are available in Unity’s different post-processing solutions, how to find those effects, and what other effects you can use to achieve a similar result.

In previous versions of Unity, you applied all post-processing effects and full-screen effects in the same way; by adding components to a Camera. In more recent versions of Unity, you can apply these effects in different ways.

Note that Unity implements effects differently depending on the package you are using. This means that effects vary in terms of performance, appearance, and configuration between packages.

**Effect Name** | **Description** | **Available in URP integrated solution?** | **Available in HDRP integrated solution?** | **Available in PPv2 package?**  
---|---|---|---|---  
Ambient Occlusion | The **Ambient Occlusion** effect darkens the areas in your scene that are not exposed to ambient lighting. | Yes   
  
See Universal Render Pipeline: Ambient Occlusion    
  
You can also apply Ambient Occlusion as part of your baked lighting. For more information, see Baked Ambient Occlusion | Yes   
  
Choose from SSAO using a Volume Override, or Ray-Traced Ambient Occlusion   
  
You can also apply per-Material Ambient Occlusion   
  
You can also apply Ambient Occlusion as part of your baked lighting. For more information, see Baked Ambient Occlusion | Yes   
  
See Post Processing: Ambient Occlusion   
You can also apply Ambient Occlusion as part of your baked lighting. For more information, see Baked Ambient Occlusion  
Anti-aliasing | The **Anti-aliasing** effect softens the appearance of edges in your scene.   
Depending on your render pipeline, you can use MSAA (hardware anti-aliasing), or FXAA, SMAA, or TAA (anti-aliasing post-processing effects) | Yes   
  
FXAA and SMAA can be enabled in the Camera component   
  
You can also configure MSAA (hardware anti-aliasing) in Quality Settings | Yes   
  
FXAA, SMAA, and TAA are implemented in **Project Settings > Frame Settings > HDRP Default Settings**; see Anti-aliasing in the High Definition Render Pipeline  
  
You can also configure MSAA (hardware anti-aliasing) in the HDRP Asset - see Anti-aliasing in the High Definition Render Pipeline. | Yes   
  
For FXAA, SMAA, and TAA, see Post Processing: Anti-aliasing   
  
You can also configure MSAA (hardware anti-aliasing) in Quality Settings  
Auto Exposure | The **Auto Exposure** effect dynamically adjusts the exposure of an image to match its mid-tone. | No | Yes   
  
In High Definition Render Pipeline: Exposure Volume Override, when **Mode** is set to **Automatic** | Yes   
  
See Post Processing:Auto Exposure  
Bloom | The **Bloom** effect makes bright areas in your image glow. Note that Bloom works differently in each package, and requires different settings; read the documentation for a given package for more information. | Yes   
  
See Universal Render Pipeline: Bloom | Yes   
  
See High Definition Render Pipeline: Bloom | Yes  
  
See Post Processing: Bloom  
Channel Mixer | The **Channel mixer** lets you adjust the balance of each input color. | Yes  
  
See Universal Render Pipeline: Channel Mixer | Yes  
  
See High Definition Render Pipeline: Channel Mixer | Yes  
  
See **Channel Mixer** in Post Processing: Color Grading   
Chromatic Aberration | The **Chromatic Aberration** effect disperses colors along the boundaries between dark and light areas of the image. | Yes  
  
See Universal Render Pipeline: Chromatic Aberration | Yes  
  
See High Definition Render Pipeline: Chromatic Aberration | Yes  
  
See Post Processing: Chromatic Aberration  
Color Adjustments | The **Color Adjustments** effect lets you change the overall tone, brightness, and contrast of the final rendered image. | Yes  
  
See Universal Render Pipeline: Color Adjustments | Yes  
  
See High Definition Render Pipeline: Color Adjustments | Yes  
  
See **Tone** in Post Processing: Color Grading  
Color Curves | The **Color Curves** effect lets you adjust specific ranges in hue, saturation, or luminosity. | Yes  
  
See Universal Render Pipeline: Color Curves | Yes  
  
See High Definition Render Pipeline: Color Curves | Yes  
  
See **Grading Curves** in Post Processing: Color Grading  
Fog | The **Fog** effect simulates the look of fog or mist in outdoor environments. | No | Yes  
  
See High Definition Render Pipeline: Fog Volume Override (note that this is not implemented as a full-screen effect or post-processing effect) | Yes  
  
See Post Processing: Deferred Fog  
Depth of Field | The **Depth of Field** effect blurs the background of your image while the objects in the foreground stay in focus. | Yes  
  
See Universal Render Pipeline: Depth of Field  | Yes  
  
See High Definition Render Pipeline: Depth of Field | Yes  
  
See Post Processing: Depth of Field  
Grain | The **Grain** effect overlays film noise onto your image. | Yes  
  
See Universal Render Pipeline: Film Grain | Yes  
  
See High Definition Render Pipeline: Film Grain | Yes  
  
See Post Processing: Grain  
Lens Distortion | The **Lens Distortion** effect simulates distortion caused by the shape of a real-world camera lens. | Yes  
  
See Universal Render Pipeline: Lens Distortion | Yes  
  
See High Definition Render Pipeline: Lens Distortion | Yes   
  
See Post Processing: Lens Distortion  
Lift, Gamma, Gain | The **Lift, Gamma, Gain** effect allows you to perform three-way color grading. | Yes   
  
See Universal Render Pipeline: Lift, Gamma, Gain | Yes   
  
See High Definition Render Pipeline: Lift, Gamma, Gain | Yes  
  
See **Trackballs** in Post Processing: Color Grading  
Motion Blur | The **Motion Blur** effect blurs the image in the direction of the **camera’s** movement | Yes   
  
See Universal Render Pipeline: Motion Blur | Yes  
  
See High Definition Render Pipeline: Motion Blur | Yes  
  
See Post Processing: Motion Blur  
Panini Projection | The **Panini Projection** effect corrects distortion at the edge of an image caused by a wide field of view. | Yes   
  
See Universal Render Pipeline: Panini Projection | Yes   
  
See High Definition Render Pipeline: Panini Projection | No  
Screen Space Reflection | The **Screen Space Reflection** effect creates subtle reflections that simulate wet floor surfaces or puddles. | No | Yes   
  
See High Definition Render Pipeline: Screen Space Reflection | Yes  
  
See Post Processing: Screen Space Reflection  
Shadows Midtones Highlights | The **Shadows Midtones Highlights** effect separately controls the tint and brightness of the shadows, midtones, and highlights in your image | Yes  
  
See Universal Render Pipeline: Shadows, Midtones, Highlights | Yes  
  
See High Definition Render Pipeline: Shadows Midtones Highlights | No  
Split Toning | The **Split Toning** effect maps two different tones in your image to two specific colors. | Yes   
  
See Universal Render Pipeline: Split Toning | Yes  
  
See High Definition Render Pipeline: Split Toning | No  
Tonemapping | The **Tonemapping** effect remaps the values of an image to high dynamic range (HDR) colors | Yes  
  
See Universal Render Pipeline: Tonemapping | Yes  
  
See High Definition Render Pipeline: Tonemapping | Yes  
  
See **Tonemapping** in Post Processing: Color Grading  
Vignette | The **Vignette** effect darkens the edges of an image | Yes  
  
See Universal Render Pipeline: Vignette | Yes  
  
See High Definition Render Pipeline:Vignette | Yes  
  
See Post Processing: Vignette  
White Balance | The **White Balance** effect preserves the white areas in your image and balances other tones around the white areas | Yes  
  
See Universal Render Pipeline: White Balance | Yes  
  
See High Definition Render Pipeline: White Balance | Yes  
  
**See White balance** in Post Processing: Color Grading  
  
## Additional resources and examples

  * 📖 **E-Book** : Recipes for popular visual effects using the Universal Render Pipeline
  * 📖 **E-Book** : Lighting and environments in the High Definition Render Pipeline (Unity 2022 LTS)
  * 📺 **Video** : 20 advanced 2D shader effects - part 1
  * 📺 **Video** : 20 advanced 2D shader effects - part 2