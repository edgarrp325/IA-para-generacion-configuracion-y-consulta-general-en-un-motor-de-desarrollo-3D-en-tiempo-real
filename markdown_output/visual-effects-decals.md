---
title: "Decals and projectors"
category: "General"
source_file: "visual-effects-decals.html"
doc_type: "manual"
---

# Decals and projectors

Decals are materials that decorate the surface of other materials. They are most commonly used for effects like paint splatters and stickers.

Unity projects these materials into a **scene** so that they wrap around other scene geometry. This means that you can also use them for effects that simulate projected light, such as blob shadows.

Decals in the Universal Render Pipeline

## Render pipeline information

How you work with decals and projectors depends on the **render pipeline** you use. 

**Feature name** | **Built-in Render Pipeline** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)**  
---|---|---|---  
**Decal and projectors** | Yes  
  
Use the Projector component. | Yes  
  
Use the Decal Renderer Feature. | Yes  
  
Use the Decal Projector.