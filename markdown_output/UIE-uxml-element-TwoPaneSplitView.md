---
title: "TwoPaneSplitView"
category: "General"
source_file: "UIE-uxml-element-TwoPaneSplitView.html"
doc_type: "manual"
---

# TwoPaneSplitView

The `TwoPaneSplitView` element is a container that arranges its children in two panes, either horizontally or vertically. The user can resize the panes by dragging the divider between them. A `TwoPaneSplitView` must have exactly two children.

TwoPaneSplitView example

## Create a TwoPaneSplitView

You can create a TwoPaneSplitView with UXML and C#.

To create a TwoPaneSplitView with C#, create a new instance of a TwoPaneSplitView object. For example:
    
    
    TwoPaneSplitView myElement = new TwoPaneSplitView();
    
    // Add two child elements to the TwoPaneSplitView
    VisualElement child1 = new VisualElement();
    VisualElement child2 = new VisualElement();
    myElement.Add(child1);
    myElement.Add(child2);
    

By default, the orientation is horizontal. You can change the orientation with the orientation property.

## Examples

The best way to learn how to use TwoPaneSplitView is to try examples:

  * Create a custom Editor window with C# script

## C# base class and namespace

**C# class** : `TwoPaneSplitView`  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : `VisualElement`

## Member UXML attributes

This element has the following member attributes:

**Name** | **Type** | **Description**  
---|---|---  
`fixed-pane-index` | `int` | 0 for setting first child as the fixed pane, 1 for the second child element.  
`fixed-pane-initial-dimension` | `int` | The initial width or height for the fixed pane.  
`orientation` | `UIElements.TwoPaneSplitViewOrientation` | Orientation of the split view.  
  
## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`focusable` | `boolean` | True if the element can be focused.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
  
This element also inherits the following attributes from `VisualElement`:

**Name** | **Type** | **Description**  
---|---|---  
`content-container` | `string` | Child elements are added to it, usually this is the same as the element itself.  
`name` | `string` | The name of this VisualElement.  
  
Use this property to write USS selectors that target a specific element. The standard practice is to give an element a unique name.  
`picking-mode` | `UIElements.PickingMode` | Determines if this element can be pick during mouseEvents or `IPanel.Pick` queries.  
`style` | `string` | Reference to the style object of this element.  
  
Contains data computed from USS files or inline styles written to this object in C#.  
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor **UI**.  
`usage-hints` | `UIElements.UsageHints` | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence (ie. tree expanded states, scroll position, zoom level).  
  
This is the key used to save/load the view data from the view data store. Not setting this key will disable persistence for this `VisualElement`.  
  
## USS classes

The following table lists all the C# public property names and their related USS selector.

**C# property** | **USS selector** | **Description**  
---|---|---  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.