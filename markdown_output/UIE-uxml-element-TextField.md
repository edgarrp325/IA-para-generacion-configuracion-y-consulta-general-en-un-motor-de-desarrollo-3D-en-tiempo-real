---
title: "TextField"
category: "General"
source_file: "UIE-uxml-element-TextField.html"
doc_type: "manual"
---

# TextField

A TextField lets users input text data into an application. It accepts and displays text input. You can set placeholder text to provide hints or instructions to the user on what to enter. You can also add validation functions to ensure that the entered data meets certain requirements.

**Note** : To align a TextField with other fields in an **Inspector** window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to `BaseField`.

## Create a TextField

You can create a TextField with **UI** Builder, UXML, and C#. The following C# example creates a TextField that allows multiple lines text input:
    
    
    var textField = new TextField();
    textField.label = "Enter your text here:";
    textField.multiline = true;
    textField.maxLength = 140;
    

## Customize the input text selection

Input text is selectable by default. You can customize the selection behaviors such as `selectAllOnMouseUP` and `selectAllOnFocus`.

In C#, set them through `textSelection`:
    
    
    myElement.textSelection.selectAllOnMouseUp = false;
    myElement.textSelection.selectAllOnFocus = false;
    

You can also style the selected text using the `--unity-selection-color` USS custom property. For example, the following USS sets the color of the selected input text to yellow: 
    
    
    .unity-base-text-field__input {
        --unity-selection-color: yellow;
    }
    

## Enable a vertical scrollbar

If you have enabled multiline text on the TextField, you can display a vertical scrollbar for the **text input field**.

In C#, set the `verticalScrollerVisibility` property to `ScrollerVisibility.Auto` or `ScrollerVisibility.AlwaysVisible`:
    
    
    // Set the multiline property to true to enable multiple lines of text
    textField.multiline = true;
    
    // Set the vertical scrollbar visibility to AlwaysVisible
    textField.verticalScrollerVisibility = ScrollerVisibility.AlwaysVisible;
    

## Control the behavior of the input text

You can use events to control the behavior of the input text. 

For example, to override the default behaviors for the **Enter** and **Shift + Tab** keyboard events in a TextField, register a KeyDownEvent to the TrickleDown phase before they’re handled by the `TextElement` base class:
    
    
    myField.RegisterCallback<KeyDownEvent>((evt) => { 
    
        if (evt.keyCode == KeyCode.Return || evt.character == '\n')
        {
            // Submit logic
            evt.StopPropagation();
            evt.PreventDefault();
        }
    
        if (evt.modifiers == EventModifiers.Shift && (evt.keyCode == KeyCode.Tab || evt.character == '\t'))
        {
            // Focus logic
            evt.StopPropagation();
            evt.PreventDefault();
        }
    
    }, TrickleDown.TrickleDown);
    

## Example

The following UXML example creates a TextField:
    
    
    <UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <TextField label="UXML Field" name="the-uxml-field" value="It's snowing outside." />
    </UXML>
    

The following C# example illustrates some of the customizable functionalities of the TextField:
    
    
    /// <sample>
    // Get a reference to the field from UXML and append a value to it.
    var uxmlField = container.Q<TextField>("the-uxml-field");
    uxmlField.value += "..";
    
    // Create a new field, disable it, and give it a style class.
    var csharpField = new TextField("C# Field");
    csharpField.value = "It's snowing outside...";
    csharpField.SetEnabled(false);
    csharpField.AddToClassList("some-styled-field");
    csharpField.value = uxmlField.value;
    container.Add(csharpField);
    
    // Mirror the value of the UXML field into the C# field.
    uxmlField.RegisterCallback<ChangeEvent<string>>((evt) =>
    {
        csharpField.value = evt.newValue;
    });
    /// </sample>
    

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.

## C# base class and namespace

**C# class** : `TextField`  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : `TextInputBaseField_1`

## Member UXML attributes

This element has the following member attributes:

**Name** | **Type** | **Description**  
---|---|---  
`multiline` | `boolean` | Set this to true to allow multiple lines in the textfield and false if otherwise.  
`value` | `string` | The string currently being exposed by the field.  
  
Note that changing this will not trigger a change event to be sent.  
  
## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`auto-correction` | `boolean` | Determines if the touch screen keyboard auto correction is turned on or off.  
`binding-path` | `string` | Path of the target property to be bound.  
`focusable` | `boolean` | True if the element can be focused.  
`hide-mobile-input` | `boolean` | Hides or shows the mobile input field.  
`is-delayed` | `boolean` | If set to true, the value property isn’t updated until either the user presses Enter or the text field loses focus.  
`keyboard-type` | `TouchScreenKeyboardType` | The type of mobile keyboard that will be used.  
`label` | `string` | The string representing the label that will appear beside the field.  
`max-length` | `int` | Maximum number of characters for the field.  
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
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor UI.  
`usage-hints` | `UIElements.UsageHints` | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence (ie. tree expanded states, scroll position, zoom level).  
  
This is the key used to save/load the view data from the view data store. Not setting this key will disable persistence for this `VisualElement`.  
  
## USS classes

The following table lists all the C# public property names and their related USS selector.

**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-text-field` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-text-field__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-text-field__input` | USS class name of input elements in elements of this type.  
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

## USS custom properties

The following table outlines the custom properties that are available exclusively for the TextField element in USS:

Property | Type | Description  
---|---|---  
`--unity-cursor-color` | string | The color code of the text caret.  
`--unity-selection-color` | string | The color code of the selected text.  
  
## Additional resources

  * Work with text
  * Label
  * DoubleField
  * LongField
  * FloatField
  * IntegerField
  * PropertyField