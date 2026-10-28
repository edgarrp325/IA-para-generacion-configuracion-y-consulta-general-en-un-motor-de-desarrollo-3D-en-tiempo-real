---
title: "Light Probe Groups"
category: "General"
source_file: "class-LightProbeGroup.html"
doc_type: "manual"
---

# Light Probe Groups

Switch to Scripting

To place Light Probes in your Scene, you must use a GameObject with a **Light Probe Group** component attached. You can add a Light Probe Group component from the menu: **Component > Rendering > Light Probe Group**.

You can add the Light Probe Group component to any GameObject in the Scene. However, it’s good practice to create a new empty GameObject (menu: **GameObject > Create Empty**) and add it to that, to decrease the possibility of accidentally removing it from the Project.

The Light Probe Group component **Property** | **Function**  
---|---  
**Edit Light Probes** | To make changes to a **Light Probe** Group, click the **Edit Light Probes** button to enable editing. This changes Unity so that you can only move and edit Light Probes, so you must remember to disable it when you are finished. You cannot move or edit **GameObjects** Group, click the **Edit Light Probes** button to enable editing. This changes Unity so that you can only move and edit Light Probes, so you must remember to disable it when you are finished. You cannot move or edit **GameObjects** or other element in Unity while **Edit Light Probes** is enabled.  
**Show Wireframe** | When this property is enabled, Unity displays the wireframe of the Light Probe Group in the **Scene** view. When it is disabled, Unity only displays the Light Probe points, and not the wireframe connecting them.  
**Remove Ringing** | When this property is enabled, Unity automatically removes Light Probe ringing from the Scene. For more information, see Ringing, later in this section.  
**Selected Probe Position** | This gives the x, y and z coordinates of the selected Light Probes in the Scene. This property is read-only.  
**Add Probe** | Click this to add a Light Probe to the Light Probe Group.  
**Select All** | Click this to select all Light Probes in the Light Probe Group.  
**Delete Selected** | Click this to delete the selected Light Probes from the Light Probe Group.  
**Duplicate Selected** | Click this to duplicate the selected Light Probes.  
  
### Ringing

Under certain circumstances, Light Probes exhibit an unwanted behaviour called “ringing”. This often happens when there are significant differences in the light surrounding a Light Probe. For example, if you have bright light on one side of a Light Probe, and no light on the other side, the light intensity can “overshoot” on the back side. This overshoot causes a light spot on the back side.

Example of Light Probe ringing

There are several ways to deal with this:

  * In the Light Probe Group component, enable **Remove Ringing**. Unity automatically removes the unintended light spots. However, this generally makes the Light Probes less accurate, and reduces light contrast, so you must check the visual results.
  * Place in-game obstacles in such a way that players can’t get to a position where they can see the light spot.
  * Avoid baking direct light into Light Probes. Direct light tends to have sharp discontinuities (such as shadow edges), which makes it unsuitable for Light Probes. To only bake indirect light, use Mixed lighting.

## Placing Light Probes

When editing a Light Probe Group, you can manipulate individual Light Probes in a similar way to GameObjects. However, Light Probes are not GameObjects; they are a set of points in the Light Probe Group component.

When you begin editing a new Light Probe Group, you start with a default formation of eight probes arranged in a cube, as shown below:

The default arrangement of Light Probes.

You can now use the controls in the Light Probe Group **inspector** to add new probe positions to the group. The probes appear in the Scene as yellow spheres which you can position in the same way as GameObjects. You can also select and duplicate individual probes or in groups, by using the usual “duplicate” keyboard shortcut (ctrl+d/cmd+d).

Remember to disable the Light Probe Group edit mode when you’ve finished editing the Light Probes, so that you can continue to edit and move GameObjects in your Scene as normal.

### Choosing Light Probe positions

Unlike **lightmaps** , which usually have a continuous resolution across the surface of an object, the resolution of the Light Probe information depends on how closely packed you choose to position the Light Probes.

To optimise the amount of data that Light Probes store, and the amount of computation done while the game is playing, you should generally attempt to place as few Light Probes as possible. However, you should also place enough Light Probes so that changes in light from one space to another are recorded at a level that is acceptable to you. This means you might place Light Probes in a more condensed pattern around areas that have complex or highly contrasting light, and you might place them in a much more spread out pattern over areas where the light does not significantly change.

Light Probes placed with varying density around a simple Scene

In the example above, the Light Probes are placed more densely near and between the buildings where there is more contrast and color variation, and less densely along the road, where the lighting does not significantly change.

