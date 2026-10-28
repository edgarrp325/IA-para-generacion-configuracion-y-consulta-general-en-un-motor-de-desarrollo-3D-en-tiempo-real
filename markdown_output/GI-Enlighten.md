---
title: "Lightmapping using Enlighten Baked Global Illumination"
category: "General"
source_file: "GI-Enlighten.html"
doc_type: "manual"
---

# Lightmapping using Enlighten Baked Global Illumination

The **Enlighten** Baked **Global Illumination** lightmapping backend is deprecated and no longer visible in the user interface by default since 2022.2. It is no longer present from 2023.1 onwards.

Enlighten Baked Global Illumination relies on precomputed real-time global illumination data to generate indirect lighting. This can be an advantage, because you can produce new **lightmaps** fairly quickly after changing the **scene** fairly quickly after changing the **scene** ’s lighting. However, Enlighten Baked Global Illumination imposes more UV layout limitations than the Progressive **Lightmapper** ’s lighting. However, Enlighten Baked Global Illumination imposes more UV layout limitations than the Progressive **Lightmapper**.

## Render pipeline support

See render pipeline feature comparison for more information about support for Enlighten Baked Global Illumination across **render pipelines**

## Using the Enlighten lightmapper

To make the Enlighten Baked Global Illumination option visible in the user interface, open **Edit** > **Project Settings** > **Editor**. In the **Graphics** section of the **Editor** menu, activate the **Enable Enlighten for Baked GI (Legacy)** setting.

After you make Enlighten Baked Global Illumination visible in the user interface, you can enable it in the **Lighting** window. Go to **Window** > **Rendering** > **Lighting** , navigate to **Lightmapping Settings** in the **Lighting** window, and set **Lightmapper** to **Enlighten**.

You can perform many of the functions available in this window via **scripts** , using the LightingSettings API.

The following properties are specific to Enlighten. To expose them, select Enlighten in the Lightmapper control.

**Property:** | **Function:**  
---|---  
**Final Gather** | Calculates the final global illumination light bounce of at the same resolution as the baked lightmap. This improves visual quality, but requires additional time to bake the lighting. If Final Gather is enabled, it exposes the settings Ray Count and Denoising.  
**Indirect Resolution** | Use this to specify the number of samples the lightmapper uses for indirect lighting calculations. Higher values can improve the quality of the lightmaps, but increase the time it takes to bake them.  
| **Ray Count** | Specifies the number of rays the lightmapper emits for every final gather point.  
| **Denoising** | Applies a denoising filter to the final gather output.  
  
## Disabling the default environment contribution

Unity automatically generates an ambient probe and a default Reflection Probe to ensure that environment lighting affects your scene and the **GameObjects**

To disable the environment contribution in the lighting result for a scene or GameObject that does not have manually created light maps and **Light Probes** , disable the default **Reflection Probe** , disable the default **Reflection Probe** and the ambient probe. For more information, see Disabling the SkyManager.