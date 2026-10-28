---
title: "Skinned Mesh Renderer component"
category: "General"
source_file: "class-SkinnedMeshRenderer.html"
doc_type: "manual"
---

# Skinned Mesh Renderer component

Switch to Scripting

The Skinned **Mesh** Renderer component renders a deformable mesh. Deformable meshes include skinned meshes (meshes that have bones and bind poses), meshes that have blend shapes, and meshes that run cloth simulation.

To render a regular mesh, use a Mesh Renderer and a Mesh Filter and a Mesh Filter instead.

When you add a deformable mesh or a model with a deformable mesh to a **scene** , Unity adds a Skinned Mesh Renderer component to the resulting **GameObject** , Unity adds a Skinned Mesh Renderer component to the resulting **GameObject**.

In C# code, the SkinnedMeshRenderer class represents a Skinned Mesh Renderer component. The `SkinnedMeshRenderer` class inherits much of its functionality from the Renderer class. As such, this component has a lot in common with other components that inherit from `Renderer`, such as Line Renderer, and Trail Renderer.

## Troubleshooting Skinned Mesh Renderer visibility

Unity uses the mesh’s bounds to determine whether to render it. If the entire **bounding volume** is outside the view of any active **Camera** is outside the view of any active **Camera** , Unity does not render the mesh.

In the case of a Skinned Mesh Renderer, its mesh bounds change as it deforms. Unity accounts for all animations present at import time when it calculates the maximum bounding volume, and uses this value to determine visibility; however, the following situations that occur after import might push vertices or bones outside of the maximum known bounds:

  * Additive animations
  * Changing the positions of bones from a script at runtime
  * Using vertex **shaders** that change vertex positions
  * Using ragdolls

If this happens, Unity might not correctly determine the visibility of the mesh, and might fail to show it when expected.

In these cases, you can try either of the following solutions to fix the problem:

  * Modify the bounds to match the maximum potential bounding volume of your mesh. Use this option if possible, because it is better for performance.
  * Enable **Update When Offscreen** , so that Unity continues to calculate the mesh bounds at all times, even when the mesh is not visible. Use this option if performance is not a major concern, or if you can’t predict the size of your bounding volume (for example, if you use ragdolls).

## Skinned Mesh Renderer Inspector reference

The Skinned Mesh Renderer component as it appears in the Inspector window.

  * Properties  

  * Materials  

  * Lighting  

  * Probes  

  * Additional Settings

### Properties

**Property** | **Description**  
---|---  
**Bounds** | Sets the bounding volume that Unity uses to determine when the mesh is offscreen. Unity pre-calculates the bounds when importing the mesh and animations in the Model file, and displays the bounds as a wireframe around the Model in the Scene view.  
  
If you set Update When Offscreen to True, Unity recalculates these bounds every frame and uses those calculated values to overwrite this property.  
  
This property corresponds to the Mesh.Bounds API.  
**BlendShapes** | Stores the weight values that Unity uses with the blend shapes defined in the mesh.  
**Quality** | Sets a runtime cap for the maximum number of bones that can affect a vertex.   
  
When Unity imports a mesh, Unity can skin every vertex with a number of bones from one to 32. A higher number of influential bones improves results during movement. However, this also increases the computational resources required, and therefore might affect performance.  
  
For performance reasons, it’s better to set the number of bones that affect a vertex on import, rather than using a runtime cap. To do this, use the Rig tab of the Model Import Settings window and adjust the Skin Weights setting.  
  
In addition to using this setting to set a runtime cap per-component, you can also set a global limit for your project under Edit > Project Settings > Quality > Other > Skin Weights.  
  
This property corresponds to the SkinnedMeshRenderer.quality API.  
| **Auto** | Use the global limit set in **Quality Settings** > **Skin Weights**.  
  
**Note:** If you import a custom number of skin weights and you want to allow more than four bones of influence, you must choose this option and make sure you set **Skin Weights** to **Unlimited**.  
| **1 Bone** | Use only one bone per vertex.  
| **2 Bones** | Use up to two bones per vertex.  
| **4 Bones** | Use up to four bones per vertex. To allow more than four bones to influence a single vertex, use the **Auto** setting.  
**Update When Offscreen** | Enable this option to calculate the bounding volume at every frame, even when the mesh is not visible by any Camera. Disable this option to stop skinning when the GameObject is off-screen and resume it when the GameObject is visible again.  
  
This is disabled by default, for performance reasons.  
  
This property corresponds to the SkinnedMeshRenderer.updateWhenOffscreen API.  
**Mesh** | Set the mesh that this Renderer uses. The mesh should either contain a valid bind pose and skin weights, use blend shapes, or run cloth simulation. If the mesh does not use any of these techniques, consider using a Mesh Renderer and a Mesh Filter.  
  
Corresponds to the SkinnedMeshRenderer.sharedMesh property.  
**Root bone** | Set the transform that is the “root” of the skeleton. The bounds move along with this transform.  
**Rendering Layer Mask** | This property determines which rendering layer Unity assigns this renderer to. You can use this property to specify an additional rendering-specific layer mask. This filters the renderers based on the mask the renderer has.  
  
This property corresponds to the Renderer.renderingLayerMask API.  
  
Unity only displays this property when you use a Scriptable Render Pipeline.  
**Renderer Priority** | Sort renderers by priority. Lower values are rendered first and higher values are rendered last.  
  
This property corresponds to the Renderer.rendererPriority API.  
  
Unity only displays this property when you use the High Definition Render Pipeline.  
  
### Materials

Wireframe view of the meshes in Unity’s 2020.1 HDRP template example project

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
**Skinned Motion Vectors** | Enable this option to double-buffer the Mesh skinning data, so Unity can interpolate the skinned motion and place it into the motion vector Texture. This uses more GPU memory, but leads to more correct motion vectors.  
**Dynamic Occlusion** | When **Dynamic Occlusion** is enabled, Unity’s occlusion culling system culls this Renderer when it is blocked from a Camera’s view by a Static Occluder. Otherwise, the system does not cull this Renderer when it is blocked from a Camera’s view by a Static Occluder.  
  
Dynamic Occlusion is enabled by default. Disable it for effects such as drawing the outline of a character behind a wall.  
  
SkinnedMeshRenderer