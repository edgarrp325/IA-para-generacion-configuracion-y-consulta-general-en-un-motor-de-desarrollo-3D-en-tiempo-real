---
title: "Package types"
category: "General"
source_file: "upm-package-types.html"
doc_type: "manual"
---

# Package types

Unity’s Package Manager supports two package types:

  * **UPM packages** (Unity Package Manager built-in format).
  * **Asset packages** (`.unitypackage` format).

The following table compares the differentiating characteristics of these package types:

**Characteristic** | **UPM packages** | **Asset packages**  
---|---|---  
Format | Collection of files and folders, which might be compressed, depending on the distribution method. | A compressed file with a `.unitypackage` extension.  
Primary source for the package | Unity registry, scoped registry, or **Asset Store** | Asset Store  
Uses a package manifest file | Yes | No  
UI action for adding the package to a project | Install | Download and import  
Project folder the package is added to | `Packages` | `Assets`  
Cache the package is added to | Global cache | Asset package cache. Refer to Location of downloaded asset package files.  
You can manually remove the package from the cache | No | Yes  
Sets of tabs that appear in the Details panel | Description, Version History, Dependencies, Samples (if provided), Images (if provided) | Overview, Releases, Imported Assets, Images  
  
## Additional resources

  * Add and remove UPM packages or feature sets
  * Add and remove asset packages