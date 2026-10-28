---
title: "Using the Built-in Particle System"
category: "General"
source_file: "PartSysUsage.html"
doc_type: "manual"
---

# Using the Built-in Particle System

The Built-in Particle System uses a component, so placing a Particle System in a Scene is a matter of adding a pre-made GameObject (menu: **GameObject** > **Effects** > **Particle System** > **Effects** > **Particle System**) or adding the component to an existing GameObject (menu: **Component**) or adding the component to an existing GameObject (menu: **Component** > **Effects** > **Particle System**). Because the component is quite complicated, the Inspector is divided into a number of collapsible sub-sections or **modules** that each contain a group of related properties. Additionally, you can edit one or more systems at the same time using a separate Editor window accessed via the **Open Editor** button in the Inspector. See documentation on the Particle System component and individual Particle System modules to learn more.

When a GameObject with a Particle System is selected, the **Scene** view contains a small **Particle Effect** panel, with some simple controls that are useful for visualising changes you make to the system’s settings.

The **Playback Speed** allows you to speed up or slow down the particle simulation, so you can quickly see how it looks at an advanced state. The **Playback Time** indicates the time elapsed since the system was started; this may be faster or slower than real time depending on the playback speed. The **Particle Count** indicates how many particles are currently in the system. The playback time can be moved backwards and forwards by clicking on the **Playback Time** label and dragging the mouse left and right. The buttons at the top of the panel can be used to pause and resume the simulation, or to stop it and reset to the initial state.

## Varying properties over time

Many of the numeric properties of particles or even the whole Particle System can vary over time. Unity provides several different methods of specifying how this variation happens:

  * **Constant:** The property’s value is fixed throughout its lifetime.
  * **Curve:** The value is specified by a curve/graph.
  * **Random Between Two Constants:** Two constant values define the upper and lower bounds for the value; the actual value varies randomly over time between those bounds.
  * **Random Between Two Curves:** Two curves define the upper and lower bounds of the value at a given point in its lifetime; the current value varies randomly between those bounds.

When you set a property to **Curve** or **Random Between Two Curves** , the Particle System Curves editor appears at the bottom of the Inspector:

To edit a curve, click and drag an end point or key to reshape the curve:

Particle System curves are similar to Animation curves. For information on using curves, see the documentation on Editing Curves.

The Particle System Curves editor has the following buttons:

  * **Optimize** : Fits the curve into four or fewer keys to build a fast evaluator called a Polynomial, which is more efficient than reading the unoptimized curve.
  * **Remove** : Deletes the selected curve.

To edit the way in which the Particle System plays curves, click the cog next to a selected key and choose one of the following options: 

  * **Loop** : Plays the curve the specified number times over a particle’s life. For example, if you make a curve that scales a particle’s size up and down, you can tell it to loop multiple times, which causes the “up and down” animation to happen multiple times before the particle dies, instead of just once.
  * **Ping Pong** : Similar to **Loop** , but plays the curve forwards then backwards in a continuous oscillation.
  * **Clamp** : Limits particle queries that fall outside the curve time range to the first or last value of the curve.

The **Start Color** property in the main module has the following options:

  * **Color:** All particles start with this color throughout the lifetime of the Particle System. Particles can still change color during their lifetime.
  * **Gradient:** The Particle System emits particles which start with the colour at the beginning of the gradient, and end at the colour at the end of the gradient. The gradient line represents the lifetime of the Particle System; the Particle System picks a color from the gradient at the point corresponding to the current age of the Particle System.
  * **Random Between Two Colors:** The Particle System chooses a starting particle color from a random linear interpolation between the two given colors.
  * **Random Between Two Gradients:** The Particle System chooses a color from each of the given gradients at the point corresponding to the current age of the system. The starting particle color is chosen as a random linear interpolation between the two chosen colors.
  * **Random Color:** Similar to **Gradient** mode, where particles take their initial color from the defined **Gradient**. However, in this mode, the Particle System does not choose samples based on the age of the Particle System, but instead it selects them at random. This mode also works well with the **Fixed Gradient Mode** , which is inside the Gradient Editor. When enabled, you can select a predefined list of precise starting colors, and apply a probability to each color.

Other color properties, such as **Color over Lifetime** , can use the **Gradient** or **Random Between Two Gradients** modes.

To calculate the final particle color result, the Particle System multiplies color properties in various modules together per channel.

When you set the **Gradient** color for particles, the Gradient Editor appears:

  * **Mode:** Determines whether the particle color settings are blended or not.
  * **Color:** Displays the color of the currently selected key in the Gradient. Use this to edit the color at that position of the Gradient.
  * **Location:** Shows how far along on the Gradient the currently selected key is.
  * **Presets:** Allows you to save Gradient settings. Click New to make the current set of values a Gradient preset.

Color properties in various modules are multiplied together per channel to calculate the final particle color result.

## Animation bindings

All particle properties are accessible by the Animation system, meaning you can **keyframe** them in and control them from your animations.

To access the Particle System’s properties, there must be an **Animator component** attached to the Particle System’s GameObject. An Animation Controller and an Animation are also required.

To animate a Particle System, add an Animator Component, and assign an Animation Controller with an Animation.

To animate a Particle System property, open the **Animation Window** with the GameObject containing the Animator and Particle System selected. Click **Add Property** to add properties.

Add properties to the animation in the Animation Window.

Scroll to the right to reveal the **add controls**.

Note that for curves, you can only keyframe the overall **curve multiplier** , which can be found next to the curve editor in the **Inspector**.

* * *

  * 2019–04–16 Page amended 

  * GameObject menu changed in Unity 4.6

  * Particle System loop/ping-pong curve playing added in 2018.3 NewIn20183