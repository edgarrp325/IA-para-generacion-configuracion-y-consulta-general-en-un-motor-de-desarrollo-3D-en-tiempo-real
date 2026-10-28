---
title: "Focused Inspectors"
category: "General"
source_file: "InspectorFocused.html"
doc_type: "manual"
---

# Focused Inspectors

A focused **Inspector** is a dedicated Inspector window for a specific **GameObject** is a dedicated Inspector window for a specific **GameObject** , Unity component, or Asset. It always displays the properties of the item you opened it for, even if you select something else in the **Scene** , Unity component, or Asset. It always displays the properties of the item you opened it for, even if you select something else in the **Scene** or Project.

Focused Inspectors work just like regular Inspectors, except for the following differences:

  * They do not update to show the properties for the current selection.
  * You cannot lock them. Each focused Inspector shows a specific item’s properties, so there’s no need.
  * You cannot toggle between Debug and Normal mode from a focused Inspector.

You can open as many focused Inspectors as you want. Focused Inspectors open in floating windows that you can reposition, dock, and resize in the same way you can any other window.

Unity saves any open focused Inspectors when you close a Project, and restores them when you reopen it.

## Open focused Inspectors

There are several ways to open a focused Inspector, depending on what you’re inspecting.

Unity adds focused Inspectors to the list of open windows (Menu: **Window > Panels > _[LIST OF OPEN WINDOWS]_**).

Select a focused Inspector from the list to bring it to the front.

### For GameObjects and Project Assets

To open a focused Inspector for a single GameObject or Asset:

  1. Right-click a GameObject in the Hierarchy view, or an Asset in the Project view.
  2. From the context menu, select **Properties**.

Alternatively, select the GameObject or Asset and do one of the following:

  * From the main menu, select **Assets > Properties**.
  * Use the **Alt + P** / **Option + Shift + P** shortcut.
  * In the **Inspector** window, select **More items** (**⋮**) > **Properties**.

Unity opens the focused Inspector in a new window.

To open focused Inspectors for multiple GameObjects and/or Assets:

  1. Select any combination of GameObjects in the Hierarchy view and Assets in the Project view.
  2. Do one of the following: 
     * Right-click one of the selected items, and from the context menu, select **Properties**.
     * From the main menu, select **Assets > Properties**.
     * Use the **Alt + P** / **Option + Shift + P** shortcut.

Unity opens a new window with a focused Inspector tab for each selected item.

The image below shows three selected items (left), two GameObjects and one Asset, and the window you get when you open a focused Inspector for them (right).

### For components

To open a focused Inspector for one of a GameObject’s components:

  1. Inspect the GameObject and locate the component you want to open a focused Inspector for.
  2. From the component’s **More items** (**⋮**) menu, select **Properties**.

This is useful for frequently edited properties. For example you may want to move a GameObject often, but leave the rest of its properties unchanged. In that case, you can open its **Transform component**.

The image below shows a **Camera** open in a regular Inspector (1), and its Transform component open in a focused Inspector (2). Notice that the focused Inspector’s tab header displays the name of the GameObject that the component belongs to.

### For reference properties

When a GameObject has reference properties, you can open focused Inspectors for the GameObjects or Assets they reference.

  1. Inspect the GameObject and locate the property whose reference you want to open in a focused Inspector.
  2. Right-click the reference field and select **Properties** from the context menu.

### For hover items

You can set up a shortcut to open a focused **Inspector** for the item your mouse hovers over in the **Hierarchy** window. This lets you open a focused **Inspector** for an item without affecting the current selection.

To assign a keyboard shortcut to the **PropertyEditor > OpenMouseOver** command, use the Shortcuts Manager.

This is useful when you want to open a focused Inspector for an item without affecting the current selection.

## Locate a focused Inspector’s source

To locate the item whose properties are displayed in a focused Inspector, do one of the following:

  * From the focused Inspector’s **More Items** (**⋮**) menu, select **Ping**. Unity highlights the item in the Hierarchy view or the Project view.

  * Hover the pointer over the focused Inspector’s tab header to display a tooltip that shows the full path to the item in the Scene Hierarchy or the Project.