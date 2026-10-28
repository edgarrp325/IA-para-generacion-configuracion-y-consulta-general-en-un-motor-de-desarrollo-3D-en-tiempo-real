---
title: "Creating a 2D game"
category: "General"
source_file: "Quickstart2DCreate.html"
doc_type: "manual"
---

# Creating a 2D game

Before you create a 2D game, you need to decide on a game perspective and an art style. 

To create a 2D game, set up your Unity project and then familiarize yourself with the relevant concepts in the following order:

  1. Fundamentals

  2. Scripting

  3. Sprites

  4. Building in-game environments

  5. Character animation

  6. Graphics

  7. Physics 2D

  8. Audio

  9. User interface

  10. Profiling, optimizing and testing

  11. Publishing

## Fundamentals

GameObjects are fundamental objects in Unity that represent characters, props, scenery, and more. Every object in your game is a GameObject.

GameObjects represent the items in your game; the space in which you place them to build your level is called a scene. Scenes in Unity are always 3D; when you make a 2D game in Unity, you typically choose to ignore the third dimension (the z-axis) but you can also use it in special cases, for example when making 2.5D games.

The behavior of GameObjects is defined by blocks of functionality called components. The following components are fundamental for 2D games: 

  * Transform: the **Transform component**

  * Sprite Renderer: the Sprite Renderer component renders the Sprite and controls how it looks in a scene.

  * Cameras: devices that capture and display the world to the player. Marking a Camera as **Orthographic** removes all perspective from the Camera’s view. This is mostly useful for making isometric or 2D games.

  * Collider 2D: this component defines the shape of a 2D GameObject for the purposes of physical **collisions**

Components are **UI** representations of C# classes; you can use scripts to change and interact with components, or create new ones. See the Scripting section for more details.

## Scripting

All 2D games need scripts. Scripts respond to input from the player and arrange for events in the gameplay to happen when they should.

For details on how to use scripts in Unity see Scripting Overview. Also see the Unity Learn Beginner Scripting course. 

Scripts are attached to GameObjects, and any script you create inherits from the MonoBehaviour class.

## Sprites

Sprites are 2D graphic objects. You use Sprites for all types of 2D games. For example, you can import an image of your main character as a Sprite. 

A character Sprite

You can also use a collection of Sprites to build a character. This allows you greater control over the movement and animation of your characters. 

Multiple Sprites that make up the parts of a character, displayed in the Sprite Editor

### Importing and setting up Sprites

Import your Sprites with Unity’s recommended settings; see Importing and Setting Up Sprites. 

### Rendering Sprites

Use the Sprite Renderer component to render your Sprites. For example, you can use the Sprite Renderer to change the color and opacity of a Sprite. 

Adjusting the color of a Sprite with the Sprite Renderer

See the Introduction to the Sprite Renderer Learn tutorial. Sorting SpritesBy organizing Sprites in layers, you can create an illusion of depth. You can sort Sprites according to many strategies. See Sorting Sprites for full details. For example, you might sort Sprites along the y-axis, so that Sprites that are higher up are sorted behind Sprites that are lower, to make the Sprites that are higher appear further away than the Sprites that are lower. 

Sprites sorted along the y-axis

To set the overlay order of Sprites, use Sorting Layers. 

To group GameObjects with Sprite Renderers, and control the order in which they render their Sprites, use Sorting Groups.

### Sprite Atlas

You can use a Sprite Atlas to consolidate several Textures into a single combined Texture. This optimizes your game and saves memory. For example, you can add all your Sprites associated with a particular character or purpose to a Sprite Atlas. 

A Sprite Atlas

See the Introduction to the Sprite Atlas Learn tutorial. 

## Building in-game environments

Environment design refers to the process of building your game’s levels and environments. You can combine the environment design tools in this section in whichever way makes the most sense for your game; for example, you can make a top-down game using only 9-slice, or you can make a side on platformer with Tilemap and SpriteShape.

### 9-slicing

9-slicing is a 2D technique that allows you to reuse an image at various sizes without needing to prepare multiple assets. Unity can dynamically stretch and tile designated parts of a Sprite to allow one Sprite to serve as the border or background for UI elements of many sizes. See 9-slicing sprites.

For example, you could use 9-slicing to stretch a Sprite to shape when you build a 2D level.

A 9-sliced Sprite, split into nine sections

See the Using 9-Slicing for Scalable Sprites Learn tutorial. 

### Tilemap

The Tilemap component is a system that stores and handles Tile assets for creating 2D levels. Use the 2D Tilemap Editor package (installed by default) to use Tilemaps. 

For example, you can use Tilemaps to paint levels using Tiles and brush tools and define rules for how Tiles behave. 

The Tile Palette window, used to edit Tilemaps

See the Introduction to Tilemaps Learn tutorial. 

#### 2D Tilemap Extras

To add some extra Tilemap assets to your Project, install the 2D Tilemap Extras package. This package contains reusable 2D and Tilemap Editor scripts that you can use for your own Projects. You can customize the behavior of the scripts to create new Brushes that suit different scenarios.

#### Isometric Tilemaps

For games with isometric perspective, you can create Isometric Tilemaps.

### SpriteShape

In a similar way to a vector drawing tool, SpriteShape provides a more flexible way to create larger Sprites, such as organic-looking landscapes and paths. See the Sprite Shape Profile. 

A path created in SpriteShape

See the Working with SpriteShape tutorial. 

## Character animation

There are three different ways you can animate 2D characters: 

2D animation type | Used for  
---|---  
Frame-by-frame | Artistic reasons, if you want your game to have a classic animation art style. Frame-by-frame animation is relatively resource-intensive, both to make and to run.  
Cutout | Smooth skeletal animation, when the characters don’t require realistic articulation.  
Skeletal | Smooth skeletal animation where Sprites bend according to the bone structure. Use this when the characters need a more organic feel.  
  
