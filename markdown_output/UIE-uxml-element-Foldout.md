---
title: "Foldout"
category: "General"
source_file: "UIE-uxml-element-Foldout.html"
doc_type: "manual"
---

# Foldout

A Foldout is a collapsible section of a **UI**. The Foldout hides or reveals the elements it contains when you click its header.

## Create a Foldout

A Foldout has the following elements:

  * **Label** : A label you can use as the name of the Foldout.
  * **Toggle** : Click the toggle to expand or collapse the container sub-element. It is styled to look like an arrow rather than the default checkbox. When the container is collapsed, the arrow points right. When the container is expanded, the arrow points down.
  * **Container** : A container contains the **visual elements** that you want to show or hide when you toggle the Foldout.

You can add elements to a Foldout’s container, and the show-or-hide function works automatically. 

The following UI Document creates a Foldout with two buttons in its container. The two buttons show or hide when you toggle the Foldout.
    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" xsi="http://www.w3.org/2001/XMLSchema-instance" engine="UnityEngine.UIElements" editor="UnityEditor.UIElements" noNamespaceSchemaLocation="../../UIElementsSchema/UIElements.xsd" editor-extension-mode="False">
        <ui:Foldout text="Foldout" name="MyFoldout" value="true">
            <ui:Button text="First item" />
            <ui:Button text="Second item" />
        </ui:Foldout>
    </ui:UXML>
    

## Respond to user actions

A Foldout and its Toggle sub-element respond to Change events. The Toggle hides or shows the Foldout container.

You can bind a Foldout to a Boolean variable or access its value through the `INotifyValueChanged<bool>` interface.

## Examples

The following C# code snippet creates a Foldout and checks whether the foldout is expanded:
    
    
    // Create a new foldout, add two elements to it and add it to the container
    var cSharpFoldout = new Foldout {text = "Elements"};
    cSharpFoldout.Add(new Label("Indented Label"));
    cSharpFoldout.Add(new Slider("Indented Slider", 0, 100));
    container.Add(cSharpFoldout);
    
    cSharpFoldout.RegisterValueChangedCallback(e =>
    {
        // Check whether the foldout is expanded
        if (cSharpFoldout.value)
        {
            Debug.Log("Foldout is expanded");
        }
        else
        {
            Debug.Log("Foldout is collapsed");
        }
    });
    

## C# base class and namespace

**C# class** : `Foldout`  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : `BindableElement`

## Member UXML attributes

This element has the following member attributes:

**Name** | **Type** | **Description**  
---|---|---  
`text` | `string` | This is the text of the toggle’s label.  
`value` | `boolean` | This is the state of the Foldout’s toggle. It is true if the `Foldout` is open and its contents are visible, and false if the Foldout is closed, and its contents are hidden.  
  
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
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor UI.  
`usage-hints` | `UIElements.UsageHints` | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence (ie. tree expanded states, scroll position, zoom level).  
  
This is the key used to save/load the view data from the view data store. Not setting this key will disable persistence for this `VisualElement`.  
  
## USS classes

The following table lists all the C# public property names and their related USS selector.

**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-foldout` | The USS class name for Foldout elements.  
  
Unity adds this USS class to every instance of a `Foldout`. Any styling applied to this class affects every Foldout located beside, or below the stylesheet in the visual tree.  
`toggleUssClassName` | `.unity-foldout__toggle` | The USS class name of Toggle sub-elements in Foldout elements.  
  
Unity adds this USS class to the `Toggle` sub-element of every `Foldout`. Any styling applied to this class affects every Toggle sub-element located beside, or below the stylesheet in the visual tree.  
`contentUssClassName` | `.unity-foldout__content` | The USS class name for the content element in a Foldout.  
  
Unity adds this USS class to the `VisualElement` that contains the elements to be shown or hidden. Any styling applied to this class affects every foldout container located beside, or below the stylesheet in the visual tree.  
`inputUssClassName` | `.unity-foldout__input` | The USS class name for the Label element in a Foldout.  
  
Unity adds this USS class to the `VisualElement` that contains the `Toggle` input elements. Any styling applied to this class affects every foldout container located beside, or below the stylesheet in the visual tree.  
`checkmarkUssClassName` | `.unity-foldout__checkmark` | The USS class name for the Label element in a Foldout.  
  
Unity adds this USS class to the `VisualElement` that represents the checkmark of the `Toggle` sub-element of every `Foldout`. Any styling applied to this class affects every foldout container located beside, or below the stylesheet in the visual tree.  
`textUssClassName` | `.unity-foldout__text` | The USS class name for the Label element in a Foldout.  
  
Unity adds this USS class to the `Label` in the `Toggle` sub-element of every `Foldout`. Any styling applied to this class affects every foldout container located beside, or below the stylesheet in the visual tree.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.

## Additional resource

  * Change events
  * Toggle