---
title: "Reflective Diffuse"
category: "General"
source_file: "shader-ReflectiveDiffuse.html"
doc_type: "manual"
---

# Reflective Diffuse

**Note.** Unity 5 introduced the Standard Shader which replaces this **shader**

## Reflective Properties

**Note.** Unity 5 introduced the Standard Shader which replaces this shader.

This shader will simulate reflective surfaces such as cars, metal objects etc. It requires an environment **Cubemap** which will define what exactly is reflected. The main texture’s alpha channel defines the strength of reflection on the object’s surface. Any **scene** which will define what exactly is reflected. The main texture’s alpha channel defines the strength of reflection on the object’s surface. Any **scene** lights will add illumination on top of what is reflected.

ReflectiveFamilyImport

## Diffuse Properties

Diffuse computes a simple (Lambertian) lighting model. The lighting on the surface decreases as the angle between it and the light decreases. The lighting depends only on this angle, and does not change as the **camera** moves or rotates around.

DiffuseSubsetImport

## Performance

Generally, this shader is cheap to render. For more details, please view the Shader Peformance page.

ReflectiveDiffuse