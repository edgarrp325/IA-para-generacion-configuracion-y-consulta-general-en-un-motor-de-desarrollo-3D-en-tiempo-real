---
title: "Install a UPM package from a local tarball file"
category: "General"
source_file: "upm-ui-tarball.html"
doc_type: "manual"
---

# Install a UPM package from a local tarball file

The Package Manager can load a **UPM package** from a tarball file stored locally. This is for advanced scenarios where you break your package publishing workflow into parts and your users can use the intermediate product of one of those parts.

For example, if you have set up continuous integration (CI) on your custom package repository, you can use the npm pack or Unity Package Manager’s Pack API to create a Gzip tarball file from a package folder. In that case, you likely want to test the tarball file before you publish it to a custom registry.

To load a UPM package from a local tarball file:

  1. Open the Package Manager window, if it’s not already open.

  2. Click the **add** button in the status bar. The options for adding packages appear.

Add package from tarball button
  3. Select **Add package from tarball** from the add menu to bring up a file browser.

  4. Navigate to the folder where you saved your tarball.

**Note** : The Package Manager only recognizes tarballs with the _.tgz_ extension.

  5. Double-click the tarball file in the file browser.

The file browser closes, and the package now appears in the package list with the  label.

## Additional resources

  * Package types
  * Add and remove UPM packages or feature sets
  * Add and remove asset packages