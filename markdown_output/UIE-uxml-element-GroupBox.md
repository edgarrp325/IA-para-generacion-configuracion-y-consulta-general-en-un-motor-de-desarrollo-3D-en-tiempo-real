---
title: "GroupBox"
category: "General"
source_file: "UIE-uxml-element-GroupBox.html"
doc_type: "manual"
---

# GroupBox

A GroupBox is a container element for a logical group of multiple **visual elements**. You can use a combination of GroupBox and RadioButton if you want to have multiple groups of options in the same panel. 

Two group boxes with three radio buttons each.

If you want to treat your group of radio buttons as a single field, use RadioButtonGroup. In most cases, it’s better to use RadioButtonGroup because you must register every single radio button when you use the GroupBox and RadioButton combo. However, use the combo if you want to add additional visual elements in the group. 

A group box with two radio buttons, an input text field, and a button.

## Create a GroupBox with C# script

The following C# code snippets create a GroupBox and add three radio buttons to it so that they’re logically grouped.
    
    
    var group = new GroupBox("Group Example");
    // Must register change events on each radio button.
    var choice1 = new RadioButton("First Choice");
    choice1.RegisterValueChangedCallback(v => Debug.Log("Choice 1 is : " + v.newValue));
    var choice2 = new RadioButton("Second Choice");
    choice2.RegisterValueChangedCallback(v => Debug.Log("Choice 2 is : " + v.newValue));
    var choice3 = new RadioButton("Third Choice");
    choice3.RegisterValueChangedCallback(v => Debug.Log("Choice 3 is : " + v.newValue));
    group.Add(choice1);
    group.Add(choice2);
    group.Add(choice3);
    rootVisualElement.Add(group);
    

## C# class and namespace

**C# class** : `GroupBox`  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : `BindableElement`

## Member UXML attributes

This element has the following member attributes:

**Name** | **Type** | **Description**  
---|---|---  
`text` | `string` | The title text of the box.  
  
## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
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
`ussClassName` | `.unity-group-box` | USS class name for GroupBox elements.  
  
Unity adds this USS class to every instance of the GroupBox element. Any styling applied to this class affects every GroupBox located beside, or below the stylesheet in the visual tree.  
`labelUssClassName` | `.unity-group-box__label` | USS class name for Labels in GroupBox elements.  
  
Unity adds this USS class to the `Label` sub-element of the `GroupBox` if the GroupBox has a Label.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.

## Additional resources

  * RadioButtonGroup
  * RadioButton