---
title: "Light Mode: Baked"
category: "General"
source_file: "LightMode-Baked.html"
doc_type: "manual"
---

# Light Mode: Baked

This page describes the behavior of a **Light** component when you set its **Mode** property to **Baked**. These are also known as **Baked Lights**.

Unity performs the calculations for Baked Lights in the Unity Editor, and saves the results to disk as lighting data. This process is called baking. At runtime, Unity loads the baked lighting data, and uses it to light the **Scene**. Because the complex calculations are performed in advance, Baked Lights reduce shading cost at runtime, and reduce the rendering cost of shadows.

Baked Lights are useful for lighting things that won’t change at runtime, such as scenery.

## Baked Light behavior

  * Unity bakes both direct lighting and indirect lighting from Baked Lights into **lightmaps**. For more information on using lightmaps, see lightmapping.
  * Unity bakes both direct and indirect lighting from Baked Lights into Light Probes. For more information on using Light Probes, see Light Probes.

## Limitations of Baked Lights

  * You cannot change the properties of Baked Lights at runtime.
  * Baked Lights do not contribute to specular lighting.
  * Dynamic **GameObjects** do not receive light or shadow from Baked Lights.

Note that if you disable **Baked**Global Illumination**** in your Scene, Unity forces Baked Lights to behave as though you set their **Mode** to **Realtime**. When this happens, Unity displays a warning on the Light component **Inspector** in your Scene, Unity forces Baked Lights to behave as though you set their **Mode** to **Realtime**. When this happens, Unity displays a warning on the Light component **Inspector**.