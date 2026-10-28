---
title: "Terrain settings"
category: "General"
source_file: "terrain-OtherSettings.html"
doc_type: "manual"
---

# Terrain settings

The final tool on the five-icon **toolbar** is for settings. In the **Inspector** is for settings. In the **Inspector** , click the gear icon to reveal the **Terrain settings**.

## Basic Terrain

**_Property_** | **_Function_**  
---|---  
**Grouping ID** | The grouping ID for the **Auto connect** feature.  
**Auto Connect** | Check this box to automatically connect the current **Terrain** tile to to neighboring tiles sharing the same **Grouping ID**.  
| **Reconnect** | On rare occasions, you might lose connections between Terrain tiles if you change the **Grouping ID** , or disable **Auto connect** for one or more tiles. To recreate connections between tiles, click the **Reconnect** button. **Reconnect** only connects two adjacent tiles if they have the same **Grouping ID** and if both tiles have **Auto Connect** enabled.  
**Draw** | Check this box to enable rendering of the Terrain.  
**Draw Instanced** | Check this box to enable instanced rendering.  
**Pixel Error** | The accuracy of the mapping between Terrain maps (such as heightmaps and Textures) and generated Terrain. Higher values indicate lower accuracy, but with lower rendering overhead.  
**Minimum Detail Limit** | Limits the minimum **level of detail** that the terrain can be reduced to. Enter a value of 0 to not limit the level of detail that the terrain can be reduced to. Values higher than 0 force the terrain to keep a minimum level of detail regardless of what the **Pixel** that the terrain can be reduced to. Enter a value of 0 to not limit the level of detail that the terrain can be reduced to. Values higher than 0 force the terrain to keep a minimum level of detail regardless of what the **Pixel** Error property is set to.  
**Maximum Complexity Limit** | Limits the maximum resolution the terrain can be rendered at. Enter a value of 0 to not limit the maximum resolution the terrain can be rendered at. Values higher than 0 prevent the terrain from rendering at higher levels of complexity regardless of what the Pixel Error property is set to.  
**Base Map Dist.** | The maximum distance at which Unity displays Terrain Textures at full resolution. Beyond this distance, the system uses a lower resolution composite image for efficiency.  
**Cast Shadows** | Use this to define how the Terrain casts shadows onto other objects in the **Scene**. Rendering.ShadowCastingMode controls how the Terrain shadow interacts with Scene objects.  
| _Off_ | The Terrain does not cast shadows.  
| _On_ | The Terrain casts shadows.  
| _Two Sided_ | Casts two-sided shadows from either side of the Terrain. The Progressive **Lightmapper** supports two-sided shadows. **Enlighten** supports two-sided shadows. **Enlighten** Baked and Enlighten Realtime **Global Illumination** do not.  
| _Shadows Only_ | Shadows from the Terrain are visible, but the Terrain itself is not.  
**Reflection Probes** | Use this to set how Unity uses Reflection Probes on Terrain. This setting only has an effect when **Material** is set to **Built In Standard** , or if you use a custom Material (with **Material** set to **Custom**) that supports rendering with reflection.  
| _Off_ | Disables Reflection Probes, and uses a **skybox** for reflection.  
| _Blend Probes_ | Enables Reflection Probes. Blending occurs only between probes. Uses default reflection if there are no Reflection Probes nearby, but no blending between default reflection and probe.  
| _Blend Probes And Skybox_ | Enables Reflection probes. Blending occurs between probes, or between probes and default reflection.  
| _Simple_ | Enables Reflection probes, but no blending occurs between probes when there are two overlapping volumes.  
**Material** | Lets you specify the Material to use for rendering Terrain.  
| **Create** | The **Create** button only appears when you select a default Terrain Material. It does not appear when you select a custom Material. When you click **Create** , Unity creates a copy of the Material in your Project folder, which you can modify, and then automatically selects this new copy.  
  
## Tree and Detail Objects

**_Property_** | **_Function_**  
---|---  
**Draw** | Check this box to draw trees, grass, and details.  
**Bake Light Probes For Trees** | If you check this box, Unity creates internal Light Probes at the position of each tree, and applies them to tree renderers for lighting. These probes are internal, and don’t affect other renderers in the Scene.  
  
If you don’t check this box, trees are still affected by Light Probe Groups. This option is only effective for trees with Light Probe enabled on their prototype Prefab.  
**Remove Light Probe Ringing** | If you check this box, Unity removes visible overshooting, which often appears as ringing on GameObjects that are affected by intense lighting. This setting reduces contrast, and is dependent on Bake Light Probes for Trees. For more information, see Light Probe Groups: Ringing.  
**Preserve Tree Prototype Layers** | Check this box if you want your tree instances to take on the layer values of their prototype **Prefabs** , instead of the Terrain **GameObject** , instead of the Terrain **GameObject** ’s layer values.  
**Tree Motion Vectors** | Set whether to use motion vectors for trees painted on the terrain. Motion vectors track each renderer’s per-pixel, screen-space motion from one frame to the next.   
  
**Note:** Not all platforms support motion vectors. See SystemInfo.supportsMotionVectors for more information.  
  
