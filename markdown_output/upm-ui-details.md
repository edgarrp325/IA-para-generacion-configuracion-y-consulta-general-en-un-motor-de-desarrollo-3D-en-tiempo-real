---
title: "Details view"
category: "General"
source_file: "upm-ui-details.html"
doc_type: "manual"
---

# Details view

In the Package Manager window, the pane on the right displays details of the selected package.

Package details for a Unity Package Manager (UPM) package (left) and an asset package (right)

These details include the following information:

**(A)** The display name.

**(B)** The package version, the date the package was published to the registry or the Asset Store, and any source or asset labels. Other information might display, if applicable:

  * The information  button might also appear before the version. When you click the information button, Unity displays information about the package (for example, if the package version you requested does not match the version installed).
  * For Unity Package Manager (UPM) packages, a lock icon () appears before the version number when an installed **feature set** requires the selected package. It prevents you from accidentally changing the version of the package so the feature set continues to work effectively.

**(C)** The registry that hosts the package and the package author (UPM packages), or the package publisher (Asset Store). 

**(D)** The package name (UPM packages only).

**(E)** For **UPM packages** , the links to open the package documentation page, the package change log (if available), and the license information. For **asset packages** , the links to open the package documentation page, the package change log (if available), and the license information. For **asset packages** , the links to open the package’s official page on the Asset Store, and if available, links to the publisher’s website and their support page.

**(F)** Package details tabs, which vary by package type:

  * For UPM packages: 
    * **Description** : A brief description of the package.
    * **Version History** : Package Manager always lists the installed or recommended package versions, with action buttons to install, update, or remove. Package Manager also lists other supported versions, if available. Expand each entry to see the release date, changelog for that version, and a link to the full changelog.
    * **Dependencies** : Dependency information for the package. This section lists dependencies in two directions: 
      * **Is using** : Whether this package depends on another package, and if so, which version. Installed packages display the status of the dependencies after the version number.
      * **Used by** : Whether another package depends on this one, and if so, which version.
    * **Samples** : This tab displays only if the package author provided samples. The tab displays a description and an **Import** button next to the sample.
  * For asset packages: 
    * **Overview** : Information about the package: 
      * Any custom labels you assigned this package on the Asset Store.
      * The supported versions of Unity.
      * The disk space required.
      * The date you acquired this package from the Asset Store.
      * A brief description of the package.
    * **Releases** : Release information, including when the package was originally released and when the current version was released.
    * **Images** : Thumbnails of the marketing images, audio, and video available on the Asset Store for Asset Store packages.

**(G)** Button(s) to unlock, install, update, remove, or disable the Unity package.

**(H)** Button(s) to download and import or update the an asset package.

## Labels

Some packages display labels next to the package name or version number. These labels provide information about the source or state of the package:

  * Source label types indicate where the package originates from (for example, whether it comes from a local folder or is downloaded from the package registry).
  * State label types indicate the package’s stage of the development cycle. For example, whether it is custom, an experimental package, or on the release track for a specific Unity version.
  * Asset Store labels indicate that the Asset Store package originated from the Asset Store and may also indicate some special status (for example, deprecated).

Some source labels imply state labels and vice versa (for example, if a package is embedded in your project, then Unity automatically assumes it is a custom package in development, so only the **custom** label appears in the details view).

The Package Manager window displays the following values:

**Label** | **Type** | **Meaning**  
---|---|---  
Released | state | Unity officially released this package and fully supports it. The Quality Assurance team has tested this version of the package and guarantees that it works with a specific version of the Editor and all other packages released for that Editor version.  
Release Candidate | state | This version of the package is on track to be fully “released” within the next TECH stage of the current release cycle.  
Pre-Release | state | This version of the package is at an earlier stage of development, but Unity guarantees to release it by the end of the LTS release cycle. It might not have complete documentation, or it might not be fully validated by either the development team or Unity’s Quality Assurance team.  
Experimental | state | These packages are either new packages or contain experimental modifications. Unity does not support Experimental packages because they are in the early stages of development.  
Custom | state  
source | This package is embedded in your project. Most custom package developers start by embedding a new package in their project, which is why the “Custom” label appears.  
local | source | The Package Manager installed this package from a folder or tarball file on your local disk external to your Unity project folder.  
git | source | The Package Manager installed this package in your project directly from a Git repository.  
asset store | asset | This is an asset package that you purchased or downloaded from the Asset Store.  
deprecated | asset | This package is no longer available on the Asset Store unless you have downloaded or purchased it previously. That is, it is no longer discoverable by new customers.  
  
**Note** : This label applies only to Asset Store packages. Unity packages that have been deprecated never appear in the Unity Editor.  
  
## Additional resources

  * Package types