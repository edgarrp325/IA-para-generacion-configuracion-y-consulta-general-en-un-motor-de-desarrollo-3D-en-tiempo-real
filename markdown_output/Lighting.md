---
title: "Types of light"
category: "General"
source_file: "Lighting.html"
doc_type: "manual"
---

# Types of light

This page describes the effects of the **Type** property on a Light component.

You can use the Type property to choose how the Light behaves. The available values are:

  * Point Light, a Light that’s located at a point in the Scene and emits light in all directions equally   

  * Spot Light, a Light that’s located at a point in the Scene and emits light in a cone shape   

  * Directional Light, a Light that’s located infinitely far away and emits light in one direction only   

  * Area Light, a Light that’s defined by a rectangle or disc in the Scene, and emits light in all directions uniformly across its surface area but only from one side of the rectangle or disc  

## Point Lights

A Point Light is located at a point in space and sends light out in all directions equally. The direction of light hitting a surface is the line from the point of contact back to the center of the light object. The intensity diminishes with distance from the light, reaching zero at a specified range. Light intensity is inversely proportional to the square of the distance from the source. This is known as ‘inverse square law’ and is similar to how light behaves in the real world.

Point lights are useful for simulating lamps and other local sources of light in a **scene**. You can also use them to make a spark or explosion illuminate its surroundings in a convincing way.

Effect of a Point Light in the scene

## Spot Lights

Like a Point Light, a Spot Light has a specified location and range over which the light falls off. However, a Spot Light is constrained to an angle, resulting in a cone-shaped region of illumination. The center of the cone points in the forward (Z) direction of the light object. Light also diminishes at the edges of a Spot Light’s cone. Widening the angle increases the width of the cone and with it increases the size of this fade, known as the ‘penumbra’.

Spot lights are generally used for artificial light sources such as flashlights, car headlights and searchlights. With the direction controlled from a script or animation, a moving spot light will illuminate just a small area of the scene and create dramatic lighting effects.

Effect of a Spot Light in the scene

## Directional Lights

Directional Lights are useful for creating effects such as sunlight in your scenes. Behaving in many ways like the sun, directional lights can be thought of as distant light sources which exist infinitely far away. A Directional Light doesn’t have any identifiable source position and so the light object can be placed anywhere in the scene. All objects in the scene are illuminated as if the light is always from the same direction. The distance of the light from the target object isn’t defined and so the light doesn’t diminish.

Directional lights represent large, distant sources that come from a position outside the range of the game world. In a realistic scene, they can be used to simulate the sun or moon. In an abstract game world, they can be a useful way to add convincing shading to objects without exactly specifying where the light is coming from.

Effect of a Directional Light in the scene

By default, every new Unity scene contains a Directional Light. This is linked to the procedural sky system defined in the Environment Lighting section of the Lighting Panel (Lighting>Scene>Skybox). You can change this behaviour by deleting the default Directional Light and creating a new light or simply by specifying a different GameObject from the ‘Sun’ parameter (Lighting>Scene>Sun).

Rotating the default Directional Light (or ‘Sun’) causes the ‘**Skybox** ’ to update. With the light angled to the side, parallel to the ground, sunset effects can be achieved. Additionally, pointing the light upwards causes the sky to turn black, as if it were nighttime. With the light angled from above, the sky will resemble daylight.

If the Skybox is selected as the ambient source, Ambient Lighting will change in relation to these colors.

## Area Lights

You can define an Area Light by one of two shapes in space: a rectangle or a disc. An Area Light emits light from one side of that shape. The emitted light spreads uniformly in all directions across that shape’s surface area. The **Range** property determines the size of that shape. The intensity of the illumination provided by an Area Light diminishes at a rate determined by the inverse square of the distance from the light source (see inverse square law). Because this lighting calculation is quite processor-intensive, Area Lights aren’t available at runtime and can only be baked into lightmaps.

Since an area light illuminates an object from several different directions at once, the shading tends to be more soft and subtle than the other light types. You might use it to create a realistic street light or a bank of lights close to the player. A small area light can simulate smaller sources of light (such as interior house lighting) but with a more realistic effect than a point light.

Light is emitted across the surface of an Area Light producing a diffuse light with soft shadowing.