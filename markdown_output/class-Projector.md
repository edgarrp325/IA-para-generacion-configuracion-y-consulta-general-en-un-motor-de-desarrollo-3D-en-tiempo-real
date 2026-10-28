---
title: "Projector component"
category: "General"
source_file: "class-Projector.html"
doc_type: "manual"
---

# Projector component

Switch to Scripting

Use a Projector component to create effects such as:

  * Decal effects, like bullet holes or paint splatters
  * Blob shadows
  * Stylized lighting effects
  * The effect of a real-world projector, using another Camera that renders to a **Render Texture** that renders to a **Render Texture**

**Note:** This workflow is compatible only with the Built-in Render Pipelne. For similar functionality in other **render pipelines** , see Decals and projectors.

A Projector creates a Blob Shadow for a robot

## Using the Projector component

A Projector works by projecting a material onto all objects that intersect its frustum. The material must use the Projector/Light or Projector/Multiply **shaders** , available in Unity’s Standard Assets.

### Material configuration

When configuring a material to use with the Projector/Light and Projector/Multiply shaders, be aware of the following:

**Cookie texture:**

  * Make sure texture wrap mode is set to “Clamp”
  * Turn on “Replicate Border” option in mipmap related import settings
  * Use uncompressed texture format
  * Projector/Shadow also requires alpha channel to be present (typically Alpha from Grayscale option is ok)

**Falloff texture (if present):**

  * Data needs to be in alpha channel, so typically Alpha8 texture format
  * Make sure texture wrap mode is set to “Clamp”
  * Make sure leftmost **pixel** column is black; and “Border mipmaps” import setting is on.

## Projector Inspector reference

**_Property:_** | **_Function:_**  
---|---  
**Near Clip Plane** | Objects in front of the near clip plane will not be projected upon.  
**Far Clip Plane** | Objects beyond this distance will not be projected upon.  
**Field Of View** | The field of view in degrees. This is only used if the Projector is not Orthographic.  
**Aspect Ratio** | This allows you to tune the height and width of the Projector.  
**Orthographic** | If enabled, the Projector will be Orthographic instead of perspective.  
**Orthographic Size** | The Orthographic size of the Projection. This is only used if Orthographic is enabled.  
**Material** | The Material that will be projected.  
**Ignore Layers** | Objects in Layers that you specify here will not be projected upon. The default value is None.  
  
Projector