### Frame-by-frame

Frame-by-frame animation is based on the traditional cel animation technique of drawing each moment of an animation as individual images, which are played in fast sequence, like flipping pages on a flipbook.

For more information, refer to Sprite Swap in the 2D Animation package manual.

Frame-by-frame animation in the Sprite Editor

See the Introduction to Sprite Animations Learn tutorial. 

### Cutout

In cutout animation, multiple Sprites make up the body of a character, and each piece moves to give the visual effect of the whole character moving. This animation style is similar to skeletal animation (see below), except that the Sprites don’t bend.

Cutout animation in the Sprite Editor

### Skeletal

With skeletal animation, you map a Sprite or a group of Sprites onto an animation skeleton. You can create and define animation bones for characters and objects, that define how they should bend and move. This approach allows the bones to bend and deform the Sprites, for a more natural movement style. To use skeletal animation, you need to use the 2D Animation package (installed by default). 

For a 2D Animation workflow, including a guide to working with the Bone Editor, see the 2D Animation documentation. 

A character with bones in the Bone Editor

## Graphics

This section describes your graphics options when using Universal **Render Pipeline** (URP). 

### Lighting

Because you’re using URP with the 2D Renderer, you can use the Light 2D component to apply optimized 2D lighting to Sprites. For details, see Introduction to Lights 2D. 

These two images show the same scene; in the image on the left, 2D Lights are disabled, and in the image on the right, 2D lights are enabled. With 2D Lights, you can use the same Sprites to create different weather conditions or moods.

To set up lighting: 

  1. Prepare your Sprites for lighting. For details, see Preparing Sprites for Lighting. 

  2. Set up **normal map** and mask Textures. 2D Lights can interact with normal map and mask Textures linked to Sprites to create advanced lighting effects, such as normal mapping. See Setting up normal map and mask Textures. 

  3. Create a 2D Light GameObject; see 2D Lights Properties. 

  4. Configure the 2D Renderer Data asset; see Configuring the 2D Renderer Asset. 

  5. (Optional) if you want to apply 2D Light effects to a **pixel** art game, see 2D Pixel Perfect. 

See the Lighting in URP Learn tutorial. 

### Shadows

To define the shape and properties that a Light uses to determine the shadows it casts, use the Shadow Caster 2D component. Increase the Light’s **Shadow Intensity** above zero. 

A shadow intensity of 0.5 in the Shadow Caster 2D component

### Enhanced look and feel

Particle systems and **post-processing** are optional tools that you can use to add polish to your game. 

#### Particle systems

You can use particle systems to create dynamic objects like fire, smoke or liquids, as an alternative to using a Sprite. Sprites are more suited to physical objects. See Particle systems. 

A fire effect, created with the Particle System and Shader Graph for 2D

#### Post-processing

You can use post-processing effects and full-screen effects to significantly improve the appearance of your game. For example, you can use these effects to simulate physical camera or film properties, or to create stylized visuals. 

URP has its own post-processing implementation. See Post-processing in the Universal Render Pipeline. 

The Lost Crypt demo uses the bloom and vignette post-processing effects

## Physics 2D

The Physics 2D settings define limits on the accuracy of the physical simulation in your 2D game. See 2D Physics. 

This video provides an overview of 2D physics features in Unity 2020.1.

To learn how to use Unity’s 2D **physics engine** , see the 2D Physics Learn tutorial.

The following 2D physics tools are useful for 2D games.

  * Rigidbody 2D

  * Collider 2D

  * Triggers

  * 2D Joints

  * 2D Effectors

### Rigidbody 2D

A **Rigidbody** 2D component places a GameObject under the control of the physics engine. See Rigidbody 2D. 

The Rigidbody 2D component

### Collider 2D

Collider 2D components define the shape of a 2D GameObject for the purposes of physical collisions. You can also use **Collider** 2D components for input detection. For example, in mobile games you can use them to make Sprites selectable.

The Collider 2D types that you can use with Rigidbody 2D are: 

  * Circle Collider 2D

  * Box Collider 2D

  * Polygon Collider 2D

  * Edge Collider 2D

  * Capsule Collider 2D

  * Composite Collider 2D

The Circle Collider 2D component

### Triggers

When you set a Collider 2D as a Trigger (by enabling its **Is Trigger** property), it no longer behaves as a physical object, and it can intersect with other Colliders without causing a collision. Instead, when a Collider enters its space, Unity calls the `OnTriggerEnter` function on the Trigger GameObject’s scripts. 

The Circle Collider 2D component with **Is Trigger** selected

### 2D Joints

Joints attach GameObjects together. You can only attach 2D **joints** to GameObjects that have a Rigidbody 2D component attached, or to a fixed position in world space. See 2D Joints. 

### 2D Effectors

Use Effector 2D components with Collider 2D components to direct the forces of physics in your scene when GameObject Colliders come into contact with each other. See 2D Effectors.

## Audio

You can add background music and sound effects to your game in Unity; see Audio Overview. Use third-party software to create your audio and import it into Unity with the recommended settings. 

## User interface

If you want to add a menu or help to your game, you need to set up a user interface. To set up a user interface, use Unity UI. 

## Profiling, optimizing and testing a build

### Profiling

Profiling allows you to see how resource-intensive the different parts of your game are. You should always profile your game on its target release platform; see Profiling your application. 

### Optimizing

After profiling, you can use the results to make performance improvements and optimizations. See Understanding optimization in Unity.

### Testing

Test your game and your code with the Unity Test Framework; see Unity Test Framework.

The Test Runner window

## Publishing

When you’ve finished your game, you’re ready to publish it. See Publishing Builds. 

The Build Settings window