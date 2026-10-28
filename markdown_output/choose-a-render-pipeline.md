---
title: "Choose a render pipeline"
category: "General"
source_file: "choose-a-render-pipeline.html"
doc_type: "manual"
---

# Choose a render pipeline

It’s important to choose the right Unity render pipeline for your project when you’re early in development.

Different **render pipelines** have different capabilities and perform differently, so they work best for different games, applications, and platforms.

It can be very time-consuming to switch a project from one render pipeline to another, especially if the project is far along in development. Different render pipelines use different **shaders** and might not have the same features.

The table shows some high-level differences between the pipelines to help you choose the right pipeline for your project at the start.

**Feature** | **Built-In Render Pipeline** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)**  
---|---|---|---  
Target uses | Projects that need rendering scalability across all platforms.  
  
2D and 3D projects. | Projects that need rendering scalability across all platforms, especially tile-based deferred rendering (TBDR) platforms, and untethered VR platforms.  
  
Projects that need to extend and customize the rendering pipeline.  
  
2D and 3D projects. | Projects that need photorealism and high-fidelity rendering on high-end platforms  
  
3D projects  
Platform support | Supports all Unity-supported platforms  | Supports all Unity-supported platforms  
  
Focuses on efficiency on tile-based deferred rendering (TBDR) platforms, and untethered VR platforms | Supports desktop, Xbox and PlayStation platforms  
  
Focuses on efficiently using advanced GPU hardware capabilities such as async compute shaders, and ray tracing if the hardware supports it.   
Source code access | Mostly C++  
  
Private access by purchasing source code access | Mostly C#  
  
Public access to the URP source code on GitHub. You can also create a custom pipeline using URP as a base  
  
Easier to read, change, and extend the source code than the Built-In Render Pipeline | Mostly C#  
  
Public access to the HDRP source code on GitHub. You can also create a custom pipeline using HDRP as a base  
  
Easier to read, change, and extend the source code than the Built-In Render Pipeline  
Pipeline extension | The API and injection points the pipeline provides  | The API and injection points the pipeline provides, or you can modify the publicly available source code  
  
Easier to extend than the Built-In Render Pipeline | The API and injection points the pipeline provides, or you can modify the publicly available source code  
  
Easier to extend than the Built-In Render Pipeline, but more difficult than URP because HDRP is complex and has advanced features  
Customization through artist tooling |  Shader Graph, which you can use to customize shading, materials, and screen space effects  
  
Shader Graph doesn’t receive updates for Built-In Render Pipeline support, aside from bug fixes for existing features   
  
Built-in Particle System, which you can use to customize visual effects. Limited customization |  Shader Graph, which you can use to customize shading, materials, and screen space effects   
  
Built-in Particle System, which you can use to customize visual effects.Limited customization   
  
VFX Graph, which you can use to design visual effects, from simple common particle behaviors to complex simulations running on the GPU.  |  Shader Graph, which you can use to customize shading, materials, and screen space effects   
  
Built-in Particle System, which you can use to customize visual effects. Limited customization  
  
VFX Graph, which you can use to design visual effects, from simple common particle behaviors to complex simulations running on the GPU.   
Customization through hand-coded shaders  | HLSL shaders and surface shaders | HLSL shaders, and URP shaders in the source code that you can customize | HLSL shaders, and HDRP shaders in the source code that you can customize  
  
Hand-coded shaders are recommended for advanced users only, because HDRP shaders are complex and have advanced features  
Lighting | Designed for both realistic and stylized lighting  
  
Basic physically-based rendering (PBR)  
  
Easier to customize for custom lighting models such as cel shading | Designed for both realistic and stylized lighting  
  
Basic PBR, and some advanced PBR such as clear coat  
  
Easier to customize for custom lighting models such as cel shading | Focuses on photorealism and physically accurate lighting with built-in support for physical light units  
  
Basic and advanced PBR. For example clear coat, skin, hair, eyes, subsurface scattering and water  
  
Advanced screen space and volumetric effects  
  
Harder to customize for custom lighting models such as cel shading  
Performance | Supports static batching and dynamic batching | Supports static batching and dynamic batching   
  
Advanced draw call batching with the Scriptable Render Pipeline (SRP) Batcher   
  
Compatible with the BatchRenderer Group API, and Entities | Supports static batching  
  
Advanced draw call batching with the Scriptable Render Pipeline (SRP) Batcher   
  
Compatible with the BatchRenderer Group API, and Entities  
  
Refer to Render pipeline feature comparison for detailed information about which pipeline is compatible with which features, to help you choose the right pipeline for your project.

## Set up a render pipeline

To create a new project with one of the render pipelines, use the Unity Hub. Refer to Manage your templates for more information.

To convert a project from the Built-In Render Pipeline to URP or HDRP, refer to the following:

  * URP Render Pipeline Converter
  * HDRP Pipeline Wizard

After you choose a rendering pipeline, you can Choose a lighting setup.

### Extend a render pipeline

If you have advanced rendering knowledge and you’re familiar with C#, you can extend URP or HDRP to add custom features. Refer to Create a custom render pipeline for more information.

## Additional resources

  * Creating Believable Visuals tutorial for the Built-In Render Pipeline