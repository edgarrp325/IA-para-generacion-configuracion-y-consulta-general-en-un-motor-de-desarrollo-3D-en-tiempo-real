---
title: "Limit Velocity over Lifetime module"
category: "General"
source_file: "PartSysLimitVelOverLifeModule.html"
doc_type: "manual"
---

# Limit Velocity over Lifetime module

This module controls how the speed of particles is reduced over their lifetime.

## Using the Limit Velocity over Lifetime module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the Limit Velocity over Lifetime module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Limit Velocity over Lifetime module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Limit Velocity over Lifetime module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**Property** | **Function**  
---|---  
**Separate Axes** | Splits the axes up into separate X, Y and Z components.  
**Speed** | Sets the speed limit of the particles.  
**Space** | Selects whether the speed limitation refers to local or world space. This option is only available when **Separate Axes** is enabled.  
**Dampen** | The fraction by which a particle’s speed is reduced when it exceeds the speed limit.  
**Drag** | Applies linear drag to the particle velocities.  
**Multiply by Size** | When enabled, larger particles are affected more by the drag coefficient.  
**Multiply by Velocity** | When enabled, faster particles are affected more by the drag coefficient.  
  
## Details

This module is very useful for simulating air resistance that slows the particles, especially when a decreasing curve is used to lower the speed limit over time. For example, an explosion or firework initially bursts at great speed but the particles emitted from it rapidly slow down as they pass through the air.

The **Drag** option offers a more physically accurate simulation of air resistance by offering options to apply varying amounts of resistance based on the size and speed of the particles.

* * *

  * 2017–09–05 Page amended 

  * Drag, Multiple by Size, Multiply by Velocity added in Unity 2017.2NewIn20172