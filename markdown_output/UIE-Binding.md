---
title: "SerializedObject data binding"
category: "General"
source_file: "UIE-Binding.html"
doc_type: "manual"
---

# SerializedObject data binding

Data bindings synchronize properties of non-UI object, such as a `string` property on a `MonoBehaviour`, with properties of **UI**

Use data binding to synchronize values between a property and a specific **visual element** , so you don’t need to write event handlers when the value changes in the UI.

**Note** : SerializedObject data binding only works in the Editor, not at runtime.

## Serialization requirements

You can only bind to serialized properties. This means you can only bind visual elements to the following objects that are compatible with the Serialization system:

  * User-defined `ScriptableObject` classes
  * User-defined `MonoBehaviour` classes
  * Native Unity component types
  * Native Unity asset types
  * Primitive C# types such as `int`, `bool`, `float`, and so on.
  * Native Unity types such as `Vector3`, `Color`, `Object`, and so on.

## Value binding

You can only bind the `value` property of visual elements that implement the `INotifyValueChanged` interface. For example, you can bind `TextField.value` to a `string`, but you can’t bind `TextField.name` to a `string`. 

You can bind between an object and any visual element that either derives from `BindableElement` or implements the `IBindable` interface.

## Create a binding

To create a binding, either call `Bind()` or `BindProperty()`.

### Call `Bind()`

You can call `Bind()` to bind an element to a SerializedObject. Before you bind an element, you must set the binding path and create a SerializedObject. 

Use this method if you don’t have easy access to the `SerializedProperty` for the binding. Refer to Create a binding with a C# script for an example.

The `Bind()` extension method sets up an entire hierarchy of visual elements with specified `bindingPath` properties. You can call the `Bind()` method on a single element or the parent of the hierarchy that you want to bind. For example, you can call `Bind()` on the `rootVisualElement` of an Editor window. This binds all child elements with specified `bindingPath` properties.

Don’t call `Bind()` from the `Editor.CreateInspectorGUI()` or `PropertyDrawer.CreatePropertyGUI()` override. These overrides are called automatically on the visual elements that these methods return.

### Call `Unbind()`

The `Unbind()` method stops the value tracking for the element and all its direct and indirect child elements. In general, you don’t need to call `Unbind()` because tracking stops when a user closes the Inspector or Editor window. Call `Unbind()` if you must bind elements to different targets in their lifetimes. 

If you construct an `InspectorElement` in C# by calling its constructor, binding occurs during the constructor call. If you want to rebind an `InspectorElement` after it has been constructed, you must call `Unbind()` and then either call `Bind()` explicitly or let a bind operation from a parent create a binding.

### Set binding path

If you call `Bind()` to create the binding, you must set the visual element’s binding path to the property name of the object that you want to bind to. 

For example:

  * If you have the following component script:
        
        using UnityEngine;
        
        public class MyComp : MonoBehaviour
        {
            [SerializeField]
            int m_Count;
        }
        

To bind your visual element to `m_Count`, set the binding path to `m_Count`.

  * If you want to bind a visual element to a **GameObject** ’s name property, which is `m_Name`, set the binding path to `m_Name`. 

You can set the binding path in UI Builder, UXML, or with a C# script:

  * In UI Builder, enter the binding path in the **Binding Path** field for a visual element in the Inspector.
  * In UXML, set the `binding-path` attribute for a visual element. Refer to Define the binding path in UXML for an example.
  * In C#, set `bindingPath` from the `IBindable` interface. Refer to Bind with the binding path for an example.

### Call `BindProperty()`

You can call `BindProperty()` to bind an element to a `SerializedProperty` directly. 

Use this method if you already have a `SerializedProperty` object, and especially if you traverse the properties of a `SerializedObject` to build a UI dynamically. Refer to Bind without the binding path for an example.

### Bind elements to nested properties

