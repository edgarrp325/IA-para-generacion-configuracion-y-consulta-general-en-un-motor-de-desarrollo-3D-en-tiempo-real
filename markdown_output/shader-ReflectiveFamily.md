---
title: "Reflective Shader Family"
category: "General"
source_file: "shader-ReflectiveFamily.html"
doc_type: "manual"
---

# Reflective Shader Family

**Note.** Unity 5 introduced the Standard Shader which replaces these **shaders**

**Reflective** shaders will allow you to use a **Cubemap** which will be reflected on your **mesh** which will be reflected on your **mesh**. You can also define areas of more or less reflectivity on your object through the alpha channel of the **Base** texture. High reflectivity is a great effect for glosses, oils, chrome, etc. Low reflectivity can add effect for metals, liquid surfaces, or video monitors.

## Reflective Vertex-Lit

shader-ReflectiveVertexLit

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map

» More details

## Reflective Diffuse

shader-ReflectiveDiffuse

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map

» More details

## Reflective Specular

shader-ReflectiveSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas & Specular Map combined
  * One **Reflection** Cubemap for Reflection Map

**Note:** One consideration for this shader is that the **Base** texture’s alpha channel will double as both the reflective areas and the Specular Map.

» More details

## Reflective Normal mapped

shader-ReflectiveBumpedDiffuse

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , no alpha channel required

» More details

## Reflective Normal Mapped Specular

shader-ReflectiveBumpedSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas & Specular Map combined
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , no alpha channel required

**Note:** One consideration for this shader is that the **Base** texture’s alpha channel will double as both the reflective areas and the Specular Map.

» More details

## Reflective Parallax

shader-ReflectiveParallaxDiffuse

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , with alpha channel for Parallax Depth

» More details

## Reflective Parallax Specular

shader-ReflectiveParallaxSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas & Specular Map
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , with alpha channel for Parallax Depth

**Note:** One consideration for this shader is that the **Base** texture’s alpha channel will double as both the reflective areas and the Specular Map.

» More details

## Reflective Normal mapped Unlit

shader-ReflectiveBumpedUnlit

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , no alpha channel required

» More details

## Reflective Normal mapped Vertex-Lit

shader-ReflectiveBumpedVertexLit

**Assets needed:**

  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , no alpha channel required

» More details

ReflectiveFamily