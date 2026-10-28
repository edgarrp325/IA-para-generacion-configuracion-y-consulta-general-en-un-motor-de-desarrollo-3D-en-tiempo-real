---
title: "Size by Speed module"
category: "General"
source_file: "PartSysSizeBySpeedModule.html"
doc_type: "manual"
---

# Size by Speed module

This module allows you to create particles that change size according to their speed in distance units per second.

## Using the Size by Speed module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the Size by Speed module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Size by Speed module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Size by Speed module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**_Property_** | **_Function_**  
---|---  
**Separate Axes** | Control the particle size independently on each axis.  
**Size** | A curve defining the particle’s size over a speed range.  
**Speed Range** | The low and high ends of the speed range to which the size curve is mapped (speeds outside the range will map to the end points of the curve).  
  
## Details

Some situations will require particles which vary in size depending on their speed. For example, you would expect small pieces of debris to be accelerated more by an explosion than larger pieces. You can achieve effects like this using **Size By Speed** with a simple ramp curve that proportionally increases the speed as the size of the particle decreases. Note that this should not be used with the **Limit Velocity Over Lifetime** module, unless you want particles to change their size as they slow down.

**Speed Range** specifies the range of values that the X (width), Y (height) and Z (depth) shapes apply to. The Speed Range is only applied when the size is in one of the curve modes. Fast particles will scale using the values at the right end of the curve, while slower particles will use values from the left side of the curve. For example, if you specify a Speed Range between 10 and 100:

  * Speeds below 10 will set the Particle size corresponding with the left-most edge of the curve.
  * Speeds above 100 will set the Particle size corresponding with the right-most edge of the curve.
  * Speeds between 10 and 100 will set the Particle size determined by the point along the curve corresponding to the Speed. In this example, a Speed of 55 would set the size according to the midpoint of the curve.

## Non-uniform particle scaling

You can specify how a particle’s width, height and depth size changes by speed independently. In the **Size by Speed** module, check the **Separate Axes** checkbox, then choose how the X (width), Y (height) and Z (depth) of the particle is affected by the speed of the particle. Remember that Z will only be used for **Mesh** particles.