---
title: "Script serialization"
category: "General"
source_file: "script-Serialization.html"
doc_type: "manual"
---

# Script serialization

**Serialization** is the automatic process of transforming data structures or GameObject states into a format that Unity can store and reconstruct later.

How you organize data in your Unity project affects how Unity serializes that data, which can have a significant impact on the performance of your project. This page outlines serialization in Unity and how to optimize your project for it.

This document covers the following topics:

  * Serialization Rules
  * Custom Serialization
  * How Unity uses serialization
  * Serialization errors
  * Serialization best practice

##  Serialization rules

Serializers in Unity are specifically designed to operate efficiently at runtime. Because of this, serialization in Unity behaves differently to serialization in other programming environments. Serializers in Unity work directly on the **fields** of your C# classes rather than their properties, so there are rules that your fields must conform to to be serialized. The following section outlines how to use field serialization in Unity.

To use field serialization you must ensure that the field:

  * Is public, or has a SerializeField attribute
  * isn’t static
  * isn’t const
  * isn’t readonly
  * Has a field type that can be serialized: 
    * Primitive data types (int, float, double, bool, string, etc.)
    * Enum types (32 bits or smaller)
    * Fixed-size buffers
    * Unity built-in types, for example, Vector2, Vector3, Rect, Matrix4x4, Color, AnimationCurve
    * Custom structs with the Serializable attribute
    * References to objects that derive from UnityEngine.Object
    * Custom classes with the Serializable attribute. (See Serialization of custom classes).
    * An array of a field type mentioned above
    * A `List<T>` of a field type mentioned above

**Note** : Unity doesn’t support serialization of multilevel types (multidimensional arrays, jagged arrays, dictionaries, and nested container types). If you want to serialize these, you have two options:

  * Wrap the nested type in a class or struct
  * Use serialization callbacks, by implementing ISerializationCallbackReceiver, to perform custom serialization.

###  Serialization of custom classes

For Unity to serialize a custom class, you must ensure the class:

  * Has the Serializable attribute
  * isn’t static.

When you assign an instance of a `UnityEngine.Object`-derived class to a field and Unity saves that field, Unity serializes the field as a reference to that instance. Unity serializes the instance itself independently, so it isn’t duplicated when multiple fields are assigned to the instance. But for custom classes which don’t derive from `UnityEngine.Object`, Unity includes the state of the instance directly in the serialized data of the MonoBehaviour or ScriptableObject that references them. There are two ways that this can happen: **inline** and by **`[SerializeReference]`**.

  * **Inline serialization** : By default, Unity serializes custom classes inline by value when you don’t specify `[SerializeReference]` on the field that references the class. This means that if you store a reference to an instance of a custom class in several different fields, they become separate objects when serialized. Then, when Unity deserializes the fields, they contain different distinct objects with identical data.
  * **`[SerializeReference]` serialization**: If you do specify `[SerializeReference]`, Unity establishes the object as a managed reference. The host object still stores the objects directly in its serialized data, but in a dedicated registry section.

`[SerializeReference]` adds some overhead but supports the following cases:

  * Fields can be null. Inline serialization can’t represent null, instead, it replaces null with an inline object that has unassigned fields.
  * Multiple references to the same object. If you store a reference to an instance of a custom class in several different fields without using `[SerializeReference]`, then they become separate objects when serialized.
  * Graphs and cyclical data (for example, an object that has a reference back to itself). Inline class serialization doesn’t support null or shared references, so any cycle in data can lead to unexpected results, such as strange **Inspector** behavior, console errors or infinite loops.
  * Polymorphism. If you create a class that derives from a parent class and assign it to a field that uses the parent class as its type, without `[SerializeReference]` Unity only serializes the fields that belong to the parent class. When Unity deserializes the class instance, it instantiates the parent class instead of the derived class.
  * When a data structure requires a stable identifier to point to a specific object without hardcoding the object’s array position or searching the entire array. See Serialization.ManagedReferenceUtility.SetManagedReferenceIdForObject.

**Note** : Inline serialization is more efficient, and you should use it unless you specifically need one of the features that `[SerializeReference]` supports. For full details on how to use `[SerializeReference]`, see the SerializeReference documentation.

### Serialization of properties