The simplest approach to positioning Light Probes is to arrange them in a regular 3D grid pattern. While this setup is simple and effective, it is likely to consume more memory than necessary, and you may have lots of redundant Light Probes. For example, in the Scene above, if there were lots of Light Probes placed along the road it would be a waste of resources. The light does not change much along the length of the road, so many Light Probes would be storing almost identical lighting data to their neighbouring Light Probes. In situations like this, it is much more efficient to interpolate this lighting data between fewer, more spread-out, Light Probes.

Light Probes individually do not store a large amount of information. From a technical perspective, each probe is a spherical, panoramic **HDR** image of the view from the sample point, encoded using Spherical Harmonics L2 which is stored as 27 floating point values. However, in large Scenes with hundreds of Light Probes they can add up, and having unnecessarily densely packed Light Probes can result in large amounts of wasted memory in your game.

### Creating a volume

Even if your gameplay takes place on a 2D plane (for example, cars driving around on a road surface), your Light Probes must form a 3D volume.

This means you should have at least two vertical “layers” of points in your group of Light Probes.

In the example below, you can see on the left the Light Probes are arranged only across the surface of the ground. This does not result in good lighting because the Light Probe system cannot calculate sensible tetrahedral volumes from the Light Probes.

On the right, the Light Probes are arranged in two layers, some low to the ground and others higher up, so that together they form a 3D volume made up of lots of individual tetrahedra. This is a good layout.

The left image shows a bad choice of Light Probe positions, because there is no height to the volume defined by the Light Probes. The right image shows a good choice of Light Probe positions.

### Light Probe placement for real-time global illumination

Enlighten Realtime **Global Illumination** makes it possible for moving lights to cast dynamically bounced light on static GameObjects.

When you use Light Probes along with **Enlighten** Realtime Global Illumination, it is also possible for moving lights to cast dynamic bounced light on moving GameObjects. The quality of the resulting lighting depends on how your Light Probes are positioned, and therefore it is important to position them carefully.

A Light Probe captures the indirect lighting at its position in space. In order to faithfully capture the lighting environment, you must place more probes in areas where you expect more variation in the lighting. For example, you may need many probes in areas with moving lights or many occluders. In areas with little or no lighting variation, you can place fewer probes to save on memory and computation resources.

Normally only a few Light Probes are needed in large areas of static light. However, if you plan to have moving lights within this area of static light, and you want moving objects to receive accurate bounced light from these moving lights, you need a dense network of Light Probes within this area to provide sufficient accuracy. The size and range of your lights, how fast these lights move, and the size(s) of the moving objects receiving dynamic light determine how you space your Light Probes.

### Troubleshooting Light Probe placement

Your choice of Light Probe positions must take into account that the lighting is interpolated between sets of Light Probes. Problems can arise if your Light Probes don’t adequately cover the changes in lighting across your Scene.

The example below shows a night-time Scene with two bright street lamps on either side, and a dark area in the middle. If Light Probes are only placed near the street lamps, and none in the dark area, the lighting from the lamps “bleeds” across the dark gap, on moving objects. This is because the lighting is being interpolated from one bright point to another, with no information about the dark area in-between.

This image shows poor Light Probe placement. There are no Light Probes in the dark area between the two lamps, so the dark area is not included in the interpolation at all.

If you are using Realtime or Mixed lights, this problem may be less noticeable, because only the _indirect_ light bleeds across the gap. The problem is more noticable if you are using fully **baked lights** , because in this situation the direct light on moving objects is also interpolated from the Light Probes. In this example Scene, the two lamps are baked, so moving objects get their direct light from Light Probes. Here you can see the result - a moving object (the ambulance) remains brightly lit while passing through the dark area, which is not the desired effect. The yellow wireframe tetrahedron shows that the interpolation is occurring between one brightly lit end of the street to the other.

This is an undesired effect - the ambulance remains brightly lit while passing through a dark area, because no Light Probes were placed in the dark area.

To solve this, you should place more Light Probes in the dark area, as shown below:

Now the Scene has Light Probes in the dark area too. As a result, the moving ambulance takes on the darker lighting as it travels from one side of the Scene to the other.

The ambulance now takes on the darker lighting in the centre of the Scene, as desired.

* * *

  * 2018–10–17 Page amended 

  * 2017–06–08 Page published 

  * **Remove Ringing** added in 2018.3 NewIn20183

  * Light Probes updated in 5.6

LightProbeGroup