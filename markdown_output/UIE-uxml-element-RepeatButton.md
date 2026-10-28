---
title: "RepeatButton"
category: "General"
source_file: "UIE-uxml-element-RepeatButton.html"
doc_type: "manual"
---

# RepeatButton

A RepeatButton performs a repetitive action when users press and hold it. You define the action, a delay, and an interval. When users press the RepeatButton, the initial delay must be met before the first action starts, and then it repeats at the specified interval.

**Note** : A RepeatButton doesn’t have the same styling as a regular Button. You can apply the `.unity-button` USS class to it to make it look like a regular Button.

## Create a RepeatButton

Although you can create a RepeatButton with UXML, you must create the action logic in C#. The following C# example creates a RepeatButton that logs a console message when pressed and held:
    
    
    // The logging delays 100ms before starting and repeats every 50ms.
    var repeatButton = new RepeatButton(() => { Debug.Log("Button being pressed"); }, 100, 50);
    repeatButton.text = "Press and hold me";
    
    // Apply the ".unity-button" USS class to make the RepeatButton look like a regular Button.
    repeatButton.AddToClassList("unity-button");
    

## C# base class and namespace

**C# class** : `RepeatButton`  
**Namespace** : `UnityEngine.UIElements`  
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
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor **UI**.  
`usage-hints` | `UIElements.UsageHints` | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence (ie. tree expanded states, scroll position, zoom level).  
  
This is the key used to save/load the view data from the view data store. Not setting this key will disable persistence for this `VisualElement`.  
  
## USS classes

The following table lists all the C# public property names and their related USS selector.

**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-repeat-button` | USS class name of elements of this type.  
`ussClassName` | `.unity-text-element` | USS class name of elements of this type.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.

## Additional resources

  * Button