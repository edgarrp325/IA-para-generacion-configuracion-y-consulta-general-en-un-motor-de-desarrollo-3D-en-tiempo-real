---
title: "The Inspector window"
category: "General"
source_file: "UsingTheInspector.html"
doc_type: "manual"
---

# The Inspector window

Use the **Inspector** window to view and edit properties and settings for almost everything in the Unity Editor, including **GameObjects**

The Inspector window docked in the Unity Editor

## Open an Inspector window

To open an Inspector window, do one of the following:

  * From the menu, select **Windows > General > Inspector** to open a floating Inspector window.
  * From any window’s More Items menu (⋮), select **Add Tab > Inspector** to open an Inspector in a new tab.

You can open as many Inspector windows as you want, and reposition, dock, and resize them in the same way you can any other window.

## Control Inspector window focus

By default, an Inspector window displays properties for the current selection. The contents of the Inspector change whenever the selection changes. To keep the same set of properties open, regardless of the current selection, do one of the following:

  * Lock the Inspector window to the current selection. When you lock an Inspector window, it no longer updates if you change the selection.
  * Open a focused Inspector for a GameObject, Asset, or component. Focused Inspectors only ever display the properties of the items you opened them for.

## Inspect items

What you can see and edit in an Inspector window depends on what you select. This section describes what an Inspector window displays for different types of items you can select.

### Inspecting GameObjects

When you select a GameObject (for example, in the Hierarchy or Scene view

### Inspect custom script components

When GameObjects have custom script components attached, the Inspector displays the **scripts** ’ public variables. You can edit script variables in the same way as you edit any other properties, which means that you can set parameters and default values in your scripts without modifying the code.

For more information, see Variables and the Inspector in the Scripting section.

### Inspect Assets

When you select an Asset (for example, from the Project window (for example, from the Project window), the Inspector displays settings that control how Unity imports and uses the Asset at runtime.

Each type of Asset has its own settings. Examples of Asset import settings that you edit in an Inspector window include the:

  * Model Import Settings window.
  * Audio Clip Import Settings window.
  * Texture Import Settings window.

### Inspect Prefabs

When you work with Prefabs, the Inspector window displays some additional information and provides some additional options. For example:

  * When you Edit a Prefab Instance, the Inspector window provides options for working with the Prefab Asset and applying overrides.
  * When you apply Instance overrides, the Inspector window displays the names of properties you override in bold.

For more information about working with Prefabs in the Inspector window, see the Prefabs section.

## Inspect multiple Items

When you have two or more items selected, you can edit all of the properties they have in common in an Inspector window. Unity copies the values you supply to all the selected items. The Inspector window displays a count of the number of selected items.

### Multiple GameObjects

When you select multiple GameObjects, the Inspector window displays all of the components they have in common.

  * For property values that are different across two or more selected GameObjects, the Inspector displays a dash (**-**) (1 in the screenshot below).
  * For property values that are the same across all selected GameObjects, the Inspector displays the actual values (2 in the screenshot below).
  * To apply a property value from one selected GameObject to all of the selected GameObjects, right-click the property name and select **Set to Value of _[Name of GameObject]_** from the context menu (3 in the screenshot below).
  * If any of the selected GameObjects has components that are not present on the other selected objects, the Inspector displays a message that some components are hidden.

Inspector showing multiple selected GameObjects

### Multiple Assets

When you select multiple Assets of the same type, the Inspector window displays all of the properties they have in common.

  * For property values that are the same across all selected Assets, the Inspector displays the actual values.
  * For property values that are different across two or more selected Assets, the Inspector displays a dash (**-**) (1 in the screenshot below).
  * For properties that you cannot edit for all of the selected Assets at once, the Inspector grays them out (2 in the screenshot below).

Inspector showing multiple selected Assets of the same type

When you select multiple Assets of different types, the Inspector displays a list that shows how many of each type of Asset are selected. Click any item in the list to Inspect all Assets of that type.

Inspector showing multiple selected Assets of different types

### Multiple Prefabs

You can inspect multiple selected instances of a Prefab in the same way as you edit multiple GameObjects, but the Inspector hides the **Select** , **Revert** , and **Apply** buttons (see Editing a Prefab via its instances).

## Locate an Inspector window’s source

When you open a GameObject or Asset in an Inspector window, you can locate it in the **Scene** view or Project View using the **Ping** command.

From the Inspector window’s **More Items** (**⋮**) menu, select **Ping**. Unity highlights the item in the Hierarchy view or the Project view.

The ping command highlights the item currently displayed in the Inspector

* * *

  * Component drag and drop added in Unity 5.6
  * Reorganized Inspector section pages in Unity 2020.1