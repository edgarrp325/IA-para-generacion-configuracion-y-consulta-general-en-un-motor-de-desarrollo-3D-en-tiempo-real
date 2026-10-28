---
title: "Add and remove UPM packages or feature sets"
category: "General"
source_file: "upm-ui-actions.html"
doc_type: "manual"
---

# Add and remove UPM packages or feature sets

You can perform a variety of package management tasks by using the Package Manager window.

Follow these tasks to manage **UPM packages** or **feature sets** or **feature sets**. For information about managing **asset packages**. For information about managing **asset packages** , refer to Add and remove asset packages.

  * Install a feature set from the Unity registry
  * Install a UPM package from a registry
  * Install a UPM package from Asset Store
  * Install a UPM package from a local folder
  * Install a UPM package from a local tarball file
  * Install a UPM package from a Git URL
  * Install a UPM package from a registry by name
  * Remove a UPM package from a project
  * Switch to another version of a UPM package

The procedures described in these sections obscure a lot of the details of what the Package Manager is actually doing behind the scenes. The Package Manager window provides a visual interface to install and uninstall packages. The Package Manager installs and uninstalls packages by adding and removing packages as project dependencies in your project’s manifest. When it adds a package, it selects the correct version to install. The version that Package Manager selects doesn’t always match the version you indicated. For more information, refer to Dependency and resolution.

## Additional resources

  * Package types
  * Add and remove asset packages
  * Disable a built-in package
  * Perform an action on multiple packages or feature sets