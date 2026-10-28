---
title: "Accessing package assets"
category: "General"
source_file: "upm-assets.html"
doc_type: "manual"
---

# Accessing package assets

This section explains how to access or refer to assets that are defined inside a package:

  * Referring to package paths
  * Loading a Texture inside a package
  * Resolving absolute paths

**Note** : Package Manager doesn’t support streaming assets in packages. Use the Addressables package instead.

## Referring to package paths

To refer to assets that are defined inside a package, use this path scheme:
    
    
    "Packages/<package-name>/..."
    

The path of the asset inside a package begins with `Packages/` and the package name (not the display name).

By contrast, you access project assets using this scheme:
    
    
    "Assets/..."
    

For example, the path for the file `image.png` in the package subfolder `/Example/Images` of the **com.unity.images-library** package is:
    
    
    "Packages/com.unity.images-library/Example/Images/image.png"
    

To get the absolute path of an item in your `Packages` folder, you can use the partial path as a parameter to the Path.GetFullPath() method. For an example, refer to Resolving absolute paths.

## Loading a Texture inside a package

To load a Texture stored inside a package, use the LoadAssetAtPath method, which requires the `using UnityEditor` directive. Specify the path following the `Packages/<package-name>/` path scheme as demonstrated in this example:
    
    
    using UnityEditor;
    // ...
    Texture2D texture = (Texture2D)AssetDatabase.LoadAssetAtPath("Packages/com.unity.images-library/Example/Images/image.png", typeof(Texture2D));
    

## Resolving absolute paths

To get the absolute path of a packaged asset, use the Path.GetFullPath() method, which requires the `using System.IO` directive. For example:
    
    
    using System.IO;
    // ...
    string absolute =   Path.GetFullPath("Packages/com.unity.images-library/Example/Images/image.png");
    

## Additional resources

  * PackageInfo.name (Scripting API)
  * Search for files