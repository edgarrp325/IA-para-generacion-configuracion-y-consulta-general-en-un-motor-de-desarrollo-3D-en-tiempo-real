---
title: "ToolbarMenu"
category: "General"
source_file: "UIE-uxml-element-ToolbarMenu.html"
doc_type: "manual"
---

# ToolbarMenu

A ToolbarMenu is an Editor-only control that serves as a menu. It has a predefined style that matches the Toolbar

## Create a ToolbarMenu

You can create a ToolbarMenu with **UI** Builder, UXML, or C#. The following C# example creates a ToolbarMenu with three menu items:
    
    
    using UnityEditor.UIElements;
    ...
    var toolbarMenu = new ToolbarMenu() { text = "Menu Text" };
    toolbarMenu.menu.AppendAction("Menu item 1", (a) => { Debug.Log("Menu item 1 clicked"); });
    toolbarMenu.menu.AppendAction("Menu item 2", (a) => { Debug.Log("Menu item 2 clicked"); });
    toolbarMenu.menu.AppendAction("Menu item 3", (a) => { Debug.Log("Menu item 3 clicked"); });
    

## C# base class and namespace

**C# class** : `ToolbarMenu`  
**Namespace** : `UnityEditor.UIElements`  
**Base class** : `TextElement`

## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`display-tooltip-when-elided` | `boolean` | When true, a tooltip displays the full version of elided text, and also if a tooltip had been previously provided, it will be overwritten.  
`enable-rich-text` | `boolean` | When false, rich text tags will not be parsed.  
`focusable` | `boolean` | True if the element can be focused.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`text` | `string` | The text to be displayed.  
  
Changing this value will implicitly invoke the `INotifyValueChanged{T}.value` setter, which will raise a `ChangeEvent_1` of type string.  
  
This element also inherits the following attributes from `VisualElement`:

**Name** | **Type** | **Description**  
---|---|---  
`content-container` | `string` | Child elements are added to it, usually this is the same as the element itself.  
`name` | `string` | The name of this VisualElement.  
  
Use this property to write USS selectors that target a specific element. The standard practice is to give an element a unique name.  
`picking-mode` | `UIElements.PickingMode` | Determines if this element can be pick during mouseEvents or `IPanel.Pick` queries.  
`style` | `string` | Reference to the style object of this element.  
  
Contains data computed from USS files or inline styles written to this object in C#.  
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor UI.  
`usage-hints` | `UIElements.UsageHints` | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence (ie. tree expanded states, scroll position, zoom level).  
  
This is the key used to save/load the view data from the view data store. Not setting this key will disable persistence for this `VisualElement`.  
  
## USS classes

The following table lists all the C# public property names and their related USS selector.

**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-toolbar-menu` | USS class name of elements of this type.  
`popupVariantUssClassName` | `.unity-toolbar-menu--popup` | USS class name of elements of this type, when they are displayed as popup menu.  
`textUssClassName` | `.unity-toolbar-menu__text` | USS class name of text elements in elements of this type.  
`arrowUssClassName` | `.unity-toolbar-menu__arrow` | USS class name of arrow indicators in elements of this type.  
`ussClassName` | `.unity-text-element` | USS class name of elements of this type.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.

## Additional resources

  * Toolbar