---
title: "Pick and select GameObjects"
category: "General"
source_file: "ScenePicking.html"
doc_type: "manual"
---

# Pick and select GameObjects

You can select a single **GameObject** in the Scene view in the Scene view or from the Hierarchy window. You can also select more than one GameObject at a time.

Unity highlights selected GameObjects and their children in the Scene view. By default, the selection outline color is orange, and the child outline color is blue. You can also choose to highlight selected GameObjects’ wireframes in a different color. You can change all of these outline highlight colors from the Preferences window. To open the **Preferences** window, go to **Edit > Preferences** (macOS: **Unity > Settings**) in the main menu. 

For more information about the outline and wireframe selection visualizations, see the documentation on the Gizmos menu. 

## Select GameObjects

To select a single GameObject, choose one of these methods:

  * Click on it in the Scene view. If you repeatedly click on the shared space between overlapping GameObjects, the selection cycles between them.
  * Click its name in the Hierarchy window.

To select or deselect multiple GameObjects choose one of these methods:

  * Drag a rectangle around multiple GameObjects. Unity selects anything that falls inside this bounding box.

  * Hold the **Shift** key and click GameObjects in the **Scene**. You can also use the **Ctrl** (Windows) or **Command** (macOS) key to add or remove GameObjects from the selection.

**Note:** When a feature in the Editor needs a single selected GameObject to perform an action, it looks for an “active” object. For example, Unity has to decide which GameObject to use as the pivot for transform tools while in Pivot mode. By default, Unity considers the last GameObject you select to be the “active” object. When you Shift+click on one of several selected GameObjects, you change which one of them is active. If a GameObject is active in the Scene view, Unity doesn’t display any visible cues that it’s active. However, you can see which GameObject is active in the Scene view when you repeatedly Shift+click in Pivot mode with multiple objects selected.

However, if you are working with a large Scene containing a lot of Scene items (such as GameObjects, Terrain objects, Cameras, and Lights), selecting multiple objects can be very tricky. To help you select only the items you want, you can block some objects from being picked, using the Scene picking controls.

## Scene picking controls

You can toggle Scene picking controls on and off to mark which items are pickable when you work in the Editor. By default, all items are pickable, but you can choose which Scene items Unity skips adding to the selection when you click on them. For example, if you are working in a large Scene with over 10,000 objects, you can temporarily block specific GameObjects from being selected to prevent accidental editing.

Once you mark an item as unpickable, Unity continues to render them even though you can no longer select or edit them in the Scene view. The pickability state persists only in the Editor and only for the user in the Project where it was set. Changing the pick state does not “dirty” the Scene (that is, count as a modification).

Scene picking controls are very similar to the Scene visibility controls.

### Toggle pickability

You control Scene pickability for individual GameObjects from the Hierarchy window.

Every GameObject has a Scene pickability icon/toggle

To toggle Scene pickability:

  * Click a GameObject’s pickability icon in the Hierarchy window to toggle between enabling and disabling picking the GameObject and its children.

Toggling pickability for a GameObject and its children affects all child GameObjects, from the “target” GameObject all the way down to the bottom of the hierarchy.

  * For multiple GameObjects, press **L**.

  * **Alt** \+ Click a GameObject’s pickability icon in the Hierarchy window to toggle between enabling and disabling picking the GameObject only.

Toggling pickability for a single GameObject does not affect its children. They retain whatever pickability status they had previously.

Because you can toggle pickability for a whole branch or a single GameObject, you can end up with GameObjects that are pickable, but have children or parents that you cannot pick. To help you track what’s going on, the pickability icon changes to indicate each GameObject’s status.

Unity only selects pickable items when you draw a selection bounding box in the Scene view |  |   
---|---|---  
**A** |  | You can pick the GameObject, but you cannot pick some of its children.  
**B** |  | You cannot pick the GameObject, but you can pick some of its children.  
**C** |  | You cannot pick the GameObject nor its children.  
**D** |  | You can pick the GameObject and its children. This icon only appears when you hover over the GameObject.  
  
Any Scene picking changes you make in the Hierarchy window are persistent. Unity re-applies them whenever you use **Select All** or **Deselect All** , close and re-open the Scene, and so on.

## Additional resources

  * Position GameObjects
  * Scene visibility
  * The Hierarchy window

* * *