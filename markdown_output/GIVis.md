---
title: "Scene View Draw Modes for lighting"
category: "General"
source_file: "GIVis.html"
doc_type: "manual"
---

# Scene View Draw Modes for lighting

The **Scene** view has a number of Draw Modes to help you understand and debug the lighting in your Scene.

Use the **Scene view** control bar to select your desired Draw Mode.

## Shading Mode

### Shaded

The default **Shading Mode** is **Shaded**. This shows the Scene fully lit according to the current lighting setup.

## Miscellaneous

### Shadow Cascades

Uses color to show the parts of the Scene using different cascade levels. Use this to help you get the shadow distance, cascade count and cascade split ratios just right. Note that this visualization use the Scene view far plane, which is usually bigger than the shadow distance, so you might need to lower the Shadow distance if you want to match the in-game behavior of the **Camera** with a small far plane.

Shadow Cascades draw mode in the Scene View

## Global Illumination

### Systems

The precompute stage will automatically subdivide the scene into systems (i.e. groups of objects sharing the same real-time lightmap) based on proximity and **Lightmap** Parameters. This is done to allow multithreading and optimizations when updating indirect lighting. This visualization shows the systems with different colors.

### Clustering

Enlighten calculates visibility information for geometry with **Contribute GI** enabled. It does this by making use of clusters generated during the Clustering step. This view displays those clusters, which should be larger than lightmap texels. The Cluster Resolution parameter in Lightmap Parameters determines this ratio. Converting geometry to clusters can be quite memory intensive if the scale of the geometry isn’t correct. Large scenes can generate more clusters than Unity can store in your system’s memory. If you are seeing high memory usage or long baking times it could be because the static geometry in your scene splits into many more clusters than necessary. The clustering scene view mode can help you identify the geometry in need of UVs or Indirect Resolution adjustments.

Both **Enlighten** Baked **Global Illumination** (deprecated and no longer visible in the user interface by default) and Enlighten Realtime Global Illumination depend on these calculations to compute indirect lighting. See Lightmapping using Enlighten Baked Global Illumination for information about how to make Enlighten visible in the user interface as an option for light baking.

### Lit Clustering

This is the Clustering view with Enlighten Realtime Global Illumination applied.

### UV Charts

This shows the optimized UV layout used when calculating Enlighten Realtime Global Illumination. It is automatically generated during the precompute process. It is available as soon as the Instance precompute stage is completed. The UV Charts scene view mode can help you identify the geometry that needs to have UVs or scale adjusted (use the Resolution parameter in Lightmap Parameters to change scale). This view is also useful when adjusting the Indirect Resolution. Each chart has a different color.

### Contributors/Receivers

This Draw Mode draws **Mesh** Renderers and **Terrain** Renderers and **Terrain** in different colors based on whether **ContributeGI** is enabled in their Static Editor Flags, and the value of their ReceiveGI property.

In the default colors:

  * Yellow means that **ContributeGI** is not enabled in the **GameObject** ’s Static Editor Flags.
  * Blue means that **ContributeGI** is enabled in the GameObject’s Static Editor Flags, and the Renderer’s **ReceiveGI** property is set to **Lightmaps**.
  * Red means that **ContributeGI** is enabled in the GameObject’s Static Editor Flags, and the Renderer’s **ReceiveGI** property is set to ****Light Probes****.

You can customize the default colors in the Preferences window.

## Realtime Global Illumination

### Albedo

Enabling **Show lightmap resolution overlay** in the Editor Manager settings indicates the albedo that **lightmappers**

### Emissive

Shows the emission used when calculating the GI. It is generated from the material information and can be fully customized by adding a custom meta pass.

### Indirect

The Indirect view displays indirect lighting as captured in the lightmaps that Enlighten Baked Global Illumination generates. Irradiance is a radiometric unit that describes how much power (radiant flux) a surface receives per unit area. Unity uses the irradiance texture to store indirect light data at runtime. If you disable Enlighten Baked Global Illumination, the Indirect view mode isn’t selectable.

In the Indirect view mode, you can use a Lightmap Exposure control to help you assess **HDR** lightmaps more effectively.

Comparison of Indirect Lightmaps with different exposure values

  1. **Default Exposure** : The lightmap exposure slider at the default value of 0.
  2. **Altered Exposure** : Here the lightmap exposure slider is at a value of –1.

### Directionality

This view shows the most dominant light direction vector. Please refer to the Directional Lightmapping page for more info.

## Baked Global Illumination

### Baked Lightmap

The Baked Lightmap view displays baked lightmaps applied to the Scene geometry. In this mode, you can use a Lightmap Exposure control to help you assess HDR lightmaps more effectively.

Scenes with high lighting intensities might require you to use exposure compensation to bring the Baked Lightmap Scene View into an easily readable range.

Comparison of Baked Lightmaps with different exposure values

  1. **Default Exposure** : The lightmap exposure slider at the default value of 0.
  2. **Altered Exposure** : Here the lightmap exposure slider is at a value of 4.

### Shadowmask

This displays the **shadowmask** texture occlusion values. It colors the mesh and the light **gizmo** texture occlusion values. It colors the mesh and the light **gizmo** in the same color so one can verify that the light occlusion factors have been baked as expected.

### Texel Validity

This mode shows which texels are marked invalid because they mostly “see” backfaces. During lightmap baking, Unity emits rays from each texel. If a significant portion of a texel’s rays are hitting backface geometry, this texel is marked invalid. This is because the texel should not be able to see the backfaces in the first place. Unity handles this by replacing invalid texels with valid neighbors. You can adjust this behaviour using the **Backface Tolerance** parameter (**LightmapParameters** > **General GI**).

This view is not compatible with Enlighten Baked Global Illumination.

### UV Overlap

If lightmap charts are too close together in UV space, the **pixel** values inside them might bleed into one another when the lightmap is sampled by the GPU. This can lead to unexpected artifacts. This mode allows you to identify texels that are too close to texels in other charts. This is useful when you want to troubleshoot your UV issues.

This view is not compatible with Enlighten Baked Global Illumination.

## Light Overlap

This mode allows you to see if all static lights have been baked to the shadowmask. If an area of the level is lit by more than four static lights, the exceeding lights will fallback to fully baked and be displayed in red. Relevant for this calculation is not the actual lit surface, but the intersection of the light sources’ volumes. So even though in the screenshot below it looks as if the colored spots on the mesh do not overlap, the cones of the four spot lights end up overlapping below the ground plane along with the directional light.

  * [GI Contributors/Receivers Draw Mode] added in 2020.1 NewIn20201