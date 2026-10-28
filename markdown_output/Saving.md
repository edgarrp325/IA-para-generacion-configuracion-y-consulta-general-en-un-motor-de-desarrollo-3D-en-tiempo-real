---
title: "Save your work"
category: "General"
source_file: "Saving.html"
doc_type: "manual"
---

# Save your work

Unity categorizes most saved information into either scene changes or project-wide changes.

  * To save all current scene and project-wide changes, go to **File** > **Save** (or **Save as**).
  * To save Project-wide changes, but not Scene changes, go to **File** > **Save Project**.

**Note** : If you edit in Prefab Mode, saving through **File** > **Save** only saves changes to the open Prefab. Exit the Prefab Mode to save wider changes.

Unity saves some information automatically while you work in the Editor. See Automatic saves for more details.

## Scene changes 

Scene changes include modifications to **GameObjects** in the **Scene** in the **Scene**. For example:

  * If you add, move, or delete a GameObject.
  * If you change a GameObject’s parameters in the **Inspector** window.

## Project-wide changes 

Project-wide changes in Unity apply to your entire project rather than a specific scene. For example, if you create a temporary scene to test changes, you can save the project and not the scene.

Project-wide changes include:

  * ****Project Settings**** : When you save your project, Unity saves changes to the Project Settings in the `ProjectSettings` folder, in these files:

    * **Input** : `InputManager.asset`
    * **Tags And Layers** : `TagManager.asset`
    * **Audio** : `AudioManager.asset`
    * **Time** : `TimeManager.asset`
    * **Player** : `ProjectSettings.asset`
    * **Physics** : `DynamicsManager.asset`
    * **Physics 2D** : `Physics2DSettings.asset`
    * **Quality** : `QualitySettings.asset`
    * **Graphics** : `GraphicsSettings.asset`
    * **Network** : `NetworkManager.asset`
    * **Editor** : `EditorUserSettings.asset`
  * **Build Settings** : Unity saves changes to the Build Settings in the `Library` folder as `EditorBuildSettings.asset`.

  * **Changed assets** : When you save project-wide settings, Unity saves any unsaved assets.

**Note:** Some asset types have an **Apply** button in the Inspector. Unity will not save these unless you select **Apply**.

  * **Dirty assets** : Unity saves **Dirty** assets, which are files on your disk that are modified in the software but not saved yet. You can use custom Editors and scripts

    * Use the SerializedObject class with SerializedProperties.
    * Use the Undo class to record modifications.
    * Use SetDirty.

## Automatic saves 

Unity automatically saves the following changes to your disk:

  * **New assets** : Unity automatically saves new assets when you create them but you need to save later changes.
  * **Asset Import Settings** : For the changes to take effect with most assets, you need to select **Apply** in the Inspector window. Unity saves the changes when you select **Apply**.
  * **Baked data** : When you have data that is set to Baked in your project, Unity saves this data after the bake finishes. This includes: 
    * Baked Lighting data
    * Baked navigation data
    * Baked **occlusion culling** data
  * **Script execution order changes** : After you select **Apply** , Unity saves this data into each script’s `.meta` file.