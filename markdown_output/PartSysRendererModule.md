---
title: "Renderer module"
category: "General"
source_file: "PartSysRendererModule.html"
doc_type: "manual"
---

# Renderer module

The Renderer module’s settings determine how a particle’s image or Mesh is transformed, shaded and overdrawn by other particles.

The Renderer module view

## Using the Renderer module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an existing GameObject, Unity adds the Renderer module to the Particle System. Unity enables this module by default.

To create a new Particle System, go to **GameObject** > **Effects** and click on the **Particle System** option. Unity then creates a new Particle System GameObject and selects it in the Hierarchy window. In the Inspector window, the Particle System component contains all settings and modules related to the Particle System. Select the Renderer module to display options for this module.

### API

Because this module is part of the Particle System component, you access it through the ParticleSystem class. For more information on how to access this class and change values at runtime, see Renderer module.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**Property:** | **Function:**  
---|---  
**Render Mode** | How Unity produces the rendered image from the graphic image (or Mesh). For more information, see Render Mode and Billboard render modes.  
| **Billboard** | Unity renders the particles as billboards and they face the direction you specify in **Render Alignment**.  
| **Stretched Billboard** | The particles face the ****Camera**** with various possible scaling options applied.  
|  | Camera Scale | This setting is only available when you use the **Stretched Billboard** Render mode.  
  
Stretches particles according to Camera movement. Set this to zero to disable Camera movement stretching.  
|  | Velocity Scale | This setting is only available when you use the Stretched Billboard Render mode.  
  
Stretches particles proportionally to their speed. Set this to zero to disable stretching based on speed.  
|  | Length Scale | This setting is only available when you use the Stretched Billboard Render mode.  
  
Stretches particles proportionally to their current size along the direction of their velocity. Setting this to zero makes the particles disappear, having effectively zero length.  
|  | Freeform Stretching | This setting is only available when you use the Stretched Billboard Render mode.  
  
Indicates whether particles should use freeform stretching. With this stretching behavior, particles don’t become thin when you view them head-on.  
|  | Rotate With Stretch | This setting is only available when you use the Stretched Billboard Render mode.  
  
Indicates whether to rotate particles based on the direction they stretch in. This is added on top of other particle rotation. This property only has an effect when you enable **Freeform Stretching**. If you disable **Freeform Stretching** , particles always rotate based on the direction they stretch in, even if **Rotate With Stretch** is disabled.  
| **Horizontal Billboard** | The particle plane is parallel to the XZ “floor” plane.  
| **Vertical Billboard** | The particle is upright on the world Y-axis, but turns to face the Camera.  
| **Mesh** | Unity renders the particle from a 3D Mesh instead of a Billboard. For more information on the specific settings for the Mesh Render mode, see the Details section below.  
|  | Mesh Distribution | Specifies the method that Unity uses to randomly assign meshes to particles.  
  
This setting is only available when you use the **Mesh** Render mode.  
|  |  | Uniform Random | Unity randomly assigns meshes to particles with an even weighting. The Particle System as a whole should contain a roughly equal number of each possible mesh at any given moment.  
  
This setting is only available when you use the **Mesh** Render mode.  
|  |  | Non-uniform Random | Unity randomly assigns meshes to particles with user-defined weights for each mesh.  
  
When this setting is enabled, the Renderer module Inspector window displays a Meshes list and a Mesh Weightings field for each mesh in the list. You can use the Mesh Weightings field to control how often Unity assigns each mesh to a particle.  
  
This setting is only available when you use the **Mesh** Render mode.  
|  | Mesh Weightings | Controls how likely Unity is to assign this mesh to a particle. The weights work relative to each other; Unity is twice as likely to assign a mesh with double the weight of another mesh, regardless of their absolute value. For more information, see Mesh Distribution: Non-uniform random in the Details section below.  
  
This setting is only available when you use the **Mesh** Render mode and the **Mesh Distribution** property is set to “Non-uniform Random”.  
| **None** | Unity doesn’t render any particles. This can be useful alongside the Trails module, if you want to only render the trails and hide any default particle rendering.  
**Normal Direction** | Specifies how to calculate lighting for the billboard. A value of 0 means Unity calculates lighting as though the billboard was a sphere. This results in the billboard looking more like a sphere. A value of 1 means Unity calculates lighting for the billboard as a flat quad.  
  
