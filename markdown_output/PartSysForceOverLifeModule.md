---
title: "Force over Lifetime module"
category: "General"
source_file: "PartSysForceOverLifeModule.html"
doc_type: "manual"
---

# Force over Lifetime module

Particles can be accelerated by forces (such as wind or attraction) that are specified in this module.

## Using the Force over Lifetime module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an existing GameObject, Unity adds the Force over Lifetime module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Force over Lifetime module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Force over Lifetime module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**_Property_** | **_Function_**  
---|---  
**X, Y, Z** | Force applied to each particle in the X, Y and Z axes.  
**Space** | Selects whether the force is applied in local or world space.  
**Randomize** | When using the Two Constants or Two Curves modes, this causes a new force direction to be chosen on each frame within the defined ranges. This causes more turbulent, erratic movement.  
  
## Details

Fluids are often affected by forces as they move. For example, smoke will accelerate slightly as it rises from a fire, carried up by the hot air around it. Subtle effects can be achieved by using curves to control the force over the particles’ lifetimes. Using the previous example, smoke will initially accelerate upward but as the rising air gradually cools, the force will diminish. Thick smoke from a fire might initially accelerate, then slow down as it spreads and perhaps even start to fall to earth if it persists for a long time.