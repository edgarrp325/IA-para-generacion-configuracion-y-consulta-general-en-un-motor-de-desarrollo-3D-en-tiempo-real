---
title: "ToolbarToggle"
category: "General"
source_file: "UIE-uxml-element-ToolbarToggle.html"
doc_type: "manual"
---

# ToolbarToggle

A ToolbarToggle is an Editor-only control that serves as a toggle in a Toolbar. It’s a Toggle with a predefined style that matches the Toolbar style. It looks like a button that you can toggle on and off.

## Create a ToolbarToggle

You can create a ToolbarToggle with **UI** Builder, UXML, or C#. The following C# example creates a ToolbarToggle with a label:
    
    
    using UnityEditor.UIElements;
    ...
    var toolbarToggle = new ToolbarToggle() { text = "Toggle me" };
    

## C# base class and namespace

**C# class** : `ToolbarToggle`  
**Namespace** : `UnityEditor.UIElements`  
**Base class** : `Toggle`

## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`label` | `string` | The string representing the label that will appear beside the field.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`text` | `string` | Optional text that appears after the BaseBoolField.  
  
Unity creates a `Label` automatically if one does not exist.  
`value` | `boolean` | The value associated with the field.  
  
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
`ussClassName` | `.unity-toolbar-toggle` | USS class name of elements of this type.  
`ussClassName` | `.unity-toggle` | USS class name for Toggle elements.  
  
Unity adds this USS class to every instance of the Toggle element. Any styling applied to this class affects every Toggle located beside, or below the stylesheet in the visual tree.  
`labelUssClassName` | `.unity-toggle__label` | USS class name for Labels in Toggle elements.  
  
Unity adds this USS class to the `Label` sub-element of the `Toggle` if the Toggle has a Label.  
`inputUssClassName` | `.unity-toggle__input` | USS class name of input elements in Toggle elements.  
  
Unity adds this USS class to the input sub-element of the `Toggle`. The input sub-element provides responses to the manipulator.  
`noTextVariantUssClassName` | `.unity-toggle--no-text` | USS class name of Toggle elements that have no text.  
  
Unity adds this USS class to the `Toggle` if the Toggle does not have a label.  
`checkmarkUssClassName` | `.unity-toggle__checkmark` | USS class name of Images in Toggle elements.  
  
Unity adds this USS class to the Image sub-element of the `Toggle` that contains the checkmark image.  
`textUssClassName` | `.unity-toggle__text` | USS class name of Text elements in Toggle elements.  
  
Unity adds this USS class to Text sub-elements of the `Toggle`.  
`mixedValuesUssClassName` | `.unity-toggle__mixed-values` | USS class name of Toggle elements that have mixed values  
  
Unity adds this USS class to checkmark of the `Toggle` when it has mixed values.  
`ussClassName` | `.unity-base-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-base-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-base-field__input` | USS class name of input elements in elements of this type.  
`noLabelVariantUssClassName` | `.unity-base-field--no-label` | USS class name of elements of this type, when there is no label.  
`labelDraggerVariantUssClassName` | `.unity-base-field__label--with-dragger` | USS class name of labels in elements of this type, when there is a dragger attached on them.  
`mixedValueLabelUssClassName` | `.unity-base-field__label--mixed-value` | USS class name of elements that show mixed values  
`alignedFieldUssClassName` | `.unity-base-field__aligned` | USS class name of elements that are aligned in a **inspector** element  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.

## Additional resources

  * Toolbar