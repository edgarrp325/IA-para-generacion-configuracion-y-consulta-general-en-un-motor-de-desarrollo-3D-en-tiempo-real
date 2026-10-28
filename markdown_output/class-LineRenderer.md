---
title: "Line Renderer component"
category: "General"
source_file: "class-LineRenderer.html"
doc_type: "manual"
---

# Line Renderer component

Switch to Scripting

The ****Line Renderer**** component takes an array of two or more points in 3D space, and draws a straight line between each one. You can use a Line Renderer to draw anything from a simple straight line to a complex spiral.

The line is always continuous; if you need to draw two or more completely separate lines, you should use multiple **GameObjects** , each with its own Line Renderer.

The Line Renderer does not render lines that have a width in **pixels**. It renders polygons that have a width in world units. The Line Renderer uses the same algorithm for line rendering as the Trail Renderer. It renders polygons that have a width in world units. The Line Renderer uses the same algorithm for line rendering as the Trail Renderer.

## Getting started

To create a Line Renderer:

  1. In the Unity menu bar, go to **GameObject** > **Effects** > **Line**.
  2. Select the Line Renderer GameObject.
  3. Add points to the Line Renderer’s Positions array, either by directly setting array values in the **Inspector** window or by using the Create Points Scene Editing Mode.
  4. Use the Inspector window to configure the color, width, and other display settings of the line.

Example Line Renderer configuration

## Line Renderer Materials

By default, a Line Renderer uses the built-in Material, **Default-Line**. You can make many changes to the appearance of the line without changing this Material, such as editing the color gradient or width of the line.

For other effects, such as applying a texture to the line, you will need to use a different Material. If you do not want to write your own **Shader** for the new Material, Unity’s built-in Standard Particle Shaders work well with Line Renderers.

See Creating and using Materials for more information.

## Line Renderer Scene Editing Mode

You can use the Line Renderer’s Inspector to change the **Scene** Editing Mode. Different Scene Editing Modes enable you to use the **Scene view** Editing Mode. Different Scene Editing Modes enable you to use the **Scene view** and the Inspector to edit the Line Renderer in different ways.

There are three Scene Editing Modes: **None** , **Edit Points** , and **Create Points**.

### Setting the Scene Editing Mode

Line Renderer Edit Points and Create Points buttons

Use the **Edit Points** and **Create Points** buttons at the top of the Inspector to set the current Scene Editing Mode.

Click the **Edit Points** button to set the Scene Editing Mode to **Edit Points**. Click it again to set the Scene Editing Mode to **None**.

Click the **Create Points** button to set the Scene Editing Mode to **Create Points**. Click it again to set the Scene Editing Mode to **None**.

### Scene Editing Mode: None

Line Renderer Simplify controls

When no Scene Editing Mode is selected, you can configure and perform a simplification operation that removes unnecessary points from the Positions array.

The following controls are visible in the Inspector:

**Control** | **Description**  
---|---  
**Simplify Preview** | Enable **Simplify Preview** to see a preview of the results of the simplification operation.  
**Tolerance** | Set the amount by which the simplified line can deviate from the original line.  
  
A value of 0 results in no deviation, and therefore little or no simplification. Higher positive values result in more deviation from the original line, and therefore more simplification.  
  
The default value is 1.  
**Simplify** | Click **Simplify** to reduce the number of elements in the Line Renderer’s **Positions** array.  
  
The simplification operation uses the Ramer-Douglas-Peucker algorithm to reduce the number of points, based on the **Tolerance** value.  
  
### Scene Editing Mode: Edit Points

Line Renderer in Edit Points Scene Editing Mode

When the Scene Editing Mode is set to **Edit Points** , Unity represents each point in the Line Renderer’s Positions array as a yellow sphere in the Scene view. You can move the individual points using the Move tool.

The following controls are visible in the Inspector:

**Control** | **Description**  
---|---  
**Show Wireframe** | When enabled, Unity draws a wireframe in the Scene view that visualizes the line.  
**Subdivide Selected** | This button is enabled when you select two or more adjacent points. Pressing this button inserts a new point between the selected adjacent points.  
  
### Scene Editing Mode: Create Points

Line Renderer in Create Points Scene Editing Mode

When the Scene Editing Mode is set to **Create Points** , you can click inside the Scene view to add new points to the end of the Line Renderer’s Positions array.

The following controls are visible in the Inspector:

