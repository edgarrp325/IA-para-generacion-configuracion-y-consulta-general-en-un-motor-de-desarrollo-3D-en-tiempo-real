---
title: "Customizing the Asset Database workflow"
category: "General"
source_file: "AssetDatabaseCustomizingWorkflow.html"
doc_type: "manual"
---

# Customizing the Asset Database workflow

Use the AssetDatabase class to customize your asset pipeline and create tools to access, load, create and manipulate assets with your own **scripts**

## Customize your asset workflow

The AssetDatabase class has a large number of methods that allow you to access and perform operations on assets in exactly the same way that the Unity Editor itself does. You can create, import, delete, copy, move, load, and save assets, and search the asset database.

This means you can create anything from simple adjustments to powerful tools and customizations to your project’s asset workflow, using Unity’s Editor scripting and Editor window customization.

For a simple example, see the documentation for the AssetDatabase.ForceReserializeAssets method. It shows how you can add a menu item to the Editor that gives you more control over how certain asset bundles should be upgraded when you upgrade your project to a newer version of Unity.

For the full list of methods available, and documentation for each of the methods, see the AssetDatabase scripting API page.

## Asset objects

From a scripting point of view, what Unity considers an “asset” is slightly different than what you see displayed in the **Project window**. The files that you place in your project’s **Assets** folder are the source files for your assets, but they differ conceptually to the asset objects that the Unity Editor works with. When Unity imports asset files, it processes them and generates an imported result: serialized C# objects that derive from UnityEngine.Object. From a scripting point-of-view, the assets that you have access to when scripting in the Unity Editor are these imported results.

For example, an asset that might start off as a binary file, such as a JPEG or PNG image file, is converted to a C# object whose type is a specialization of UnityEngine.Object. In the case of JPEG or PNG files, they are converted to serialized instances of the Texture class, which in turn inherits from UnityEngine.Object. The serialized object data is then stored as an artifact in the Library folder. So, when you access a Texture asset with a script, you are not accessing the original JPEG or PNG file, you are accessing the serialized version of the C# Texture object that was generated when the original image file was imported. The **.meta** file which Unity creates during the import process, stored next to the original asset file, contains the asset’s import settings, and contains a GUID which allows Unity to connect the original asset file with the artifact in the asset database.

When you import an asset, Unity creates a .meta file in the Assets folder, and an artifact file in the Library folder

## Inside asset files and artifact files

Some types of asset files that Unity itself creates, such as **.**prefab**** , **.**scene**** , **.**scene**** , **.asset** , and **.mat** , already contain serialized data in their source file, so the artifact file that Unity produces and caches is very similar to the source file. The source files for these, for example a **.mat** material file in your project’s **Assets** folder, are human-readable (provided **Asset Serialization Mode** is set to **Force Text** , which is the default setting). This is in contrast to binary asset files imported from external sources such as textures or audio, where the files are not normally human-readable.

Asset files can contain multiple serialized objects, and each of these can be considered an “asset” for the purposes of scripting with the AssetDatabase methods. For example, a **.prefab** asset file could contain a serialized **GameObject** with multiple components attached. Each of those components are also serialized as objects in the asset file, and so when accessing the contents of the prefab asset using AssetDatabase methods, the component objects within the asset file are considered **sub assets** , (explained in more detail below).

The serialized objects generated during the import process are called **artifacts** , and Unity stores them in the Asset Database’s cache of import artifacts, in the **Library** folder of your project. They are treated as cached data because Unity can always regenerate them from the source assets, using the importer settings and **project settings** saved in your project.

You can inspect the artifacts produced for the assets in your project by using the Import Activity window, which reveals the specific cached artifact files that Unity generates, along with other useful information such as when the import happened, and how long it took.

Each artifact file name is a unique hash (a GUID) with no file extension. Unity separates these files into subfolders, each subfolder with a name matching the first two characters of the artifact filename. 

These artifact files contain binary data, and are not designed to be human-readable. While it’s useful to understand that these files contain the data used by the asset database, you do not need to view, edit, or use these files directly while working with Unity. Instead, the AssetDatabase class provides the methods necessary to work with assets within the Editor.

