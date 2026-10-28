---
title: "Hardware requirements for the Built-in Render Pipeline"
category: "General"
source_file: "RenderTech-HardwareRequirements.html"
doc_type: "manual"
---

# Hardware requirements for the Built-in Render Pipeline

## Summary

|  |  |  |   
---|---|---|---|---  
| Win/Mac/Linux | iOS/Android | Consoles  
**Forward rendering** | Yes | Yes | Yes  
Vertex Lit rendering | Yes | Yes | -  
Realtime Shadows | GPU support | GPU support | Yes  
Image Effects | Yes | Yes | Yes  
Programmable **Shaders** | Yes | Yes | Yes  
Fixed Function Shaders | Yes | Yes | -  
  
## Realtime Shadows

Realtime Shadows work on most PC, console & mobile platforms. On Windows (Direct3D), the GPU also needs to support shadow mapping features; most discrete GPUs support that since 2003 and most integrated GPUs support that since 2007. Technically, on Direct3D 10, the GPU should support D16/D24X8 or DF16/DF24 **texture formats**

Mobile shadows (iOS/Android) require OpenGL ES 2.0 and `GL_OES_depth_texture` extension, or OpenGL ES 3.0. Most notably, the extension is **not** present on Tegra 3 and Tegra 4 based Android devices, so shadows do not work there.

## Post-processing Effects

Post-processing effects require render-to-texture functionality, which is generally supported on anything made in this millenium.

## Shaders

You can write programmable or fixed function shaders. Programmable shaders are supported everywhere, and default to Shader Model 2.0 (desktop) and OpenGL ES 2.0 (mobile). You can target higher shader models if you want to add more functionality. Fixed function is supported everywhere except consoles.