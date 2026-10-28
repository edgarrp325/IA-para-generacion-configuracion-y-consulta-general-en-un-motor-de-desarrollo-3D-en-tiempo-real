---
title: "Label"
category: "General"
source_file: "UIE-uxml-element-Label.html"
doc_type: "manual"
---

# Label

A Label is a text element that you can use to display text. You can use a Label to display a title or a description for a control.

## Create a Label

You can create a Label with **UI** Builder, UXML, or C#. The following C# example creates a Label with the text “Hello World” and sets the font size, font style, text alignment, and color:
    
    
    var label = new Label("Hello World");
    label.style.fontSize = 14;
    label.style.unityFontStyleAndWeight = FontStyle.Bold;
    label.style.unityTextAlign = TextAnchor.MiddleCenter;
    label.style.color = Color.red;
    

## Example

The following UXML example creates a Label:
    
    
    <UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <Label text="UXML Label" name="the-uxml-label" />
    </UXML>
    

The following C# example illustrates some of the customizable functionalities of the Label:
    
    
    /// <sample>
    // Get a reference to the label from UXML and update its text.
    var uxmlLabel = container.Q<Label>("the-uxml-label");
    uxmlLabel.text += " (Updated in C#)";
    
    // Create a new label and give it a style class.
    var csharpLabel = new Label("C# Label");
    csharpLabel.AddToClassList("some-styled-label");
    container.Add(csharpLabel);
    /// </sample>
    

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.

## C# base class and namespace

**C# class** : `Label`  
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
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor UI.  
`usage-hints` | `UIElements.UsageHints` | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence (ie. tree expanded states, scroll position, zoom level).  
  
This is the key used to save/load the view data from the view data store. Not setting this key will disable persistence for this `VisualElement`.  
  
## USS classes

The following table lists all the C# public property names and their related USS selector.

**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-label` | USS class name of elements of this type.  
`ussClassName` | `.unity-text-element` | USS class name of elements of this type.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.

## Additional resources

  * TextElement