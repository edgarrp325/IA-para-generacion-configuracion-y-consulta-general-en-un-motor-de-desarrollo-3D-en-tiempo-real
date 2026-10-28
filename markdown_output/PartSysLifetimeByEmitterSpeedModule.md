---
title: "Lifetime by Emitter Speed module"
category: "General"
source_file: "PartSysLifetimeByEmitterSpeedModule.html"
doc_type: "manual"
---

# Lifetime by Emitter Speed module

This module controls the initial lifetime of each particle based on the speed of the emitter when the particle spawns. It multiplies the start lifetime of particles by a value that depends on the speed of the object that spawned them. For most Particle Systems, this is the **GameObject** velocity, but for sub-emitters, the velocity comes from the parent particle that the sub-emitter particle originated from.

## Using the Lifetime by Emitter Speed module

This module is part of the Particle System component. When you create a new Particle System GameObject, or add a Particle System component to an exiting GameObject, Unity adds the Lifetime by Emitter Speed module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Lifetime by Emitter Speed module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Lifetime by Emitter Speed module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**Property** | **Function**  
---|---  
**Multiplier** | The multiplier to apply to the particle’s initial lifetime. The module uses this value differently depending on the curve mode you set. The curve modes are:  
• **Constant** : Uses the constant multiplier value you set for this property. Using this curve mode ignores the **Speed Range** property.  
• **Curve** : Takes the emitter’s speed, maps it to a value between 0 and 1 based on the **Speed Range** , then uses the normalized value to sample the curve.  
• **Random Between Two Constants** : Sets a random multiplier for each particle between the two values you set for this property. Using this curve mode ignores the **Speed Range** property.  
• **Random Between Two Curves** : Takes the emitter’s speed, maps it to a value between 0 and 1 based on the **Speed Range** , then uses the normalized value to sample each curve. For each particle, the module sets the multiplier to a random value between the two samples.  
**Speed Range** | The minimum and maximum emitter speeds the Particle System maps to a value along the **Multiplier** curve. If the emitter’s speed is equal to the first value, the multiplier is the value at the start of the curve. If the emitter’s speed is equal to the second value, the multiplier is the value at the end of the curve.  
This property is only relevant if the curve mode for **Multiplier** is set to **Curve** or **Random Between Two Curves**.