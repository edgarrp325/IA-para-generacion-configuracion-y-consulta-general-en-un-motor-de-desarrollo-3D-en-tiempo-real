---
title: "Working in the Inspector"
category: "General"
source_file: "InspectorOptions.html"
doc_type: "manual"
---

# Working in the Inspector

This page describes some options for controlling the **Inspector** window itself. For information about setting properties for **GameObjects** window itself. For information about setting properties for **GameObjects** , **scripts** , **scripts** , and Assets, see Editing properties. 

## Lock the Inspector

Normally, the Inspector shows the properties of the currently selected GameObject, script, or Asset. But sometimes, it’s useful to keep one item in the Inspector while you work with other items. In that case, you can lock an Inspector window to a specific item.

To lock an Inspector window to an item, click the lock icon in the Inspector window. The lock icon changes to show that the Inspector is now locked to the selection.

The Inspector lock button in in its unlocked (left) and locked (right) states

This is useful when you’re editing one item’s properties frequently. For example, if you’re fine-tuning a Camera’s position, you can lock an Inspector window to the Camera, and open a second Inspector window (**More Items** (**⋮**) menu: **Add Tab > Inspector**) to continue displaying the properties of the current selection.

**Note:**  
---  
Focused Inspectors are an alternative to locking the Inspector window. A focused Inspector only ever displays the properties of the item you open it for.  
  
## Reorder GameObject components

You can reorder a GameObject’s components in the Inspector window. The component order you apply in the Inspector is the same order that you need to use when you query components in your scripts.

A GameObject’s **Transform component** is always the topmost component. You cannot move it, or place other components above it.

To reorder a GameObject’s components in the Inspector window, do one of the following:

  * Drag-and-drop component headers from one position to another. When you drag a component header, a blue insertion marker appears where Unity will place the component.

Reordering GameObject components in the Inspector by dragging and dropping

  * Right-click a component to open the context menu, and select **Move Up** or **Move Down**.

Reordering GameObject components in the Inspector using the context menu

### Reordering components for multiple GameObjects

When you select multiple GameObjects, the Inspector displays all of the components that the selected GameObjects have in common. If you reorder these common components, the changes apply to all of the selected GameObjects.

## Assign icons

You can assign custom icons to GameObjects, **Prefabs** , and scripts from the Inspector window. Custom icons appear in the Scene view, and scripts from the Inspector window. Custom icons appear in the Scene view in the same way as default icons for items such as Lights and **Cameras** in the same way as default icons for items such as Lights and **Cameras**.

  * When you assign an icon to a GameObject, the icon appears in the **Scene** view over that GameObject, and any duplicates.
  * When you assign an icon to a Prefab, the icon appears in the Scene view over any instances of that Prefab.
  * When you assign an icon to a script, the icon appears in the Scene view over any GameObject that has the script attached.

To control how Unity draws custom icons in the Scene view, use the Gizmos menu.

NOTE  
---  
When you change an Asset’s icon, Unity marks the Asset as modified, and **version control** systems register the change.  
  
### Assign custom icons to GameObjects, scripts, and Prefabs

To assign a custom icon to a GameObject or a script:

  1. Open the item in an Inspector window.
  2. Click the **Select icon** button.
  3. Choose an icon from the **Select icon** menu (see below).

The Select Icon button for GameObjects/Prefabs (left) and scripts (right)

To assign a custom icon to a Prefab, you must open the Prefab in Prefab Mode.

### Choose icons from the Select icon menu

You assign custom Icons from the **Select Icon** menu.

Icon type: | Description:  
---|---  
1 | Label icons are colored capsules. In the Scene view, they display the names of the items they’re assigned to.  
  
Click a label icon to assign it.  
2 | Image-only icons are colored divots. They’re useful when you work with objects that may not have a visual representation. For example, you can assign image-only icons to navigation waypoints so you can see and select them in the Scene view.   
  
Click an image-only icon to assign it.  
3 | Asset icons are image Assets in your Scene that you use as custom icons. For example, you could use a skull and crossbones icon to indicate danger areas in a game level.  
  
Click the **Other** button to open an Object Picker window and select an image Asset to assign as an icon.  
  
## Toggle Debug Mode

Normally, the Inspector window is configured as an editor for the selection’s properties. But sometimes it’s useful to only see the properties and their values. When you activate Debug mode, the Inspector shows only the properties and their values. If the selection has script components, Debug mode also displays private variables, although you can’t edit their values.

You can toggle Debug mode for each Inspector window individually.

  * To turn on Debug mode, click the **More Items** (**⋮**) button to open the context menu, and select **Debug**.
  * To return to Normal mode, click the **More Items** (**⋮**) button to open the context menu, and select **Normal**.

A Mesh Renderer component in Normal mode (left) and Debug mode (right)

* * *

  * Reorganized Inspector section pages in Unity 2020.1