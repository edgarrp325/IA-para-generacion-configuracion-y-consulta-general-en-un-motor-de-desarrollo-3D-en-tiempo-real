---
title: "Shadow troubleshooting"
category: "General"
source_file: "ShadowPerformance.html"
doc_type: "manual"
---

# Shadow troubleshooting

## Shadow performance

Real-time shadows have quite a high rendering overhead; any **GameObjects** that might cast shadows must first be rendered into the shadow map and then that map will be used to render objects that might receive shadows.

Soft shadows have a greater rendering overhead than hard shadows, but this only affects the GPU and does not cause much extra CPU work.

If rendering real-time shadows for complex geometry is prohibitively expensive, consider using low **LOD** meshes or even primitives to cast shadows.

If this is too resource-intensive, you can fake shadows using a blurred texture applied to a simple **mesh** or **quad** or **quad** underneath your characters, or can create blob shadows with custom shaders.

## Shadow acne

A surface directly illuminated by a Light sometimes appears to be partly in shadow. This is because **pixels** that should be exactly at the distance specified in the shadow map are sometimes calculated as being further away (this is a consequence of using shadow filtering, or a low-resolution image for the shadow map). The result is arbitrary patterns of pixels in shadow when they should be lit, giving a visual effect known as “shadow acne”.

Shadow acne in the form of false self-shadowing artifacts

### The light bias settings

To prevent shadow acne, you can adjust the **light bias** settings.

You can add a bias to the distance in the shadow map to ensure that pixels on the borderline pass the comparison, or you can inset geometry a little bit along its normals. 

In the Built-in **Render Pipeline** , you can set these values with the **Bias** and **Normal Bias** properties in the Light **Inspector** , you can set these values with the **Bias** and **Normal Bias** properties in the Light **Inspector** window when shadows are enabled.

Do not set the **Bias** value too high, because areas around a shadow near the GameObject casting it are sometimes falsely illuminated. This results in a disconnected shadow, making the GameObject look as if it is flying above the ground.

A high **Bias** value makes the shadow appear “disconnected” from the GameObject

Likewise, setting the **Normal Bias** value too high makes the shadow appear too narrow for the GameObject:

A high **Normal Bias** value makes the shadow shape too narrow

In some situations, **Normal Bias** can cause an unwanted effect called “light bleeding”, where light bleeds through from nearby geometry into areas that should be shadowed. A potential solution is to open the GameObject’s Mesh Renderer and change the **Cast Shadows** property to **Two Sided**. This can sometimes help, although it can be more resource-intensive and increase performance overhead when rendering the **Scene** and change the **Cast Shadows** property to **Two Sided**. This can sometimes help, although it can be more resource-intensive and increase performance overhead when rendering the **Scene**.

The bias values for a Light may need tweaking to make sure that unwanted effects don’t occur. It is generally easier to gauge the right value by eye rather than attempting to calculate it.

A low Shadow near plane offset value create the appearance of holes in shadows Correct shadowing

### Shadow pancaking

To further prevent shadow acne we are using a technique known as **Shadow pancaking**. The idea is to reduce the range of the light space used when rendering the shadow map along the light direction. This leads to an increased precision in the shadow map, reducing shadow acne.

A diagram showing the shadow pancaking principle

In the above diagram:

  * The **light blue circles** represent the shadow casters
  * The **dark blue rectangle** represents the original light space
  * The **green line** represents the optimized near plane (excluding any shadow casters not visible in the view frustum)

Clamp these shadow casters to the near clip plane of the optimized space (in the Vertex Shader). Note that while this works well in general, it can create artifacts for very large triangles crossing the near clip plane:

Large triangle problem

In this case, only one vertex of the blue triangle is behind the near clip plane and gets clamped to it. However, this alters the triangle shape, and can create incorrect shadowing.

You can tweak the **Shadow Near Plane Offset** property from the Quality window to avoid this problem. This pulls back the near clip plane. However, setting this value very high eventually introduces shadow acne, because it raises the range that the shadow map needs to cover in the light direction. Alternatively, you can also tesselate the problematic shadow casting triangles.

## Shadows not appearing

If you find that one or more objects are not casting shadows then you should check the following points:

  * Real-time shadows can be disabled completely in the Quality window. Make sure that you have the correct quality level enabled and that shadows are switched on for that setting.

  * All Mesh Renderers in the scene must be set up with their _Receive Shadows_ and _Cast Shadows_ correctly set. Both are enabled by default, but check that they haven’t been disabled unintentionally.

  * Only opaque objects cast and receive shadows, so objects using the built-in Transparent or Particle shaders will neither cast nor receive. Generally, you can use the Transparent Cutout shaders instead for objects with “gaps” such as fences, vegetation, etc. Custom Shaders

  * Objects using **VertexLit** shaders can’t receive shadows, but they can cast them.

  * Unity can’t calculate shadows for GameObjects that have materials with “Unlit” type shaders. Unity can only calculate shadows for materials with shaders that support lighting.

  * In the Built-in Render Pipeline, using the Forward rendering path, some shaders allow only the brightest directional light to cast shadows (in particular, this happens with Unity’s built-in shaders from 4.x versions). If you want to have more than one shadow-casting light then you should use the Deferred Shading **rendering path** instead. You can enable your own shaders to support “full shadows” by using the `fullforwardshadows` surface shader instead. You can enable your own shaders to support “full shadows” by using the `fullforwardshadows` surface shader directive.