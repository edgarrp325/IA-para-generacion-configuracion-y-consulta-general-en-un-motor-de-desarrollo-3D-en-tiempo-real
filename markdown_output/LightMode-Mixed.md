---
title: "Light Mode: Mixed"
category: "General"
source_file: "LightMode-Mixed.html"
doc_type: "manual"
---

# Light Mode: Mixed

This page describes the behavior of a Light component when you set its **Mode** property to **Mixed**. These are also known as Mixed Lights.

Mixed Lights combine elements of both real-time and baked lighting. You can use Mixed Lights to combine dynamic shadows with baked lighting from the same light source, or when you want a light to contribute direct real-time lighting and baked indirect lighting.

To use Mixed Lights, you must first understand the benefits and limitations of Realtime Lights and Baked Lights and Baked Lights.

## Mixed Light behavior

  * The behavior of all Mixed Lights in a **Scene** depends on the **Lighting Mode** setting in the Lighting window. The different Lighting Modes have very different performance characteristics, and different levels of visual fidelity. For more information, see Lighting Modes.
  * You can change properties of Mixed Lights at runtime. This updates their real-time lighting but not their baked lighting. When doing this, take care to avoid unwanted visual effects.

## Limitations of Mixed Lights

  * The performance cost of Mixed Lights differs considerably, depending on the Lighting Mode. However, because Mixed Lights always combine at least some real-time and some baked lighting, Mixed Lights always involve more runtime calculations than fully baked lighting, and higher memory usage than fully real-time lighting.

Note that if you disable **Baked**Global Illumination**** in your Scene, Unity forces Mixed Lights to behave as though you set their **Mode** to **Realtime**. When this happens, Unity displays a warning on the Light component **Inspector** in your Scene, Unity forces Mixed Lights to behave as though you set their **Mode** to **Realtime**. When this happens, Unity displays a warning on the Light component **Inspector**.