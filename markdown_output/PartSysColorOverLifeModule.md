---
title: "Color over Lifetime module"
category: "General"
source_file: "PartSysColorOverLifeModule.html"
doc_type: "manual"
---

# Color over Lifetime module

This module specifies how a particle’s color and transparency changes over its lifetime.

## Using the Color over Lifetime module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the Color over Lifetime module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Color over Lifetime module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Color over Lifetime module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**_Property:_** | **_Function:_**  
---|---  
**Color** | The color gradient of a particle over its lifetime. The very left-hand point of the gradient bar indicates the beginning of the particle’s life, and the very right-hand side of the gradient bar indicates the end of the particle’s life.   
  
In the image above, the particle starts off orange, fades in opacity over time, and is invisible by the time its life ends.  
  
## Details

Many types of natural and fantastical particles vary in color over time, and so this property has many uses. For example, white hot sparks will cool as they pass through the air and a magic spell might burst into a rainbow of colors. Equally important, though, is the variation of alpha (transparency). It is very common for particles to burn out, fade or dissipate as they reach the end of their lifetime (for example, hot sparks, fireworks and smoke particles) and a simple diminishing gradient produces this effect.

When also using the Start Color property, this module multiples the 2 colors together, to get the final particle color.

## Fade particles near opaque GameObjects

To fade particles near opaque GameObjects, follow these steps:

  1. Enable a deferred **rendering path** , or output a depth texture from the camera.
  2. Go to **Edit** > **Project Settings** > **Quality** , then enable **Soft Particles**.

Soft particles are supported only on platforms that support depth textures.

Soft particles disabled, with visible intersections with the scene. Soft particles enabled, with intersections that fade out smoothly.

## Additional resources

  * Quality settings tab reference