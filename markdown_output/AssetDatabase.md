---
title: "The Asset Database"
category: "General"
source_file: "AssetDatabase.html"
doc_type: "manual"
---

# The Asset Database

With most types of asset, Unity needs to convert the data from the asset’s source file into a format that it can use in a game or real-time application. It stores these converted files, and the data associated with them, in the **Asset Database**.

The conversion process is required because most file formats are optimized to save storage space, whereas in a game or a real-time application, the asset data needs to be in a format that is ready for hardware, such as the CPU, graphics, or audio hardware, to use immediately. For example, when Unity imports a .png image file as a texture, it does not use the original .png-formatted data at runtime. Instead, when you import the texture, Unity creates a new representation of the image in a different format which is stored in the Project’s _Library_ folder. The Texture class in the Unity engine uses this imported version, and Unity uploads it to the GPU for real-time display.

If you subsequently modify an asset’s source file that you have already imported (or if you change any of its dependencies) Unity reimports the file and updates the imported version of the data. See Refreshing the Asset Database for more information on this process.

The Asset Database also provides an AssetDatabase API that you can use to access Assets, and control or customize the import process.

## Asset import dependencies

The Asset Database keeps track of all the dependencies for each asset, and keeps a cache of the imported versions of all the Assets.

An Asset’s import dependencies consists of all of the data that might influence the imported data. For example, the source file of an Asset is a dependency, as well as the Asset’s import settings (such as a texture’s compression type), or the target platform of your Project (for instance, PS4 hardware requires data in a different format to Android hardware). If you modify any of these dependencies, the cached version of the imported Asset becomes invalid and Unity must re-import it to reflect the changes.

## Asset caching

The Asset Cache is where Unity stores the imported versions of assets. Because Unity can always recreate these imported versions from the source asset file and its dependencies, these imported versions are treated as a cache of pre-calculated data, which saves time when you use Unity. For this reason, you should exclude the files in the Asset Cache from **version control** systems.

Unity uses a local cache by default, which means that the imported versions of Assets are cached in the _Library_ folder in your Project’s folder on your local machine. You should use an **ignore file** to exclude this folder from version control.

However, if you work as part of a team and use a version control system, it might be beneficial to also use Unity Accelerator, which shares the Asset Cache across your LAN.

Because cached Assets are not suitable for storing in a version control system, when your team works together on a Project and uses local caching, every team member’s copy of Unity performs the import process if an Asset or dependency changes, which can be time consuming.

Unity provides a solution to this called Unity Accelerator. One of the Accelerator’s features is a software agent which stores and serves the cached versions of Assets to everyone who is working on the same Project together on the same local network. This means that only one team member needs to import any given asset. The imported version of the Asset is then stored in the Accelerator and the other team members can download the cached version instead of waiting for the import process locally.

## Source Assets and Artifacts

Unity maintains two database files in the Library folder, which together are called the Asset Database. These two databases keep track of information about your source asset files, and Artifacts, which is information about the import results.

### The source Asset Database

The source Asset Database contains meta-information about your source asset files which Unity uses to determine whether the file has been modified, and therefore whether it should reimport the files. This includes information such as last modified date, a hash of the file’s contents, GUIDs and other meta-information.

### The Artifact database

Artifacts are the results of the import process. The Artifact database contains information about the import results of each source asset. Each Artifact contains the import dependency information, Artifact meta-information and a list of Artifact files.

**Note:** The database files are located in your Project’s _Library_ folder, and as such you should exclude them from version control systems. You can find them in the following locations:

  * Source Asset Database: `Library\SourceAssetDB`
  * Artifact Database: `Library\ArtifactDB`

## Importing an Asset

Unity normally imports assets automatically when they are dragged into the project but it is also possible to import them under script control. To do this you can use the AssetDatabase.ImportAsset method as in the example below.
    
    
    using UnityEngine;
    using UnityEditor;
    
    public class ImportAsset {
        [MenuItem ("AssetDatabase/ImportExample")]
        static void ImportExample ()
        {
            AssetDatabase.ImportAsset("Assets/Textures/texture.jpg", ImportAssetOptions.Default);
        }
    }
    
    

You can also pass an extra parameter of type AssetDatabase.ImportAssetOptions to the AssetDatabase.ImportAsset call. The scripting reference page documents the different options and their effects on the function’s behaviour.

## Loading an Asset

