---
title: "Customize the global cache location"
category: "General"
source_file: "upm-config-cache.html"
doc_type: "manual"
---

# Customize the global cache location

The Package Manager maintains a global cache for registry data and uncompressed packages. The global cache includes subsidiary caches, each serving a different purpose. The Package Manager stores the global caches in a default location, which you can override.

You might want to override the cache location for several reasons:

  * You want to save space on your internal drive.
  * You want to store the cache on a shared drive, which is accessible to others.
  * You want to store the cache in a folder that’s not in a system directory.

By default, the Package Manager uses the following folder structure for the global cache:
    
    
    <global-cache-root>
      ├── npm
      │   └── <registry data (package metadata and tarballs)>
      ├── packages
      │   └── <uncompressed contents of package tarballs>
      └── git-lfs (if enabled)
           └── <downloaded Git LFS files>
    

For information on the default location of the global cache root, refer to global cache.

**Note** : The Package Manager maintains a global cache separately from the **asset package** cache. For information on overriding the default location for the asset package cache, refer to Customize the asset package cache location. 

To override the default location of the global cache root, you can use the following methods: 

  * The Preferences window is the recommended method because of its ease and permanence. When you change the package cache location using this method, Unity stores the preference for the current session and future sessions. 
    * **Note** : Using the **Preferences** window sets the `cacheRoot` property in a user configuration file. If you want to set the user configuration file manually, refer to Using the user configuration file.
  * The environment variable method isn’t permanent, but advanced users might find it preferable in specific use cases.

## Important notes before you begin

  * Regardless of the method you choose, changing the cache location tells the Package Manager to use that location going forward. Existing packages that Package Manager stored in the original location remain in that folder structure.
  * You can use environment variables to override the location of the global cache root or its subsidiary caches (registry data cache, uncompressed packages cache, and the Git LFS [Large File Storage] cache). However, environment variables and configuration file properties aren’t equivalent, so using different methods to configure settings can produce unexpected results.
  * There are several factors that affect how setting several values with different methods work together: 
    * If you used the environment variable method to change the cache location, then you can’t use the **Preferences** window to change the location.
    * When you use a user configuration file, your change applies to the current user account. Although a global configuration file exists, you can’t set the global cache location in the global configuration file.
    * If you set different values for the global cache root with both the `UPM_CACHE_ROOT` environment variable and the `cacheRoot` property, Package Manager uses the location in the `UPM_CACHE_ROOT` environment variable.
    * If you set an environment variable for the registry data cache (`UPM_NPM_CACHE_PATH`), the uncompressed packages cache (`UPM_CACHE_PATH`), or the Git LFS cache (`UPM_GIT_LFS_CACHE_PATH`), Package Manager uses the location specified by the environment variable, regardless of where the global cache root is.
    * If you enable the Git LFS cache (`UPM_ENABLE_GIT_LFS_CACHE`) without explicitly setting its path (`UPM_GIT_LFS_CACHE_PATH`), Package Manager uses the `git-lfs` folder under the global cache root as its location.

## Using the Preferences window

To use the **Preferences** window to override the default location of the global cache, follow these steps.

  1. Use one of the following methods to open the **Preferences** window: 

     * Use the Unity Editor’s menus, as described in Preferences.
     * Open the Package Manager window, open the **Advanced** menu, and select **Preferences**.
  2. Select the **Package Manager** category.

  3. Under **Packages** , open the menu beside **Cache Location** .

  4. Choose **Change Location**. 

  5. Choose a new location for the global cache.

The Preferences window with the Package Manager category selected

## Using the user configuration file

You can manually edit the user configuration file to override the location of the global cache root. Although a global configuration file exists, you can’t set the global cache location in the global configuration file.

Follow these steps to edit the user configuration file:

  1. Locate the `.upmconfig.toml` user configuration file. To find the file location, refer to Configuration files. If the file doesn’t exist, create an empty text file.

  2. Add the `cacheRoot` key and set its value as an absolute path to a custom location. **Important** : When setting Windows paths in TOML files, use forward slashes (`/`) or double backslashes (`\\`). Don’t use single backslashes (`\`) because they’re special characters which mark escape sequences and can cause TOML parsing errors.

**Windows example**
         
         cacheRoot = "E:\\Unity\\cache"
         

**macOS and Linux example**
         
         cacheRoot = "/dev/external/shared/Unity/cache"
         

You don’t need to restart the Unity Editor or the Hub after setting the `cacheRoot` key for the change to take effect.

## Using environment variables

In scenarios that involve automation or continuous integration, it’s less practical and more error prone to configure settings in the user configuration file or the **Preferences** window. In such scenarios, you might consider using environment variables to configure settings for the global cache and its subsidiary caches. The following environment variables are available:

**Environment variable:** | **Description:**  
---|---  
`UPM_CACHE_ROOT` | Specify the location of the global cache (the root folder containing the registry data and uncompressed packages caches).  
`UPM_NPM_CACHE_PATH` | Specify the absolute path to the location where you want Package Manager to store package metadata and tarballs. By default, this is the `npm` subdirectory under the global cache root.  
`UPM_CACHE_PATH` | Specify the absolute path to the location where you want Package Manager to store the uncompressed contents of package tarballs. By default, this is the `packages` subdirectory under the global cache root.  
`UPM_ENABLE_GIT_LFS_CACHE` | Specify any value except empty ("") to enable the Git LFS cache. By default, Package Manager uses the `git-lfs` subdirectory under the global cache root, unless you specify a different path using the `UPM_GIT_LFS_CACHE_PATH` environment variable.  
`UPM_GIT_LFS_CACHE_PATH` | Specify the absolute path to the location where you want Package Manager to store the Git LFS cache. By setting this path, you automatically enable the Git LFS cache.  
  
**Important** : Follow these guidelines when you use this method:

  * Close the Unity Editor and Unity Hub if they’re already running before setting environment variables.
  * Launch the Unity Editor or Unity Hub from the same command prompt or terminal session where you set the environment variables.
  * Any environment variables you set in the preceding table must be set every time you launch Unity.

For information on setting environment variables, refer to the documentation for your operating system. For an introduction to environment variables, refer to https://en.wikipedia.org/wiki/Environment_variable. 

## Additional resources

  * Configuration files
  * Customize the Asset Store cache location