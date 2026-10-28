---
title: "Package Manager"
category: "General"
source_file: "class-PackageManager.html"
doc_type: "manual"
---

# Package Manager

The **Package Manager** settings (menu: **Edit > Project Settings**, then the **Package Manager** category) let you manage your scoped registries and modify the advanced settings for your current project.

The Package Manager settings window. The top of the window displays pre-release package settings (A). The main area of the window (B) displays scoped registries (1) and details for the selected scoped registry (2).

**(A)** Under the **Advanced Settings** section, toggle whether pre-release packages are visible in the Package Manager window.

**(B)** Add, modify, and remove scoped registries for your project under the **Scoped Registries** group, which contains the following areas:

**(1)** The list of scoped registries currently defined for this project

**(2)** The details for the selected scoped registry

  

## Advanced Settings

Use the Advanced Settings group to toggle the Enable Pre-release Packages setting for your current project.

### Enable Pre-release Packages

Enable the **Enable Pre-release Packages** setting to display pre-release packages in the Package Manager window. Pre-release packages appear with the  tag in the list view and the  tag in the details view, as a reminder of which packages will release with the next long-term support (LTS) version of the Unity Editor.

**Warning** : 

By default this setting is disabled because pre-release packages are still being verified as stable enough for production, but are not fully released yet. For more information about the lifecycle of packages, see Package states and lifecycle.

  

## Scoped Registries

The **Scoped Registries** group displays a list of scoped registries already added to the current project on the left, and the details of the selected registry on the right.

For detailed information about scoped registries, including how to use and configure them with the Unity Package Manager, see the documentation on Scoped Registries.

**Note** : If you added a scoped registry but you don’t see it in the **My Registries** context or the **My Registries** context isn’t available at all, it might be because the package registry server you added does not implement the `/-/v1/search` or `/-/all` endpoints, which means that it is not compatible with Unity’s Package Manager.

### Adding a new registry

To add a new scoped registry to your project:

  1. Select the **+** button at the bottom of the list. A new entry appears as **New Scoped Registry** in the list and blank values for the details on the right and the **Revert** and **Apply** buttons change to **Cancel** and **Save** buttons.
  2. Enter values for the Name, URL, and Scope(s) properties.
  3. If you need to specify more than one scope, select the **+** button underneath the last **Scope(s)** value. Another text box appears.
  4. When you are finished entering the information for the selected scoped registry, click **Save**. To cancel adding the new scoped registry entirely, click **Cancel**.

### Modifying an existing registry

To modify an existing scoped registry:

  1. Select the registry you want to modify from the list on the left. The existing information appears on the right.
  2. Modify any of the Name, URL, and Scope(s) properties.
  3. When you are finished updating the information for the selected scoped registry, click **Apply**. To cancel adding the new scoped registry entirely, click **Revert**.

### Removing a registry

To delete an existing scoped registry:

  1. Select the registry you want to delete from the list
  2. Click the **-** button underneath the list. A dialog box prompts you to confirm the removal.
  3. Click **Ok** to proceed or **Cancel** to leave it intact.

  

* * *

  

  * **Scoped Registries** , __Enable Preview Packages__ and __Show Dependencies__ project settings added in 2020.1 NewIn20201
  * **Enable Preview Packages** project setting changed to __Enable Pre-release Packages__ in 2021.1 NewIn20211

PackageManager