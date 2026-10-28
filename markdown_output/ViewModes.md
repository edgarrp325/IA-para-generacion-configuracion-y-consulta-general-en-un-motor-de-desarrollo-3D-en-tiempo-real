---
title: "Scene view View Options toolbar"
category: "General"
source_file: "ViewModes.html"
doc_type: "manual"
---

# Scene view View Options toolbar

You can use the **Scene** view View Options **toolbar** view View Options **toolbar** overlay to choose various options for viewing the Scene and to enable/disable lighting and audio. These controls only affect the **Scene view** overlay to choose various options for viewing the Scene and to enable/disable lighting and audio. These controls only affect the **Scene view** during development and have no effect on the built game.

## Draw mode menu

The first dropdown menu selects which **Draw Mode** will be used to depict the Scene. The available options are:

**Draw Mode** |  | **Function**  
---|---|---  
**Shading Mode** |  |   
| Shaded | Show surfaces with their textures visible.  
| Wireframe | Draw meshes with a wireframe representation.  
| Shaded Wireframe | Show meshes textured and with wireframes overlaid.  
**Miscellaneous** |  |   
| Shadow Cascades | Show directional light shadow cascades.  
| Render Paths | Show the rendering path for each GameObject using a color code:   
  
Blue indicates deferred shading for each GameObject using a color code:   
  
Blue indicates deferred shading  
Yellow indicates forward rendering  
Yellow indicates forward rendering  
Red indicates vertex lit  
| Alpha Channel | Render colors with alpha.  
| Overdraw | Render **GameObjects** as transparent “silhouettes”. The transparent colors accumulate, making it easy to spot places where one object is drawn over another.  
| Mipmaps | Show ideal texture sizes using a color code:   
  
Red indicates that the texture is larger than necessary (at the current distance and resolution)  
Blue indicates that the texture might be larger. The ideal texture sizes depend on the resolution at which your application will run and how close the Camera can get to particular surfaces.  
| Texture Streaming | Tint GameObjects green, red, or blue, depending on their status in the Texture Streaming system. For more information, see documentation on Texture Streaming debugging.  
| **Sprite** Mask | Sprite Masks are used to either hide or reveal parts of a Sprite or group of Sprites. See Sprite Masks for more information.  
**Deferred** |  | These modes let you view each of the elements of the G-buffer (**Albedo** , **Specular** , **Smoothness** and **Normal**) in isolation. See documentation on Deferred Shading for more information.  
**Global Illumination** |  | The following modes are available to help visualize aspects of the Global Illumination system: **Systems** , **Clustering** , **Lit Clustering** , **UV Charts** , and **Contributors/Receivers**. See documentation on GI Visualisations for information about each of these modes.  
**Realtime Global Illumination** |  | The following modes are available to help visualize aspects of the Enlighten Realtime Global Illumination system: **Albedo** , **Emissive** , **Indirect** , and **Directionality**. See documentation on GI Visualisations for information about each of these modes.  
**Baked Global Illumination** |  | The following modes are available to help visualize aspects of the Baked Global Illumination system: **Baked Light Map** , **Directionality** , ****Shadowmask**** , **Albedo** , **Emissive** , **UV Charts** , **Texel Validity** , **UV Overlap** , **Baked**Lightmap**** , **Albedo** , **Emissive** , **UV Charts** , **Texel Validity** , **UV Overlap** , **Baked**Lightmap** Culling**, **Lightmap Indices** , and **Light Overlap**. See documentation on GI Visualisations for information about each of these modes.  
**Material Validator** |  | There are two **Material Validator** modes: **Albedo** and **Metal Specular**. These allow you to check whether your physically-based materials use values within the recommended ranges. See Physically Based Material Validator for more information.   
  
## 2D, lighting and Audio switches

To the right of the **Render Mode** menu are three buttons that switch certain Scene view options on or off:

  * **2D** : switches between 2D and 3D view for the Scene. In 2D mode the **camera** is oriented looking towards positive z, with the x-axis pointing right and the y-axis pointing up.
  * **Lighting** : turns Scene view lighting (lights, object shading, etc) on or off.
  * **Audio** : turns Scene view **audio effects** on or off.

## Effects button and menu

The menu (activated by the icon to the right of the **Audio** button) has options to enable or disable rendering effects in the Scene view.

  * **Skybox** : a skybox texture rendered in the Scene’s background
  * **Fog** : gradual fading of the view to a flat color with distance from the camera.
  * **Flares** : **lens flares** on lights.
  * **Always Refresh** : Defines whether animated materials display the animation. When selected, any time-based effects (for example, Shaders) will animate. For example, Scene effects (like grass waving on a Terrain).
  * **Post Processing** : Shows Post-processing effects.
  * **Particle Systems** : Shows Particle System effects.

The **Effects** button itself acts as a switch that enables or disables all the selected effects at once.

## Scene visibility switch

The Scene visibility switch toggles Scene visibility for GameObjects on and off. When it’s on, Unity applies the Scene visibility settings. When it’s off, Unity ignores them.

For more information, see the documentation on Scene Visibility.

## Camera settings menu

The Camera settings menu contains options for configuring the Scene view camera. For more information, see the documentation on Camera settings.

## Gizmos menu

The **Gizmos** menu contains options for how objects, icons, and gizmos are displayed. This menu is available in both the Scene view and the Game view. See documentation on the Gizmos Menu manual page for more information.

# Additional resources

  * Overlays
  * Display or hide an overlay