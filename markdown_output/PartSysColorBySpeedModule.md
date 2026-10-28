---
title: "Color by Speed module"
category: "General"
source_file: "PartSysColorBySpeedModule.html"
doc_type: "manual"
---

# Color by Speed module

The color of a particle can be set here to change according to its speed in distance units per second.

## Using the Color by Speed module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the Color by Speed module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Color by Speed module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Color by Speed module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**_Property_** | **_Function_**  
---|---  
**Color** | The color gradient of a particle defined over a speed range.  
**Speed Range** | The low and high ends of the speed range to which the color gradient is mapped (speeds outside the range will map to the end points of the gradient).  
  
## Details

Burning or glowing particles (such as sparks) tend to burn more brightly when they move quickly through the air (for example, when sparks are exposed to more oxygen), but then dim slightly as they slow down. To simulate this, you might use _Color By Speed_ with a gradient that has white at the upper end of the speed range, and red at the lower end (in the spark example, faster particles will appear white while slower particles are red).