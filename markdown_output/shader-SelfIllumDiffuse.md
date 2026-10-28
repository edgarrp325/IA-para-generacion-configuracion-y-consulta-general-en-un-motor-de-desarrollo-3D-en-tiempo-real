---
title: "Self-Illuminated Diffuse"
category: "General"
source_file: "shader-SelfIllumDiffuse.html"
doc_type: "manual"
---

# Self-Illuminated Diffuse

**Note.** Unity 5 introduced the Standard Shader which replaces this **shader**

## Self-Illuminated Properties

**Note.** Unity 5 introduced the Standard Shader which replaces this shader.

This shader allows you to define bright and dark parts of the object. The alpha channel of a secondary texture will define areas of the object that “emit” light by themselves, even when no light is shining on it. In the alpha channel, black is zero light, and white is full light emitted by the object. Any **scene** lights will add illumination on top of the shader’s illumination. So even if your object does not emit any light by itself, it will still be lit by lights in your scene.

SelfIllumFamilyImport

## Diffuse Properties

Diffuse computes a simple (Lambertian) lighting model. The lighting on the surface decreases as the angle between it and the light decreases. The lighting depends only on this angle, and does not change as the **camera** moves or rotates around.

DiffuseSubsetImport

## Performance

Generally, this shader is cheap to render. For more details, please view the Shader Peformance page.

SelfIllumDiffuse