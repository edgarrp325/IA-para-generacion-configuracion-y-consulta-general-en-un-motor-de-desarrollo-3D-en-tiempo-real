---
title: "IMGUIContainer"
category: "General"
source_file: "UIE-uxml-element-IMGUIContainer.html"
doc_type: "manual"
---

# IMGUIContainer

The IMGUIContainer element renders IMGUI code in a **UI**

## Create an IMGUIContainer

You can create an IMGUIContainer with UXML or C#. 

Assume you have an IMGUI code snippet like the following:
    
    
    void IMGUICode()
    {
        GUILayout.BeginArea(new Rect(0, 0, 100, 100));
        GUILayout.Button("Hello World");
        GUILayout.EndArea();
    }
    

You can create an IMGUIContainer with the following:

**UXML**
    
    
    <IMGUIContainer onGUIHandler="IMGUICode" />
    

**C#**
    
    
    var imguiContainer = new IMGUIContainer(IMGUICode);
    

## C# base class and namespace

**C# class** : `IMGUIContainer`  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : `VisualElement`

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
`ussClassName` | `.unity-imgui-container` | USS class name of elements of this type.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.

## Additional resources

  * VisualElement
  * Immediate Mode GUI (IMGUI)