---
title: "Lighting Mode: Baked Indirect"
category: "General"
source_file: "LightMode-Mixed-BakedIndirect.html"
doc_type: "manual"
---

# Lighting Mode: Baked Indirect

This page describes the behavior of all Mixed Lights in a **Scene** in a **Scene** , when that Scene uses a Lighting Settings Asset with its Lighting Mode property set to **Baked Indirect**.

When you set a Scene’s Lighting Mode to **Baked Indirect** , Mixed Lights behave like Realtime Lights, with the additional benefit of baking indirect lighting into **lightmaps** , with the additional benefit of baking indirect lighting into **lightmaps**. **GameObjects**. **GameObjects** lit by Mixed Lights cast real-time shadows up to the Shadow Distance you define in the Project.

## Render pipeline support

See render pipeline feature comparison for more information about support for Baked Indirect Lighting Mode across **render pipelines**

## Mixed Light behavior

When you set a Scene’s Lighting Mode to **Baked Indirect** , Mixed Lights behave as follows:

  * Dynamic GameObjects lit by Mixed Lights receive: 
    * Real-time direct lighting.
    * Baked indirect lighting, using **Light Probes**.
    * Shadows from dynamic GameObjects, using the shadow map, up to the Shadow Distance.
    * Real-time shadows from static GameObjects, using the shadow map, up to the Shadow Distance.
  * Static GameObjects lit by Mixed Lights receive: 
    * Real-time direct lighting.
    * Baked indirect lighting, using lightmaps.
    * Real-time shadows from static GameObjects, using the shadow map, up to the Shadow Distance.
    * Real-time shadows from dynamic GameObjects, using the shadow map, up to the Shadow Distance.

## Setting your Scene’s Lighting Mode to Baked Indirect

  1. Select the Lighting Settings Asset for the Scene.
  2. In the **Inspector** , navigate to **Mixed Lighting**.
  3. Use the drop-down menu to set the **Lighting Mode** to **Baked Indirect**.

## Shadows and runtime performance

Because all shadows from Mixed Lights are real-time in Baked Indirect Lighting Mode, this can impact performance. You can reduce this impact by using the Shadow Distance property to limit the distance up to which Unity draws real-time shadows.

## Changing Light properties at runtime

In the Baked Indirect Lighting Mode, you can subtly change the properties of a Mixed Light at runtime. Changes affect the real-time direct lighting that the Mixed Light contributes to the Scene, without affecting the baked indirect lighting that the Mixed Light contributes to the Scene. This allows you to combine the benefits of baked indirect lighting with some of the dynamic capabilities of a Realtime Light. This works especially well in Baked Indirect Lighting Mode, due to the lack of precomputed shadows.

You must be careful with runtime changes to Light properties, and only make small changes that don’t cause unrealistic combinations of real-time direct and baked indirect lighting. For example, if you bake a red Mixed Light into a lightmap and then change its color to green at runtime, the direct lighting is green but the indirect lighting baked into the lightmap remains red. The same applies to moving a Mixed Light at runtime: direct lighting follows the Light’s new position, but indirect lighting remains at the position at which the Light was baked.

This video shows an example of how to slightly modify a Mixed Light without causing noticeable inconsistencies in the indirect lighting: https://youtu.be/XN6ya31gm1I