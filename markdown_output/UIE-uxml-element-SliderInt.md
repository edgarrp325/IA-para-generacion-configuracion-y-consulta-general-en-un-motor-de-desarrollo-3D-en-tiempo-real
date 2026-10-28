---
title: "SliderInt"
category: "General"
source_file: "UIE-uxml-element-SliderInt.html"
doc_type: "manual"
---

# SliderInt

The SliderInt lets users select an integer value from a range of values. You can use a SliderInt to adjust a value, such as the number of lives in a game. To set the value, you drag a thumb along a track, or click the track itself. A slider can also include a **text input field** , where you can modify the value directly.

**Note** : To align an element with other fields in an **Inspector** window, simply apply the `.unity-base-field__aligned` USS class to it. For more information, refer to `BaseField`.

## Create a SliderInt

You can create a SliderInt with **UI** Builder, UXML, or C#. The following C# example creates a SliderInt with a default value, low value, and high value, and sets the direction of the slider:
    
    
    var sliderInt = new SliderInt();
    sliderInt.value = 42;
    sliderInt.lowValue = 0;
    sliderInt.highValue = 100;
    sliderInt.direction = SliderDirection.Horizontal;
    

## Set page size

The SliderInt control has a page-size property that controls how much the thumb moves, and how much the value changes, when you click the track to either side of the thumb.

If the page size value is `0`, clicking the track moves the thumb to the cursor or pointer position, and updates the value accordingly.

If the page size value is greater than `0`, clicking the track moves the thumb toward the cursor or pointer position by a specific amount. SliderInt controls treat page-size as a percentage of the total range.

For example, if the total range is `200`, and the page size is `20`, then the page size amount is `20%` of `200`, or `40`. Each time you click the track, the thumb moves, and the value increases or decreases by `40`.

## Keyboard Shortcuts

You can use keyboard shortcuts to navigate and adjust the SliderInt control. The following table lists the keyboard shortcuts: 

**Shortcut** | **Action**  
---|---  
**Arrow Keys** | Move by `1/100` of the entire range.  
**Arrow Keys + Shift** | Move by `1/10` of the entire range.  
**Home** | Jump to the start of the slider.  
**End** | Jump to the end of the slider.  
**Page Up** | Move up by `(1/100 of the range) × page size`.  
**Page Down** | Move down by `(1/100 of the range) × page size`.  
  
## Example

The following UXML example creates a SliderInt:
    
    
    <UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <SliderInt
            label="UXML Slider"
            name="the-uxml-slider"
            low-value="0"
            high-value="100"
            page-size="1"
            value="42" />
    </UXML>
    

The following C# example illustrates some of the customizable functionalities of the SliderInt:
    
    
    /// <sample>
    // Get a reference to the slider from UXML and assign it its value.
    var uxmlSlider = container.Q<SliderInt>("the-uxml-slider");
    uxmlSlider.value = 42;
    
    // Create a new slider, disable it, and give it a style class.
    var csharpSlider = new SliderInt("C# Slider", 0, 100);
    csharpSlider.SetEnabled(false);
    csharpSlider.AddToClassList("some-styled-slider");
    csharpSlider.value = uxmlSlider.value;
    container.Add(csharpSlider);
    
    // Mirror value of uxml slider into the C# field.
    uxmlSlider.RegisterCallback<ChangeEvent<int>>((evt) =>
    {
        csharpSlider.value = evt.newValue;
    });
    /// </sample>
    

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.

## C# base class and namespace

**C# class** : `SliderInt`  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : `BaseSlider_1`

## Member UXML attributes

This element has the following member attributes:

**Name** | **Type** | **Description**  
---|---|---  
`page-size` | `int` | The value to add or remove to the SliderInt.value when it is clicked.  
  
This is casted to int.  
  
## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`direction` | `UIElements.SliderDirection` | This is the actual property to contain the direction of the slider.  
`focusable` | `boolean` | True if the element can be focused.  
`high-value` | `int` | This is the maximum value that the slider encodes.  
`inverted` | `boolean` | This indicates whether or not this slider is inverted. For an inverted horizontal slider, high value is located to the left, low value is located to the right For an inverted vertical slider, high value is located to the bottom, low value is located to the top.  
`label` | `string` | The string representing the label that will appear beside the field.  
`low-value` | `int` | This is the minimum value that the slider encodes.  
`page-size` | `int` | This is a generic page size used to change the value when clicking in the slider.  
`show-input-field` | `boolean` | The visibility of the optional field inside the slider control.  
  
Set this property to true to display a numerical text field that provides another way to edit the slider value.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`value` | `int` | The actual value of the slider.  
  
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
`ussClassName` | `.unity-slider-int` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-slider-int__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-slider-int__input` | USS class name of input elements in elements of this type.  
`ussClassName` | `.unity-base-slider` | USS class name of elements of this type.  
`labelUssClassName` | `.unity-base-slider__label` | USS class name of labels in elements of this type.  
`inputUssClassName` | `.unity-base-slider__input` | USS class name of input elements in elements of this type.  
`horizontalVariantUssClassName` | `.unity-base-slider--horizontal` | USS class name of elements of this type, when they are displayed horizontally.  
`verticalVariantUssClassName` | `.unity-base-slider--vertical` | USS class name of elements of this type, when they are displayed vertically.  
`dragContainerUssClassName` | `.unity-base-slider__drag-container` | USS class name of container elements in elements of this type.  
`trackerUssClassName` | `.unity-base-slider__tracker` | USS class name of tracker elements in elements of this type.  
`draggerUssClassName` | `.unity-base-slider__dragger` | USS class name of dragger elements in elements of this type.  
`draggerBorderUssClassName` | `.unity-base-slider__dragger-border` | USS class name of the dragger border element in elements of this type.  
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

  * Slider
  * MinMaxSlider