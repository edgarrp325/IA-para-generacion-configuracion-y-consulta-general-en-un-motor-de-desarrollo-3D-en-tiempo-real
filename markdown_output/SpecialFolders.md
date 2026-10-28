---
title: "Special folder names"
category: "General"
source_file: "SpecialFolders.html"
doc_type: "manual"
---

# Special folder names

You can usually choose any name you like for the folders you create to organize your Unity project. However, there are folder names that Unity reserves for special purposes. For example, you must place Editor **scripts** in a folder called **Editor** for them to work correctly.

This page contains the full list of special folder names used by Unity. They are the following:

  * Assets
  * Editor
  * Editor Default Resources
  * Gizmos
  * Resources
  * Standard Assets
  * StreamingAssets
  * Android Asset Packs
  * Android Library Projects

## Assets

The **Assets** folder is the main folder that contains the Assets used by a Unity project. The contents of the **Project window** folder is the main folder that contains the Assets used by a Unity project. The contents of the **Project window** in the Editor correspond directly to the contents of the Assets folder. Most API functions assume that everything is located in the Assets folder and don’t require it to be mentioned explicitly. However, some functions do need to have the Assets folder included as part of a pathname (for example, certain functions in the AssetDatabase class).

## Editor

Editor scripts add functionality to Unity during development but aren’t available in builds at runtime. Scripts in an **Editor** folder run as Editor scripts, not runtime scripts.

You can have multiple Editor folders placed anywhere inside the Assets folder. Place your Editor scripts inside an Editor folder or a subfolder within it.

The exact location of an Editor folder affects the time at which its scripts are compiled relative to other scripts. See documentation on Special Folders and Script Compilation Order for a full description.

Use the EditorGUIUtility.Load function in Editor scripts to load Assets from a Resources folder within an Editor folder. These Assets are only loaded through Editor scripts and are stripped from builds.

**Note:** Unity doesn’t allow components derived from MonoBehaviour to be assigned to **GameObjects** if the scripts are in the Editor folder.

## Editor Default Resources

Editor scripts can make use of Asset files loaded on-demand using the EditorGUIUtility.Load function. This function looks for the Asset files in a folder called **Editor Default Resources**.

You can only have one Editor Default Resources folder and you must place it in Project root, directly within the Assets folder. Place the needed Asset files in this Editor Default Resources folder or a subfolder within it. Always include the subfolder path in the path passed to the EditorGUIUtility.Load function if your Asset files are in subfolders.

## Gizmos

Gizmos allow you to add graphics to the **Scene** View to help visualize design details that are otherwise invisible. The Gizmos.DrawIcon function places an icon in the Scene to act as a marker for a special object or position. You must place the image file used to draw this icon in a folder called **Gizmos** for the DrawIcon function to locate it.

You can only have one Gizmos folder, and it must be placed in the root of the Project, directly within the Assets folder. Place the needed Asset files in this Gizmos folder or a subfolder within it. Always include the subfolder path in the path passed to the Gizmos.DrawIcon function if your Asset files are in subfolders.

## Resources

You can load Assets on-demand from a script instead of creating instances of Assets in a Scene for use in gameplay. You do this by placing the Assets in a folder called **Resources**. Load these Assets by using the Resources.Load function.

You can have multiple Resources folders placed anywhere inside the Assets folder. Place the needed Asset files in a Resources folder or a subfolder within it. Always include the subfolder path in the path passed to the Resources.Load function if your Asset files are in subfolders.

**Note** : If the Resources folder is an Editor subfolder, the Assets in it are loadable from Editor scripts but are removed from builds.

## Standard Assets

When you import a Standard Asset package, Unity puts the assets in a folder called `Standard Assets`. In addition to containing the assets, these folders have an effect on script compilation order. For more information, see the page on Special Folders and Script Compilation Order.

You can only have one `Standard Assets` folder, and you must leave it in the root of the project, directly within the `Assets` folder. Place the asset files you need inside the `<project-root>/Assets/Standard Assets` folder or one of its subfolders.

## StreamingAssets

You may want the Asset to be available as a separate file in its original format (though it’s more common to directly incorporate Assets into a build). For example, you need to access a video file from the filesystem to play the video on IOS using Handheld.PlayFullScreenMovie.

To include streaming Assets, do the following:

  1. Place the file in the StreamingAssets folder.
  2. The file remains unchanged when copied to the target machine, where it’s available from a specific folder.

See the page about Streaming Assets for further details.

You can only have one StreamingAssets folder, and it must be placed in the root of the Project, directly within the Assets folder. Place the Assets files in the StreamingAssets folder or subfolder. Always include the subfolder path in the path used to reference the streaming asset if your Asset files are in subfolders.

## Android Asset Packs

Unity interprets any folder that ends with `.androidpack` as an Android asset packs. For more information, see Create a custom asset pack.

## Android Library Projects

Unity interprets any folder that ends with `.androidlib` as an Android Library Project. For more information, see Import and Android Library Project.

## Hidden Assets

During the import process, Unity ignores the following files and folders in the **Assets** folder (or a sub-folder within it):

  * Hidden folders.
  * Files and folders which start with ‘**.** ’.
  * Files and folders which end with ‘**~** ’.
  * Files and folders named **cvs**.
  * Files with the extension **.tmp**.

This prevents importing special and temporary files created by the operating system or other applications.

## Additional resources

  * Script compilation order