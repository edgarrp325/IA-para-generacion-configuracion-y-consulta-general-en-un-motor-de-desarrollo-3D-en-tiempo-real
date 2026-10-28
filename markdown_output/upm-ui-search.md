---
title: "Search box"
category: "General"
source_file: "upm-ui-search.html"
doc_type: "manual"
---

# Search box

You can use the search box at the top of the Package Manager window to find any packages or feature sets that match the text you enter. The Package Manager updates the list as you enter text, displaying every package or **feature set** within the current context that matches. For example, if you enter **web** in the search box, the list displays different results depending on whether you choose the **Built-in packages** list context or the **Unity Registry** list context:

Search for specific text

You can look for a package or a feature set by its name (ID) or its display name. You can search for either the display name as it appears in the Package Manager window or, for Unity packages and feature sets, the registered package name that begins with **com.unity**.

Your search text could match the beginning, middle, or end of the name. The Package Manager updates the list dynamically.

**Note** : You can search for either Unity packages and feature sets or **Asset Store** packages. The list context you choose defines where the Package Manager searches:

**List context:** | **Where the Package Manager searches:**  
---|---  
**Unity Registry** | The list of packages and feature sets on the Unity registry  
**My Registries** | Any scoped registry defined for your project  
**In Project** | The package cache and the `Packages` folder under your current project  
**My Assets** | The list of Asset Store packages available with your Unity account  
**Built-in packages** | The list of built-in packages on the Unity registry