---
title: "Packages list context"
category: "General"
source_file: "upm-ui-filter.html"
doc_type: "manual"
---

# Packages list context

To change which packages appear in the list, select the context you want from the **Packages** drop-down menu on the Package Manager window.

Set the context for which packages you want to appear in the list

You can select from these options:

**Context:** | **Description:**  
---|---  
**Unity Registry** | Displays all feature sets and packages on the Unity package registry, regardless of whether they are already installed in your project. This does not include packages installed from any other location or from any scoped registry.  
  
This is the default list context.  
**My Registries** | Displays any packages available from any scoped registry installed in this project.  
  
**Note** : If you added a scoped registry but you don’t see it in the **My Registries** context or the **My Registries** context isn’t available at all, it might be because the package registry server you added does not implement either of the `/-/v1/search` or `/-/all` endpoints, which means that it is not compatible with Unity’s Package Manager.  
**In Project** | Displays all **feature sets** and packages currently installed in your project, including local, git, and embedded packages, and packages installed from any registry.  
**My Assets** | Displays all Asset Store packages (`.unitypackage`) that you have purchased using the Unity ID you are currently logged in with.  
**Built-in** | Displays only built-in Unity packages, which represent some of the core Unity features. You can use these packages to turn Unity modules on and off.  
  
**Tip** : You can find out more about what each built-in package (module) implements in the Unity Scripting API. Each module assembly page lists which APIs the built-in package implements.  
  
When you select a new context, your choice appears on the **Packages** drop-down menu and the list displays the feature sets and packages matching your choice.

**Note** : If you entered any text in the search box or set any filters, the list only displays feature sets and packages which match the context, the search criteria, and the active filters.

  

* * *

  * **My Assets** context added in Unity 2019.3 NewIn20193

  * **Unity Registry** context replaced the **All packages** context and the **My Registries** context added in Unity 2019.4 NewIn20194

  * Filtering Asset Store packages added in Unity 2020.1 NewIn20201