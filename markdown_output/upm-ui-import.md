---
title: "Download and import an asset package"
category: "General"
source_file: "upm-ui-import.html"
doc_type: "manual"
---

# Download and import an asset package

You can import an asset package that you got from the **Asset Store** and download it to your project by using the Package Manager window.

**Notes:**

  * This task applies only to asset packages in the `.unitypackage` format. For information about installing packages from the Asset Store that are in the UPM format, refer to Install a UPM package from Asset Store. For information about the differences between the package types, refer to Package types.
  * Follow this task to import an asset package that isn’t in your project yet. For information about updating an asset package that’s already in your project, refer to Updating an asset package.

## Prerequisites

Before you begin:

  * Make sure you’ve acquired the package from the Asset Store. Refer to Purchase or download a package from the Asset Store.
  * Make sure the package appears in the List view of the Package Manager window when you select the **My Assets** context.

## Procedure

  1. Open the Package Manager window and select **My Assets** from the Packages menu.

Switch the context to **My Assets**

The list view displays any Asset Store packages that you have purchased.

  2. If many asset packages appear in the **My Assets** list, you can search for a specific Asset Store package by name or version number.

  3. Select the asset package you want to import from the list of packages. The asset package information appears in the details view.

If you haven’t downloaded the asset package to this computer or device before, the **Download** button appears. Otherwise, the **Import** button appears instead and you can skip to step 6 to import the package right away.

  4. Click the **Download** button to download the asset package if it appears in the details view.

**Download** button in the corner of the details view

While the package downloads to your computer, a progress bar appears and **Pause** and **Cancel** buttons replace the **Download** button you clicked.

Download progress, and buttons to control the progress

These buttons give you control over the download progress:

     * Click the **Cancel** button to stop the download entirely.
     * Click the **Pause** button to pause downloading. You can click the **Play** button to continue.

When the download finishes, the Package Manager replaces **Download** with **Re-Download** , and an **Import** button appears next to **Re-Download**.

  5. Click the **Import** button to import the selected asset package.

If the asset package is a complete project, a confirmation dialog appears. See Importing a complete project from the Asset Store.

For all other asset packages, an import window displays, with all items in the package selected, ready to install.

The **Import** window
  6. Clear any items you don’t want to import and click **Import**.

The Package Manager puts the contents of the imported package into the `Assets` folder, so that you can access them from your **project window**.

**Note** : You can download multiple packages with one click by using the multiple select feature. For more information, see Perform an action on multiple packages or feature sets.

## Importing a complete project from the Asset Store

A complete project contains assets and **project settings**. The process for importing a complete project is similar to other asset packages, except for an additional step for project settings.

The project settings in the complete project might conflict with settings in your project, so when you import a complete project from Asset Store, the Package Manager offers a choice.

Dialog box for importing a complete project

Choose **Import** if you’re sure that you want to add the package’s assets to your project. An Import Unity Package dialog box appears, like the one pictured below. Clear any asset content you don’t want to import and click **Next**. The second step of the dialog box lists the package’s project settings. If you have any of those project settings in your project, Package Manager identifies them with an **Override** flag; they will be overwritten with the project settings from the package unless you clear the selection. Clear any project settings you don’t want to import and click **Import**.

Choose **Switch Project** if you want to explore the package’s assets and project settings in a safe environment. Choosing **Switch Project** creates a new, temporary project that contains only that package’s assets and project settings. After exploring the temporary project, you can close it without saving. If you want to continue to use that package in your main project, return to your main project and import the package again. Choose **Import** on the warning dialog box that appears. 

Importing asset content (left) and project settings (right) from a complete package

  

## Additional resources

  * Package types
  * Asset packages