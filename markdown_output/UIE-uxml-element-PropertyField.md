---
title: "PropertyField"
category: "General"
source_file: "UIE-uxml-element-PropertyField.html"
doc_type: "manual"
---

# PropertyField

A PropertyField is a field element specifically designed to be bound to a SerializedProperty. Once you bind a property to a PropertyField, a nested BaseField element is created based on the property type. For example, if you bind an int property to a PropertyField, an IntegerField is nested inside the PropertyField.

## Align a PropertyField with other fields in an Inspector window

By default, PropertyFields are created with the `.unity-base-field__aligned` USS class, which is also applied to each nested field that gets created upon binding. However, if you manually add a child BaseField element to a PropertyField, you must add the style class manually to that child field element. When the `.unity-base-field__aligned` class is present in an InspectorElement, the field calculates the label width to align with other fields in the **Inspector** window. If there are IMGUI fields present, **UI** window. If there are IMGUI fields present, **UI** Toolkit fields are aligned with them for consistency and compatibility.

## C# base class and namespace

**C# class** : `PropertyField`  
**Namespace** : `UnityEditor.UIElements`  
**Base class** : `VisualElement`

## Member UXML attributes

This element has the following member attributes:

**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`label` | `string` | Optionally overwrite the label of the generate property field. If no label is provided the string will be taken from the SerializedProperty.  
  
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
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor UI.  
`usage-hints` | `UIElements.UsageHints` | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence (ie. tree expanded states, scroll position, zoom level).  
  
This is the key used to save/load the view data from the view data store. Not setting this key will disable persistence for this `VisualElement`.  
  
## USS classes

The following table lists all the C# public property names and their related USS selector.

**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-property-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-property-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-property-field__input` | USS class name of input elements in elements of this type.  
`inspectorElementUssClassName` | `.unity-property-field__inspector-property` | USS class name of property fields in inspector elements  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.

## Additional resources

  * Create a custom inspector
  * TextField
  * DoubleField
  * LongField
  * FloatField
  * IntegerField