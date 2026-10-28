---
title: "Examples"
category: "General"
source_file: "UIE-examples.html"
doc_type: "manual"
---

# Examples

This page lists a collection of examples that you can build with **UI** Toolkit:

## Layout

**Topics** | **Description**  
---|---  
Relative and absolute positioning C# example | Use relative and absolute positioning to lay out UI in C#.  
  
## List and tree views

**Topics** | **Description**  
---|---  
Create list and tree views | Use ListView, TreeView, MultiColumnListView, and MultiColumnTreeView to create list and tree views.  
Create a complex list view | Use ListView to create a custom Editor window with a list of characters.  
Create a list view runtime UI | Use ListView to create a simple character selection screen runtime UI.  
  
## Scroll view

**Topics** | **Description**  
---|---  
Wrap content inside a ScrollView | Use styles to wrap content inside a scroll view.  
  
## Label

**Topics** | **Description**  
---|---  
Create a tabbed menu for runtime | Use Label to create tabbed menu.  
  
## Pop-up window

**Topics** | **Description**  
---|---  
Create a pop-up window | Use `UnityEditor.PopupWindow` to create a pop-up window  
  
## Toggle

**Topics** | **Description**  
---|---  
Use Toggle to create a conditional UI | Use Toggle to create a conditional UI in an Editor window.  
  
## Custom control

**Topics** | **Description**  
---|---  
Create a custom control with two attributes | Create a simple custom control with two attributes and expose the custom control to the UXML and UI Builder.  
Create a slide toggle custom control | Create a “switch-like” toggle custom control.  
Create a radial progress indicator | Create a custom control that displays a floating point number between 0 and 100.  
Create a bindable custom control | Create a custom control that bounds to a property with the double data type.  
Create a custom style for a custom control | Create a custom control that reads two colors from USS and uses them to generate a texture.  
  
## Transition

**Topics** | **Description**  
---|---  
Create a simple transition with UI Builder and C# scripts | Create a custom Editor window with three labels that rotate and scale when you hover over them.  
Create a transition event | Create a custom Editor window with a button and color palette.  
Create looping transitions | Create a Yo-yo and a A-to-B looping animations.  
  
## Drag-and-drop

**Topics** | **Description**  
---|---  
Create a drag-and-drop UI inside a custom Editor window | Create several slots, and one object that can be dragged into any slot.  
Create a drag-and-drop UI to drag between Editor windows | Create two custom Editor windows that an asset can be dragged from one window to another.  
  
## Basic binding examples

**Topics** | **Description**  
---|---  
Bind with binding path in C# script | Use `bindingPath` to create a binding that changes the name of a **GameObject** in a custom Editor window.  
Bind without the binding path | Use `BindProperty()` to create a binding that changes the name of a GameObject in a custom Editor window.  
Bind with UXML and C# | Create a binding and set the binding path in UXML, and bind with `Bind()` in C#.  
Create a binding with the Inspector | Create a binding that binds among a custom **Inspector** , a custom Editor, and serialized objects.  
Bind to nested properties | Use the `binding-path` attribute of a BindableElement in UXML to bind fields to nested properties of a SerializedObject  
Bind to a UXML template | Create a binding and set binding paths with UXML templates.  
Receive callbacks when a bound property changes | Creates a custom Editor window with a TextField that binds to the name of a GameObject in a **scene**.  
Receive callbacks when any bound properties change | Create a custom Inspector with two fields that warns the user if the values of the fields fall outside certain ranges.  
  
## Advanced binding examples

**Topics** | **Description**  
---|---  
Bind to a list with ListView | Create a list of toggles and binds the list to an underlying list of objects.  
Bind to a list without ListView | Create a binding that binds to a list with array instead of ListView.  
Bind a custom control | Create a custom control and bind it to a native Unity type.  
Bind a custom control to custom data type | Create a custom control and bind it to a custom data type.  
  
## Vector UI examples

**Topics** | **Description**  
---|---  
Create a pie chart in the Editor and runtime UI | Use the Vector API to create a pie chart.  
Use Vector API to create a radial progress indicator | Use the Vector API to create a radial progress indicator custom control and add the custom control in a runtime UI.