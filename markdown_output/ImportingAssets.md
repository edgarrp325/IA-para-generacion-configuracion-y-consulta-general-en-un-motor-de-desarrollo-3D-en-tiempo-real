---
title: "Importing assets"
category: "General"
source_file: "ImportingAssets.html"
doc_type: "manual"
---

# Importing assets

You can bring assets created outside of Unity into your Unity project. To do this, you can either export the file directly into the `Assets` folder for your project, or copy it into that folder. For many common formats, you can save your source file directly into your project’s `Assets` folder and Unity can read it. Unity also detects when you save new changes to the file and re-imports files as necessary.

When you create a Unity project, Unity creates a folder (named after your project) which contains the following subfolders:

  * `Temp`
  * `Library`
  * `Assets`
  * `ProjectSettings`
  * `Logs`
  * `Packages`

You can save or copy files that you want to use in your project into the `Assets` folder, and you can use the **Project window** inside Unity to view the contents of your `Assets` folder. Therefore, if you save or copy a file to your `Assets` folder, Unity imports it and it then appears in your Project window.

When you modify a file in Unity, Unity does not modify your original source file, even though you can often choose between various ways to compress, modify, or otherwise process the asset within Unity. Instead, the import process reads your source file, and creates a game-ready representation of your asset internally, matching your chosen import settings. If you modify the import settings for an asset, or make a change to the source file in the `Assets` folder, Unity re-imports the asset again to reflect your changes. 

**Warning:** In most cases, the items that appear in your Project window represent actual files on your computer. If you delete them within the Unity Editor Project window, you also delete them from your computer.

Unity automatically detects files as they are added to the `Assets` folder, or if they are modified. When you put any asset into your `Assets` folder, it appears in your Project window.

The Project window shows Assets that Unity has imported into your project

If you drag a file from your computer’s file browser into Unity’s Project window, Unity makes a copy and places it into your `Assets` folder. You can then access this copy from the Project window.

To bring collections of assets into your project from another Unity project, you can use Asset packages.

## Asset Import Settings

The simplest way to safely move or rename your assets is to always do it from within Unity’s project folder. This way, Unity automatically moves or renames the corresponding meta file. To read more about .meta files and the import process, see How Unity imports assets.

Each type of asset that Unity supports has a set of Import Settings, which affect how the asset appears or behaves. To view an asset’s import settings, select the asset in the Project View. The import settings for this asset will appear in the **Inspector**. The options that appear vary depending on the type of asset selected.

For example, an image’s import settings allow you to choose whether Unity imports it as a Texture, a 2D **sprite** , or a **normal map**. The import settings for an FBX file allow you to adjust the scale, generate normals or **lightmap** , or a **normal map**. The import settings for an FBX file allow you to adjust the scale, generate normals or **lightmap** coordinates, and split & trim **animation clips** coordinates, and split & trim **animation clips** defined in the file.

Clicking on an image asset in the Project window shows the import settings for that asset in the Inspector

For other asset types, the import settings look different. The various settings you see relate to the type of asset selected. Here’s an example of an Audio asset, with its related import settings shown in the inspector:

An Audio asset selected in the Project window shows the Audio import settings for that asset in the Inspector

If you are developing a cross-platform project, you can override the “default” settings and assign different import settings on a per-platform basis.

## Asset processing

Unity reads and processes any files that you add to the `Assets` folder, and converts the contents of the file to internal game-ready data. The asset files themselves remain unchanged, and the internal data is stored in the project’s `Library` folder. This data is part of the Unity Editor’s Asset Database.

Using internal formats for assets allows Unity to have internal versions of your assets ready to use at runtime in the Editor, and to keep your unmodified source files in the `Assets` folder. A distinction between the asset files and the internal versions means that you can quickly edit the asset file, and have the Editor pick up the changes automatically. For example, you can save `.psd` files directly into your `Assets` folder, but hardware such as mobile devices and PC graphics cards can’t process that format directly in order to render them as textures. Instead, Unity can convert an internal version into a format that those platforms can process.

Unity stores the internal representation of your assets in the `Library` folder, which behaves like a cache folder. As a user, you should never need to alter the `Library` folder manually; if you do, you might negatively affect your project in the Unity Editor. This also means that you should not include the `Library` folder under **version control**.

**Note:** If your project is not open in Unity, you can safely delete the `Library` folder, because Unity can regenerate all of its data from the `Assets` and `ProjectSettings` folders the next time you launch your project.

## Complex assets

In some cases, Unity might create multiple assets while importing a single asset file. For example:

  * When a 3D file (such as an FBX file) defines Materials or contains embedded Textures. To handle this, Unity extracts the Materials and embedded Textures as separate assets.
  * When you want to import an image file as multiple 2D sprites. You should use the 2D Sprite Editor to define multiple sprites from a single graphic image. Unity displays each sprite defined in the Editor as a separate Sprite asset in the Project window.
  * When a 3D file contains multiple animation timelines or multiple clips. To handle this, Unity automatically defines separate animation timelines or clips based on its animation import settings. The resulting multiple animation clips appear as separate Animation Clip assets in the Project window.

## See also

  * Asset packages
  * Materials and Shaders
  * Textures and Videos
  * Sprite Editor
  * Sprite Packer
  * Audio Files
  * Tracker Modules