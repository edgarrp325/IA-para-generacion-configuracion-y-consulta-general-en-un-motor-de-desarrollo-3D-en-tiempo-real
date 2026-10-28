---
title: "Install a UPM package from a Git URL"
category: "General"
source_file: "upm-ui-giturl.html"
doc_type: "manual"
---

# Install a UPM package from a Git URL

The Package Manager can load a **UPM package** from a Git repository on a remote server.

## Prerequisites

  * Install the Git client (minimum version 2.14.0) on your computer.
  * On Windows, add the Git executable path to the `PATH` system environment variable.
  * If the target repository tracks files with Git LFS, install the Git LFS client on your computer.
  * Read the information about using Git dependencies in your project.

## Procedure

To load a UPM package from a Git URL:

  1. Open the **add** menu in the Package Manager’s toolbar.

  2. The options for adding packages appear.

Add package from git URL button
  3. Select **Add package from git URL** from the add menu. A text box and an **Add** button appear.

  4. Enter a valid Git URL in the text box. For information about how to construct a valid Git URL, refer to Git URLs and extended syntax. Examples of valid Git URLs include: 
     * `https://github.example.com/myuser/myrepo.git` (if your package is in the root of the repository).
     * `https://github.example.com/myuser/myrepo.git?path=/subfolder` (if your package is in a subfolder within the repository).
  5. Select **Add**.

If Unity was able to install the package successfully, the package now appears in the package list with the  label. If Unity wasn’t able to install the package, the Unity Console displays an error message, such as:

  * No ‘git’ executable was found
  * git-lfs: command not found
  * Repository not found
  * Could not read Username: terminal prompts disabled

Click on an error message link to get some help for it on the Troubleshooting page.

**Tip** : If you want to check for updates and update your Git dependency to the latest version from the repository, click **Update**. You can also use the Add package from git URL menu item to update your Git dependency. For information on Git dependencies, see Locked Git dependencies.

## Additional resources

  * Package types
  * Add and remove UPM packages or feature sets
  * Add and remove asset packages