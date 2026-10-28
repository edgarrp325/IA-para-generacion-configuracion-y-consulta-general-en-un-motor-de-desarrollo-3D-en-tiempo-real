---
title: "Finding package documentation"
category: "General"
source_file: "upm-docs.html"
doc_type: "manual"
---

# Finding package documentation

The Unity Manual provides documentation for a specific version of Unity. For package documentation, each package has its own version, so each package provides documentation for a specific version of that package. For this reason, the package documentation isn’t part of the main Unity Manual documentation; instead, documentation for each package lives on its own _micro-site_ on Unity’s documentation server.

To access the documentation for a specific package, you have two options:

  * Get documentation for the latest version (from the Unity Manual).
  * Get documentation for a specific package version (from the Package Manager window).

When the package page opens, you can see four links at the top of the page **(A)** , and a drop-down menu **(B)** where you can select a different version:

Unity’s package documentation

Use the links at the top of the page to view the documentation for the package’s core usage (**Manual**), the package’s **Scripting API** documentation, the **Changelog** for the package, and the **License** information for the package.

## Getting documentation for the latest version

Each version of the Unity Manual documentation provides a list of verified and preview packages, a list of built-in packages, and a list of keywords with links to the matching package documentation which you can use with that version of Unity:

List of Unity packages available in the manual

**Note** : Only packages that are compatible with the version of Unity matching the documentation appear in these lists.

You can expand the entries in the sidebar navigation **(A)** to access specific information about each package, including the list of compatible versions, a brief description of the package, and any associated keywords. Or you can click the link on the list pages **(B)** to directly open the most compatible version of that package documentation that matches the documentation version.

If you can’t find the package you want in this list, there might be several reasons:

  * It isn’t compatible with this version of Unity.
  * It is an experimental or private package. Some packages are not available to everyone because someone outside of Unity is developing them or because they are under a special license.

You might be able to access the documentation through the Package Manager window for packages released in another version of Unity. In the case of private packages, try to contact the developer directly to request access.

## Getting documentation for a specific package version

You can find out more about a package by viewing its documentation, changelog, or license information.

To access any of these pages, you can click the **View documentation** , **View changelog** , or **View licenses** links from inside the Package Manager window.

To access the documentation for a specific package version:

  1. Open the Package Manager window in Unity.

  2. Follow the guidelines in Finding packages to locate the specific package and version number you want.

  3. Click the **View documentation** link to open the documentation for the selected version of the package. 

**Note** : If you are offline when you click the **View documentation** link and the package is already installed, the Package Manager opens the `<package-root-folder>/Documentation~` folder in your file browser. If the Package Manager is not installed, a message appears to let you know that the package is not available offline. 

You can follow this procedure for any version of any package. Note that the documentation is not necessarily different for each package version release, since some version updates (patches) involve only bug fixes or trivial changes.