---
title: "Transparent Cutout Shader Family"
category: "General"
source_file: "shader-TransparentCutoutFamily.html"
doc_type: "manual"
---

# Transparent Cutout Shader Family

**Note.** Unity 5 introduced the Standard Shader which replaces these **shaders**

The Transparent Cutout shaders are used for objects that have fully opaque and fully transparent parts (no partial transparency). Things like chain fences, trees, grass, etc.

## Transparent Cutout Vertex-Lit

shader-TransCutVertexLit

**Assets needed:**

  * One **Base** texture with alpha channel for Transparency Map

» More details

## Transparent Cutout Diffuse

shader-TransCutDiffuse

**Assets needed:**

  * One **Base** texture with alpha channel for Transparency Map

» More details

## Transparent Cutout Specular

shader-TransCutSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for combined Transparency Map/Specular Map

**Note:** One limitation of this shader is that the **Base** texture’s alpha channel doubles as a Specular Map for the Specular shaders in this family.

» More details

## Transparent Cutout Bumped

shader-TransCutBumpedDiffuse

**Assets needed:**

  * One **Base** texture with alpha channel for Transparency Map
  * One **Normal map** normal map, no alpha channel required

» More details

## Transparent Cutout Bumped Specular

shader-TransCutBumpedSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for combined Transparency Map/Specular Map
  * One **Normal map** normal map, no alpha channel required

**Note:** One limitation of this shader is that the **Base** texture’s alpha channel doubles as a Specular Map for the Specular shaders in this family.

» More details

TransparentCutoutFamily