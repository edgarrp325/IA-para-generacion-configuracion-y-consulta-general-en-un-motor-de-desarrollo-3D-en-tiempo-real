---
title: "ProgressBar"
category: "General"
source_file: "UIE-uxml-element-ProgressBar.html"
doc_type: "manual"
---

# ProgressBar

A ProgressBar element displays the progress of an ongoing task or process. Use it to provide visual feedback to the user about the progress of a task, such as file downloads, game level loading, or any other task that might take a while to complete.

You can set low and high values for the ProgressBar. The ProgressBar’s current value is constrained within these bounds. `0` is the lowest value that the ProgressBar can have.

## Create a ProgressBar

You can create a ProgressBar with **UI** Builder, UXML, and C#.

To create a ProgressBar with C#, create a new instance of a ProgressBar object. For example:
    
    
    ProgressBar myElement = new ProgressBar("Label text");
    

## Customize the bar

To change the style of the bar, use the `.unity-progress-bar__progress` USS selector. For example, the following USS changes the size and the color of the bar:
    
    
    .unity-progress-bar__progress {
        width: 20px;
        height: 50px;
        background-color: yellow;
    }
    

## C# base class and namespace

**C# class** : `ProgressBar`  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : `AbstractProgressBar`

## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`high-value` | `float` | Sets the maximum value of the ProgressBar.  
`low-value` | `float` | Sets the minimum value of the ProgressBar.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`title` | `string` | Sets the title of the ProgressBar that displays in the center of the control.  
`value` | `float` | Sets the progress value. If the value has changed, dispatches an `ChangeEvent_1` of type float.  
  
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
`ussClassName` | `.unity-progress-bar` | USS Class Name used to style the `ProgressBar`.  
`containerUssClassName` | `.unity-progress-bar__container` | USS Class Name used to style the container of the `ProgressBar`.  
`titleUssClassName` | `.unity-progress-bar__title` | USS Class Name used to style the title of the `ProgressBar`.  
`titleContainerUssClassName` | `.unity-progress-bar__title-container` | USS Class Name used to style the container of the title of the `ProgressBar`.  
`progressUssClassName` | `.unity-progress-bar__progress` | USS Class Name used to style the progress bar of the `ProgressBar`.  
`backgroundUssClassName` | `.unity-progress-bar__background` | USS Class Name used to style the background of the `ProgressBar`.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.

## Additional resources

  * Label
  * RadioButton