You can bind a visual element to nested properties in the source object. To do so, combine the binding path of an element with the binding path of the first ancestor. Use this method with the following elements:

  * `BindableElement`
  * `TemplateContainer` (corresponds to the `<Instance>` tag in UXML)
  * `GroupBox`

See Bind to nested properties for an example.

### Receive callbacks when values change

You can create a binding to receive a callback when a bound serialized property changes. To do so, leverage the `TrackPropertyValue()` extension method, which is available to any `VisualElement`. This registers a callback that executes when the provided `SerializedProperty` changes. Refer to Receive callbacks when a serialized property changes for an example.

You can also create a binding to receive a callback when any properties of the bound serialized object change. To do so, leverage the `TrackSerializedObjectValue()` extension method, which is available to any `VisualElement`. This registers a callback that executes when the provided `SerializedProperty` changes. Refer to Receive callbacks when any properties change for an example.

### Bind custom elements

You can create custom elements and bind them to serialized properties through the value binding system.

To create bindable custom elements:

  1. Declare a custom element.
  2. Inherit the element from `BindableElement` or implement the `IBinding` interface.
  3. Implement the `INotifyValueChanged` interface.
  4. Implement the `SetValueWithoutNotify()` method to the `INotifyValueChanged` interface.
  5. Implement the `value` property accessors to the `INotifyValueChanged` interface.

Refer to Create and style a custom control for an example.

**Note** : You can’t bind custom data types directly to custom elements because the binding system only allows you to bind an element to a type supported by SerializedPropertyType of `enum`. This means you can’t define a class or structure, for example, a struct called `MyStruct`, and bind it to an element that implements `INotifyValueChanged<MyStruct>`. However, you can bind to serializable nested properties of custom data types. This includes polymorphic serialization (when a field uses the `[SerializeReference]` attribute). Refer to Bind a custom control to custom data type for an example.

## Best practices

Based on the type of UI you create, binding occurs at various times. This is called bind time.

The following table describes the bind time of a control:

**Condition** | **Automatic bind time (assuming binding path was set)**  
---|---  
**An`InspectorElement` constructed in C#** | During the constructor call  
**A child element that is under the return value of`CreateInspectorGUI()` or `CreatePropertyGUI()` when those methods return** | After `CreateInspectorGUI()` or `CreatePropertyGUI()` returns  
**A child element that is under an element when`Bind()` or `BindProperty()` is called on the parent element** | During the `Bind()` or `BindProperty()` call  
**Other** | No automatic binding; you must bind the element or one of its parents manually  
  
The following are best practices when creating a binding regarding bind time:

  * If you create a custom `Editor` or custom `PropertyDrawer`, set the elements’ binding paths instead of calling `Bind()` or `BindProperty()` on any visual elements that are in the visual tree by the end of the body of `CreateInspectorGUI()` or `CreatePropertyGUI()`. These elements are bound automatically after `CreateInspectorGUI()` or `CreatePropertyGUI()` returns. However, if you add any elements to the visual tree after that point, call `Bind()` or `BindProperty()` to bind them.
  * If you create any other type of UI, call `Bind()` or `BindProperty()` regardless of the time at which the elements get added to the visual tree. If you call `Bind()` or `BindProperty()` and bind multiple controls at the same time, set the binding path of each control and then call `Bind()` on the lowest-level parent element that encompasses all the controls. `Bind()` binds the element on which it’s called if it has a binding path and recursively binds all its child elements if they have binding paths. To prevent a negative performance impact, don’t bind a visual element with the `Bind()` method more than once.

## Binding examples

Try the following examples to learn how to code with data binding:

  * Bind with binding path in C# script
  * Bind without the binding path
  * Bind with UXML and C#
  * Create a binding with the Inspector
  * Bind to nested properties
  * Bind to a UXML template
  * Receive callbacks when a bound property changes
  * Receive callbacks when any bound properties change
  * Bind to a list with ListView
  * Bind to a list without ListView
  * Bind a custom control
  * Bind a custom control to custom data type

## Additional resources

  * Binding data type conversion
  * Implementation details
  * Binding examples