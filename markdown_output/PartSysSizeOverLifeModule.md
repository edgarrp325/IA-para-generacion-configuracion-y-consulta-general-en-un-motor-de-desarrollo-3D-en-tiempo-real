---
title: "Size over Lifetime module"
category: "General"
source_file: "PartSysSizeOverLifeModule.html"
doc_type: "manual"
---

# Size over Lifetime module

Many effects involve a particle changing size according to a curve, which can be set in this module.

## Using the Size over Lifetime module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the Size over Lifetime module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Size over Lifetime module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Size over Lifetime module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**_Property_** | **_Function_**  
---|---  
**Separate Axes** | Control the particle size independently on each axis.  
**Size** | A curve which defines how the particle’s size changes over its lifetime.  
  
## Details

Some particles will typically change in size as they move away from the point of emission, such as those that represent gases, flames or smoke. For example, smoke will tend to disperse and occupy a larger volume over time. You can achieve this by setting the curve for the smoke particle to an upward ramp, increasing with the particle’s age. You can also further enhance this effect using the **Color Over Lifetime** module to fade the smoke as it spreads. 

For fireballs created by burning fuel, the flame particles will tend to expand after emission but then fade and shrink as the fuel is used up and the flame dissipates. In this case, the curve would have a rising “hump” that rises and then falls back down to a smaller size.

The values specified in the curves are multiplied by the Start Size to get the final particle size.

## Non-uniform particle scaling

You can specify how a particle’s width, height and depth changes over lifetime independently. In the **Size over Lifetime** module, check the **Separate Axes** checkbox, then change the X (width), Y (height) and Z (depth). Remember that Z will only be used for **Mesh** particles.