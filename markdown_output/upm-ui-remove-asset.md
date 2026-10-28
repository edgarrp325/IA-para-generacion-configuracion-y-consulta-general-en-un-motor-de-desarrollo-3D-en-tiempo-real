---
title: "Remove imported assets from a project"
category: "General"
source_file: "upm-ui-remove-asset.html"
doc_type: "manual"
---

# Remove imported assets from a project

When you import an **asset package** from the **Asset Store** from the **Asset Store** , the Unity Package Manager places the package’s assets in the `Assets` directory in your project.

You can manually remove assets from a project if you know the assets aren’t in use. You might consider this action to unclutter your project directory or to free up space on your local hard drive.

**Warning** : Make sure your project isn’t using any of the assets you remove. Unlike _installed_ packages, the Package Manager doesn’t track _imported_ packages, so it can’t detect when you remove dependent assets.

## Before you begin

Make sure you understand these important notes before you begin:

  * Use this procedure to remove assets only if they came from an asset package and you _imported_ them by following the Download and import an asset package procedure or by importing a custom package. Don’t use this procedure to attempt to remove **UPM packages** that you _installed_ from a registry. Installed UPM packages can come from a registry, but they can also come from the Asset Store. For information about removing UPM packages that you installed from a registry, see Remove a UPM package from a project.

  * This procedure removes assets from the current project. It doesn’t remove the same assets that might exist in other projects. It also doesn’t remove asset packages from the cache. To completely remove an asset package and its assets from your computer, you must remove them from multiple locations:

    1. Use the following procedure to remove the assets from each project that uses them.
    2. Delete this asset package from the cache. See Delete an asset package from the cache.

## Procedure

To remove imported assets from your project:

  1. Open your project.

  2. Open the Package Manager window.

  3. Open the **Packages** menu and select the **My Assets** context.

  4. Select the asset package you want to remove from your project and take note of the package name (A) and the publisher name (B). These names might help you identify the asset directory in a later step.

The **My Assets** context shows the package name (A) and the publisher name (B)
  5. Open the **Project window**.

  6. Expand the `Assets` directory.

  7. Locate the subdirectory for the package you identified in the Package Manager window in a previous step.

  8. Explore the directory structure that the publisher created (C), confirm it’s the correct package, and identify the assets you want to delete (D). **Note** : Unity doesn’t impose directory names or structures on publishers, so their assets might not be in an easily identifiable directory. The directory structure might be simple or complex.

The Project window with an assets folder selected (C) and its contents (D)
  9. Select the asset or assets you want to delete. Your selection can be a single asset, multiple assets, all assets in a subdirectory, or more.

  10. Right-click the selected items, and select **Delete**.

**Important** : 

  * **Scenes** that depend on deleted assets aren’t reported as errors in the **Console window** that depend on deleted assets aren’t reported as errors in the **Console window**. If you suspect the removal caused issues, import the package again. Refer to Download and import an asset package.
  * Assets that you remove from your project remain in the My Assets list view. To remove asset packages from **My Assets** , refer to Delete an asset package from the cache.

## Additional resources

  * Package types
  * Remove a UPM package from a project
  * Delete an asset package from the cache
  * Download and import an asset package