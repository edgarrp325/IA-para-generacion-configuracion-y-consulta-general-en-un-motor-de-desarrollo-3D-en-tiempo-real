---
title: "Load UXML and USS C# scripts"
category: "General"
source_file: "UIE-manage-asset-reference.html"
doc_type: "manual"
---

# Load UXML and USS C# scripts

Unity represents UXML files as `VisualTreeAsset` objects in C# and represents USS files as `StyleSheet` objects in C#. Since `VisualTreeAsset` and `StyleSheet` are regular Unity assets, you can use Unity’s standard workflows to load them.

## Use serialization references

Unity automatically detects fields from your C# **scripts** that are of type `VisualTreeAsset` or `StyleSheet`. You can use the **Inspector** that are of type `VisualTreeAsset` or `StyleSheet`. You can use the **Inspector** to set references to specific UXML or USS files imported into your project. Such references remain valid even when the location of your assets changes in your project.

There are three ways to use this in your scripts:

**Description** | **How to display the Inspector** | **Reference save location**  
---|---|---  
Instances of custom scripts (such as `MonoBehaviour`) | Select the **GameObject** holding the instance of the script | Inside the **scene**  
Default references for a script that derives from `EditorWindow` or `Editor` | Select the actual C# file in the Project Browser | Inside the meta file associated with the script  
Custom assets in your project that derive from `ScriptableObject` | Select the asset in the Project browser | Inside the serialized data of the asset itself  
  
**Note** : The default references work for all scripts that derive from `MonoBehaviour` or `ScriptableObject`. It provides a way to populate default values for serialized fields of scripts.

The following example `MonoBehaviour` class receives a UXML file and a list of USS files from the Inspector:
    
    
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class MyBehaviour : MonoBehaviour
    {
      // Note that public fields are automatically exposed in the Inspector
      public VisualTreeAsset mainUI;
      [Reorderable]
      public StyleSheet[] seasonalThemes;
    }
    

The following example `EditorWindow` class receives default references from the Inspector:
    
    
    using UnityEditor;
    using UnityEngine.UIElements;
    
    public class MyWindow : EditorWindow
    {
      [SerializeField]
      private VisualTreeAsset uxml;
      [SerializeField]
      private StyleSheet uss;
    }
    

## Use the Asset Database (Editor only)

You can load your **UI** Assets by path or GUID with the `AssetDatabase` class. 

The following example shows how to locate an asset by path:
    
    
    VisualTreeAsset uxml = AssetDatabase.LoadAssetAtPath<VisualTreeAsset>("Assets/Editor/main_window.uxml");
    StyleSheet uss = AssetDatabase.LoadAssetAtPath<StyleSheet>("Assets/Editor/main_styles.uss");
    

The following example shows how to locate an asset by path from a package:
    
    
    VisualTreeAsset uxml = AssetDatabase.LoadAssetAtPath<VisualTreeAsset>("Packages/<name-of-the-package>/main_window.uxml");
    StyleSheet uss = AssetDatabase.LoadAssetAtPath<StyleSheet>("Packages/<name-of-the-package>/main_styles.uss");
    

## Use Addressables (Runtime only)

The Addressables system provides tools and scripts to organize and package content for your application and an API to load and release assets at runtime.

You can use UXML and USS assets with the Addressable system.

For information about how to set up Addressables for any assets in Unity, see Getting started with Addressables.

## Use a Resources folder

If you add a `Resources` folder in your project and place your UI assets in it, you can use the `Resources.Load` method to load your assets. 

The following example shows how to load an asset in the `Resources` folder:
    
    
    VisualTreeAsset uxml = Resources.Load<VisualTreeAsset>("main_window");
    StyleSheet uss = Resources.Load<StyleSheet>("main_styles");
    

**Note** : This method increases the final build size significantly. If you are concerned with the build size, use `Addressables` instead. 

## Additional resources

  * The Resources folder
  * Assets, Resources and AssetBundles