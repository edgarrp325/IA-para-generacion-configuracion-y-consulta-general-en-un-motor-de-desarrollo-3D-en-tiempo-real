---
title: "The Lighting window"
category: "General"
source_file: "lighting-window.html"
doc_type: "manual"
---

# The Lighting window

The Lighting window (menu: **Window** > **Rendering** > **Lighting**) is the main control point for Unity’s lighting features. You can use the Lighting window to adjust settings related to the lighting in your Scene, and to optimise your precomputed lighting data for quality, bake time, and storage space.

## Related APIs

You can perform many of the functions available in the Lighting window in **scripts** , using the LightingSettings and Lightmapping APIs.

## Lighting window layout

The Lighting window contains the following elements:

  * The Scene tab
  * The Environment tab
  * The Realtime Lightmaps tab
  * The Baked Lightmaps tab
  * The control area, at the bottom of the window

## The Scene tab

The **Scene** tab displays information about the Lighting Settings Asset that is assigned to the active Scene. If no Lighting Settings Asset is assigned to the active Scene, it displays information about the default LightingSettings object.

The Scene tab is divided into several sections:

  * Lighting Settings Asset controls
  * Lighting settings \- Realtime Lighting, Mixed Lighting and Lightmapping settings
  * Workflow Settings

### Lighting Settings Asset controls

Use the controls in this section to assign a Lighting Settings Asset to the active Scene, or to create a new Lighting Settings Asset.

**Property:** | **Function:**  
---|---  
**Lighting Settings** | The Lighting Settings Asset assigned to the active Scene.  
**New Lighting Settings** | Click this button to generate a new Lighting Settings Asset in your Project, and automatically assign the new Lighting Settings Asset to the active Scene.  
  
### Lighting Settings

Use this section to view and edit the properties of the Lighting Settings Asset or `LightingSettings` object assigned to the current Scene. See Lighting Settings Asset.

### Workflow settings

This section contains settings that help you debug your Scene.

**Property:** | **Function:**  
---|---  
**GPU Baking Device** | Use this to change the GPU that Unity uses for precomputing lighting data. This property is visible only when you use the GPU Progressive Lightmapper backend.  
**Light Probe Visualization** | Use this to filter which Light Probes are visualized in the **Scene view** are visualized in the **Scene view**. The default value is **Only Probes Used By Selection**.  
| Only Probes Used By Selection | Only Light Probes that affect the current selection are visualized in the Scene view.  
| All Probes No Cells | All Light Probes are visualized in the Scene view.  
| All Probes With Cells | All Light Probes are visualized in the Scene view, and the tetrahedrons that are used for interpolation of Light Probe data are also displayed.  
| None | No Light Probes are visualized in the Scene view.  
**Display Weights** | When enabled, Unity draws a line from the Light Probe used for the active selection to the positions on the tetrahedra used for interpolation. This is a way to debug probe interpolation and placement problems.  
**Display Occlusion** | When enabled, Unity displays occlusion data for Light Probes if the **Lighting Mode** is set to **Shadowmask**.  
**Highlight Invalid Cells** | Enable to highlight tetrahedrons that Unity can’t use for indirect lighting. For example if the Light Probes are very close together.  
**Recalculate Environment Lighting** | When enabled, Unity automatically calculates environment lighting using the SkyManager for all open scenes, if you haven’t generated precomputed lighting data.  
  
## The Environment tab

The Environment tab contains settings related to environmental lighting effects for the current Scene. The contents depend on the **render pipeline** that your Project uses.

The Environment tab is divided into two sections:

  * Environment
  * Other settings

#### Environment

The Environment section contains lighting-related settings and controls that apply to the environmental lighting in the current scene, such as the Skybox, diffuse lighting and reflections.

**Property:** | **Function:**  
---|---  
**Skybox Material** | A Skybox is a Material that appears behind everything else in the Scene to simulate the sky or other distant background. Use this property to choose the Skybox you want to use for the Scene. The default value is the built-in Default Skybox.  
**Sun Source** | Select a Light to use as the sun in your Scene. Unity uses this Light to simulate the effect of sun position and intensity on the Skybox and your Scene. If you set this to **None** , Unity considers the brightest directional light in the Scene the sun. Lights whose **Render Mode** property is set to **Not Important** do not affect the Skybox.   
  
