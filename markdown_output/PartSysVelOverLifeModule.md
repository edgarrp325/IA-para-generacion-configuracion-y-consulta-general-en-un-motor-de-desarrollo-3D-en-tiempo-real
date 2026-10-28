---
title: "Velocity over Lifetime module"
category: "General"
source_file: "PartSysVelOverLifeModule.html"
doc_type: "manual"
---

# Velocity over Lifetime module

The **Velocity over Lifetime** module allows you to control the velocity of particles over their lifetime.

## Using the Velocity over Lifetime module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the Velocity over Lifetime module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Velocity over Lifetime module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Velocity over Lifetime module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**Property** | **Function**  
---|---  
**Linear X, Y, Z** | Linear velocity of particles in the X, Y and Z axes.  
**Space** | Specifies whether the **Linear X, Y, Z** axes refer to local or world space.  
**Orbital X, Y, Z** | Orbital velocity of particles around the X, Y and Z axes.  
**Offset X, Y, Z** | The position of the center of orbit, for orbiting particles.  
**Radial** | Radial velocity of particles away from/towards the center position.  
**Speed Modifier** | Applies a multiplier to the speed of particles, along/around their current direction of travel.  
  
## Details

To create particles that drift in a particular direction, use the Linear X, Y and Z curves.

To create effects with particles that spin around a center position, use the **Orbital** velocity values. Additionally, you can propel particles towards or away from a center position using the **Radial** velocity values. You can define a custom center of rotation for each particle by using the **Offset** value.

You can also use this module to adjust the speed of the particles in the Particle System without affecting their direction, by leaving all the above values at zero and only modifying the **Speed Modifier** value.

* * *

  * 2018–03–28 Page amended 

  * Speed Modifier property added to Velocity over Lifetime module in 2017.3 NewIn20173

  * Orbital XYZ, Offset XYZ and Radial properties added to Velocity over Lifetime module in 2018.1 NewIn20181