---
title: "HelpBox"
category: "General"
source_file: "UIE-uxml-element-HelpBox.html"
doc_type: "manual"
---

# HelpBox

A HelpBox displays a message to the user. You can set the type of message to display, such as a warning or an error. You can also set the message to display as rich text.

## Create a HelpBox

You can create a HelpBox with UXML and C#. The following C# example creates a HelpBox with the message “Help text” and the information icon:
    
    
    HelpBox helpBox = new HelpBox("Help text", HelpBoxMessageType.Info);
    

## Example

The following UXML example creates a HelpBox with a warning message:
    
    
    <UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <HelpBox text="UXML Help Box" message-type="Info" name="the-uxml-help-box" />
    </UXML>
    

The following C# example illustrates some of the customizable functionalities of the HelpBox:
    
    
    /// <sample>
    // Get a reference to the help box from UXML and update its text.
    var uxmlHelpBox = container.Q<HelpBox>("the-uxml-help-box");
    uxmlHelpBox.text += " (Updated in C#)";
    
    // Create a new help box and give it a style class.
    var csharpHelpBox = new HelpBox("This is a help box", HelpBoxMessageType.Warning);
    csharpHelpBox.AddToClassList("some-styled-help-box");
    container.Add(csharpHelpBox);
    /// </sample>
    

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.

## C# base class and namespace

**C# class** : `HelpBox`  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : `VisualElement`

## Member UXML attributes

This element has the following member attributes:

**Name** | **Type** | **Description**  
---|---|---  
`message-type` | `UIElements.HelpBoxMessageType` | The type of message.  
`text` | `string` | The message text.  
  
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
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor **UI**.  
`usage-hints` | `UIElements.UsageHints` | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence (ie. tree expanded states, scroll position, zoom level).  
  
This is the key used to save/load the view data from the view data store. Not setting this key will disable persistence for this `VisualElement`.  
  
## USS classes

The following table lists all the C# public property names and their related USS selector.

**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-help-box` | The USS class name for Elements of this type.  
`labelUssClassName` | `.unity-help-box__label` | The USS class name for labels in Elements of this type.  
`iconUssClassName` | `.unity-help-box__icon` | The USS class name for images in Elements of this type.  
`iconInfoUssClassName` | `.unity-help-box__icon--info` | The USS class name for the `HelpBoxMessageType.Info` state in Elements of this type.  
`iconwarningUssClassName` | `.unity-help-box__icon--warning` | The USS class name for the `HelpBoxMessageType.Warning` state in Elements of this type.  
`iconErrorUssClassName` | `.unity-help-box__icon--error` | The USS class name for the `HelpBoxMessageType.Error` state in Elements of this type.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.

## Additional resources

  * Work with text