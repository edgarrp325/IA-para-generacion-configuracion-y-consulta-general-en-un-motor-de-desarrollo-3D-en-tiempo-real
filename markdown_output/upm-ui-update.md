---
title: "Switch to another version of a UPM package"
category: "General"
source_file: "upm-ui-update.html"
doc_type: "manual"
---

# Switch to another version of a UPM package

Use the information on this page to update **UPM packages** that were installed from the Unity Registry or a scoped registry, or from a local source. The information on this page also applies to packages you installed from the **Asset Store** that were installed from the Unity Registry or a scoped registry, or from a local source. The information on this page also applies to packages you installed from the **Asset Store** , if they’re in the UPM format.

If you want to install a specific version of a package, install the package by name and follow its optional step to specify a version.

If you want to update packages that were installed from a Git URL, you can use any of the following methods:

  * Locate the package in the Package Manager, select it, then click the **Update** button.
  * Reinstall it as a Git dependency using a new revision. For more information about how to specify revisions with **Git dependencies**
  * Reinstall it from the Unity Registry.

To update a package while in the **In Project** , **Unity Registry** , or **My Registries** context:

  1. Open the Package Manager window and select **In Project** from the Packages menu.

Switch the context to **In Project**

An arrow icon () appears next to any packages that have updates available.

  2. Select the installed package you want to update from the list of packages. The package information appears in the details view. 

  3. The lock icon () indicates that this package and version is locked to an installed **feature set**. To unlock the package and select another version, click the **Unlock** button.

**Note** : The package is temporarily unlocked. If you change to a different list context, or close either the Package Manager or the Editor, the package reverts to a locked state again. However, if you switch versions when the package is unlocked (for example, with the Install a package from a registry by name method), the package stays unlocked.

  4. Select a package in the list of packages.

A package that has an available update
  5. In the details view, select the **Version History** tab. If multiple versions are available, expand the entries to see information specific to each version.

Version numbers for installed packages display in multiple places and the recommended version appears on the **Update to** button
  6. Click the **Update to** button, or click the **Update** button beside the version listed in the **Version History** tab.

When the progress bar finishes, any new functionality is immediately available.

**Notes:**

  * If you switch to an older version of a package, you might have to run the API Updater on the package contents.
  * You can switch versions for multiple packages with one click by using the multiple select feature. For more information, see Perform an action on multiple packages or feature sets.

## Additional resources

  * Package types
  * Add and remove UPM packages or feature sets