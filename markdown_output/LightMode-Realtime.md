---
title: "Light Mode: Realtime"
category: "General"
source_file: "LightMode-Realtime.html"
doc_type: "manual"
---

# Light Mode: Realtime

This page describes the behavior of a Light component when you set its **Mode** property to **Realtime**. These are also known as **Realtime Lights**.

Unity performs the lighting calculations for Realtime Lights at runtime, once per frame. You can change the properties of Realtime Lights at runtime to create effects such as flickering light bulbs, or a torch being carried through a dark room. 

Realtime Lights are useful for lighting and casting shadows on characters or moveable geometry.

## Realtime Light behavior

  * Realtime Lights cast shadows up to the **Shadow Distance**.
  * By default, Realtime Lights contribute only realtime direct lighting to a **Scene**. If you’re using the Built-in **Render Pipeline**. If you’re using the Built-in **Render Pipeline** and you enable ****Enlighten** and you enable ****Enlighten** Realtime **Global Illumination**** in your Project, Realtime Lights also contribute realtime indirect lighting to your Scene.**

## Limitations of Realtime Lights

  * Performing runtime calculations for Realtime Lights might be costly, especially in complex scenes or on low-end hardware.
  * Because Realtime Lights only contribute direct lighting to the Scene by default, shadows appear completely black and there aren’t any indirect lighting effects, such as color bounce. This might cause unrealistic lighting in the Scene.