## Main assets and sub-assets

Because Unity can store multiple serialized objects within the same asset file, Unity has a concept of the **main asset** within any asset file. When Unity creates asset files that contain a single asset, such as a material, the main asset is always that single asset. For other types containing more than one serialized asset object, the main asset is always the first asset added to the file, unless otherwise specified with the SetMainObject method.

You can sometimes see sub-assets in the Project window of the Editor, if those sub-assets are of certain types. For example, looking at this FBX asset file containing a “Space Frigate” model in the Project window, its view has been expanded to reveal that it has a material and a **mesh** as sub-assets.

An FBX asset file in the Project window, showing two sub-assets, a material and mesh

Assets can also have sub-asset types that do not show in the Project window like this. For example, the “Space Frigate” asset file above actually contains more than the two sub-assets displayed in the Project window. You can see the real number of assets when you access the asset file using AssetDatabase methods, as demonstrated in the script below:
    
    
    using UnityEngine;
    using UnityEditor;
    
    public class Example : MonoBehaviour
    {
        [MenuItem("AssetDatabase/InspectAssets")]
    
        private static void InspectAssets()
        {
            Object[] data = AssetDatabase.LoadAllAssetsAtPath("Assets/Space Frigate.fbx");
    
            Debug.Log(data.Length + " Assets");
            foreach (Object o in data)
            {
                Debug.Log(o);
            }
        }
    }
    

In this case, the output would show that the imported, serialized version of this file contains six assets:
    
    
    6 Assets
    Space Frigate (UnityEngine.GameObject)
    space_frigate_0 (UnityEngine.Material)
    space_frigate_0 (UnityEngine.Mesh)
    Space Frigate (UnityEngine.Transform)
    Space Frigate (UnityEngine.MeshRenderer)
    Space Frigate (UnityEngine.MeshFilter)
    

This is because the GameObject, material, the mesh data itself, and each of the components that Unity automatically added to the GameObject during the import process (the Transform, the MeshFilter, and the MeshRenderer), each count as a separate serialized object. Therefore they are sub-assets of the asset file, and as far as the Asset Database API is concerned, are each a separate asset.

## Asset Import Order

If you are scripting using the AssetDatabase class, it’s important to understand how the order of Unity’s import processes can affect your scripts, otherwise you may get unexpected results. The order is as follows:

  1. Import Script Assets (.cs, .dll, .asmdef files)
  2. Compilation
  3. Domain reload
  4. InitializeOnLoad callback
  5. Import all other assets

Scripts are always imported and compiled before all other regular assets, because the Editor needs to know whether there are custom asset post-processors or scripted importers in the project. This ensures that the Editor uses any new or changed importers or post-processors when importing the rest of the non-script assets.

The **InitializeOnLoad** callback is often used to run some code on project startup or when scripts change. As shown in the list above, this callback is run after Unity reloads the domain, but before it starts importing assets. This means if you’re using the **[InitializeOnLoad]** callback to access assets, your code is executed _before_ the current asset import cycle completes. In particular:

  * For assets being imported for the first time, methods like **AssetDatabase.LoadAssetAtPath, AssetDatabase.FindAssets,**Shader**.Find, Resources.Load** will return null, since those assets have not yet been imported.

  * For assets that have already been imported at least once, methods like **AssetDatabase.LoadAssetAtPath, AssetDatabase.FindAssets, Shader.Find, Resources.Load** will return the previous (outdated) version of the asset if it was modified before reloading the domain, since domain reload occurs before the regular asset import phase.

When you are writing scripted importers, asset pre-processors, and asset post-processors, you should not make your code assume that other specific assets are already imported according to any particular order. When importing, Unity groups assets into queues by type, and while the types are imported in a predefined order, assets within a queue of the same type are imported in an arbitrary order unless you use ScriptedImporter.GatherDependenciesFromSourceFile. Using `GatherDependenciesFromSourceFile` also creates a dependency between the assets, so if one asset is modified, the other that depends on it is reimported.