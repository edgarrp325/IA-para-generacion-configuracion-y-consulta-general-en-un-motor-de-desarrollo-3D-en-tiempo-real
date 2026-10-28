---
title: "Embedded dependencies"
category: "General"
source_file: "upm-embed.html"
doc_type: "manual"
---

# Embedded dependencies

Any package that appears under your project’s `Packages` folder is embedded in that project. You can create an **embedded package** in several ways:

  * Create a new package directly in your project’s `Packages` folder.
  * Manually copy a Unity package from the project’s package cache into your project’s `Packages` folder.
  * Use a C# script to embed a version of a package that’s already installed.

Embedded packages don’t need to appear in the **project manifest** as a dependency. However, if you embedded a version of an installed package, your project manifest still lists the dependency on the original installed version. In that case, the package on disk takes priority over the version of the package listed as a dependency, so it doesn’t need to be removed from the project manifest. For example, if the project manifest specifies a dependency on version 1.3.1 of the `com.unity.example` package but the project also has an embedded package with that name, the Package Manager uses the embedded package, regardless of its apparent version, instead of downloading version 1.3.1 from the registry.

Make sure you track the contents of your embedded packages, and any changes you make to it. If your Unity project is under source control, add any packages embedded in that project to the same source control. 

## Creating a new custom package

To embed a new package, create your new package content inside a folder under the `Packages` folder. For more information, follow the instructions for creating your own custom package. 

Typically, your new package remains embedded in your project until you are ready to share it with other users and test it in other projects. Then you can publish it to a scoped package registry.

## Copying a Unity package from the cache

A package installed from a registry is **immutable** , which means you can’t edit it. If you want to edit a package, you can make it **mutable** by copying it to the `Packages` subfolder in your `Projects` folder. This package type is called an embedded package, and it overrides what’s in your package cache. Later, you can delete that embedded package’s folder from the `Packages` subfolder, and the Package Manager will automatically change to the immutable, cached package.

**Important** : Unity supports the following procedure for creating an embedded package only. Accessing the package cache folder for any other purpose is discouraged and not supported by Unity. Don’t manipulate the contents of the package cache folder.

To find your package’s folder in the cache, locate the installed version directly in the Unity Editor:

  1. Open the Project window by opening the **Window** menu and selecting **General** > **Project**.

  2. From the **Project window** , find the installed package you want to embed.

  3. Right-click the folder of the selected package and select **Show in Explorer** (Windows) or **Reveal in Finder** (macOS). That package’s folder opens directly in a file browser and uses the `<package-name>@<package-version>` naming convention.

File browser opened to the package folder under the project’s package cache
  4. Copy the package folder and paste it directly into your project’s `Packages` subfolder, not the `Packages` root folder. Don’t put it inside the `Assets` folder, because the Package Manager doesn’t scan that folder for packages.

  5. Remove the `@<package-version>` part of the folder name.

  6. Add the newly embedded package to source control if your project is already under source control.

**Note** : You can also find package folders under the global cache, but the global cache contains packages from all versions of the Unity Editor that have ever been installed on your system, so be careful to pick a version that’s compatible with your project’s Editor version.

If you want to delete the embedded package, use your file browser or command line to locate that package in your `Packages` folder. Consider backing up the folder for the embedded package, otherwise you’ll lose any changes you made to the package. Then, delete the folder for that package from your `Packages` folder. The Package Manager will automatically revert to the immutable, cached package.

## Additional resources

  * Use a script to embed a package in your project