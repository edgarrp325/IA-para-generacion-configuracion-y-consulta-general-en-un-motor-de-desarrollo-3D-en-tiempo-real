---
title: "External Forces module"
category: "General"
source_file: "PartSysExtForceModule.html"
doc_type: "manual"
---

# External Forces module

This property modifies the effect of **wind zones** and Particle System Force Fields on particles emitted by the system.

## Using the External Forces module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the External Forces module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the External Forces module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the External Forces module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**_Property_** | **_Function_**  
---|---  
**Multiplier** | Scale value applied to wind zone forces.  
**Influence Filter** | Choose whether to include Force Fields based on a **Layer Mask** , or via an explicit **List**.  
**List** | Define an explicit list of Force Fields that can affect this Particle System. This appears when the **Influence Filter** is set to **List**.  
**Influence Mask** | Use a Layer Mask to determine which Force Fields affect this Particle System. This appears when the **Influence Filter** is set to **Layer Mask**.   
This is set to **Everything** by default, but you can enable or disable the following options individually:  
\- **Nothing** (automatically unticks all other options, turning them off)  
\- **Everything** (automatically ticks all other options, turning them on)  
\- **Default**   
\- **TransparentFX**   
\- **IgnoreRaycast**  
\- **Water**   
\- **UI**  
  
## Details

To get the best results out of this feature, create separate GameObjects with ParticleSystemForceFields components.

A **Terrain** can incorporate _wind zones_ which affect the movement of trees on the landscape. Enabling this section allows the wind zones to blow particles from the system. The _Multiplier_ value lets you scale the effect of the wind on the particles, since they will often be blown more strongly than tree branches.

* * *

  * 2018–10–19 Page amended 

  * Influence Filter and Influence Mask added to Particle System in 2018.3 NewIn20183