Unity doesn’t normally serialize properties except in the following situations:

  * If a property has an explicit backing field, Unity serializes it according to regular serialization rules. For example:

    
    
    public int MyInt
    {
    get => m_backing;
    private set => m_backing = value;
    }
    [SerializeField] private int m_backing;
    

  * Unity serializes properties with autogenerated fields during hot reloading only.   
  
`public int MyInt { get; set; }`   
  
If you don’t want Unity to serialize a property with autogenerated fields, use the [field: NonSerialized] attribute.

##  Custom serialization

Sometimes you might want to serialize something that Unity’s serializer doesn’t support (for example, a C# Dictionary). The best approach is to implement the ISerializationCallbackReceiver interface in your class. This allows you to implement callbacks that are invoked at key points during serialization and deserialization:

  1. When an object is about to be serialized, Unity invokes the `OnBeforeSerialize()` callback. Inside this callback is where you can transform your data into something Unity understands. For example, to serialize a C# Dictionary, copy the data from the Dictionary into an array of keys and an array of values.
  2. After the `OnBeforeSerialize()` callback is complete, Unity serializes the arrays.
  3. Later, when the object is deserialized, Unity invokes the `OnAfterDeserialize()` callback. Inside this callback is where you can transform the data back into a form that’s convenient for the object in memory. For example, use the key and value arrays to repopulate the C# Dictionary.

##  How Unity uses serialization

### Saving and loading

Unity uses serialization to load and save scenes, Assets, Assets, and AssetBundles to and from your device’s memory. This includes data saved in your own scripting API objects such as MonoBehaviour components and ScriptableObjects.

Many of the features in the Unity Editor are built on top of the core serialization system. Two things to be particularly aware of with serialization are the Inspector window, and hot reloading.

#### The Inspector window

The Inspector window shows the value of the serialized fields of the inspected objects. When you change a value in the Inspector, the Inspector updates the serialized data and triggers a deserialization that updates the inspected object.

The same applies for both built-in Unity objects, and scripting objects such as MonoBehaviour-derived classes.

Unity doesn’t call any C# property getters and setters when you view or change values in the Inspector window; instead, Unity accesses the serialized backing field directly.

#### Hot reloading

Hot reloading is where you create or edit **scripts** while the Editor is open and apply the script behaviors immediately. You don’t have to restart the Editor for changes to take effect.

When you change and save a script, Unity hot reloads all the script data that’s loaded at the time. Unity stores all serializable variables in all loaded scripts, then reloads those scripts and restores the serialized variables. Hot reloading discards all data that isn’t serializable, so you won’t be able to access the data afterward.

This affects all Editor windows and all MonoBehaviours in the project. Unlike other cases of serialization, Unity serializes private fields by default when reloading, even if they don’t have the ‘SerializeField’ attribute.

When Unity reloads scripts:

  1. Unity serializes and stores all variables in all loaded scripts.
  2. Unity restores them to their original, pre-serialization values: 
     * Unity restores all variables - including private variables - that fulfill the requirements for serialization, even if a variable has no `[SerializeField]` attribute. Sometimes, you need to prevent Unity from restoring private variables, for example, if you want a reference to be null after reloading from scripts. In this case, use the `[field: NonSerialized]` attribute.
     * Unity never restores static variables, so don’t use static variables for states that you need to keep after Unity reloads a script because the reloading process will discard them.

### Prefabs

A Prefab is the serialized data of one or more GameObjects is the serialized data of one or more GameObjects or components or components. A Prefab instance contains a reference to both the Prefab source and a list of modifications to it. The modifications are what Unity needs to do to the Prefab source to create that particular Prefab instance.

The Prefab instance only exists while you edit your project in the Unity Editor. The Unity Editor instantiates a GameObject from its two sets of serialization data: the Prefab source and the Prefab instance’s modifications.

### Instantiation

When you call `Instantiate` on anything that exists in a scene, such as a Prefab or a GameObject:

  1. Unity serializes it. This happens both at runtime and in the Editor. Unity can serialize everything that derives from `UnityEngine.Object`.
  2. Unity creates a new GameObject and deserializes the data onto the new GameObject.
  3. Unity runs the same serialization code in a different variant to report which other `UnityEngine.Objects` it references. It checks all referenced `UnityEngine.Objects` to see if they’re part of the data Unity instantiates. If the reference points to something external, such as a Texture, Unity keeps that reference as it is. If the reference points to something internal, such as a child GameObject, Unity patches the reference to the corresponding copy.

### Unloading unused assets

`EditorUtility.UnloadUnusedAssetsImmediate` is the native Unity garbage collector and has a different purpose to the standard C# garbage collector. It runs after you load a scene and checks for objects (like Textures) that it no longer references and unloads them safely. The native Unity garbage collector runs the serializer in a variation in which objects report all references to external `UnityEngine.Objects`. This is how Textures that one scene uses, the garbage collector unloads in the next.

### Differences between Editor and runtime serialization

Most serialization happens in the Editor, whereas deserialization is the focus at runtime. Unity serializes some features only in the Editor, while it can serialize other features in both the Editor and at runtime:

**Feature** | **Editor** | **Runtime**  
---|---|---  
**Assets in Binary Format** | Read/write supported | Read supported  
**Assets in YAML format** | Read/write supported | Not supported  
**Saving scenes, prefabs and other assets** | Supported, unless in Play mode | Not supported  
**Serialization of individual objects withJsonUtility** | Read/write support with JsonUtility.  
  
Support for additional types of objects with EditorJsonUtility | Read/write support with JsonUtility  
**SerializeReference** | Supported | Supported  
**ISerializationCallbackReceiver** | Supported | Supported  
**FormerlySerializedAs** | Supported | Not supported  
  
Objects can have additional fields that only the Editor serializes, such as when you declare fields within the UNITY_EDITOR scripting symbol:
    
    
    public class SerializeRules : MonoBehaviour
    {
    #if UNITY_EDITOR
    public int m_intEditorOnly;
    #endif
    }
    

In the above example, the `m_intEditorOnly` field is only serialized in the editor and isn’t included in the build. This allows you to save memory by omitting data that’s only required in the Editor from your build. Any code that uses that field would also need to be conditionally compiled, for example within #if UNITY_EDITOR blocks, so that the class can compile at build time.

The Editor doesn’t support objects with fields that Unity only serializes at runtime, (for example, when you declare fields within the UNITY_STANDALONE directive).

##  Script serialization errors

Script serialization can cause errors. Fixes to some of these are listed below.

### “Find isn’t allowed to be called from a MonoBehaviour constructor (or instance field initializer), call in Awake or Start instead.”

Calling Scripting API such as `GameObject.Find` inside a MonoBehaviour constructor or field initializer triggers this error.

To fix this, make the call to the Scripting API in `MonoBehaviour.Start` instead of in the constructor.

### “Find isn’t allowed to be called during serialization, call it from Awake or Start instead.”

Calling Scripting API such as GameObject.Find from within the constructor of a class marked with `System.Serializable` triggers this error.

To fix this, edit your code so that it makes no Scripting API calls in any constructors for any serialized objects.

### Thread-safe Unity Scripting API

The restrictions above affect the majority of the Scripting API. Only some parts of the Unity scripting API are exempt and you can call them from anywhere:

  * `Debug.Log`
  * `Mathf` functions
  * Simple self-contained structs; for example math structs like `Vector3` and `Quaternion`

To reduce the risk of errors during serialization, only call API methods that are self-contained and don’t need to get or set data in Unity itself, unless there is no alternative.

##  Serialization best practice

You can organize your data to ensure you get optimal use of Unity’s serialization.

  * Aim to have Unity serialize the smallest possible set of data. The purpose of this isn’t to save space on your computer’s hard drive, but to make sure that you can maintain backwards compatibility with previous versions of the project. Backwards compatibility can become more difficult later on in development if you work with large sets of serialized data.
  * Never have Unity serialize duplicate data or cached data. This causes significant problems for backwards compatibility: it carries a high risk of error because data can get out of sync.
  * Avoid nested, recursive structures where you reference other classes. The layout of a serialized structure always needs to be the same; independent of the data and only dependent on what’s exposed in the script. The only way to reference other classes is through classes derived from `UnityEngine.Object`. These classes are separate; they only reference each other and they don’t embed the contents.

Serialization