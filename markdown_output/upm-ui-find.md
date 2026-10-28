---
title: "Finding packages and feature sets"
category: "General"
source_file: "upm-ui-find.html"
doc_type: "manual"
---

# Finding packages and feature sets

The Package Manager window provides several ways to help you find a specific package or **feature set** :

At the top of the Package Manager window, there are several controls to help you narrow down the list of packages  
---  
**(A)** | **Packages** list context | Choose the “context” that determines what appears in the list. The context might be the source of the package, such as a registry server, the Asset Store, or the Unity Editor itself (for built-in packages). However, the **In Project** context displays only those packages and feature sets that are already installed in the current project, regardless of their origin.  
  
For example, you can choose the **My Assets** context to display only Asset Store packages available to you in the list, or choose the **In Project** context to display only Unity packages and feature sets that are already installed in your project.  
**(B)** | **Sort** | Sort the list in either ascending or descending order by name, published date (**Unity Registry** , **My Registries** , **In Project only**), purchased date (Asset Store packages only), or recently updated (In Project and My Assets only).   
  
For example, if you want to find a Unity package that had a recent update but you can’t remember the name of it, try sorting by **Recently updated** in descending order and browse the list from the top down to find it.   
  
Sorting affects the items under each expander, but leaves the expanders in place. If you sort from Z-A, the Package Manager reorders all the feature sets from Z- A inside its expander, and all the packages under each expander but doesn’t mix the content in the list.  
**(C)** | **Filters** | Select options to narrow down the packages listed. Packages listed in My Assets have enhanced filtering options:  
  
\- **Status** (Downloaded, Update available, Unlabeled, Hidden, Deprecated)  
\- **Categories** (2D, 3D, Audio, Templates, Tools, etc.)  
\- **Labels** (Custom labels you define in the Asset Store)  
**(D)** | Search | Use the search box to look for a Unity package or an **Asset Store** package by name.  
  
These controls help narrow down which packages and feature sets appear in the list view and in what order. This makes it easier to find what you are looking for or help you browse when you don’t know exactly what you want.

When you use several of these controls at the same time, you narrow the set of matches that appears in the list.

After you find the Unity package you need, you can select it, then potentially locate a specific version in the details view. For feature sets, there’s always only one version available, so you can either install it or remove it.

## Finding a specific version

To find a specific package version:

  1. In Unity, open the Package Manager window (navigate to Unity’s main menu and go to **Window** > **Package Manager**).

  2. If you are looking for a pre-release package, follow these steps:

     * Select **Project Settings** under the Advanced menu.

Project Settings opens the Package Manager project settings window

The Package Manager Project Settings window appears.

     * Under the **Advanced Settings** group, enable the **Enable Pre-release Packages** option.

     * Close the **Project Settings** window. Any pre-release packages now appear in the list with the  label.

  3. You can either browse the list of packages or find a specific package using one of these methods:

     * Search for a package by name or keyword.
     * Sort the list (for example, by last updated in descending order to find the most recently updated packages).
     * Apply filters to the list.
  4. Select a package from the list of packages.

  5. In the details view, select the **Version History** tab. If multiple versions are available, expand the entries to see information specific to each version.

Version numbers for installed packages display in multiple places and the recommended version appears on the **Update** button
  6. You can perform a variety of actions when you expand a specific version in the **Version History** tab:

     * You can view the changelog for that version and click **Changelog** to see the full list of changes across versions.
     * If you don’t already have this package installed in your project, you can install this version.
     * If another version of this package is already installed in your project, you can update the package to this version.
     * If you installed this package in your project but don’t want it anymore, you can remove the package from your project.