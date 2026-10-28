---
title: "DoubleField"
category: "General"
source_file: "UIE-uxml-element-DoubleField.html"
doc_type: "manual"
---

# DoubleField

A DoubleField lets users input a numerical double value into an application. It accepts and displays text input. You can set placeholder text to provide hints or instructions to the user on what to enter. You can also add validation functions to ensure that the entered data meets certain requirements.

**Note** : To align a DoubleField with other fields in an **Inspector** window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to `BaseField`.

## Create a DoubleField

You can create a DoubleField with **UI** Builder, UXML, and C#.

To create a DoubleField with C#, create a new instance of a DoubleField object. For example:
    
    
    DoubleField myElement = new DoubleField("Label text");
    

## Customize the input text selection

Input text is selectable by default. You can customize the selection behaviors such as `selectAllOnMouseUP` and `selectAllOnFocus`.

In C#, set them through `textSelection`:
    
    
    myElement.textSelection.selectAllOnMouseUp = false;
    myElement.textSelection.selectAllOnFocus = false;
    

## C# base class and namespace

**C# class** : `DoubleField`  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : `TextValueField_1`

## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`is-delayed` | `boolean` | If set to true, the value property isn’t updated until either the user presses Enter or the text field loses focus.  
`label` | `string` | The string representing the label that will appear beside the field.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`value` | `double` | This is the value of the field.  
  
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
`ussClassName` | `.unity-double-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-double-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-double-field__input` | USS class name of input elements in elements of this type.  
`ussClassName` | `.unity-base-text-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-base-text-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-base-text-field__input` | USS class name of input elements in elements of this type.  
`singleLineInputUssClassName` | `.unity-base-text-field__input--single-line` | USS class name of single line input elements in elements of this type.  
`multilineInputUssClassName` | `.unity-base-text-field__input--multiline` | USS class name of multiline input elements in elements of this type.  
`ussClassName` | `.unity-base-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-base-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-base-field__input` | USS class name of input elements in elements of this type.  
`noLabelVariantUssClassName` | `.unity-base-field--no-label` | USS class name of elements of this type, when there is no label.  
`labelDraggerVariantUssClassName` | `.unity-base-field__label--with-dragger` | USS class name of labels in elements of this type, when there is a dragger attached on them.  
`mixedValueLabelUssClassName` | `.unity-base-field__label--mixed-value` | USS class name of elements that show mixed values  
`alignedFieldUssClassName` | `.unity-base-field__aligned` | USS class name of elements that are aligned in a inspector element  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.

## Additional resources

  * Work with text
  * Label
  * TextField
  * IntegerField
  * LongField
  * FloatField
  * PropertyField