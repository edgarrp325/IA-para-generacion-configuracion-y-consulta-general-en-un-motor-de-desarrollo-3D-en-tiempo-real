---
title: "Diffuse"
category: "General"
source_file: "shader-NormalDiffuse.html"
doc_type: "manual"
---

# Diffuse

**Note.** Unity 5 introduced the Standard Shader which replaces this **shader**

## Diffuse Properties

Diffuse computes a simple (Lambertian) lighting model. The lighting on the surface decreases as the angle between it and the light decreases. The lighting depends only on this angle, and does not change as the **camera** moves or rotates around.

DiffuseSubsetImport

## Performance

Generally, this shader is cheap to render. For more details, please view the Shader Peformance page.

NormalDiffuse