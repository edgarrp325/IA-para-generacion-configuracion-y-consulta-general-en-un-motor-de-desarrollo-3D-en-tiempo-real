---
title: "Rotation by Speed module"
category: "General"
source_file: "PartSysRotBySpeedModule.html"
doc_type: "manual"
---

# Rotation by Speed module

The rotation of a particle can be set here to change according to its speed in distance units per second.

## Using the Rotation by Speed module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the Rotation by Speed module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Rotation by Speed module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Rotation by Speed module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**_Property_** | **_Function_**  
---|---  
**Separate Axes** | Control rotation independently for each axis of rotation.  
**Angular Velocity** | Rotation velocity in degrees per second.  
**Speed Range** | The low and high ends of the speed range to which the size curve is mapped (speeds outside the range will map to the end points of the curve).  
  
## Details

This property can be used when the particles represent solid objects moving over the ground such as rocks from a landslide. The rotation of the particles can be set in proportion to the speed so that they roll over the surface convincingly.

The Speed Range is only applied when the velocity is in one of the curve modes. Fast particles will rotate using the values at the right end of the curve, while slower particles will use values from the left side of the curve.