For more information about the **Render Mode** setting, see the Additional settings section of Lights.  
**Realtime Shadow Color** | Define the color that Unity uses to render real-time shadows in Subtractive Lighting Mode.  
**Environment Lighting** | This section contains settings that affect ambient light in the current Scene.  
**Source** | Use this to define a source color for ambient light in the Scene. The default value is **Skybox**.  
| **Skybox** | Use the colors of the Skybox set in **Skybox Material** to determine the ambient light coming from different angles. This allows for more precise effects than **Gradient**.  
| **Gradient** | Choose separate colors for ambient light from the sky, horizon and ground, and blend smoothly between them.  
| **Color** | Use a flat color for all ambient light.  
**Intensity Multiplier** | Use this to set the brightness of the ambient light in the Scene, defined as a value between 0 and 8. The default value is 1.  
**Environment Reflections** | This section contains global settings for Reflection Probe baking, and settings that affect global reflections.  
**Source** | Use this setting to specify whether you want to use the Skybox for reflection effects, or a Cubemap of your choice. The default value is **Skybox**.  
| **Skybox** | Select this to use the Skybox as the reflection source.  
| **Custom** | Select this to use either a Cubemap asset or a RenderTexture of type cube for reflections.  
**Resolution** | Use this to set the resolution of the Skybox for reflection purposes. This property is visible only when **Source** is set to **Skybox**.  
**Cubemap** | Use this to specify the Cubemap to use for reflection purposes. This property is visible only when **Source** is set to **Cubemap**.  
**Compression** | Use this to define whether or not reflection textures are compressed. The default setting is **Auto**.  
| **Auto** | The reflection texture is compressed if the compression format is suitable.  
| **Uncompressed** | The reflection texture is stored in memory uncompressed.  
| **Compressed** | The texture is compressed.  
**Intensity Multiplier** | The degree to which the reflection source is visible in reflective objects.  
**Bounces** | A reflection bounce occurs when a reflection from one object is then reflected by another object. Use this property to set how many times the Reflection Probes evaluate bounces back and forth between objects. If this is set to 1, then Unity only takes the initial reflection (from the skybox or cube map specified in the **Reflection Source** property) into account.  
  
#### Other Settings

The Other Settings section contains settings for fog, Halos, Flares and Cookies.

| Property: | Function:  
---|---|---  
**Fog** | Enables or disables fog in the Scene. Note that fog is not available with the Deferred rendering path.  
| Color | Use the color picker to set the color Unity uses to draw fog in the Scene.  
| Mode | Define the way in which the fogging accumulates with distance from the **camera**.  
| **Linear** | Fog density increases linearly with distance.  
| Start | Set the distance from the Camera at which the fog starts.  
| End | Set the distance from the Camera at which the fog completely obscures Scene **GameObjects**.  
| **Exponential** | Fog density increases exponentially with distance.  
| Density | Use this to control the density of the fog. The fog appears more dense as the **Density** increases.  
| **Exponential Squared** | Fog density increases faster with distance (exponentially and squared).  
| Density | Use this to control the density of the fog. The fog appears more dense as the **Density** increases.  
**Halo Texture** | Set the Texture you want to use for drawing a Halo around lights.  
**Halo Strength** | Define the visibility of Halos around Lights, from a value between 0 and 1.  
**Flare Fade Speed** | Define the time (in seconds) over which lens flares fade from view after initially appearing. This is set to 3 by default.  
**Flare Strength** | Define the visibility of lens flares from lights, from a value between 0 and 1.  
**Spot Cookie** | Set the Cookie texture you want to use for Spot Lights. The default is ‘Soft’. To revert to ‘Soft’, select **None**.  
  
## The Realtime Lightmaps tab

The Realtime **Lightmaps** tab shows a list of all lightmaps generated by the **Enlighten** tab shows a list of all lightmaps generated by the **Enlighten** Realtime **Global Illumination** system in the current Scene. If Enlighten Realtime Global Illumination is not enabled in your Project, this tab will be empty.

## The Baked Lightmaps tab

This tab shows a list of all lightmaps generated by lightmapper for the current Scene, along with the Lighting Data Asset. If Baked Global Illumination is not enabled in your Project, this tab will be empty.

## Control area

Controls for precomputing lighting data are at the bottom of the Lighting window.

**Property:** | **Function:**  
---|---  
**Auto Generate** | If **Auto Generate** is enabled, Unity precomputes lighting data automatically when you make changes to the Scene.  
  
This data includes lightmaps for the Baked Global Illumination system, lightmaps for the Enlighten Realtime Global Illumination system, Light Probes, and Reflection Probes.  
  
Unity usually begins the bake a few seconds after you make a change to the Scene. If **Auto Generate** is disabled, you must manually invoke a bake yourself, using the **Generate Lighting** button in the Lighting window, or the Lightmapping.Bake or Lightmapping.BakeAsync APIs.  
  
When you precompute lighting data using **Auto Generate** , Unity does not store the Scene’s precomputed lighting data as Assets in your Project. Instead, Unity stores this data in memory and serializes it as part of the Scene.  
  
This property is only available if the active Scene has a Lighting Settings Asset assigned to it.  
  
Note: From Unity Editor version 2022.2, **Auto Generate** mode is unavailable when the Entities package is installed. When you generate lighting in a project where you have installed the Entities package, the Unity Editor opens all loaded subscenes, which may slow down Editor performance.  
**Generate Lighting** | Select the **Generate Lighting** button to precompute lighting data. This data includes lightmaps for the Baked Global Illumination system, lightmaps for the Enlighten Realtime Global Illumination system, Light Probes, and Reflection Probes. Edits you make after starting the bake process using the **Generate Lighting** button do not affect baked lighting.  
  
Open the **Generate Lighting** dropdown and select **Bake Reflection Probes** to bake only the Reflection Probes for all open Scenes. **Note:** If you select **Bake Reflection Probes** but you haven’t baked the scene before, Unity also bakes lightmaps and Light Probes.  
  
Open the **Generate Lighting** dropdown and select **Clear Baked Data** to clear all precomputed lighting data from all open scenes without clearing the GI Cache.  
  
  
  
* * *

  * [Lighting Settings Asset] added in 2020.1 NewIn20201