---
title: "Bindable data types and fields"
category: "General"
source_file: "UIE-binding-data-type-conversion.html"
doc_type: "manual"
---

# Bindable data types and fields

This following describs the data type conversions and fields supported by `PropertyField`.

## Data type conversions

Most built-in controls in UI Toolkit implement the `INotifyValueChanged` interface for a specific data type. For example, `DoubleField` implements `INotifyValueChanged<Double>`, which means you can bind the `DoubleField` control to a property of type `double`. You can bind more data types with the binding system. For example, you can bind a property of type `int` to a `DoubleField`.

The following table lists the source and target data types that you can bind:

**Source data type** | **Target data type of`INotifyValueChanged`**  
---|---  
`long` | 

  * `long`
  * `int`
  * `string`
  * `float`

  
`int` | 

  * `int`
  * `string`
  * `float`

  
`double` | 

  * `double`
  * `float`

  
`float` | 

  * `float`
  * `double`

  
`char` | 

  * `char`
  * `string`

  
  
**Note** : To prevent data loss, use a `PropertyField` or use the appropriate data types as shown in the Fields supported by PropertyField table below.

## Fields supported by `PropertyField`

When the **Inspector** window is populated, if a custom Editor doesn’t exist for a type, the binding system calls `InspectorElement.FillDefaultInspector()`. This creates a `PropertyField` for each `SerializedProperty` on the `SerializedObject`. 

Each `PropertyField` has a matching control under it, such as an `IntegerField` to represent an `int`, or a `Toggle` to represent a `bool`. If the property has sub-properties, the `PropertyField` has a `Foldout` control. That `Foldout` has the appropriate default controls under each sub-property. If you created a custom `PropertyDrawer` for a Property, the **visual tree** returned from the `PropertyDrawer`’s `CreatePropertyGUI()` method is used instead.

**Note** : 

When you create a custom **UI** , don’t use a `PropertyField` unless you can’t find a specific control for it. For example, to create a control in your visual tree and bind it to a `Color`, use a `ColorField` rather than a `PropertyField`. This makes visual trees more lightweight and operations faster.

The use of `PropertyField` incurs additional overhead because it resolves the concrete field to use after binding. This extra step can affect performance. However, `PropertyField` is beneficial for some uses. For example, it supports custom drawers, which you can use to handle specific properties in a personalized way. This eliminates the need to guess the field type for drawing, which can reduce errors.

The following table lists fields supported by `PropertyField` and their data type:

**Field** | **Data type**  
---|---  
`BoundsField` | Bounds  
`BoundsIntField` | BoundsInt  
`ColorField` | Color  
`CurveField` | AnimationCurve  
`FloatField` | float  
`GradientField` | Gradient  
`Hash128Field` | Hash128  
`IntegerField` | int  
`IntegerField` | int, for the ArraySize  
`LayerMaskField` | unit  
`LongField` | long  
`ObjectField` | UnityEngine.Object  
`PopupField`<string> | Enum  
`RectField` | Rect  
`RectIntField` | RectInt  
`TextField` | string  
`TextField`, with a maxLength=1 | char  
`Toggle` | bool  
`Vector2Field` | Vector2  
`Vector2IntField` | Vector2Int  
`Vector3Field` | Vector3  
`Vector3IntField` | Vector3Int  
`Vector4Field` | Vector4  
  
## Additional resources

  * SerializedObject data binding
  * Bindable elements
  * Implementation details
  * Binding examples