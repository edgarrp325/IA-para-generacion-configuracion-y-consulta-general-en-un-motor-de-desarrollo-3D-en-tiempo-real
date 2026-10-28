---
title: "Types of Reflection Probe"
category: "General"
source_file: "RefProbeTypes.html"
doc_type: "manual"
---

# Types of Reflection Probe

Reflection probes come in three basic types as chosen by the **Type** property in the **inspector** (see the component reference page for further details).

  * **Baked** probes store a reflection **cubemap** generated (“baked”) within the editor. You can trigger the baking by clicking either the _Bake_ button at the bottom of the Reflection Probe inspector or the **Generate Lighting** button in the Lighting window. If you have **Auto** enabled in the Lighting window then baked probes will be updated automatically as you place objects in the **Scene** generated (“baked”) within the editor. You can trigger the baking by clicking either the _Bake_ button at the bottom of the Reflection Probe inspector or the **Generate Lighting** button in the Lighting window. If you have **Auto** enabled in the Lighting window then baked probes will be updated automatically as you place objects in the **Scene** view. The reflection from a baked probe can only show objects marked as **Reflection Probe Static** in the inspector. This indicates to Unity that the objects will not move at runtime.
  * **Realtime** probes create the cubemap at runtime in the player rather than the editor. This means that the reflections are not limited to static objects and can be updated in real time to show changes in the scene. However, it takes considerable processing time to refresh the view of a probe so it is wise to manage the updates carefully. Unity allows you to trigger updates from a script so you can control exactly when they happen. Also, there is an option to apply **timeslicing** to probe updates so that they can take place gradually over a few frames.
  * A **Custom** probe type is also available. These probes let you bake the view in the editor, as with Baked probes, but you can also supply a custom cubemap for the reflections. Custom probes cannot be updated at runtime.

The three types are explained in detail below.

## Baked and Custom Reflection Probes

A **Baked** Reflection Probe is one whose reflection cubemap is captured in the Unity editor and stored for subsequent usage in the player (see the Reflection Probes Introduction for further information). Once the capture process is complete, the reflections are “frozen” and so baked probes can’t react to runtime changes in the scene caused by moving objects. However, they come with a much lower processing overhead than Realtime Probes (which do react to changes) and are acceptable for many purposes. For example, if there is only a single moving reflective object then it need only reflect its static surroundings.

### Using Baked probes

You should set the probe’s **Type** property to **Baked** or _Custom_ in order to make it behave as a baked probe (see below for the additional features offered by Custom probes).

The reflections captured by baked probes can only include scene objects marked as **Reflection Probe Static** (using the **Static** menu at the top left of the inspector panel for all objects). You can further refine the objects that get included in the reflection cubemap using the ****Culling Mask**** and ****Clipping Planes**** and ****Clipping Planes**** properties, which work the same way as for a Camera properties, which work the same way as for a Camera (the probe is essentially like a camera that is rotated to view each of the six cubemap faces).

When the **Auto** option is switched on (from the Lighting window), the baked reflections will update automatically as you position objects in the scene. If you are not making use of auto baking then you will need to click the **Bake** button in the Reflection Probe inspector to update the probes. (The **Generate Lighting** button in the Lighting window will also trigger the probes to update.)

Whether you use auto or manual baking, the bake process will take place asynchronously while you continue to work in the editor. However, if you move any static objects, change their materials or otherwise alter their visual appearance then the baking process will be restarted.

## Custom Probes

By default, Custom probes work the same way as Baked probes but they also have additional options that change this behaviour.

The **Dynamic Objects** property on a custom probe’s inspector allows objects that are not marked as **Reflection Probe Static** to be included in the reflection cubemap.

**Note** : The positions of these objects are still “frozen” in the reflection at the time of baking.

The **Cubemap** property allows you to assign your own cubemap to the probe and therefore make it completely independent of what it can “see” from its view point. You could use this, say, to set a **skybox** or a cubemap generated from your 3D modelling app as the source for reflections.

## Realtime Probes

Baked probes are useful for many purposes and have good runtime performance but they have the disadvantage of not updating live within the player. This means that objects can move around in the scene without their reflections moving along with them. In cases where this is too limiting, you can use **Realtime** probes, which update the reflection cubemap at runtime. This effect comes with a higher processing overhead but offers greater realism.

### Using Realtime Probes

To enable a probe to update at runtime, you should set its **Type** property to **Realtime** in the Reflection Probe Inspector. You don’t need to mark objects as **Reflection Probe Static** to capture their reflections (as you would with a baked probe). However, you can selectively exclude objects from the reflection cubemap using the **Culling Mask** and **Clipping Planes** properties, which work the same way as for a Camera (the probe is essentially like a camera that is rotated to view each of the six cubemap faces).

In the editor, real-time probes have much the same workflow as baked probes, although they tend to render more quickly.

**Note** : Currently, real-time probes will only update their reflections in the **Scene view** when **Reflection Probe Static** objects are moved or change their appearance. This means that moving dynamic objects won’t cause an update even though those objects appear in the reflection. You should choose the **Bake Reflection Probes** option from the **Generate Lighting** button dropdown in the Lighting window to update reflections when a dynamic object is changed.