This property is only available when using one of the Billboard rendering modes: **Billboard** , **Stretched Billboard** , **Horizontal Billboard** or **Vertical Billboard**.  
**Material** | The material Unity uses to render the particles.  
**Trail Material** | The material Unity uses to render particle trails.  
  
This option is only available when the **Trails** module is enabled.  
**Sort Mode** | The order in which Unity draws and overlays particles with a Particle System.  
| None | When this setting is enabled, Unity doesn’t sort particles.  
| By Distance | Sorts particles in the system based on distance to the active Camera. Unity renders particles closer to the Camera on top of those that are further away. The order of particles doesn’t change when you rotate the camera with the setting.  
| Oldest in Front | Unity renders particles that have existed the longest at the front of the Particle System.  
| Youngest in Front | Unity renders particles that have existed for the shortest time at the front of the Particle System.  
| By Depth | Unity renders particles based on their distance from the camera’s near plane. The order of particles can change when you rotate the camera with this setting.  
**Sorting Fudge** | The bias of the Particle System sort ordering. Lower values increase the relative chance that Unity draws Particle Systems over other transparent GameObjects, including other Particle Systems. This setting only affects Particle Systems as a whole that appear in the **scene** \- it does not perform sorting on individual particles within a system.  
**Min Particle Size** | The smallest particle size (regardless of other settings), expressed as a fraction of viewport size.  
  
This property is only available when using one of the Billboard rendering modes: **Billboard** , **Stretched Billboard** , **Horizontal Billboard** or **Vertical Billboard**.  
**Max Particle Size** | The largest particle size (regardless of other settings), expressed as a fraction of viewport size.   
  
This property is only available when using one of the Billboard rendering modes: **Billboard** , **Stretched Billboard** , **Horizontal Billboard** or **Vertical Billboard**.  
**Render Alignment** | This property determines the direction that particle billboards face.  
| View | Particles face the Camera plane.  
| World | Particles align with the world axes.  
| Local | Particles align to the ****Transform component**** of their GameObject.  
| Facing | Particles face the direct position defined by the Transform component in the GameObject of the active Camera.  
| Velocity | Particles face in the same direction as their velocity vector.  
**Enable Mesh GPU Instancing** | This property is only available when using the Mesh render mode.  
  
This property controls whether Unity renders the Particle System using GPU Instancing. This requires the use of a compatible shader. For more information, see Particle Mesh GPU Instancing.  
**Flip** | Mirror a proportion of the particles across the specified axes. A higher value flips more particles.  
**Allow Roll** | Controls whether camera-facing particles can rotate around the Z-axis of the camera. Disabling this can be particularly useful for **VR** applications, where HMD (Head-Mounted Display) roll can cause undesirable particle rotation for Particle Systems.  
**Pivot** | Modify the central pivot point for rotating particles. The value is a multiplier of the particle size.  
**Visualize Pivot** | Preview the particle pivot points in the **Scene** View.  
**Masking** | Set how the particles rendered by the Particle System behave when they interact with a ****Sprite** Mask**.  
| No Masking | The Particle System does not interact with any **Sprite Masks** in the Scene. This is the default option.  
| Visible Inside Mask | The particles are visible where the Sprite Mask overlays them, but not outside of it.  
| Visible Outside Mask | The particles are visible outside of the Sprite Mask, but not inside it. The Sprite Mask hides the sections of the particles it overlays.  
**Apply Active Color Space** | When rendering in Linear Color Space, the system converts particle colors from Gamma Space before it uploads them to the GPU.  
**Custom Vertex Streams** | Configure which particle properties are available in the Vertex **Shader** of your Material. For more information, see Particle System vertex streams and Standard Shader support.  
**Cast Shadows** | If this property is enabled, the Particle System creates shadows when a shadow-casting Light shines on it.  
| On | Enables shadows for this Particle System.  
| Off | Disables shadows for this Particle System.  
| Two-Sided | Select **Two Sided** to allow shadows to be cast from either side of the Mesh. Backface culling is not taken into account when this property is enabled.  
| Shadows Only | Select **Shadows Only** to make it so that the shadows are visible, but the Mesh itself is not.  
**Shadow Bias** | Move the shadows along the direction of the light. This removes shadowing artifacts caused by approximating volumes with billboards.  
**Motion Vectors** | Set whether to use motion vectors to track the per-pixel, screen-space motion of this Particle System’s Transform component from one frame to the next.  
  
