---
title: "Scroller"
category: "General"
source_file: "UIE-uxml-element-Scroller.html"
doc_type: "manual"
---

# Scroller

A Scroller lets users scroll through content in your user interface. 

## Create a Scroller

You can create a Scroller with **UI** Builder, UXML, or C#. The following C# example creates a Scroller with a default value, low limit, and high limit, and sets the direction of the Scroller:
    
    
    var scroller = new Scroller();
    scroller.value = 42;
    scroller.lowValue = 0;
    scroller.highValue = 100;
    scroller.direction = SliderDirection.Vertical;
    

## Example

The following UXML example creates a Scroller:
    
    
    <UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <Scroller
            name="the-uxml-scroller"
            direction="Horizontal"
            low-value="0"
            high-value="100" />
    </UXML>
    

The following C# example illustrates some of the customizable functionalities of the Scroller:
    
    
    /// <sample>
    // Get a reference to the scroller from UXML and assign it its value.
    var uxmlField = container.Q<Scroller>("the-uxml-scroller");
    uxmlField.valueChanged += (v) => {};
    uxmlField.value = 42;
    
    // Create a new scroller, disable it, and give it a style class.
    var csharpField = new Scroller(0, 100, (v) => {}, SliderDirection.Vertical);
    csharpField.SetEnabled(false);
    csharpField.AddToClassList("some-styled-scroller");
    csharpField.value = uxmlField.value;
    container.Add(csharpField);
    
    // Mirror value of uxml scroller into the C# field.
    uxmlField.RegisterCallback<ChangeEvent<float>>((evt) =>
    {
        csharpField.value = evt.newValue;
    });
    /// </sample>
    

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.

## C# base class and namespace

**C# class** : `Scroller`  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : `VisualElement`

## Member UXML attributes

This element has the following member attributes:

**Name** | **Type** | **Description**  
---|---|---  
`direction` | `UIElements.SliderDirection` | Direction of this scrollbar.  
`high-value` | `float` | Maximum value.  
`low-value` | `float` | Minimum value.  
`value` | `float` | Value that defines the slider position. It lies between `lowValue` and `highValue`.  
  
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
`ussClassName` | `.unity-scroller` | USS class name of elements of this type.  
`horizontalVariantUssClassName` | `.unity-scroller--horizontal` | USS class name of elements of this type, when they are displayed horizontally.  
`verticalVariantUssClassName` | `.unity-scroller--vertical` | USS class name of elements of this type, when they are displayed vertically.  
`sliderUssClassName` | `.unity-scroller__slider` | USS class name of slider elements in elements of this type.  
`lowButtonUssClassName` | `.unity-scroller__low-button` | USS class name of low buttons in elements of this type.  
`highButtonUssClassName` | `.unity-scroller__high-button` | USS class name of high buttons in elements of this type.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.

## Additional resources

  * ScrollView