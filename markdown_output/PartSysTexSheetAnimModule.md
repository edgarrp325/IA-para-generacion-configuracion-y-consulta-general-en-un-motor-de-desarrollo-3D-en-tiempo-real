---
title: "Texture Sheet Animation module"
category: "General"
source_file: "PartSysTexSheetAnimModule.html"
doc_type: "manual"
---

# Texture Sheet Animation module

A particle’s graphic need not be a still image. This module lets you treat the Texture as a grid of separate sub-images that can be played back as frames of animation.

## Using the Texture Sheet Animation module

This module is part of the Particle System component. When you create a new Particle System **GameObject** component. When you create a new Particle System **GameObject** , or add a Particle System component to an exiting GameObject, Unity adds the Texture Sheet Animation module to the Particle System. By default, Unity disables this module. To create a new Particle System and enable this module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Texture Sheet Animation module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Texture Sheet Animation module API documentation.

## Grid mode properties

**Property** | **Function**  
---|---  
**Mode popup** | Select **Grid** mode.  
**Tiles** | The number of tiles the Texture is divided into in the X (horizontal) and Y (vertical) directions.  
**Animation** | The Animation mode can be set to **Whole Sheet** or **Single Row** (that is, each row of the sheet represents a separate Animation sequence).  
**Time Mode** | Choose how the Particle System samples frames in the animation.  
Lifetime | Sample frames using an Animation Curve over the lifetime of the particle.  
Speed | Sample frames based on the speed of the particle. A speed range specifies the minimum and maximum speed range for the frame selection.  
**FPS** | Sample frames based on the specified frames-per-second value.  
**Row Mode** | Make the Particle System choose a row from the Texture sheet to produce the animation. This property is only available when the **Animation** mode is set to **Single Row**.  
Custom | Use a specific row of the Texture sheet for the animation.  
Random | Randomly select a row for each particle when producing the animation.  
**Mesh** Index | Select a row based on the Mesh index assigned to a particle. This is useful when you want to ensure that a particle using a particular Mesh also uses the same Texture.  
**Random Row** | Chooses a row from the sheet at random to produce the animation. This option is only available when **Single Row** is selected as the **Animation** mode.  
**Row** | Selects a particular row from the sheet to produce the animation This option is only available when **Single Row** mode is selected and **Random Row** is disabled.  
**Frame over Time** | A curve that specifies how the frame of animation increases as time progresses.  
**Start Frame** | Allows you to specify which frame the particle animation should start on (useful for randomly phasing the animation on each particle).  
**Cycles** | The number of times the animation sequence repeats over the particle’s lifetime.  
**Affected UV Channels** | Allows you to specify exactly which UV streams are affected by the Particle System.  
  
## Sprite mode properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**Property** | **Function**  
---|---  
**Mode popup** | Select **Sprites** mode.  
**Frame over Time** | A curve that specifies how the frame of animation increases as time progresses.  
**Start Frame** | Allows you to specify which frame the particle animation should start on (useful for randomly phasing the animation on each particle).  
**Cycles** | The number of times the animation sequence repeats over the particle’s lifetime.  
**Enabled UV Channels** | Allows you to specify exactly which UV streams are affected by the Particle System.  
  
## Details

Particle animations are typically simpler and less detailed than character animations. In systems where the particles are visible individually, animations can be used to convey actions or movements. For example, flames may flicker and insects in a swarm might vibrate or shudder as if flapping their wings. In cases where the particles form a single, continuous entity like a cloud, animated particles can help add to the impression of energy and movement.

You can use the **Single Row** mode to create separate animation sequences for particles and switch between animations from a script. This can be useful for creating variation or switching to a different animation after a **collision**. The **Random Row** option is highly effective as a way to break up conspicuous regularity in a particle system (for example, a group of flame objects that are all repeating the exact same flickering animation over and over again). This option can also be used with a single frame per row as a way to generate particles with random graphics. This can be used to break up regularity in a object like a cloud or to produce different types of debris or other objects from a single system. For example, a blunderbuss might fire out a cluster of nails, bolts, balls and other projectiles, or a car crash effect may result in springs, car paint, screws and other bits of metal being emitted.

Use the **Row Mode** property to break up conspicuous regularity in a Particle System (for example, a group of GameObjects that all repeat an identical flickering animation over and over again). To generate particles with random graphics, use this property with a single frame per row. This is useful for breaking up regularity in a single system, such as cloud, or to produce different types of debris. For example, a gun might fire out a cluster of nails, bolts and other projectiles, or a car crash effect could emit springs, car paint, screws and other bits of metal.

UV flipping is a great way to add more visual variety to your effects without needing to author additional textures.

Selecting the **Sprites** option from the Mode dropdown allows you to define a list of Sprites to be displayed for each particle, instead of using a regular grid of frames on a texture. Using this mode allows you to take advantage of many of the features of Sprites, such as the **Sprite Packer** , custom pivots and different sizes per Sprite frame. The Sprite Packer can help you share materials between different Particle Systems, by atlasing your textures, which in turn can improve performance via **Dynamic Batching** , custom pivots and different sizes per Sprite frame. The Sprite Packer can help you share materials between different Particle Systems, by atlasing your textures, which in turn can improve performance via **Dynamic Batching**. There are some limitations to be aware of with this mode. Most importantly, all Sprites attached to a Particle System must share the same texture. This can be achieved by using a Multiple Mode Sprite, or by using the Sprite Packer. If using custom pivot points for each Sprite, please note that you cannot blend between their frames, because the geometry will be different between each frame. Only simple Sprites are supported, not 9 slice. Also be aware that Mesh particles do not support custom pivots or varying Sprite sizes.   
  

* * *

  * 2019–04–16 Page amended 

  * Functionality of Texture Sheet Animation module changed in Unity 2017.1 NewIn20171

  * Time Mode added to Particle System in Unity 2018.3 NewIn20183

  * Row Mode added to Particle System in Unity 2019.1 NewIn20191