**Control** | **Description**  
---|---  
**Input** | Set the input method you want to use to create points.  
| **Mouse position** | Create points based on the mouse position in the Scene view.  
| **Physics Raycast** | Create points based on a raycast into the Scene. Unity creates the point at the position where the raycast hits.  
****Layer Mask**** | The layer mask to use when performing a raycast. This property is visible only when **Input** is set to **Physics Raycast**.  
**Min Vertex Distance** | When you drag the mouse to create points in the Scene view, the Line Renderer creates a new point when this distance from the last point is exceeded.  
**Offset** | The offset applied to created points. When **Input** is set to **Mouse Position** , Line Renderer applies the offset from the Scene **camera**. When Input is set to **Physics Raycast** , Line Renderer applies the offset from the raycast normal.  
  
## Line Renderer Inspector reference

This section contains the following sub-sections:

  * Line settings
  * Materials
  * Lighting
  * Probes
  * Additional Settings

### Line settings

**Property** | **Function**  
---|---  
**Loop** | Enable this to connect the first and last positions of the line, and form a closed loop.  
**Positions** | The array of Vector3 points to connect.  
**Width** | Define a width value, and a curve value to control the width of your line along its length.  
  
The curve is sampled at each vertex, so its accuracy is limited by the number of vertices in your line. The overall width of the line is controlled by the width value.  
**Color** | Define a gradient to control the color of the line along its length.  
  
Unity samples colors from the Color gradient at each vertex. Between each vertex, Unity applies linear interpolation to colors. Adding more vertices to your line might give a closer approximation of a detailed gradient.  
**Corner Vertices** | This property dictates how many extra vertices are used when drawing corners in a line. Increase this value to make the line corners appear rounder.  
**End Cap Vertices** | This property dictates how many extra vertices are used to create end caps on the line. Increase this value to make the line caps appear rounder.  
**Alignment** | Set the direction that the line faces.  
| **View** | The line faces the Camera.  
| **TransformZ** | The line faces the Z axis of its **Transform component**.  
**Texture Mode** | Control how the Texture is applied to the line.  
| **Stretch** | Map the texture once along the entire length of the line.  
| **Tile** | Repeat the texture along the line, based on its length in world units. To set the tiling rate, use Material.SetTextureScale.  
| **DistributePerSegment** | Map the texture once along the entire length of the line, assuming all vertices are evenly spaced.  
| **RepeatPerSegment** | Repeat the texture along the line, repeating at a rate of once per line segment. To adjust the tiling rate, use Material.SetTextureScale.  
**Shadow Bias** | Set the amount to move shadows away from the Light to remove shadowing artifacts caused by approximating a volume with billboarded geometry.  
**Generate Lighting Data** | If enabled, Unity builds the line geometry with normals and tangents included. This allows it to use Materials that use the Scene lighting.  
**Use World Space** | If enabled, the points are considered as world space coordinates. If disabled, they are local to the transform of the GameObject to which this component is attached.  
  
### Materials

The **Materials** section lists all the materials that this component uses.

**Property** | **Description**  
---|---  
**Size** | The number of elements in the material list.  
  
If you decrease the number of elements, Unity deletes the elements at the end of the list. If you increase the number of elements, Unity adds new elements to the end of the list. Unity populates new elements with the same material that the element at the end of the list uses.  
**Element** | The materials in the list. You can assign a material asset to each element.  
  
By default, Unity orders the list alphabetically based on the name of the materials. This list is reorderable, and Unity updates the number of the elements automatically as you change their order.  
  
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
**Motion Vectors** | Set whether to use motion vectors to track this Renderer’s per-pixel, screen-space motion from one frame to the next. You can use this information to apply post-processing effects such as motion blur.  
  
**Note:** not all platforms support motion vectors. See SystemInfo.supportsMotionVectors for more information.  
  
This property corresponds to the Renderer.motionVectorGenerationMode API.  
| **Camera Motion Only** | Use only Camera movement to track motion.  
| **Per Object Motion** | Use a specific pass to track motion for this Renderer.  
| **Force No Motion** | Do not track motion.  
**Dynamic Occlusion** | When **Dynamic Occlusion** is enabled, Unity’s occlusion culling system culls this Renderer when it is blocked from a Camera’s view by a Static Occluder. Otherwise, the system does not cull this Renderer when it is blocked from a Camera’s view by a Static Occluder.  
  
Dynamic Occlusion is enabled by default. Disable it for effects such as drawing the outline of a character behind a wall.  
**Sorting Layer** | The name of this Renderer’s Sorting Layer.  
**Order in Layer** | This Renderer’s order within a Sorting Layer.  
  
LineRenderer