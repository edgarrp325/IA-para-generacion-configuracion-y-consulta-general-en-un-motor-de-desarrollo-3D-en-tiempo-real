---
title: "Creating Prefabs"
category: "General"
source_file: "CreatingPrefabs.html"
doc_type: "manual"
---

# Creating Prefabs

In Unity’s **Prefab** system, **Prefab Assets** act as templates. You create Prefab Assets in the Editor, and they are saved as an Asset in the **Project window** system, **Prefab Assets** act as templates. You create Prefab Assets in the Editor, and they are saved as an Asset in the **Project window**. From **Prefab Assets** , you can create any number of **Prefab instances**. Prefab instances can either be created in the editor and saved as part of your **Scenes**. From **Prefab Assets** , you can create any number of **Prefab instances**. Prefab instances can either be created in the editor and saved as part of your **Scenes** , or instantiated at runtime.

## Creating Prefab Assets

To create a Prefab Asset, drag a **GameObject** from the Hierarchy window into the Project window. The GameObject, and all its components and child GameObjects, becomes a new Asset in your Project window. Prefabs Assets in the Project window are shown with a thumbnail view of the GameObject, or the blue cube Prefab icon, depending on how you have set up your Project window.

Two prefabs (“FatBlob” and “Key”) shown in the Project window in two-column view (left) and one-column view (right)

This process of creating the Prefab Asset also turns the original GameObject into a Prefab instance. It is now an instance of the newly created Prefab Asset. Prefab instances are shown in the Hierarchy in blue text, and the root GameObject of the Prefab is shown with the blue cube Prefab icon, instead of the red, green and blue GameObject icon.

A Prefab instance (Key) in the scene

## Creating multiple Prefab Assets

To create multiple Prefab Assets at once, drag multiple GameObjects from the Hierarchy window into the Project window. This functionality is the same as in the above paragraph.

If you drag multiple GameObjects that are not already Prefabs into the Project window, Unity creates new original Prefab Assets for each one without any additional steps. 

If any of the GameObjects you drag into the Project Window are existing Prefab variants or Model Variants, Unity displays a dialog box which asks you to confirm whether you want to create new Prefab Assets or new variants from the GameObjects. The content of this dialog box changes depending on the number and type of GameObjects you drag into the Project window.

## Creating Prefab instances

You can create instances of the Prefab Asset in the Editor by dragging the Prefab Asset from the Project view to the Hierarchy or **Scene view**.

Dragging a Prefab “Key” into the Scene

You can also create instances of Prefabs at runtime using scripting. For more information, see Instantiating Prefabs.

## Replacing existing prefabs

You can replace a Prefab by dragging a new GameObject from the Hierarchy window and dropping it on top of an existing Prefab asset in the Project window.

If you are replacing an existing Prefab, Unity tries to preserve references to the Prefab itself and the individual parts of the Prefab such as child GameObjects and Components. To do this, it matches the names of GameObjects between the new Prefab and the existing Prefab that you are replacing.

**Note:** _Because this matching is done by name only, if there are multiple GameObjects with the same name in the Prefab’s hierarchy, it is not possible to predict which will be matched. Therefore if you need to ensure your references are preserved when saving over an existing prefab, you must ensure all GameObjects within the Prefab have unique names._

**Also note:** _You may encounter a similar problem in the case of preserving references to existing Components when you save over an existing Prefab, if a single GameObject within the Prefab has more than one of the same Component type attached. In this case it is not possible to predict which of them will be matched to the existing references._

* * *

  * 2018–07–31 Page published 

  * Nested Prefabs and Prefab Variants added in 2018.3