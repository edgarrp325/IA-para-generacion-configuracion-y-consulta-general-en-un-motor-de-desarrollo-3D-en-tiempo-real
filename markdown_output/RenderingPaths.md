---
title: "Rendering paths in the Built-in Render Pipeline"
category: "General"
source_file: "RenderingPaths.html"
doc_type: "manual"
---

# Rendering paths in the Built-in Render Pipeline

Unity’s Built-In **Render Pipeline** supports different rendering paths. A **rendering path** is a series of operations related to lighting and shading. Different rendering paths have different capabilities and performance characteristics. Deciding on which rendering path is most suitable for your Project depends on the type of Project, and on the target hardware.

You can choose the rendering path that your Project uses in the Graphics window, and you can override that path for each Camera

If the GPU on the device running your Project does not support the rendering path that you have selected, Unity automatically uses a lower fidelity rendering path. For example, on a GPU that does not handle **Deferred Shading** , Unity uses **Forward Rendering** , Unity uses **Forward Rendering**.

## Forward Rendering

Forward Rendering is the default rendering path in the Built-in Render Pipeline. It is a general-purpose rendering path.

Real-time lights are very expensive to render in forward rendering. To offset this cost, you can choose how many lights Unity should render per-pixel at any one time. Unity renders the rest of the lights in the **Scene** at lower fidelity: per-vertex, or per-object.

If your project does not use a large amount of real-time lights, or if lighting fidelity is not important to your project, then this rendering path is likely to be a good choice for your project.

For more details see the Forward Rendering page.

## Deferred Shading

Deferred Shading is the rendering path with the most lighting and shadow fidelity in the Built-in Render Pipeline.

Deferred shading requires GPU support, and has some limitations. It does not support semi-transparent objects (Unity renders these using forward rendering), orthographic projection (Unity uses forward rendering for these Cameras), or hardware anti-aliasing (although you can use a post-process effect to achieve similar results). It has limited support for **culling masks** , and treats the Renderer.receiveShadows flag as always true.

If your project has a large number of real-time lights and requires a high level of lighting fidelity, and your target hardware supports deferred shading, then this rendering path might be a good choice for your project.

For more details, including advice on this rendering path’s limitations, see the Deferred Shading page.

## Legacy Vertex Lit

_Legacy Vertex Lit_ is the rendering path with the lowest lighting fidelity and no support for real-time shadows. It is a subset of the Forward rendering path.

For more details see the Vertex Lit page.

## Rendering Path comparison

| **_Deferred_** | **_Forward_** | **_Vertex Lit_**  
---|---|---|---  
**Features** |  |  |   
Per-pixel lighting (normal maps, light cookies) | Yes | Yes | -  
Real-time shadows | Yes | With caveats | -  
**Reflection Probes** | Yes | Yes | -  
Depth & Normal Buffers | Yes | Additional render passes | -  
**Soft Particles** | Yes | - | -  
Semi-transparent objects | - | Yes | Yes  
Anti-Aliasing | - | Yes | Yes  
Light Culling Masks | Limited | Yes | Yes  
Lighting Fidelity | All per-pixel | Some per-pixel | All per-vertex  
**Performance** |  |  |   
Cost of a per-pixel Light | Number of **pixels** it illuminates | Number of pixels * Number of objects it illuminates | -  
Number of times objects are normally rendered | 1 | Number of per-pixel lights | 1  
Overhead for simple Scenes | High | None | None  
**Platform Support** |  |  |   
PC (Windows/Mac) | **Shader** Model 3.0+ & MRT | All | All  
Mobile (iOS/Android) | OpenGL ES 3.0 & MRT, Metal | All | All  
Consoles | XB1, PS4 | All | -