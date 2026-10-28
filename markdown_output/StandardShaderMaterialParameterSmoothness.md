---
title: "Smoothness"
category: "General"
source_file: "StandardShaderMaterialParameterSmoothness.html"
doc_type: "manual"
---

# Smoothness

The Smoothness Property, shown in both Metallic & Specular shader modes.

The concept of Smoothness applies to both the Specular workflow and the Metallic workflow, and works in very much the same way in both. By default, without a Metallic or Specular texture map assigned, the smoothness of the material is controlled by a slider. This slider allows you to control the “microsurface detail” or smoothness across a surface.

Both **shader** modes are shown above, because if you choose to use a texture map for the **Metallic** or **Specular** Property, the smoothness values are taken from that same map. This is explained in further detail down the page.

A range of smoothness values from 0 to 1

The “microsurface detail” is not something directly visible in Unity. It is a concept used in the lighting calculations. You can, however, see the effect of this microsurface detail represented by the amount the light that is diffused as it bounces off the object. With a smooth surface, all light rays tend to bounce off at predictable and consistent angles. Taken to its extreme, a perfectly smooth surface reflects light like a mirror. Less smooth surfaces reflect light over a wider range of angles (as the light hits the bumps in the microsurface), and therefore the reflections have less detail and are spread across the surface in a more diffuse way.

A comparison of low, medium and high values for smoothness (left to right), as a diagram of the theoretical microsurface detail of a material. The yellow lines represent light rays hitting the surface and reflecting off the angles encountered at varying levels of smoothness.

A smooth surface has very low microsurface detail, or none at all, so light bounces off in uniform ways, creating clear reflections. A rough surface has high peaks and troughs in its microsurface detail, so light bounces off in a wide range of angles which, when averaged out, create a diffuse colour with no clear reflections.

A comparison of low, medium and high values for smoothness (top to bottom).

At low smoothness levels, the reflected light at each point on the surface comes from a wide area, because the microsurface detail is bumpy and scatters light. At high values of smoothness, the light at each point comes from a narrowly focused area, giving a much clearer reflection of the object’s environment.

## Using a Smoothness Texture Map

In a similar way to many of the other Properties, you can assign a texture map instead of using a single slider value. This allows you greater control over the strength and colour of the specular light reflections across the surface of the material.

Using a map instead of a slider means you can create materials which include a variety of smoothness levels across the surface (usually designed to match what is shown in the albedo texture).

**_Property:_** | **_Function:_**  
---|---  
**Smoothness source** | Select the texture channel where the smoothness value is stored.  
 _Specular/Metallic Alpha_ | Use the Alpha channel of the Specular or Metallic map (depending which of these two modes you are using) as the Smoothness value. Because the smoothness of each point on the surface is a single value, only a single channel of an image texture is required for the data. Unity assumes the smoothness data is in the Alpha Channel of the texture used for the Metallic or Specular texture map .  
 _Albedo Alpha_ | Use the Alpha channel of the Albedo map as the Smoothness value. This lets you reduce the total number of textures, or use textures of different resolutions for the Smoothness value and Specular/Metallic map.  
  
You can toggle highlights and reflections with the settings found in the ****Forward Rendering** Options** section of the Material when it is open in the **Inspector** Options section of the Material when it is open in the **Inspector**.

**_Property:_** | **_Function:_**  
---|---  
**Highlights** | Check this box to disable highlights. This is an optional performance optimization for mobile. It removes the calculation of highlights from the Standard Shader. How this affects the appearance mainly depends on the Specular/Metallic value and the Smoothness.  
**Reflections** | Check this box to disable environment reflections. This is an optional performance optimization for mobile. It removes the calculation of highlights from the Standard Shader. Instead of sampling the environment map, an approximation is used. How this affects the appearance depends on the smoothness.  
  
Smoother surfaces are more reflective and have smaller, more tightly-focused specular highlights. Less smooth surfaces do not reflect as much, so specular highlights are less noticable and spread wider across the surface. By matching the specular and smoothness maps to the content in your albedo map, you can begin to create very realistic-looking textures.