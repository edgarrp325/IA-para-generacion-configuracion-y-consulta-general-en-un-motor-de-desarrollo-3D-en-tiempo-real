---
title: "Global Cache"
category: "General"
source_file: "upm-cache.html"
doc_type: "manual"
---

# Global Cache

When the Unity Package Manager fetches **UPM packages** , it stores the package contents and metadata in a global cache. This makes reusing and sharing packages more efficient, and allows you to install and update stored packages even when offline.

**Note** : Storing packages in the global cache applies to UPM packages fetched from a registry. Packages in the UPM format that come from the **Asset Store** are also stored in the global cache. However, asset packages are also stored in the global cache. However, asset packages in the `.unitypackage` format that come from the Asset Store aren’t stored in the global cache. The Package Manager stores asset packages in a separate cache. For more information, refer to Asset Store packages.

## Location

By default, Unity stores the global cache in a root directory that depends on the operating system (and the user account type on Windows):

**Operating system** | **Default root directory**  
---|---  
Windows (user account) | `%LOCALAPPDATA%\Unity\cache`  
Windows (system user account) | `%ALLUSERSPROFILE%\Unity\cache`  
macOS | `$HOME/Library/Unity/cache`  
Linux | `$HOME/.config/unity3d/cache`  
  
**Tip** : You can override the location of this root directory. Refer to Customize the global cache location for more information.

## Structure

The Package Manager global cache uses two different subsidiary caches, each serving a different purpose. The Package Manager stores these subsidiary caches in subdirectories under the folder of the global cache:

**Subfolder** | **Description**  
---|---  
`npm` | Stores data obtained from registries using the npm protocol. This includes package metadata and package tarballs.  
`packages` | This cache contains the uncompressed contents of package tarballs fetched from a registry.  
`git-lfs` | This cache contains downloaded Git Large File Storage (LFS) files, if you’ve enabled Git LFS.  
  
Inside each of these subfolders, each registry has its own path so that packages hosted on different registries aren’t mixed up.

**Tip** : You can override the location of these folders. Refer to Customize the global cache location for more information.

## Requirements

The user account running the Unity Editor process must have full write permissions on the root directory and its contents. Without these permissions, the Package Manager can’t download and save the package metadata and contents in the cache.

# Additional resources

  * Package types