**Note:** Not all platforms support motion vectors. See SystemInfo.supportsMotionVectors for more information.  
| Camera Motion Only | Use only Camera movement to track motion.  
| Per Object Motion | Use a specific pass to track motion for this Renderer.  
| Force No Motion | Do not track motion.  
**Receive Shadows** | Dictates whether particles in this system can receive shadows from other sources. Only opaque materials can receive shadows.  
**Sorting Layer ID** | The name of the Renderer’s sorting layer.  
**Order in Layer** | This Renderer’s order within a sorting layer.  
**Light Probes** | Probe-based lighting interpolation mode.  
**Reflection Probes** | If enabled, and if reflection probes are present in the Scene, Unity assigns a reflection texture from the nearest reflection probe to this GameObject and sets the texture as a built-in Shader uniform variable.  
**Anchor Override** | A Transform that determines the interpolation position when you use the Light Probe or Reflection Probe systems.  
  
##  Details

###  Render Mode

Use **Render Mode** to choose between several 2D Billboard graphic modes and a Mesh mode. 3D Meshes give particles extra authenticity when they represent solid GameObjects, such as rocks, and can also improve the sense of volume for clouds, fireballs and liquids. Meshes must be read/write enabled to work in the Particle System’s **Mesh** Render Mode. When you assign meshes to a Particle System (using the **Meshes** list in the Inspector window), Unity automatically enables the read/write enabled setting for those meshes.

####  Billboard render modes

When you use 2D billboard graphics, the different render modes can produce a variety of results that make them suitable for specific uses:

  * Billboard mode is useful for particles that represent volumes that look similar from any direction (such as clouds).
  * Horizontal Billboard mode is useful when the particles cover the ground (such as target indicators and magic spell effects) or when they are flat objects that fly or float parallel to the ground.
  * Vertical Billboard mode keeps each particle upright and perpendicular to the XZ plane, but allows it to rotate around its y-axis. This can be helpful when you are using an orthographic Camera and want particle sizes to stay consistent.
  * Stretched Billboard mode accentuates the apparent speed of particles in a similar way to the “stretch and squash” techniques used by traditional animators. Note that in Stretched Billboard mode, particles are aligned to face the Camera and also aligned to their velocity. This alignment occurs regardless of the Velocity Scale value - even if Velocity Scale is set to 0, particles in this mode still align to the velocity.

When you use Billboard render modes, you can use the Normal Direction to create spherical shading on the flat rectangular billboards. This can help create the illusion of 3D particles if you use a Material that applies lighting to your particles. 

###  Mesh Distribution: Non-uniform Random

The Renderer module Inspector window, with a **Mesh Weightings** input highlighted

When **Mesh Distribution** is set to **Non-uniform Random** , you can customize how often Unity randomly assigns specific meshes to particles. To do this, you use the **Meshes** list and the **Mesh Weighting** field. 

In the **Meshes** list, the field on the left contains the mesh you want the Particle System to use, and the field on the right (highlighted in the image above) contains the Mesh Weighting for that mesh. Use the Mesh Weighting field for each mesh to control how often Unity assigns that mesh to a particle, relative to every other mesh. This is set to 1 by default, which results in the likelihood that Unity assigns a mesh being equal.

To add a mesh to the Meshes list, select the Add (+) icon. To remove a mesh from the Meshes list, select the mesh, then select the Remove (-) icon.

* * *

  * 2018–10–16 Page published 

  * GPU instancing added in Unity 2018.1

  * New particle system options added to Renderer module in 2018.3 NewIn20183