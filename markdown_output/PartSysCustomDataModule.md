---
title: "Custom Data module"
category: "General"
source_file: "PartSysCustomDataModule.html"
doc_type: "manual"
---

# Custom Data module

The Custom Data module allows you to define custom data formats in the Editor to be attached to particles. You can also set this in a script. See documentation on Particle System vertex streams for more information on how to set custom data from a script and feed that data into your **shaders**

Data can be in the form of a **Vector** , with up to 4 MinMaxCurve components, or a **Color** , which is an HDR-enabled MinMaxGradient. Use this data to drive custom logic in your **scripts**

The default labels for each curve/gradient can be customized by clicking on them and typing in a contextual name. When passing custom data to shaders, it is useful to know how that data is used inside the shader. For example, a curve may be used for custom alpha testing, or a gradient may be used to add a secondary color to particles. By editing the labels, it is simple to keep a record in the **UI** of the purpose of each custom data entry.

## Using the Custom Data module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the Custom Data module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Custom Data module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Custom Data module API documentation.

  * 2017–09–04 Page amended 
  * Editable custom data labels added in Unity 2017.2 NewIn20172