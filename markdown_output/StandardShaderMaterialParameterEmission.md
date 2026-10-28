---
title: "Emission"
category: "General"
source_file: "StandardShaderMaterialParameterEmission.html"
doc_type: "manual"
---

# Emission

Adding emission to a Material makes it appear as a visible source of light in your **Scene**. The Material emission properties control the color and intensity of light that the surface of a Material emits.

Emission is useful when you want some part of a **GameObject** to appear lit from the inside, such as the screen of a monitor, the disc brakes of a car braking at high speed, or glowing buttons on a control panel. GameObjects that use emissive Materials appear to remain bright even in dark areas of your Scene.

Red, Green, and Blue spheres using emissive Materials. Even though they are in a dark Scene, they appear to be lit from an internal light source.

# Using Emission

You can define basic emissive Materials with a single color and emission level. To make a Material emissive, enable the **Emission** checkbox. This exposes the **Color** and ****Global Illumination**** properties. 

## Properties

**Property** | **Description**  
---|---  
**Color** | Specifies the color and intensity of the emission. Click the **Color** box to open the ****HDR** Color** picker. Here you can alter the color of the illumination and the **Intensity** of the emission. To specify which areas of the Material emit light, you can assign an emission map to this property. If you do this, Unity uses the full color values of the map for the emission color and brightness. You can also use the HDR color picker to tint the map and change the emission intensity.  
**Global Illumination** | Specifies how the light that this Material emits affects the contextual lighting of other nearby GameObjects. There are three options:  
• **Realtime** : Unity adds the emissive light from this Material to the **Realtime** Global Illumination calculations for the Scene. This means that this emissive light affects the illumination of nearby GameObjects, including ones that are moving.  
• **Baked** : Unity bakes the emissive light from this Material into the static Global Illumination lighting for the Scene. This Material affects the lighting of nearby static GameObjects, but not dynamic GameObjects. However, Light Probes still affect the lighting of dynamic GameObjects.  
• **None** : The emissive light from this Material does not affect Realtime lightmaps, Baked lightmaps, or Light Probes in the Scene. It does not illuminate or affect other GameObjects. The Material itself does have the emission color.  
  
## Emission map examples

Shown in the inspector, Left: An emission map for a computer terminal. It has two glowing screens and glowing keys on a keyboard. Right: The emissive Material using the emission map. The Material has both emissive and non-emissive areas. In this image, there are areas of high and low levels of light, and shadows falling across the emissive areas which gives a full representation of how emissive Materials look under varying light conditions. Baked emissive values from the computer terminal’s emission map light up the surrounding areas in this dark Scene

* * *

  * 2019–11–21 Page amended