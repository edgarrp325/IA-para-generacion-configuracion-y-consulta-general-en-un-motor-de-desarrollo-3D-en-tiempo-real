---
title: "EnumFlagsField"
category: "General"
source_file: "UIE-uxml-element-EnumFlagsField.html"
doc_type: "manual"
---

# EnumFlagsField

An EnumFlagsField lets users select multiple values from an enumeration that are marked with the Flags attribute.

**Note** : To align an EnumFlagsField with other fields in an **Inspector** window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to `BaseField`.

## Create an EnumFlagsField

You can create an EnumField with UXML and C#. 

Assume you have the following enumeration:
    
    
    [Flags]
    enum MyEnum
    {
        None = 0,
        First = 1,
        Second = 2,
        Third = 4
    }
    

The following C# example creates an EnumFlagsField with the `MyEnum` enumeration and selects the first and second values:
    
    
    var myEnumFlagsField = new EnumFlagsField("Select Options", MyEnum.First | MyEnum.Second);
    

## Example

The following UXML example creates an EnumFlagsField element:
    
    
    <UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <uie:EnumFlagsField label="UXML Field" name="the-uxml-field" include-obsolete-values="false"/>
    </UXML>
    

The following C# example illustrates some of the customizable functionalities of the EnumFlagsField element:
    
    
    /// <sample>
    // Get a reference to the field from UXML,
    // initialize it with an Enum type,
    // and assign a value to it.
    var uxmlField = container.Q<EnumFlagsField>("the-uxml-field");
    uxmlField.Init(EnumFlags.First);
    uxmlField.value = EnumFlags.Second;
    
    // Create a new field, disable it, and give it a style class.
    var csharpField = new EnumFlagsField("C# Field", uxmlField.value);
    csharpField.SetEnabled(false);
    csharpField.AddToClassList("some-styled-field");
    csharpField.value = uxmlField.value;
    container.Add(csharpField);
    
    // Mirror the value of the UXML field into the C# field.
    uxmlField.RegisterCallback<ChangeEvent<Enum>>((evt) =>
    {
        csharpField.value = evt.newValue;
    });
    /// </sample>
    

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.

## C# base class and namespace

**C# class** : `EnumFlagsField`  
**Namespace** : `UnityEditor.UIElements`  
**Base class** : `BaseMaskField_1`

## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`label` | `string` | The string representing the label that will appear beside the field.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`value` | `string` | The value associated with the field.  
  
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
`ussClassName` | `.unity-enum-flags-field` | USS class name for elements of this type.  
`labelUssClassName` | `.unity-enum-flags-field__label` | USS class name for labels of this type.  
`inputUssClassName` | `.unity-enum-flags-field__input` | USS class name for input elements of this type.  
`ussClassName` | `.unity-base-popup-field` | USS class name of elements of this type.  
`textUssClassName` | `.unity-base-popup-field__text` | USS class name of text elements in elements of this type.  
`arrowUssClassName` | `.unity-base-popup-field__arrow` | USS class name of arrow indicators in elements of this type.  
`labelUssClassName` | `.unity-base-popup-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-base-popup-field__input` | USS class name of input elements in elements of this type.  
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

  * EnumField