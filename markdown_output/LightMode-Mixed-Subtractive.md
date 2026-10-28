---
title: "Lighting Mode: Subtractive"
category: "General"
source_file: "LightMode-Mixed-Subtractive.html"
doc_type: "manual"
---

# Lighting Mode: Subtractive

This page describes the behavior of all Mixed Lights in a **Scene** in a **Scene** , when that Scene uses a Lighting Settings Asset with its Lighting Mode property set to **Subtractive**.

In Subtractive Lighting Mode, all Mixed Lights in your Scene provide baked direct and indirect lighting. Unity bakes shadows cast by static **GameObjects** into the **lightmaps** into the **lightmaps**. In addition to the baked shadows, one Directional Light, known as the Main Directional Light, provides real-time shadows for dynamic GameObjects.

Because shadows are baked into the lightmaps, Unity doesn’t have the information it needs to accurately combine baked and real-time shadows at runtime. Instead, Unity provides a **Realtime Shadow Color** for reducing the contribution from the lightmap to create the illusion of a correct blend between baked and real-time shadows. You can also tweak the color to achieve a certain artistic style.

Subtractive Lighting Mode is useful on low-end hardware where performance is a concern, and where you need only one real-time shadow casting light. It doesn’t provide particularly realistic lighting effects, and is more suitable for stylized aesthetics, such as cel shading.

## Render pipeline support

See render pipeline feature comparison for more information about support for Subtractive Lighting Mode across **render pipelines**

## Mixed Light behavior

When you set a Scene’s Lighting Mode to Subtractive, Mixed Lights behave as follows.

  * Dynamic GameObjects lit by Mixed Lights receive: 
    * real-time direct lighting
    * baked indirect lighting, using Light Probes
    * real-time shadows from dynamic GameObjects that are lit by the Main Directional Light, using the shadow map, up to the Shadow Distance
    * shadows from static GameObjects, using Light Probes
  * Static GameObjects lit by Mixed Lights receive: 
    * baked direct lighting, using lightmaps
    * baked indirect lighting, using lightmaps
    * baked shadows from static GameObjects, using lightmaps
    * real-time shadows from dynamic GameObjects that are lit by the Main Directional Light, using the shadow map, up to the Shadow Distance

## Setting your Scene’s Lighting Mode to Subtractive

  1. Select the Lighting Settings Asset for the Scene.
  2. In the **Inspector** , navigate to **Mixed Lighting**..
  3. Use the drop-down menu to set the **Lighting Mode** to **Subtractive**.

## Changing the shadow color

When you set a Scene’s Lighting Mode to Subtractive, Unity displays the **Realtime Shadow Color** property in the Lighting window. Unity uses this color when it combines real-time shadows with baked shadows. Change this value to approximate the color of the indirect lighting in your Scene, to better match the real-time shadows with the baked shadows.

## The Main Directional Light

Unity automatically chooses the Directional Light in your Scene with the highest intensity value to be the Main Directional Light.