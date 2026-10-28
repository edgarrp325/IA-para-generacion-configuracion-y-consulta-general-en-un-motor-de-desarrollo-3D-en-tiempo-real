---
title: "Lights module"
category: "General"
source_file: "PartSysLightsModule.html"
doc_type: "manual"
---

# Lights module

Add real-time lights to a percentage of your particles using this module.

## Using the Lights module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the Lights module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Lights module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Lights module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

Property | Function  
---|---  
**Light** | Assign a Light **Prefab**  
**Ratio** | A value between 0 and 1 describing the proportion of particles that will receive a light.  
**Random Distribution** | Choose whether lights are assigned randomly or periodically. When set to true, every particle has a random chance of receiving a light based on the Ratio. Higher values increase the probability of a particle having a light. When set to false, the Ratio controls how often a newly created particle receives a light (for example, every Nth particle will receive a light).  
**Use Particle Color** | When set to True, the final color of the Light will be modulated by the color of the particle it is attached to. If set to False, the Light color is used without any modification.  
**Size Affects Range** | When enabled, the **Range** specified in the Light will be multiplied by the size of the particle.  
**Alpha Affects Intensity** | When enabled, the **Intensity** of the light is multiplied by the particle alpha value.  
**Range Multiplier** | Apply a custom multiplier to the Range of the light over the lifetime of the particle using this curve.  
**Intensity Multiplier** | Apply a custom multiplier to the Intensity of the light over the lifetime of the particle using this curve.  
**Maximum Lights** | Use this setting to avoid accidentally creating an enormous number of lights, which could make the Editor unresponsive or make your application run very slowly.  
  
## Details

The Lights module is a fast way to add real-time lighting to your particle effects. It can be used to make systems cast light onto their surroundings, for example for a fire, fireworks or lightning. It also allows you to have the lights inherit a variety of properties from the particles they are attached to. This can make it more believable that the particle effect itself is emitting light. For example, this can be achieved by making the lights fade out with their particles and having them share the same colors.

This module makes it easy to create a lot of real-time lights very quickly, and real-time lights have a high performance cost, especially in **Forward Rendering** mode. If the lights also cast shadows, the performance cost is even higher. To help guard against an accidental tweak to the emission rate and thus causing thousands of real-time lights to be created, the Maximum Lights property should be used. Creating more lights than your target hardware is able to manage can cause slowdowns and unresponsiveness.