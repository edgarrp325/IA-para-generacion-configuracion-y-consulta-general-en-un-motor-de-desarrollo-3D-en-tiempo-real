---
title: "Wind Zones"
category: "General"
source_file: "class-WindZone.html"
doc_type: "manual"
---

# Wind Zones

Switch to Scripting

To create the effect of wind on your **Terrain** and Particle Systems, you can add one or more GameObjects with Wind Zone components. Trees within a wind zone bend in a realistic animated fashion, and the wind itself moves in pulses to create natural patterns of movement among the trees.

## Using Wind Zones

To create a Wind Zone GameObject directly, go to Unity’s top menu and then go to **GameObject** > **3D Object** > **3D Object** > **Wind Zone**. You can add the Wind Zone component to any suitable GameObject already in the **Scene** > **Wind Zone**. You can add the Wind Zone component to any suitable GameObject already in the **Scene** (menu: **Component** (menu: **Component** > **Miscellaneous** > **Wind Zone**). The **Inspector** > **Miscellaneous** > **Wind Zone**). The **Inspector** for the Wind Zone has a number of settings to control its behavior.

Wind Zone Inspector

You can set the **Mode** to **Directional** or **Spherical**.

  * In **Directional** mode, the wind affects the whole Terrain at once. This is useful for creating effects like the natural movement of the trees.
  * In **Spherical** mode, the wind blows outwards within a sphere defined by the **Radius** property. This is useful for creating special effects like explosions.

The **Main** property determines the overall strength of the wind, and you can use **Turbulence** to give these some random variation.

The wind blows over the trees in pulses to create a more natural effect. You can control the strength of the pulses with **Pulse Magnitude** , and the time interval between them with **Pulse Frequency**.

## Properties

**_Property:_** | **_Function:_**  
---|---  
**Mode**  
**Spherical** | Wind zone only has an effect inside the radius, and has a falloff from the center towards the edge.  
**Directional** | Wind zone affects the entire scene in one direction.  
**Radius** | Radius of the Spherical Wind Zone (only active if the mode is set to **Spherical**).  
**Main** | The primary force applied to all objects affected by the Wind Zone.  
**Turbulence** | The value represents the noise of the wind. A greater value creates higher variation in wind direction.  
**Pulse Magnitude** | Defines the strength multiplier of the wind pulses.  
**Pulse Frequency** | Defines the length and frequency of the wind pulses.  
  
## Particle Systems

The main use of wind is to animate trees, but it can also affect particles in a Particle System if that Particle System uses the External Forces module module. See the Particle System

WindZone