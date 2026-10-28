---
title: "RadioButton"
category: "General"
source_file: "UIE-uxml-element-RadioButton.html"
doc_type: "manual"
---

# RadioButton

A RadioButton lets users select a single choice when used along with other RadioButtons in a group. You can use a GroupBox to group RadioButtons. Otherwise, the panel acts as the default group.

**Note** : To align an element with other fields in an **Inspector** window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to `BaseField`.

## Create a RadioButton

You can create a RadioButton with **UI** Builder, UXML, or C#. The following C# example creates two new radio buttons in the same container and logically groups them together in the panel.
    
    
    var choice1 = new RadioButton() { text = "Choice 1" };
    choice1.RegisterValueChangedCallback(v => Debug.Log("Choice 1 is : " + v.newValue));
    var choice2 = new RadioButton() { text = "Choice 2" };
    choice2.RegisterValueChangedCallback(v => Debug.Log("Choice 2 is : " + v.newValue));
    container.Add(choice1);
    container.Add(choice2);
    

## Examples

The following UXML example creates a RadioButton:
    
    
    <UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <GroupBox>
            <RadioButton label="UXML Field 1" name="the-uxml-field1" />
            <RadioButton label="UXML Field 2" name="the-uxml-field2" />
        </GroupBox>
    </UXML>
    

The following C# example illustrates some of the customizable functionalities of the RadioButton:
    
    
    /// <sample>
    // Note: See also RadioButtonGroup in the ChoiceField section of UI Toolkit Samples
    
    // Get a reference to the first radio button from UXML and assign a value to it.
    var uxmlField1 = container.Q<RadioButton>("the-uxml-field1");
    var uxmlField2 = container.Q<RadioButton>("the-uxml-field2");
    uxmlField1.value = true;
    
    // Create two RadioButtons in a separate group, disable them, and give them a style class.
    var groupBox = new GroupBox();
    container.Add(groupBox);
    
    var csharpField1 = new RadioButton("C# Field 1");
    csharpField1.SetEnabled(false);
    csharpField1.AddToClassList("some-styled-field");
    groupBox.Add(csharpField1);
    
    var csharpField2 = new RadioButton("C# Field 2");
    csharpField2.SetEnabled(false);
    csharpField2.AddToClassList("some-styled-field");
    groupBox.Add(csharpField2);
    
    csharpField1.value = uxmlField1.value;
    
    // Mirror the value of the UXML field into the C# field.
    uxmlField1.RegisterCallback<ChangeEvent<bool>>((evt) =>
    {
        csharpField1.value = evt.newValue;
    });
    uxmlField2.RegisterCallback<ChangeEvent<bool>>((evt) =>
    {
        csharpField2.value = evt.newValue;
    });
    /// </sample>
    

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.

## C# class and namespace

**C# class** : `RadioButton`  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : `BaseBoolField`

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
`ussClassName` | `.unity-radio-button` | USS class name for RadioButton elements.  
  
Unity adds this USS class to every instance of the RadioButton element. Any styling applied to this class affects every RadioButton located beside, or below the stylesheet in the visual tree.  
`labelUssClassName` | `.unity-radio-button__label` | USS class name for Labels in RadioButton elements.  
  
Unity adds this USS class to the `Label` sub-element of the `RadioButton` if the RadioButton has a Label.  
`inputUssClassName` | `.unity-radio-button__input` | USS class name of input elements in RadioButton elements.  
  
Unity adds this USS class to the input sub-element of the `RadioButton`. The input sub-element provides responses to the manipulator.  
`checkmarkBackgroundUssClassName` | `.unity-radio-button__checkmark-background` | USS class name of checkmark background in RadioButton elements.  
  
Unity adds this USS class to the checkmark background sub-element of the `RadioButton`.  
`checkmarkUssClassName` | `.unity-radio-button__checkmark` | USS class name of checkmark in RadioButton elements.  
  
Unity adds this USS class to the checkmark sub-element of the `RadioButton`.  
`textUssClassName` | `.unity-radio-button__text` | USS class name of Text elements in RadioButton elements.  
  
Unity adds this USS class to Text sub-elements of the `RadioButton`.  
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

  * RadioButtonGroup
  * GroupBox