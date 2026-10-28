---
title: "Disable a built-in package"
category: "General"
source_file: "upm-ui-disable.html"
doc_type: "manual"
---

# Disable a built-in package

You can disable a **Built-in package** if you don’t need some modules and you want to save resources. However, when you disable a built-in package, the corresponding Unity functionality is no longer available. This results in the following:

  * If you use a Scripting API implemented by a disabled package, you get compiler errors.
  * Components implemented by the disabled built-in package are also disabled, which means you cannot add them to any GameObjects. If you have a **GameObject** that already has one of these components, Unity ignores them in Play mode. You can see them in the **Inspector** that already has one of these components, Unity ignores them in Play mode. You can see them in the **Inspector** window but they are greyed out to indicate that they are not available.
  * When building a game, Unity strips all disabled components. For build targets which support engine code stripping (like WebGL, iOS, and Android), Unity doesn’t add any code from a disabled built-in package.

To disable a built-in package:

  1. Open the Package Manager window and select **Built-in packages** from the Packages drop-down menu.

Switch the list context to Built-in packages
  2. Select the built-in package you want to disable. Its information appears in the details view.

  3. Click the **Disable** button. 

**Disable** button in the corner of the details view

When the progress bar finishes, the check mark no longer appears next to the built-in package and the **Disable** button becomes an **Enable** button.

  4. If you want to re-enable a disabled built-in package, click the **Enable** button.

**Note** : You can disable multiple built-in packages with one click by using the multiple select feature. For more information, see Perform an action on multiple packages or feature sets.