This property corresponds to the Terrain.treeMotionVectorModeOverride API.  
| **Camera** Motion Only | Use only camera movement to track motion.  
| Per Object Motion | Use a specific pass to track motion.  
| Force No Motion | Do not track motion.  
| Inherit From Prototype | Use the **Motion Vector** property setting of the tree prototype.  
**Detail Distance** | The distance from the camera beyond which details are culled.  
**Detail Density Scale** | Scaling factor applied to the density of all details with the “Affected by Density Scaling” setting enabled. For more information, see Detail Settings.  
**Tree Distance** | The distance from the camera beyond which trees are culled.  
**Billboard Start** | The distance from the camera at which **Billboard** images replace 3D Tree objects.  
**Fade Length** | The distance over which Trees transition between **3D objects** and Billboards.  
**Max Mesh Trees** | The maximum number of visible Trees that are represented as solid 3D meshes. Beyond this limit, Billboards replace Trees.  
**Detail Scatter Mode** | The scatter mode type to be used while painting details. Coverage paints areas details should be populated in based on their density setting, Instance Count paints the amount per sample.  
  
## Wind Settings for Grass

**_Property_** | **_Function_**  
---|---  
**Speed** | The speed of the wind as it blows across the grass.  
**Size** | The size of ripples on grassy areas as the wind blows over them.  
**Bending** | The degree to which the wind bends over grass objects.  
**Grass Tint** | The overall color tint applied to grass objects. The final color that appears is the **Grass Tint** multiplied by the **Healthy Color** and **Dry Color** settings of each grass object.  
  
**Wind Settings for Grass** have no connection with Wind Zone components. The two are unrelated.

## Mesh Resolution

**_Property_** | **_Function_**  
---|---  
**Terrain Width** | The size of the Terrain GameObject in its X-axis, in world units.  
**Terrain Length** | The size of the Terrain GameObject in its Z-axis, in world units.  
**Terrain Height** | The difference in Y-coordinate between the lowest possible **heightmap** value and the highest one, in world units.  
**Detail Resolution Per Patch** | The number of cells in a single patch (mesh). This value is squared to form a grid of cells, and must be a divisor of the detail resolution.  
**Detail Resolution** | The number of cells available for placing details onto the Terrain tile. This value is squared to make a grid of cells.  
  
## Holes Settings

**_Property_** | **_Function_**  
---|---  
**Compress Holes Texture** | If you check this box, Unity compresses the Terrain Holes Texture to the DXT1 graphics format in the Player during runtime. If you don’t check this box, Unity does not compress the Texture.  
  
## Texture Resolutions

**_Property_** | **_Function_**  
---|---  
**Heightmap Resolution** | The pixel resolution of the Terrain’s heightmap. This value must be a power of two plus one, for example, 513, which is 512 + 1.  
**Control Texture Resolution** | The resolution of the splatmap that controls the blending of the different Terrain Textures.  
**Base Texture Resolution** | The resolution of the composite Texture to use on the Terrain when you view it from a distance greater than the Basemap Distance.  
  
**Require resampling on change** indicates that when you change properties under **Texture Resolutions** , the Editor resizes the Terrain tile’s content to the new size you specify, which can potentially affect the quality of your content.

### Heightmap Import/Export buttons

The **Import Raw** and **Export Raw** buttons allow you to set or save the Terrain’s heightmap to an image file in the RAW grayscale format. You can create RAW format files in third-party terrain editing tools (such as Bryce), and you can open, edit, and save them in Photoshop. This allows for sophisticated generation and editing of terrains outside Unity.

## Lighting

**_Property_** | **_Function_**  
---|---  
**Contribute Global Illumination** | Enable this check box to indicate to Unity that the Terrain influences Global Illumination computations. When you enable this property, **Lightmapping** properties appear.  
**Receive Global Illumination** | You can only configure this option if you’ve enabled **Contribute Global Illumination** above. If you don’t enable **Contribute Global Illumination** , the Terrain registers as non-static, and receives Global Illumination from **Light Probes**.  
  
## Lightmapping

**_Property_** | **_Function_**  
---|---  
**Scale in Lightmap** | Lets you specify the relative size of an object’s UVs within a **lightmap**. If you set this to zero, the object is not lightmapped, but still contributes lighting to other objects in the Scene. A value greater than 1.0 increases the number of pixels (the lightmap resolution) used for this GameObject, while a value less than 1.0 decreases it.  
**Lightmap Parameters** | Lets you adjust advanced parameters that affect the process of generating a lightmap for an object using global illumination. See Lightmap Parameters for more information about these settings.  
**Rendering Layer Mask** | Determines which rendering layer this Terrain lives on. When you use a scriptable render pipeline, you can specify an additional rendering-specific **layer mask**  
  
## Quality Settings

**Property** | **Function**  
---|---  
**Ignore Quality Settings** | If you check this box, this Terrain ignores the Terrain Override Settings set in the Quality settings.  
  
## Terrain Collider

The Terrain **Collider** component manages **collisions** component manages **collisions** on the terrain. For details about the **Terrain Collider** on the terrain. For details about the **Terrain Collider** component properties, see the Terrain Collider component reference.

* * *

  * 2022–07–20 Page amended 

  * Updated content to reflect new quality change settings and updated UI