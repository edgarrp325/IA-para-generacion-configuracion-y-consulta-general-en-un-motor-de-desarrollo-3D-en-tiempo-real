---
title: "Install a UPM package from a registry"
category: "General"
source_file: "upm-ui-install.html"
doc_type: "manual"
---

# Install a UPM package from a registry

**Note** : When you install a **UPM package** through the Package Manager window, the Package Manager evaluates other packages and their dependencies to see if there are any version conflicts with the version you selected. If it detects any conflicts or restrictions, it installs whatever version resolves these issues. For more information, see Dependency and resolution.

Use the same process for installing a package from either the Unity registry or any scoped registry defined in your project. The only difference is what you choose from the **Packages** drop-down menu:

  1. Open the Package Manager window and select **Unity Registry** from the Packages drop-down menu. If you set up a scoped registry and you want to install a package from a scoped registry, choose **My Registries** instead.

**Note** : If you haven’t defined any scoped registries for this project, **My Registries** doesn’t appear in the drop-down menu.

Change the context to **Unity Registry**
  2. Select the package you want to install from the list of packages. The package information appears in the details view.

**Note:** If you don’t see the package you want to install in the list of packages, it might be an undiscoverable package, such as experimental and pre-release packages. The Package Manager doesn’t display experimental packages unless they are already installed, but pre-release packages appear in the Package Manager when you enable the Enable Pre-release Packages project setting.

  3. Optional: If multiple versions are available, select the version to install. For more information on available versions, see Finding a specific version.

  4. Click the **Install** button.

When the progress bar finishes, the new package is ready to use.

**Note** : You can install multiple packages with one click by using the multiple select feature. For more information, see Perform an action on multiple packages or feature sets.

## Additional resources

  * Package types
  * Install a UPM package from Asset Store
  * Download and import an asset package