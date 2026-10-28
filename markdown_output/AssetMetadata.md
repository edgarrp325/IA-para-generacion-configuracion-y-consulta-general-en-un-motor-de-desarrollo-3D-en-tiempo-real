---
title: "Asset Metadata"
category: "General"
source_file: "AssetMetadata.html"
doc_type: "manual"
---

# Asset Metadata

When Unity imports assets, it also stores and manages additional data about the asset, such as what import settings Unity should use to import the asset, and where the asset is used throughout your project. Below is a description of how this process works:

  1. Unity assigns the asset a unique ID.
  2. Unity creates a `.meta` file to accompany the asset file.
  3. Unity processes the asset.

The Import settings for any given asset affects how Unity processes the asset. If you modify the asset file, or any of the asset’s import settings, Unity reimports the asset. For more information, see Assets and their import settings.

## Unique IDs

The Unity Editor frequently checks the contents of the `Assets` folder against the list of assets it already knows about. When you place an asset in the `Assets` folder, Unity detects that you have added a new file.

When Unity finds the new file, it assigns a unique ID to the asset. This is an ID that Unity uses internally to reference the asset, so that Unity can move or rename the asset without breaking anything.

The IDs are not normally visible in the Editor, 

## Meta files

The image below shows `.meta` files that Unity creates for each item in your project’s `Assets` folder. Unity creates meta files for asset files and folders.

These files are hidden in Unity’s **Project window** , and might also be hidden in your file system by default (see Wikipedia: Hidden file and hidden directory), so you might not see them in Windows Explorer or Finder unless you make your hidden files visible on your computer.

The relationship between the `Assets` folder in your Unity project on your computer, meta files, and the Project window in Unity

This example demonstrates that Unity creates a `.meta` file for each asset or folder inside the project’s `Assets` folder, because they appear in a system file browser. However, these `.meta` files are not visible in the Project window because they are hidden by default. To make them visible, open the Mode project setting and enable **Visible Meta Files**.

When Unity creates a `.meta` file for an asset, it writes the asset’s ID inside the `.meta` file and stores the `.meta` file in the same location as the asset file. 

The `.meta` files contain the unique ID assigned to the asset, and values for all the import settings you see in the **Inspector** window when you select an asset in your Project window. For example, for a Texture, this includes the Texture Type, Wrap Mode, Filter Mode and Aniso Level import settings.

If you change the import settings for an asset, Unity saves those new settings to the `.meta` file that accompanies the asset. Unity then re-imports the asset according to your updated settings, and updates the corresponding imported “game-ready” data in the project’s `Library` folder.

### Meta files and asset files

**Important** : Meta files contain important information about how the asset is used in the Project, and they must stay with the asset file they relate to. If you move or rename an asset within Unity’s own Project window, Unity also automatically moves or renames the corresponding .meta file. However, if you move or rename an asset outside of Unity (that is, in Windows Explorer, or Finder on macOS), you must move or rename the .meta file to match.

If an asset loses its meta file (for example, if you move or rename the asset outside of Unity, but don’t move or rename the corresponding .meta file), any reference to that asset is broken in your project. In this situation, Unity notices that the asset does not have a corresponding meta file, generates a new one for the moved/renamed asset as if it is a brand new asset, and deletes the old “orphaned” .meta file.

This process can cause significant problems in your project. For example: * If a texture asset loses its .meta file, any materials that use that texture lose their reference to that texture. To fix it, you would need to manually re-assign that texture to any materials which require it. * If a script asset loses its .meta file, any **GameObjects** or **Prefabs** or **Prefabs** that have that script assigned instead have an “unassigned script” component, and lose their functionality. To fix it, you would need to manually re-assign that script to any GameObjects which require it. 

## Empty folders, meta files, and version control

Unity assigns each folder in your project’s `Assets` folder its own `.meta` file. However, some **version control** systems (VCS) can’t store empty folders. This means that when you add or delete an empty folder from your project, your VCS stores the `.meta` file as added or removed, but doesn’t store the change of adding or removing the folder itself, which can be confusing or problematic.

To help with this issue, Unity behaves in the following specific ways relating to empty folders:

If Unity detects an empty folder that no longer has a corresponding meta file, when that folder previously had a meta file, Unity assumes the meta file was removed via the deletion of the folder by another user in your VCS, and deletes the empty folder locally.

If Unity detects a new meta file for a folder, but that folder does not exist locally, Unity assumes the new meta file was created via to the addition of the folder by another user in the VCS, and creates the corresponding empty folder locally.