---
title: "Mesh Renderer component"
category: "General"
source_file: "class-MeshRenderer.html"
doc_type: "manual"
---

# Mesh Renderer component

Switch to Scripting

A **Mesh** Renderer component renders a mesh. It works with a Mesh Filter Renderer component renders a mesh. It works with a Mesh Filter component on the same **GameObject** component on the same **GameObject** ; the **Mesh Renderer** renders the mesh that the Mesh Filter references.

To render a deformable mesh, use a Skinned Mesh Renderer instead.

In C# code, the MeshRenderer class represents a Mesh Renderer component. The `MeshRenderer` class inherits much of its functionality from the Renderer class. As such, this component has a lot in common with other components that inherit from `Renderer`, such as Line Renderer, and Trail Renderer.

## Mesh Renderer Inspector reference

The Mesh Renderer component as it appears in the Inspector window with Receive **Global Illumination** set to **Light Probes**.

A: Materials  
B: Lighting  
C: Lightmapping  
D: Probes  
E: Additional Settings

### Materials

The Materials section

The **Materials** section lists all the materials that this component uses.

**Property** | **Description**  
---|---  
**Size** | The number of elements in the material list.  
  
If you decrease the number of elements, Unity deletes the elements at the end of the list. If you increase the number of elements, Unity adds new elements to the end of the list. Unity populates new elements with the same material that the element at the end of the list uses.  
**Element** | The materials in the list. You can assign a material asset to each element.  
  
By default, Unity orders the list alphabetically based on the name of the materials. This list is reorderable, and Unity updates the number of the elements automatically as you change their order.  
  
**Note:** If there are more materials than there are sub-meshes, Unity renders the last sub-mesh with each of the remaining materials, one on top of the next. If the materials are not fully opaque, you can layer different materials and create interesting visual effects. However, fully opaque materials overwrite previous layers, so any additional opaque materials that Unity applies to the last sub-mesh negatively affect performance and produce no benefit.

## Lighting

The **Lighting** section contains properties that relate to lighting.

**Property** | **Description**  
---|---  
**Cast Shadows** | Specify if and how this Renderer casts shadows when a suitable Light shines on it.  
  
This property corresponds to the Renderer.shadowCastingMode API.  
| **On** | This Renderer casts a shadow when a shadow-casting Light shines on it.  
| **Off** | This Renderer does not cast shadows.  
| **Two-sided** | This Renderer casts two-sided shadows. This means that single-sided objects like a plane or a quad can cast shadows, even if the light source is behind the mesh.  
  
For Baked Global Illumination or Enlighten Realtime Global Illumination to support two-sided shadows, the material must support Double Sided Global Illumination.  
| **Shadows Only** | This Renderer casts shadows, but the Renderer itself isn’t visible.  
**Receive Shadows** | Specify if Unity displays shadows cast onto this Renderer.  
  
This property only has an effect if you enable Baked Global Illumination or Enlighten Realtime Global Illumination for this scene.  
  
This property corresponds to the Renderer.receiveShadows API.  
**Contribute Global Illumination** | Include this Renderer in global illumination calculations, which take place at bake time.  
  
This property only has an effect if you enable Baked Global Illumination or Enlighten Realtime Global Illumination for this scene.  
  
Enabling this property enables the Contribute GI flag in the GameObject’s Static Editor Flags. It corresponds to the StaticEditorFlags.ContributeGI API.  
**Receive Global Illumination** | Whether Unity provides global illumination data to this Renderer from baked lightmaps, or from runtime Light Probes.  
  
This property is only editable if you enable **Contribute Global Illumination**. It only has an effect if you enable Baked Global Illumination or Enlighten Realtime Global Illumination for this scene.  
  
This property corresponds to the MeshRenderer.receiveGI API.  
| **Lightmaps** | Unity provides global illumination data to this Renderer from lightmaps.  
| **Light Probes** | Unity provides global illumination data to this Renderer from Light Probes in the scene.  
**Prioritize Illumination** | Enable this property to always include this Renderer in Enlighten Realtime Global Illumination calculations. This ensures that the Renderer is affected by distant emissives, even those which are normally excluded from Global Illumination calculations for performance reasons.  
  
This property is visible only if **Contribute GI** is enabled in the GameObject’s Static Editor Flags, your project uses the Built-in Render Pipeline, and Enlighten Realtime Global Illumination is enabled in your scene.  
  
## Lightmapping

The **Lightmapping** section contains properties relating to baked and real-time **lightmaps**.

This section is visible only if only if **Receive**Global Illumination**** is set to **Lightmaps**.

**Property:** | **Function:**  
---|---  
**Scale in Lightmap** | Specify the relative size of the Renderer’s UVs within a lightmap.  
  
A value of 0 results in the Renderer not being lightmapped, but it still contributes to lighting other Renderers in the Scene. A value greater than 1.0 increases the number of pixels (the lightmap resolution) used for this Renderer, while a value less than 1.0 decreases it.  
  
You can use this property to optimize lightmaps so that important and detailed areas are more accurately lit. For example, an isolated building with flat, dark walls uses a low lightmap scale (less than 1.0) while a collection of colourful motorcycles displayed close together requires a high scale value.  
  
