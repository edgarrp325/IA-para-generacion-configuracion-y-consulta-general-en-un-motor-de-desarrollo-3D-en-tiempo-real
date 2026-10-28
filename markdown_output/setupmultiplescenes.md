---
title: "Set up multiple scenes"
category: "General"
source_file: "setupmultiplescenes.html"
doc_type: "manual"
---

# Set up multiple scenes

You can add multiple scenes, edit how you view them, and change the **scene** settings. 

To create a new scene, see Creating, loading, and saving Scenes.

## Add scenes

To add a new scene to your project, do one of the following: 

  * Right click to open the menu of a scene asset in the **Project window** and select **Open Scene Additive**.
  * Drag one or more scenes from the Project window into the Hierarchy window.

## View scenes

The Hierarchy window displays all the scenes that are part of your project:

The Hierarchy window with multiple scenes added.

A: Scenes with unsaved changes have an asterisk by the scene name.  
B: The scene More menu allows you to perform actions on the scene.  
C: The scene divider (an inverted triangle) lets you collapse a scene and hide its contents from the Hierarchy to better manage multiple scenes. 

**Tip** : To add a scene to the Hierarchy window without loading it, press Alt (macOS: press Option) and drag the scene into the Hierarchy window. This lets you load the scene when it’s convenient for you.

## Loaded scene More menu (⋮)

You can interact with and edit a loaded scene in several ways. 

The More menu for a loaded scene. **Setting** | **Description**  
---|---  
**Set Active Scene** | Sets the scene as the target for new **GameObjects** created through **scripts** created through **scripts**. For more information, see SceneManager.SetActiveScene.  
**Save Scene** | Saves the scene that you selected.  
**Save Scene As** | Opens your file browser so you can choose where and how to save the scene.  
**Save All** | Saves all the scenes you have open in the Hierarchy window.  
**Unload Scene** | Hides the contents of the scene from the **Scene view** and the Hierarchy window. If you have unsaved changes, save them before you unload the scene to not lose any changes.  
**Remove Scene** | Removes the scene from the Hierarchy window.  
**Discard changes** | Undoes any changes that you haven’t saved.  
**Select Scene Asset** | Highlights the scene asset in the Project window.  
**Add New Scene** | Adds a new untitled scene below the scene you have selected.  
**GameObject** | Opens a dropdown menu of GameObjects that you can add to the scene you have selected.  
  
## Unloaded scene More menu (⋮)

You can interact with and edit an unloaded scene in fewer ways than you can a loaded scene. 

The More menu for an unloaded scene. **Setting** | **Description**  
---|---  
**Load Scene** | Displays the contents of the scene in the Hierarchy window and the Scene view, and allows you to edit them.  
**Remove Scene** | Removes the scene from the Hierarchy window.  
**Select Scene Asset** | Highlights the scene asset in the Project window.  
**Add New Scene** | Adds a new untitled scene below the scene you have selected.  
  
## Multiple scenes in Play mode

When you are in Play mode and have multiple scenes in the Hierarchy window, the Editor displays an additional scene called DontDestroyOnLoad. 

## Scene-specific settings

The following settings are specific to each scene:

  * RenderSettings and LightmapSettings (both found in the Lighting window).
  * Scene settings in the Occlusion Culling window.

Each scene manages its own settings, so only settings associated with that scene save to the scene file.

To change the settings of a specific scene, either open that specific scene and change the settings, or set the scene as the active scene then change the settings. Otherwise, if you have multiple scenes open, Unity uses the rendering settings from the active scene. 

When you switch to a new active scene in the Editor or at runtime, Unity replaces all previous settings with the settings from the new active scene.

## Additional resources

  * Creating, loading, and saving Scenes
  * Bake data in multiple scenes
  * Use scripts to edit multiple scenes