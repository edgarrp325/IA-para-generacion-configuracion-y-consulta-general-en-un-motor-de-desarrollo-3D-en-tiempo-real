---
title: "Creating an AnimatorController"
category: "General"
source_file: "AnimatorControllerCreation.html"
doc_type: "manual"
---

# Creating an AnimatorController

### Animator Controller

You can view and set up character behavior from the **Animator Controller** view (Menu: **Window** > **Animation** > **Animator**).

The various ways an Animator Controller can be created:

  * From the **Project View** by selecting ‘**Create > Animator Controller**’.

  * By right-clicking in the Project View and selecting ‘**Create > Animator Controller**’.

  * From the Assets menu by selecting ‘**Assets > Create > Animator Controller**’.

This creates a `.controller` asset on disk. In the **Project Browser** window the icon will look like:

Animator Controller asset on disk

### Animator Window

After the **state machine** setup has been made, you can drop the controller onto the **Animator component** setup has been made, you can drop the controller onto the **Animator component** of any character with an **Avatar** of any character with an **Avatar** in the **Hierarchy View**. 

The Animator Controller window contains: 

  * The **Animation Layer Widget** (top-left corner, see Animation Layers)
  * The **Event Parameters Widget** (top-left, see Animation Parameters)
  * The visualization of the State Machine itself.

The Animator Controller Window

Note that the Animator Controller Window will always display the state machine from the most recently selected `.controller` asset, regardless of what **scene** is currently loaded.