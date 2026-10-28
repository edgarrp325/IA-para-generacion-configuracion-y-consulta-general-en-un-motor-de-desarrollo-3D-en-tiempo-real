---
title: "Binding examples"
category: "General"
source_file: "UIE-binding-examples.html"
doc_type: "manual"
---

# Binding examples

Learn Editor data binding from examples.

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
  
## Additional resources

  * Create a bindable custom control