The editor loads assets only as needed, say if they are added to the **scene** or edited from the **Inspector** or edited from the **Inspector** panel. However, you can load and access assets from a script using AssetDatabase.LoadAssetAtPath, AssetDatabase.LoadMainAssetAtPath, AssetDatabase.LoadAllAssetRepresentationsAtPath and AssetDatabase.LoadAllAssetsAtPath. See the scripting documentation for further details.
    
    
    using UnityEngine;
    using UnityEditor;
    
    public class ImportAsset {
        [MenuItem ("AssetDatabase/LoadAssetExample")]
        static void ImportExample ()
        {
            Texture2D t = AssetDatabase.LoadAssetAtPath("Assets/Textures/texture.jpg", typeof(Texture2D)) as Texture2D;
        }
    }
    
    

## File Operations using the AssetDatabase

Since Unity keeps metadata about asset files, you should never create, move or delete them using the filesystem. Instead, you can use AssetDatabase.Contains, AssetDatabase.CreateAsset, AssetDatabase.CreateFolder, AssetDatabase.RenameAsset, AssetDatabase.CopyAsset, AssetDatabase.MoveAsset, AssetDatabase.MoveAssetToTrash and AssetDatabase.DeleteAsset.
    
    
    public class AssetDatabaseIOExample {
        [MenuItem ("AssetDatabase/FileOperationsExample")]
        static void Example ()
        {
            string ret;
            
            // Create
            Material material = new Material (Shader.Find("Specular"));
            AssetDatabase.CreateAsset(material, "Assets/MyMaterial.mat");
            if(AssetDatabase.Contains(material))
                Debug.Log("Material asset created");
            
            // Rename
            ret = AssetDatabase.RenameAsset("Assets/MyMaterial.mat", "MyMaterialNew");
            if(ret == "")
                Debug.Log("Material asset renamed to MyMaterialNew");
            else
                Debug.Log(ret);
            
            // Create a Folder
            ret = AssetDatabase.CreateFolder("Assets", "NewFolder");
            if(AssetDatabase.GUIDToAssetPath(ret) != "")
                Debug.Log("Folder asset created");
            else
                Debug.Log("Couldn't find the GUID for the path");
            
            // Move
            ret = AssetDatabase.MoveAsset(AssetDatabase.GetAssetPath(material), "Assets/NewFolder/MyMaterialNew.mat");
            if(ret == "")
                Debug.Log("Material asset moved to NewFolder/MyMaterialNew.mat");
            else
                Debug.Log(ret);
            
            // Copy
            if(AssetDatabase.CopyAsset(AssetDatabase.GetAssetPath(material), "Assets/MyMaterialNew.mat"))
                Debug.Log("Material asset copied as Assets/MyMaterialNew.mat");
            else
                Debug.Log("Couldn't copy the material");
            // Manually refresh the Database to inform of a change
            AssetDatabase.Refresh();
            Material MaterialCopy = AssetDatabase.LoadAssetAtPath("Assets/MyMaterialNew.mat", typeof(Material)) as Material;
            
            // Move to Trash
            if(AssetDatabase.MoveAssetToTrash(AssetDatabase.GetAssetPath(MaterialCopy)))
                Debug.Log("MaterialCopy asset moved to trash");
            
            // Delete
            if(AssetDatabase.DeleteAsset(AssetDatabase.GetAssetPath(material)))
                Debug.Log("Material asset deleted");
            if(AssetDatabase.DeleteAsset("Assets/NewFolder"))
                Debug.Log("NewFolder deleted");
            
            // Refresh the AssetDatabase after all the changes
            AssetDatabase.Refresh();
        }
    }
    
    

## Platform Switching and reimporting

Switching between platforms might cause Unity to reimport your assets. This usually happens when the way the asset is imported differs between platforms, which is often the case. For example, different platforms have different **texture formats** , so textures are imported differently for each platform.

When using Asset Database V2, the platform is part of the hash that the Asset Database uses to store the import results for Unity’s built-in importers. This means that the results for importing your assets on different platforms are stored as separate pieces of cached data.

The result of this feature is that the first time you switch platform with new assets in your project that haven’t already been imported for that platform, they are reimported. This means that you have to wait for that process to complete. However the new reimported data does not overwrite the old data cached import for the previous platform. 

This means whenever you subsequently switch back to a platform where you have already imported assets for that platform, those asset import results are already cached and ready to use, making the switch much faster.

## Asset Database version

This documentation refers to the **version 2** of the Asset Database, which is the default in new Projects created with Unity 2019.3 or newer. The legacy version (version 1) was the default in earlier versions of Unity, which behaves in a different way. The legacy version cannot be used in Unity 2020+.