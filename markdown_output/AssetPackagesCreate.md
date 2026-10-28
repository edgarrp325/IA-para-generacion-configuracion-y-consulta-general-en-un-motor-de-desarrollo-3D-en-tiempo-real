---
title: "Create and export asset packages"
category: "General"
source_file: "AssetPackagesCreate.html"
doc_type: "manual"
---

# Create and export asset packages

If you want to share **scenes** , samples, tools, or other assets, you can export an **asset package** , samples, tools, or other assets, you can export an **asset package** (`.unitypackage` format). You might want to create an asset package to copy several assets or an entire scene from one project to another. Another option is to create your own Unity package.

Follow these instructions to export an asset package.

**Note** : If your assets are high quality and other users might find them useful, refer to Publishing to the Asset Store for instructions to create a package draft and upload it to the **Asset Store**

To create and export an asset package:

  1. Open the project you want to export assets from.

  2. Go to the **Project** window and select one or more items or folders. These items become the starting list for your export. You can also select the `Assets` folder as a way include all assets as your starting point.

  3. Choose **Assets** > **Export Package** from the menu to open the **Exporting package** dialog.

Exporting package dialog
  4. In the dialog, select the assets you want to include in the package by clicking on the boxes.

  5. Leave **Include dependencies** enabled to automatically select any assets used by the assets you already selected. Enabling **Include dependencies** also includes any **scripts** that are directly required by the selected assets.

  6. Leave **Include all scripts** enabled to export all scripts from your project. If you disable **Include all scripts** but enable **Include dependencies** , Unity still exports the scripts that your selected items directly depend on. Unity doesn’t have a way to determine whether the scripts in your selection reference other scripts. Enabling **Include all scripts** reduces the likelihood of compilation errors when using the exported package in another project.

**Tip** : Selecting all items and enabling both checkboxes is a simple way of exporting the assets in a scene without manually locating them all.

  7. Click **Export** to bring up the file explorer and choose where you want to store your package file.

  8. Name and save the package.

## Re-exporting asset packages

If you want to change the contents of an asset package and create a newer, updated version of your asset package, select the asset files you want in your package (both the unchanged ones and the new ones). Then follow the previous instructions to export the files.

### Naming strategies

Rename your updated package using incremental names: for example, `MyAssetPackageVer1`, `MyAssetPackageVer2`. Unity recognizes it as an update, so you should use a naming convention that’s clear for you and anyone you share it with.

**Warning:** Don’t remove files from asset packages and then add different files with the same name. Unity uses unique IDs to track files, so it recognizes them as different and possibly conflicting files. In these cases, Unity displays a warning symbol when importing them. If you have removed a file and then decide to replace it, rename it something else, even if it is close to the original name.

## Additional resources

  * Create custom packages