---
title: "Self-Illuminated Shader Family"
category: "General"
source_file: "shader-SelfIllumFamily.html"
doc_type: "manual"
---

# Self-Illuminated Shader Family

**Note.** Unity 5 introduced the Standard Shader which replaces these **shaders**

The **Self-Illuminated** shaders will emit light only onto themselves based on an attached alpha channel. They do not require any Lights to shine on them to emit this light. Any vertex lights or **pixel** lights will simply add more light on top of the self-illumination.

This is mostly used for light emitting objects. For example, parts of the wall texture could be self-illuminated to simulate lights or displays. It can also be useful to light power-up objects that should always have consistent lighting throughout the game, regardless of the lights shining on it.

## Self-Illuminated Vertex-Lit

shader-SelfIllumVertexLit

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Illumination** texture with alpha channel for Illumination Map

» More details

## Self-Illuminated Diffuse

shader-SelfIllumDiffuse

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Illumination** texture with alpha channel for Illumination Map

» More details

## Self-Illuminated Specular

shader-SelfIllumSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for Specular Map
  * One **Illumination** texture with alpha channel for Illumination Map

» More details

## Self-Illuminated Bumped

shader-SelfIllumBumpedDiffuse

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Normal map** normal map with alpha channel for Illumination

» More details

## Self-Illuminated Bumped Specular

shader-SelfIllumBumpedSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for Specular Map
  * One **Normal map** normal map with alpha channel for Illumination Map

» More details

## Self-Illuminated Parallax

shader-SelfIllumParallaxDiffuse

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Normal map** normal map with alpha channel for Illumination Map & Parallax Depth combined

**Note:** One consideration of this shader is that the **Bumpmap** texture’s alpha channel doubles as a Illumination and the Parallax Depth.

» More details

## Self-Illuminated Parallax Specular

shader-SelfIllumParallaxSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for Specular Map
  * One **Normal map** normal map with alpha channel for Illumination Map & Parallax Depth combined

**Note:** One consideration of this shader is that the **Bumpmap** texture’s alpha channel doubles as a Illumination and the Parallax Depth.

» More details

SelfIllumFamily