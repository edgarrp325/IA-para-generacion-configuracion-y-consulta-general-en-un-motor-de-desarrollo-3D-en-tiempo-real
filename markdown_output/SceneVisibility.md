---
title: "Scene visibility"
category: "General"
source_file: "SceneVisibility.html"
doc_type: "manual"
---

# Scene visibility

Unity’s **scene** visibility controls allow you to quickly hide and display **GameObjects** visibility controls allow you to quickly hide and display **GameObjects** in the Scene view in the Scene view without changing their in-game visibility. This is useful for working with large or complex scenes where it can be difficult to view and select specific GameObjects.

Selected GameObjects are highlighted in blue Changing the Scene visibility settings hides the selected GameObjects in the scene view

Using visibility options is safer than deactivating GameObjects because visibility options only affect the Scene view. This means you can’t accidentally remove GameObjects from the rendered scene, or trigger unnecessary bake jobs for lighting, occlusion, and other systems.

The Editor saves Scene visibility settings to a file called `SceneVisibilityState.asset` in the Project’s `Library` folder. The scene reads from this file and updates it automatically whenever you change the visibility settings. This makes it possible for your settings to persist from one session to the next. Because source control setups for Unity typically ignore the `Library` folder, changing visibility settings should not create source control conflicts.

You can set visibility on specific scene items in the Hierarchy window, but if the scene-wide visibility setting is disabled, items marked as hidden might still appear in the Scene view. To change this setting, you can toggle Scene visibility on the Toolbar.

To control the scene visibility from script, refer to SceneVisibilityManager. 

Scene visibility controls are very similar to the Scene picking controls.

## Set Scene visibility for GameObjects and their children

You control Scene visibility for individual GameObjects from the Hierarchy window.

Every GameObject has a Scene visibility icon/toggle

To toggle between hiding and showing the GameObject and its children:

  * Click a GameObject’s visibility icon in the Hierarchy window, or press **H**.
  * For multiple GameObjects, press **H**.

Toggling visibility for an object and its children affects all child objects, from the “target” object all the way down to the bottom of the hierarchy.

  * **Alt** \+ Click a GameObject’s visibility icon in the Hierarchy window to toggle between hiding and showing the GameObject only.

Toggling visibility for a single object does not affect its children. They retain whatever visibility status they had previously.

**Tip** : You can also click the Scene’s visibility icon to toggle between hiding and showing items marked hidden in the Scene.

Because you can toggle visibility for a whole branch or a single GameObject, you can end up with GameObjects that are visible, but have hidden children or parents. To help you track what’s going on, the visibility icon changes to indicate each GameObject’s status.  
  
---  
**A** |  | The GameObject is visible, but some of its children are hidden.  
**B** |  | The GameObject is hidden, but some of its children are visible.  
**C** |  | The GameObject and its children are visible. This icon only appears when you hover over the GameObject.  
**D** |  | The GameObject and its children are hidden.  
  
Scene visibility changes you make in the Hierarchy window are persistent. Unity re-applies them whenever you toggle scene visibility off and on again in the Scene view, close and re-open the Scene, and so on.

## Turn Scene visibility on and off

The Scene visibility switch in the Scene view View Options Overlay **toolbar**

The Scene visibility icon in the View Options Overlay toolbar

Turning Scene visibility off essentially mutes the Scene visibility settings you set in the Hierarchy window, but doesn’t delete or change them. All hidden GameObjects are temporarily visible.

Turning Scene visibility back on re-applies the visibility settings set in the Hierarchy window.

## Isolate selected GameObjects

The Isolation view temporarily overrides the Scene visibility settings so that only the selected GameObjects are visible, and everything else is hidden.

Isolation view overrides Scene visibility settings so only the selection and its children (A) are visible.  
Clicking the Exit button (B) reverts to the previous Scene visibility settings.

To enter the Isolation view:

  * Press **Shift + H**.

This isolates all selected GameObjects and their children. Isolating hidden GameObjects makes them visible until you exit the Isolation view.

While in the Isolation view, you can continue to change Scene visibility settings, but any changes you make are lost on exit.

To exit the Isolation view:

  * Press **Shift + H** again, or click the **Exit** button in the Scene view.

Exiting the Isolation view reverts back to your original Scene visibility settings.

## Additional resources

  * Hierarchy window
  * Scene view
  * Scene picking
  * SceneVisibilityManager