---
title: "Package Manifest window"
category: "General"
source_file: "class-PackageManifestImporter.html"
doc_type: "manual"
---

# Package Manifest window

When you click on the **package manifest** file in the Project view, the Package Manifest window opens:

The Package Manifest window for the Cinemachine package. From top to bottom, the window displays the package name and controls (A), package information (B), a brief description (C), and a list of dependencies (D). 

**(A)** Click the **Open** button to load this package manifest in your default code editor, such as Visual Studio. Click the **View in Package Manager** button to open the Package Manager window and load this package in the details view. If you want to choose a different importer, click the **Importer** drop-down menu and select the package importer you want to use.

**(B)** The Information section contains details about this specific package version.

**(C)** Use the **Brief Description** text box to specify the text that you want to appear in the details view of the Package Manager window. For more information, see the documentation for the description property.

**(D)** Use the Dependencies section to manage the list of packages that this package depends on.

**(E)** Click the **Revert** button to discard any changes you’ve made to the manifest. Click the **Apply** button to save any changes you’ve made to the manifest.

## Information section

**Property** | **Description**  
---|---  
**Name** | The official name for this package. For Unity packages, this is the short name (the official name without the `com.unity.` string at the beginning.)  
**Organization name** | The identifier of the Unity Organization that created this package.  
**Display name** | The user-facing name on display in the **Project window** and the Package Manager window. For more information, refer to the documentation for the displayName property.  
**Version** | The package version number. For more information, refer to the documentation for the version property.  
**Minimal Unity version** | Enable this option to specify the lowest Unity version this package is compatible with. When you enable this option, the **Major** , **Minor** , and **Release** properties appear.   
  
If this package is compatible with all Unity versions, clear this checkbox and remove the **Major** , **Minor** , and **Release** properties.   
  
For more information, refer to the documentation for the unity property.  
**Major** | Specify the MAJOR portion of the minimal Unity version. For more information, refer to the documentation for the unity property.  
**Minor** | Specify the MINOR portion of the minimal Unity version. For more information, refer to the documentation for the unity property.  
**Release** | Specify the UPDATE and RELEASE portion of the minimal Unity version. For more information, refer to the documentation for the unityRelease property.  
  
## Dependencies section

Lists the other packages that are dependencies for this package. Each entry consists of the official package name (for example, `com.unity.probuilder`) and its version number.

To add a new dependency:

  1. Select the **Add** (**+**) button. A new row appears in the list.
  2. Enter the package name on the left and the version on the right. For more information, refer to the documentation for the dependencies property.

To remove a dependency:

  1. Click the selector  to the left of the package you want to remove.
  2. Select the **Remove** (**−**) button. The row disappears from the list.

PackageManifestImporter