---
title: "Inherit Velocity module"
category: "General"
source_file: "PartSysInheritVelocity.html"
doc_type: "manual"
---

# Inherit Velocity module

Use this module on subemitters. Each particle in the parent system can spawn particles in the subemitter. This module reads the velocity from the parent particle and controls how the speed of the subemitter particles reacts to that velocity over time.

## Using the Inherit Velocity module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the Inherit Velocity module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Inherit Velocity module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Inherit Velocity module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**Property** | **Function**  
---|---  
**Mode** | Specifies how the emitter velocity is applied to particles  
Current | The emitter’s current velocity will be applied to all particles on every frame. For example, if the emitter slows down, all particles will also slow down.  
Initial | The emitter’s velocity will be applied once, when each particle is born. Any changes to the emitter’s velocity made after a particle is born will not affect that particle.  
**Multiplier** | The proportion of the emitter’s velocity that the particle should inherit.  
  
## Details

This effect is very useful for emitting particles from a moving object, such as dust clouds from a car, smoke from a rocket, steam from a steam train’s chimney, or any situation where the particles should initially be moving at a percentage of the speed of the object they appear to come from. This module only has an effect on the particles when **Simulation Space** is set to **World** in the Main module.

It is also possible to use curves to influence the effect over time. For example, you could apply a strong attraction to newly created particles, which reduces over time. This could be useful for steam train smoke, which would drift off slowly over time and stop following the train it was emitted from. 

Unity calculates the emitter’s velocity in one of two ways: * Based on the velocity of an attached **Rigidbody** component * Based on how far the Particle System’s **Transform component** travelled during the current frame

To specify the method Unity uses, see the Main module’s Emitter Velocity property: