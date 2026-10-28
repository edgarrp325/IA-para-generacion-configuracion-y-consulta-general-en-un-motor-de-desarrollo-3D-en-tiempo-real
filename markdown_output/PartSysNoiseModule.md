---
title: "Noise module"
category: "General"
source_file: "PartSysNoiseModule.html"
doc_type: "manual"
---

# Noise module

Add turbulence to particle movement using this module.

## Using the Noise module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the Noise module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Noise module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Noise module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

Property | Function  
---|---  
**Separate Axes** | Control the strength and remapping independently on each axis.  
**Strength** | A curve that defines how strong the noise effect is on a particle over its lifetime. Higher values will make particles move faster and further.  
**Frequency** | Low values create soft, smooth noise, and high values create rapidly changing noise. This controls how often the particles change their direction of travel, and how abrupt those changes of direction are.  
**Scroll Speed** | Move the noise field over time to cause more unpredictable and erratic particle movement.  
**Damping** | When enabled, strength is proportional to frequency. Tying these values together means the noise field can be scaled while maintaining the same behaviour, but at a different size.  
**Octaves** | Specify how many layers of overlapping noise are combined to produce the final noise values. Using more layers gives richer, more interesting noise, but significantly adds to the performance cost.  
**Octave Multiplier** | For each additional noise layer, reduce the strength by this proportion.  
**Octave Scale** | For each additional noise layer, adjust the frequency by this multiplier.  
**Quality** | Lower quality settings reduce the performance cost significantly, but also affect how interesting the noise looks. Use the lowest quality that gives you the desired behavior for maximum performance.  
**Remap** | Remap the final noise values into a different range.  
**Remap Curve** | The curve that describes how the final noise values are transformed. For example, you could use this to pick out the lower ranges of the noise field and ignore the higher ranges by creating a curve that starts high and ends at zero.  
**Position Amount** | A multiplier to control how much the noise affects particle positions.  
**Rotation Amount** | A multiplier to control how much the noise affects particle rotations, in degrees per second.  
**Size Amount** | A multiplier to control how much the noise affects particle sizes.  
  
## Details

Adding noise to your particles is a simple and effective way to create interesting patterns and effects. For example, imagine how embers from a fire move around, or how smoke swirls as it moves. Strong, high frequency noise could be used to simulate the fire embers, while soft, low frequency noise would be better suited to modeling a smoke effect.

For maximum control over the noise, you can enable the Separate Axes option. This allows you to control the strength and remapping on each axis independently.

The noise algorithm used is based on a technique called Curl Noise, which internally uses multiple samples of Perlin Noise to create the final noise field.

The settings on the Quality window control how many unique noise samples are generated. When using Medium and Low, less samples of Perlin Noise are used, and those samples are re-used across multiple axes but combined in a way to try and hide the re-use. This means that the noise may look less dynamic and diverse when using lower quality settings. However, there is a significant performance benefit when using lower quality settings.

* * *

  * 2017–09–05 Page amended 

  * Position Amount, Rotation Amount, Size Amount added in Unity 2017.1 NewIn20171

  * Strength, Frequency, noise algorithm and quality settings added in Unity 2017.2 NewIn20172