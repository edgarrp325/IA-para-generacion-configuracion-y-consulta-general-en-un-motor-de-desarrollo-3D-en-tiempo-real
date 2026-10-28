---
title: "Emission module"
category: "General"
source_file: "PartSysEmissionModule.html"
doc_type: "manual"
---

# Emission module

The properties in this module affect the rate and timing of Particle System emissions.

## Using the Emission module

This module is part of the Particle System component. When you create a new Particle System **GameObject**

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the **Inspector** , find the Particle System component.
  3. In the Particle System component, find the Emission module fold-out.
  4. To the left of the fold-out header, enable the checkbox.

### API

Since this module is part of the Particle System component, you access it through the ParticleSystem class. For information on how to access it and change values at runtime, see the Emission module API documentation.

## Properties

For some properties in this section, you can use different modes to set their value. For information on the modes you can use, see Varying properties over time.

**Property** | **Function**  
---|---  
**Rate over Time** | The number of particles emitted per unit of time.  
**Rate over Distance** | The number of particles emitted per unit of distance moved.  
**Bursts** | A burst is an event which spawns particles. These settings allow particles to be emitted at specified times.  
 _Time_ | Set the time (in seconds, after the Particle System begins playing) at which to emit the burst.  
 _Count_ | Set a value for the number of particles that may be emitted.  
 _Cycles_ | Set a value for how many times to play the burst.  
 _Interval_ | Set a value for the time (in seconds) between when each cycle of the burst is triggered.  
 _Probability_ | Controls how likely it is that each burst event spawns particles. A higher value makes the system produce more particles, and a value of 1 guarantees that the system produces particles.  
  
## Details

The rate of emission can be constant or can vary over the lifetime of the system according to a curve. If **Rate over Distance** mode is active, a certain number of particles are released per unit of distance moved by the parent object. This is very useful for simulating particles that are actually created by the motion of the object (for example, dust from a car’s wheels on a dirt track).

If **Rate over Time** is active, then the desired number of particles are emitted each second regardless of how the parent object moves. Additionally, you can add bursts of extra particles that appear at specific times (for example, a steam train chimney that produces puffs of smoke).

* * *

  * 2018–10–19 Page amended 

  * Burst probability added to Particle System Emission module in Unity 2018.3 NewIn20183