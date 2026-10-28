---
title: "Sorting Groups"
category: "General"
source_file: "class-SortingGroup.html"
doc_type: "manual"
---

# Sorting Groups

**Sorting Groups** allow you to group **GameObjects** with Sprite Renderers with Sprite Renderers together, and control the order in which they render their Sprites. Unity renders **Sprite** together, and control the order in which they render their Sprites. Unity renders **Sprite** Renderers in the same Sorting Group together, as if they are a single GameObject.

## Set up a Sorting Group

To place a GameObject into a Sorting Group, add the Sorting Group component to it. To do this, select the GameObject and go to **Component > Rendering > Sorting Group**, or select the Add Component button in the Inspector window of the GameObject.

When you add a Sorting Group component to a GameObject, Unity applies the same Sorting Group to all child GameObjects of the GameObject the component is attached to.

  
The ‘Sprite’ child objects belong to the empty parent GameObject’s **Sorting Group**.

Unity uses the Sorting Group’s settings to determine how to sort its Renderers among other Renderers and Sorting Groups in the **Scene**. See 2D sorting for more information.

To sort Renderers within a Sorting Group, Unity uses the individual sort settings of the Renderers in the Sorting Group. See Sorting Renderers within a Sorting Group for more information.

## Sorting Group properties

Unity uses a **Sorting Group** ’s Sorting Layer and **Order in Layer** values to determine its priority in the rendering queue among other Sorting Groups and GameObjects in the Scene.

The Sorting Group component Property | Function  
---|---  
**Sorting Layer** | Select or add a Sorting Layer from this drop-down menu to determine the Sorting Group’s position in the render queue. Unity determines the Sorting Layer order by its place in the Sorting Layer settings; it renders Sorting Layers in the order they appear in the list. See Tags and Layers for information on setting up Sorting Layers.  
**Order in Layer** | Set the render order of this Sorting Group within its **Sorting Layer**. Unity queues Renderers with lower values first in the render queue, so they appear before Renderers with higher values.  
**Sort At Root** | Enable this option to ignore all parent Sorting Groups if this Sorting Group is nested. This allows this Sorting Group to be sorted against other Renderers and Sorting Groups at the root level.  
  
See 2D Sorting for more information on using Sorting Layers to sort Sprites, and Unity’s Renderer sorting criteria.

## Sorting Renderers within a Sorting Group

Unity sorts all Renderers within the same Sorting Group by their individual **Sorting Layer** and **Order in Layer** Renderer properties. Unity does not consider each Renderer’s individual **Distance to**Camera****

The Sorting Group’s internal sort order remains constant when Unity sorts the Sorting Group among other Renderers and Sorting Groups in the Scene.

The following diagram shows the sorting process.

Internal Sorting Group sorting process.

Unity treats all Renderers that belong to the same Sorting Group as a single layer, and sorts non-grouped Renderers based on their **Sorting Layer** and **Order in Layer** property settings.

### Particle System

The Editor treats a Particle System that is a child of a Sorting Group as another Renderer within that Sorting Group, and sorts it internally among other Renderers based on its **Sorting Layer** and **Order in Layer** property settings.

When Unity sorts the Particle System with the other Renderers within the Sorting Group, it ignores the Particle System’s **Sorting Fudge** value.

### Nested Sorting Groups

A nested Sorting Group is a Sorting Group that has a parent Sorting Group. Unity sorts Renderers within a nested Sorting Group first, before their parent (see Sorting Renderers within a Sorting Group.

After Unity determines the internal sort order of the nested Sorting Group, it sorts the nested Sorting Group with other Renderers or Sorting Groups within the parent Sorting Group. A nested Sorting Group can have a nested Sorting Group as a child. Unity sorts the innermost child Groups first, before their respective parents.

The following diagram gives you an example of the nested Sorting Group sorting process.

Nested Sorting Group sorting process.

### Sort At Root

In certain situations, you may have a nested Sorting Group that is ordered based on the Scene Hierarchy. However, you may want this nested Sorting Group to be rendered separately from its parent Sorting Group without changing its position in the Scene Hierarchy.

You can enable this option to allow this Sorting Group to ignore its parent Sorting Groups, which allows this Sorting Group to be sorted against other Renderers and Sorting Groups globally without requiring the GameObject to be reparented to another Transform. All child Renderers and Sorting Groups (which have not ignored their parents) will be sorted under this Sorting Group.

## Using Sorting Groups

The most common way to create a 2D multi-Sprite character is to arrange and parent multiple Sprite Renderers together in the Hierarchy window to form a character. You can use **Sorting Groups** to help manage this kind of complex multi-Sprite character.

In the example below, the Sprite Renderers belong to the same **Sorting Layer** , but with different **Order in Layer** values. Unity sorts the different parts of a character in the order that you want them to appear.

A character Prefab with its parts in a hierarchy.

After you’ve configured the Sorting Groups and Sorting Layers, you can save your character as a Prefab, and clone it as many times as you need to.

However, Prefab Sprites all have the same **Sorting Layer** and **Order in Layer** values and render to the same layers as other Prefabs, which can cause different parts of a Prefab character to intersect and layer incorrectly.

Sprites from two Prefabs intersect incorrectly, because Unity is rendering the Sprites on the same layers.

To make sure Prefabs keep their own render order consistent so they appear correctly, add the Sorting Group component to the root GameObject of each Prefab. Save the edited Prefab, so that all current and future instances of the Prefab also have the Sorting Group component.

Each Prefab should have a Sorting Group component with the same **Sorting Layer** and **Order in Layer** property settings. This might cause Renderers in the Prefabs that are on the same **Sorting Layer** to render in inconsistent ways, because they have the same priority in the Render Queue.

To prevent this issue, give each Prefab’s Sorting Group component a unique **Order in Layer** value. Unity renders Sorting Groups with lower **Order in Layer** values first and those with higher values overlap the Sorting Groups that are lower. Refer to Tags and Layers for more information about editing and reordering **Sorting Layers**.

Each Prefab has a Sorting Group component with a unique **Order in Layer** value to ensure that Unity renders each character and their parts correctly.

SortingGroup