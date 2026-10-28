---
title: "Transparent Cutout Bumped Diffuse"
category: "General"
source_file: "shader-TransCutBumpedDiffuse.html"
doc_type: "manual"
---

# Transparent Cutout Bumped Diffuse

**Note.** Unity 5 introduced the Standard Shader which replaces this **shader**

## Transparent Cutout Properties

**Note.** Unity 5 introduced the Standard Shader which replaces this shader.

Cutout shader is an alternative way of displaying transparent objects. Differences between Cutout and regular Transparent shaders are:

  * This shader cannot have partially transparent areas. Everything will be either fully opaque or fully transparent.
  * Objects using this shader can cast and receive shadows!
  * The graphical sorting problems normally associated with Transparent shaders do not occur when using this shader.

This shader uses an alpha channel contained in the **Base** Texture to determine the transparent areas. If the alpha contains a blend between transparent and opaque areas, you can manually determine the cutoff point for the which areas will be shown. You change this cutoff by adjusting the **Alpha Cutoff** slider.

TransCutFamilyImport

## Normal Mapped Properties

Like a **Diffuse** shader, this computes a simple (Lambertian) lighting model. The lighting on the surface decreases as the angle between it and the light decreases. The lighting depends only on the angle, and does not change as the **camera** moves or rotates around.

**Normal mapping** simulates small surface details using a texture, instead of spending more polygons to actually carve out details. It does not actually change the shape of the object, but uses a special texture called a **Normal Map** to achieve this effect. In the normal map, each **pixel** to achieve this effect. In the normal map, each **pixel** ’s color value represents the angle of the surface normal. Then by using this value instead of the one from geometry, lighting is computed. The normal map effectively overrides the **mesh** ’s color value represents the angle of the surface normal. Then by using this value instead of the one from geometry, lighting is computed. The normal map effectively overrides the **mesh** ’s geometry when calculating lighting of the object.

### Creating Normal maps

You can import normal maps created outside of Unity, or you can import a regular grayscale image and convert it to a Normal Map from within Unity. (This page refers to a legacy shader which has been superseded by the Standard Shader, but you can learn more about how to use Normal Maps in the Standard Shader)

### Technical Details

The Normal Map is a tangent space type of normal map. Tangent space is the space that “follows the surface” of the model geometry. In this space, Z always points away from the surface. Tangent space Normal Maps are a bit more expensive than the other “object space” type Normal Maps, but have some advantages:

  1. It’s possible to use them on deforming models - the bumps will remain on the deforming surface and will just work.
  2. It’s possible to reuse parts of the normal map on different areas of a model; or use them on different models.

BumpSubsetImport

## Diffuse Properties

Diffuse computes a simple (Lambertian) lighting model. The lighting on the surface decreases as the angle between it and the light decreases. The lighting depends only on this angle, and does not change as the camera moves or rotates around.

DiffuseSubsetImport

## Performance

Generally, this shader is cheap to render. For more details, please view the Shader Peformance page.

TransCutBumpedDiffuse