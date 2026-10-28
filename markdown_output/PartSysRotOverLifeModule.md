---
title: "Rotation over Lifetime module"
category: "General"
source_file: "PartSysRotOverLifeModule.html"
doc_type: "manual"
---

# Rotation over Lifetime module

Here, you can configure particles to rotate as they move.

## Using the Rotation over Lifetime module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the Rotation over Lifetime module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Rotation over Lifetime module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Rotation over Lifetime module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

Property | Function  
---|---  
**Separate Axes** | Allow rotation to be specified per axis. When this is enabled, the option to set a rotation for each of X, Y and Z is presented.  
**Angular Velocity** | Rotation velocity in degrees per second. See below for more information.  
  
## Details

This setting is useful when particles represent small solid objects, such as pieces of debris from an explosion. Assigning random values of rotation will make the effect more realistic than having the particles remain upright as they fly. The random rotations will also help to break up the regularity of similarly shaped particles (the same texture repeated many times can be very noticeable).

Leaves rendered using particles with random 3D rotation

## Options

The angular velocity option can be changed from the default constant speed. The drop-down to the right of the velocity can provide:

Property | Function  
---|---  
**Constant** | The velocity for particle rotation in degrees per second.  
**Curve** | The angular velocity can be set to change over the lifetime of the particle. A curve editor appears at the bottom of the Inspector which allows you to control how the velocity changes throughout the lifetime of the particle (see Image A below). If the Separate Axes box is ticked, each of the X, Y and Z axes can be given curved velocity values.  
**Random Between Two Constants** | The angular velocity properties has two angles allowing a rotation between them.  
**Random Between Two Curves** | The angular velocity can be set to change over the lifetime of the particle specified by a curve. In this mode, two curves are editable, and each particle will pick a random curve between the range of these two curves that you define (see Image B below).  
  
Image A: Z-axis angular velocity

Image B: Angular velocity between two curves