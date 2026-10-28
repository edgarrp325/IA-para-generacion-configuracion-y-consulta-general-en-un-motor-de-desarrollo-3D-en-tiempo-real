---
title: "Lighting Mode: Shadowmask"
category: "General"
source_file: "LightMode-Mixed-Shadowmask.html"
doc_type: "manual"
---

# Lighting Mode: Shadowmask

This page describes the behavior of all Mixed Lights in a **Scene** in a **Scene** , when that Scene uses a Lighting Settings Asset with its Lighting Mode property set to ****Shadowmask****.

Similar to Baked Indirect Lighting Mode, Shadowmask Lighting Mode combines real-time direct lighting with baked indirect lighting. However, Shadowmask Lighting Mode differs from Baked Indirect Lighting Mode in the way that it renders shadows. Shadowmask Lighting Mode makes it possible for Unity to combine baked and real-time shadows at runtime and render shadows in the far distance. It does this by using an additional **lightmap** texture known as a shadow mask, and by storing additional information in Light Probes. Unity generates Shadow masks and Light Probe occlusion data for baked shadows.

Shadowmask Lighting Mode provides the highest fidelity shadows among all the Lighting Modes, but has the highest performance cost and memory requirements. It’s suitable for rendering realistic scenes where distant **GameObjects** are visible, such as open worlds, on high-end or mid-range hardware.

## Render pipeline support

See render pipeline feature comparison for more information about support for Shadowmask Lighting Mode across **render pipelines**

## Shadowmask quality settings

Use the Quality Settings panel to set the Shadowmask Mode Unity uses at runtime.

  * ****Distance Shadowmask**** provides greater fidelity shadows at a higher performance cost.
  * **Shadowmask** provides lower fidelity shadows at a lower performance cost.

## Mixed Light behavior

### With the Distance Shadowmask quality setting

When you set a Scene’s Lighting Mode to Shadowmask and your Project uses the Distance Shadowmask quality setting, Mixed Lights behave as follows.

  * Dynamic GameObjects lit by Mixed Lights receive: 
    * Real-time direct lighting.
    * Baked indirect lighting, using Light Probes.
    * Real-time shadows from dynamic GameObjects, using the shadow map, up to the Shadow Distance.
    * Real-time shadows from static GameObjects, using the shadow map, up to the Shadow Distance.
    * Baked shadows from static GameObjects using Light Probes, beyond the Shadow Distance.
  * Static GameObjects lit by Mixed Lights receive: 
    * Real-time direct lighting.
    * Baked indirect lighting, using lightmaps.
    * Real-time shadows from dynamic GameObjects, using the shadow map, up to the Shadow Distance.
    * Real-time shadows from static GameObjects, using the shadow map, up to the Shadow Distance.
    * Baked shadows from static GameObjects, using the shadow mask, beyond the Shadow Distance.

### With the Shadowmask quality setting

When you set a Scene’s Lighting Mode to Shadowmask and your Project uses the Shadowmask quality setting, Mixed Lights behave as follows.

  * Dynamic GameObjects lit by Mixed Lights receive: 
    * Real-time direct lighting.
    * Baked indirect lighting, using Light Probes.
    * Real-time shadows from dynamic GameObjects, using the shadow map, up to the Shadow Distance.
    * Baked shadows from static GameObjects using Light Probes, up to and beyond the Shadow Distance.
  * Static GameObjects lit by Mixed Lights receive: 
    * Real-time direct lighting.
    * Baked indirect lighting, using lightmaps.
    * Real-time shadows from dynamic GameObjects, using the shadow map, up to the Shadow Distance.
    * Baked shadows from static GameObjects, using the shadow mask, up to and beyond the Shadow Distance.

## Setting your Scene’s Lighting Mode to Shadowmask

In the Built-in Render Pipeline:

  1. Select the Lighting Settings Asset for the Scene.
  2. In the **Inspector** , navigate to **Mixed Lighting**.
  3. Use the drop-down menu to set the **Lighting Mode** to **Shadowmask**.
  4. Open the Quality Settings (menu: **Edit** > **Project Settings** , then select the **Quality** category).
  5. Use the Shadowmask Mode drop-down menu to select either **Shadowmask** or **Shadowmask Distance**.

In HDRP:

Follow the instructions in the HDRP Shadowmask Lighting Mode documentation.

## Shadows and runtime performance

You can use the Shadow Distance property to limit the distance up to which Unity draws real-time shadows.

## Shadowmask implementation details

At runtime, Unity uses the shadow mask to determine whether a **pixel** is in shadow or not. The shadow mask Texture contains occlusion information about **baked lights** is in shadow or not. The shadow mask Texture contains occlusion information about **baked lights**. It shares the same UV layout and resolution with its corresponding lightmap. It contains occlusion information for up to four lights per texel, stored in RGBA format.

If more than four lights overlap, any additional lights fall back to Baked Lighting. The baking system determines which lights fall back to Baked Lighting, and this stays consistent across bakes, unless you modify one of the overlapping lights. Light Probes also receive the same information for up to four lights.

Unity computes light overlapping independently of shadow receiving objects. So, an object can get the influence of ten different mixed lights all from the same Shadowmask/Probe channel, as long as those light **bounding volumes** don’t overlap at any point in space. If some lights overlap then Unity uses more channels. And, if a light does overlap while all four channels are already in use, that light falls back to fully baked.