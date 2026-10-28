---
title: "List view"
category: "General"
source_file: "upm-ui-list.html"
doc_type: "manual"
---

# List view

The Package Manager window displays the list of feature sets, packages, or **Asset Store** packages according to the criteria that you select by filtering, including, or searching:

The image on the left displays all features sets and packages installed in your project, and the image on the right displays packages from **My Assets**

**(A)** Feature sets appear at the top of the list view, indicated with the feature set icon (). Toggle the expander icon to show or hide the list of feature sets. When you select a feature set from the list, details about it appear on the right, including a brief description, a list of included packages, and a link to the QuickStart guide for that feature set.

**(B)** Registry groups organize the list of packages installed in your project (or available for installation when you are in the **My Registries** context). Select the expander on the left to show or hide the list of packages for each registry.

**(C)** Icons display in this column when a package is locked () or installed as a dependency (), and more.

**(D)** The package version displays the version of the package that’s installed. If the package is not yet installed, the version that appears is the recommended version. Special icons often appear beside the version number indicating its state:

  * Released
  * Release Candidate
  * Pre-release
  * Experimental
  * Custom (embedded)

For packages from the Asset Store, the version that appears is either the version you already downloaded or the version that is available for download from the Asset Store.

**(E)** These icons display the status of the package:

**Icon:** | **Description**  
---|---  
| A check mark indicates that the package or feature set is already installed or enabled.  
  
**Note** : Installed Asset Store packages display the import icon () if they are up to date.  
| The update icon indicates that the package has an available update. To update your package, follow the instructions for either type of package:  
  
\- For Unity Package Manager (UPM) packages, refer to Switch to another version of a UPM package.   
\- For asset packages, refer to Update an asset package.  
\- Feature set versions are fixed to the Editor version and can’t be updated.  
| The import icon indicates that there is an **asset package** available to import. It also appears when you have imported the package in the project already.  
| The download icon indicates that there is an asset package available to download.  
| An error icon indicates that something went wrong during installation or loading. For more advice on resolving errors, refer to Error messages.  
  
**(F)** The **My Assets** context displays a counter showing the number of packages from the Asset Store that are available but not shown in the list. To load more packages from the Asset Store , click the **Load** link.

**Note** : If you select the **My Assets** context but the Package Manager window doesn’t list any packages, refer to Error messages in the Package Manager window for an explanation and solution.

**(G)** The status bar displays messages about the package load status and network warnings.

**(H)** Click the **reload** button to force Package Manager to reload your packages and feature sets.

By default, the Package Manager window displays the list of all packages and feature sets available in the selected context, but you can filter the list to display packages and feature sets that meet your criteria. While viewing the **Unity Registry** or **In Project** context, you can also switch from the **All** tab to the **Services** tab to display services

You can also include pre-release packages in the list and search for a specific package or feature set by name (ID) or display name.

## Additional resources

  * Package types