This property corresponds to the MeshRenderer.scaleInLightmap API.  
**Stitch Seams** | Enable Lightmap seam stitching for this Renderer.  
  
This property corresponds to the MeshRenderer.stitchLightmapSeams API.  
**Lightmap Parameters** | Choose or create a Lightmap Parameters asset for this Renderer.  
**Optimize Realtime UVs** | Determine whether Unity merges the real-time lightmap UVs for this Renderer.  
  
This property is visible only if your Project uses the Built-in Render Pipeline, and Enlighten Realtime Global Illumination is enabled in your scene.  
**Max Distance** | Specify the maximum worldspace distance for UV chart simplification in real-time lightmaps. If charts are within this distance, Unity simplifies them.  
  
This property is visible only if your Project uses the Built-in Render Pipeline, and Enlighten Realtime Global Illumination is enabled in your scene.  
**Max Angle** | Specify the maximum angle in degrees between faces sharing a UV edge in real-time lightmaps. If the angle between the faces is below this value, Unity simplifies the UV charts.  
  
This property is visible only if your Project uses the Built-in Render Pipeline, and Enlighten Realtime Global Illumination is enabled in your scene.  
**Ignore Normals** | Enable this option to prevent Unity from splitting the UV charts in real-time lightmaps.  
  
This property is visible only if your Project uses the Built-in Render Pipeline, and Enlighten Realtime Global Illumination is enabled in your scene.  
**Min Chart Size** | Specify the minimum texel size used for a UV chart in real-time lightmaps. If stitching is required, a value of 4 creates a chart of 4x4 texels to store lighting and directionality. If stitching is not required, a value of 2 reduces the texel density and provides better lighting build times and game performance.  
  
This property is visible only if your Project uses the Built-in Render Pipeline, and Enlighten Realtime Global Illumination is enabled in your scene.  
  
When you’ve baked your lighting data (menu: **Window** > **Rendering** > **Lighting** > **Generate Lighting** ), this section also shows the baked lightmaps and real-time lightmaps in the current scene that this Renderer uses.

Example of lightmaps that appear in your Scene after baking.

### Probes

The **Probes** section contains properties relating to Light Probe and Reflection Probes

**Property** | **Description**  
---|---  
**Light Probes** | Set how this Renderer receives light from the Light Probes system.  
  
This property corresponds to the Renderer.lightProbeUsage API.  
| **Off** | The Renderer doesn’t use any interpolated Light Probes.  
| **Blend Probes** | The Renderer uses one interpolated Light Probe. This is the default value.  
| **Use Proxy Volume** | The Renderer uses a 3D grid of interpolated Light Probes.  
| **Custom Provided** | The Renderer extracts Light Probe shader uniform values from the MaterialPropertyBlock.  
**Proxy Volume Override** | Set a reference to another GameObject that has a Light Probe Proxy Volume component.  
  
This property is only visible when **Light Probes** is set to **Use Proxy Volume**.  
**Reflection Probes** | Set how the Renderer receives reflections from the Reflection Probe system.  
  
This property corresponds to the Renderer.probeAnchor API.  
| **Off** | Disables Reflection Probes. Unity uses a skybox for reflection.  
| **Blend Probes** | Enables Reflection Probes. Blending occurs only between Reflection Probes. This is useful in indoor environments where the character may transition between areas with different lighting settings.  
| **Blend Probes and Skybox** | Enables Reflection Probes. Blending occurs between Reflection Probes, or between Reflection Probes and the default reflection. This is useful for outdoor environments.  
| **Simple** | Enables Reflection Probes, but no blending occurs between Reflection Probes when there are two overlapping volumes.  
**Anchor Override** | Set the Transform that Unity uses to determine the interpolation position when using the Light Probe or Reflection Probe systems. By default, this is the centre of the bounding box of the Renderer’s geometry.  
  
This property corresponds to the Renderer.probeAnchor API.  
  
### Additional Settings

The **Additional Settings** section contains additional properties.

**Property** | **Description**  
---|---  
**Motion Vectors** | Set whether to use motion vectors to track this Renderer’s per-pixel, screen-space motion from one frame to the next. You can use this information to apply post-processing effects such as motion blur.  
  
**Note:** not all platforms support motion vectors. See SystemInfo.supportsMotionVectors for more information.  
  
This property corresponds to the Renderer.motionVectorGenerationMode API.  
| **Camera Motion Only** | Use only Camera movement to track motion.  
| **Per Object Motion** | Use a specific pass to track motion for this Renderer.  
| **Force No Motion** | Do not track motion.  
**Dynamic Occlusion** | When **Dynamic Occlusion** is enabled, Unity’s occlusion culling system culls this Renderer when it is blocked from a Camera’s view by a Static Occluder. Otherwise, the system does not cull this Renderer when it is blocked from a Camera’s view by a Static Occluder.  
  
Dynamic Occlusion is enabled by default. Disable it for effects such as drawing the outline of a character behind a wall.  
  
MeshRenderer