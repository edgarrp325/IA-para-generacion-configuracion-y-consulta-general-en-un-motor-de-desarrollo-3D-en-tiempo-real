---
title: "Normal Shader Family"
category: "General"
source_file: "shader-NormalFamily.html"
doc_type: "manual"
---

# Normal Shader Family

**Note.** Unity 5 introduced the Standard Shader which replaces these **shaders**

These shaders are the basic shaders in Unity. They are not specialized in any way and should be suitable for most opaque objects. They are not suitable if you want your object to be transparent, emitting light etc. 

## Vertex Lit

shader-NormalVertexLit

**Assets needed:**

  * One **Base** texture, no alpha channel required

## Diffuse

shader-NormalDiffuse

**Assets needed:**

  * One **Base** texture, no alpha channel required

## Specular

shader-NormalSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for Specular Map

## Normal mapped

shader-NormalBumpedDiffuse

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Normal map**

## Normal mapped Specular

shader-NormalBumpedSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for Specular Map
  * One **Normal map**

## Parallax

shader-NormalParallaxDiffuse

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Normal map**
  * One **Height** texture with Parallax Depth in the alpha channel

## Parallax Specular

shader-NormalParallaxSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for Specular Map
  * One **Normal map**
  * One **Height** texture with Parallax Depth in the alpha channel

## Decal

shader-NormalDecal

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Decal** texture with alpha channel for Decal transparency

## Diffuse Detail

shader-NormalDiffuseDetail

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Detail** grayscale texture; with 50% gray being neutral color

NormalFamily