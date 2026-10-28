---
title: "Built-in shaders"
category: "General"
source_file: "shader-built-in.html"
doc_type: "manual"
---

# Built-in shaders

Unity comes with a number of built-in **shaders** that you can use in your projects.

## Render pipeline compatibility

Different **render pipelines** are compatible with different built-in shaders.

**Feature name** | **Built-in Render Pipeline** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP**  
---|---|---|---|---  
**Standard Shader** | Yes | No  
  
Can convert Standard Shader to equivalent on import | No  
  
Can convert Standard Shader to equivalent on import | No  
**Standard Particle Shaders** | Yes | No | No | No  
**Legacy shaders** | Yes | Yes  
  
Simple unlit Legacy shaders will likely render fine, but they might not be SRP Batcher compatible. | Yes  
  
Simple unlit Legacy shaders will likely render fine, but they might not be SRP Batcher compatible. They also do not support any HDRP features. For an unlit shader that supports HDRP features, use the HDRP/Unlit shader. | Yes  
  
Simple unlit Legacy shaders will likely render fine, but they might not be SRP Batcher compatible.  
**URP prebuilt shaders** | No | Yes | No | No  
**HDRP prebuilt shaders** | No | No | Yes | No