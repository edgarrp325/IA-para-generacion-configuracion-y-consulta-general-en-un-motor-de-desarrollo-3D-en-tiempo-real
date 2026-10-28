---
title: "Particle System Force Field"
category: "General"
source_file: "class-ParticleSystemForceField.html"
doc_type: "manual"
---

# Particle System Force Field

Switch to Scripting

The **Particle System Force Field** component applies forces to particles in Particle Systems. To attach this component to a Particle System, enable the External Forces Module in the Particle System, and assign either a **Layer Mask**. To attach this component to a Particle System, enable the External Forces Module in the Particle System, and assign either a **Layer Mask** , or the specific Force Field component. 

For a full introduction to particle systems and their uses, see documentation on Particle Systems.

## Properties

Use the Particle System Force Field component to apply various types of forces to particles.

All forces are applied in the local space of the Force Field. For example, rotating Transform affects the direction and rotation properties.

**_Property_** | **_Function_**  
---|---  
**Shape**  
| Shape | Select the shape of the area of influence.  
| Start Range | Set the value for the inner point within the shape where the area of influence begins.  
| End Range | Set the value for the outer point of the shape where the area of influence ends.  
| Direction X, Y and Z | Set a linear force to apply to particles along the x-axis, y-axis and z-axis. The higher the value, the greater the force. You can specify a **constant force** or vary the force over time. See Varying properties over time documentation for more information.  
**Gravity**  
| Strength | Set the amount of attraction that particles have towards the focal point within the shape. The higher the value, the greater the strength. You can specify a constant strength or vary the strength over time. For more informtion, see Varying properties over time documentation.  
| Gravity Focus | Set the focal point for gravity to pull particles towards. A value of 0 attracts particles to the center of the shape, and a value of 1 attracts particles to the outer edge of the shape.  
**Rotation**  
| Speed | Set the speed for the Particle System to propel particles around the vortex, which is the center of the force field. The higher the value, the faster the speed. You can specify a constant speed or vary the speed over time. For more information, see the Varying properties over time documentation.  
| Attraction | Set the strength that particles are dragged into the vortex motion. A value of 1 applies the maximum attraction, and a value of 0 applies no attraction. You can specify a constant attraction or vary the attraction over time. For more information, see the Varying properties over time documentation.  
| Rotation Randomness | Set a random axes of the shape to propel particles around. A value of 1 applies maximum randomness, and a value of 0 applies no randomness.  
**Drag**  
| Strength | Set the strength of the drag effect which slows particles down. The higher the value, the greater the strength. You can specify a constant strength or vary the strength over time. For more information, see the Varying properties over time documentation.  
| Multiply Drag by Size | Enable this checkbox to adjust the drag based on the size of the particles.  
| Multiply Drag by Velocity | Enable this checkbox to adjust the drag based on the velocity of the particles.  
**Vector Field**  
| Volume Texture | Select the texture of the vector field.  
| Speed | Set the speed of the multiplier to apply to particles traveling through the vector field. The higher the value, the faster the speed. You can specify a constant strength or vary the strength over time. See Varying properties over time.  
| Attraction | Set the strength at which Unity drags particles into the vector field motion. The higher the value, the greater the attraction. You can specify a constant attraction or vary the attraction over time. See Varying properties over time.  
  
* * *

  * 2019–05–16 Page amended 

  * Particle System Force Field added in 2018.3 NewIn20183

ParticleSystemForceField