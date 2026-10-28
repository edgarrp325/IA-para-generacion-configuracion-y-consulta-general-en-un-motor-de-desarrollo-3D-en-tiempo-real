---
title: "Introduction to components"
category: "General"
source_file: "Components.html"
doc_type: "manual"
---

# Introduction to components

**Components** are the functional pieces of every **GameObject**. Components contain properties which you can edit to define the behavior of a GameObject. For more information on the relationship between components and GameObjects, see GameObjects.

To view a list of the components attached to a GameObject in the **Inspector** window, select a GameObject in either the Hierarchy window or the **Scene** window, select a GameObject in either the Hierarchy window or the **Scene** view.

You can attach many components to a GameObject, but every GameObject must have one and only one Transform component. This is because the Transform component dictates the GameObject’s location, rotation, and scale. To create an empty GameObject, select **GameObject** > **Create Empty**. When you select the new GameObject, the Inspector displays the Transform component with default values.

Empty GameObjects have a Transform component

A component must be in the same project as the GameObject you want to attach it to. A component can be specific to a package or created by a script. The Unity Editor can’t search for components from:

  * Other projects.
  * **Scripts** that are not attached to the project.
  * Packages that haven’t been added to the project.