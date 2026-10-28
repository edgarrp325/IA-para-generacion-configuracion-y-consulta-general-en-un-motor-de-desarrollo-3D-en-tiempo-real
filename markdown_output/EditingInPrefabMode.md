---
title: "Editing a Prefab in Prefab Mode"
category: "General"
source_file: "EditingInPrefabMode.html"
doc_type: "manual"
---

# Editing a Prefab in Prefab Mode

To edit a **Prefab** Asset, open it in **Prefab Mode**. Prefab Mode allows you to view and edit the contents of the Prefab Asset separately from any other **GameObjects** Asset, open it in **Prefab Mode**. Prefab Mode allows you to view and edit the contents of the Prefab Asset separately from any other **GameObjects** in your **Scene** in your **Scene**. Changes that you make in Prefab Mode affect all instances of that Prefab.

## Entering and exiting Prefab Mode

You can edit a Prefab Asset **in isolation** , or **in context**.

Left: editing a Prefab in isolation. Right: editing a Prefab in context.

  * **In isolation:** When you edit a Prefab in isolation, Unity hides the rest of your current working Scene, and you only see the GameObjects that relate to the Prefab itself (plus, optionally, a pre-set **editing environment** \- see below).

  * **In context:** When you edit a Prefab in context, the rest of your current working Scene remains visible, but locked for editing. 

### Editing in isolation

You can begin to edit a Prefab in Prefab Mode in several ways. To open a Prefab Asset and edit it **in isolation** you can do it in the following ways:

  * Double-click the Prefab Asset in the Project window
  * Select a Prefab Asset in the **Project window** and click the **Open Prefab** button in the ****Inspector** and click the **Open Prefab** button in the ****Inspector**** window**

A Prefab Asset selected in the Project window (left), and the Open Prefab button visible in the inspector (right)

When you enter Prefab Mode in isolation, Unity only shows the contents of that Prefab in the ****Scene view**** and the Hierarchy window. In the following image, the root of the Prefab is a regular **GameObject** \- it doesn’t have the blue Prefab instance icon.

The Scene view and Hierarchy, with Prefab Mode in isolation

In Prefab Mode, the **Scene** view displays a breadcrumb bar at the top. The rightmost entry is the currently open Prefab. Use the breadcrumb bar to navigate back to the main Scenes or other Prefab Assets that you might have opened.

The breadcrumb bar at the top of the Scene view, visible when in Prefab Mode

The **Hierarchy** window displays a Prefab header bar at the top which shows the currently open Prefab. You can use the back arrow in the header bar to navigate back one step, which is equivalent to clicking the previous breadcrumb in the breadcrumb bar in the Scene view.

The back arrow in the header bar of the Hierarchy window, visible when in Prefab Mode

### Editing in context

Alternatively, you can open a Prefab Asset **in Context** via an instance of that Prefab. Ways of doing that include:

  * Select a Prefab instance in the Hierarchy window and click the **Open** button in the Inspector window
  * Select a Prefab instance in the Hierarchy window and press **P** on the keyboard. This is the default keyboard binding
  * Use the **arrow button** next to the Prefab instance in the Hierarchy window

The Open button in the Inspector when a Prefab Instance is selected The arrow button next to a Prefab in the Hierarchy window

By default, Unity displays the visual representation of the context in gray scale to visually distinguish it from the Prefab contents you edit. However, you can use the **Context:** control in the Prefab bar to set it to any of the following states:

  * **Normal** \- Shows the context with its normal colors
  * **Gray** \- Shows the context in gray scale
  * **Hidden** \- Hides the context entirely so only the Prefab content is visible

The Prefab Mode controls in the Prefab bar in at the top of the Scene view, including the Context control and the Show Overrides toggle

You cannot select the GameObjects that are part of the context, nor do they show in the Hierarchy. This is so you can focus on editing your Prefab without accidentally selecting other unrelated GameObjects, and without having a cluttered Hierarchy window. However, when you move GameObjects around that are part of the Prefab contents, you can use the snapping features in Unity to snap to GameObjects in the context, provided the context is not set to **Hidden**.

In Prefab Mode in Context, Unity displays the Prefab contents at a position that matches that of the Prefab instance it was opened through. This means that you might preview the **root Transform** of the Prefab contents with different position and rotation values than the Prefab Asset actually has. 

You cannot edit these values in Prefab Mode in Context. If you need to edit them, you can either open the Prefab in isolation, or select the Prefab Asset in the Project window and edit the values in the Inspector.

Apart from the root Transform properties, you can also override other properties of a Prefab instance, which might drastically change its appearance compared to the Prefab Asset it’s an instance of. To preview these overridden values from the Prefab instance, while in Prefab Mode in Context enable the **Show Overrides** toggle in the Prefab bar. While this setting is enabled, any properties that you override on the Prefab instance are previewed the same way on the Prefab contexts and you cannot edit them. To edit those properties, disable the **Show Overrides** toggle again.

## Auto Save

Prefab Mode has an **Auto Save** setting in the top right corner of the Scene view. When it is enabled, Unity automatically saves any changes that you make to a Prefab to the Prefab Asset. **Auto Save** is on by default.

The Auto Save toggle in the upper right corner of the Scene view in Prefab Mode

If you want to make changes without automatically saving those changes to the Preset Asset, disable the **Auto Save** checkbox. In this case, Unity asks you if you want to save unsaved changes or not when you exit Prefab Mode for the current Prefab. If editing a Prefab in Prefab Mode seems slow, turning off **Auto Save** might help.

## Changing between isolation or in context mode

When you open Prefab Mode via a Prefab Asset, Unity displays the contents of the Prefab in isolation. However, when you open Prefab Mode via a Prefab instance in the Hierarchy window, this opens **Prefab Mode in Context**. 

When you open Prefab Mode this way, you can see the context of the Prefab instance in the Scene view even though you are not editing the instance but rather the Prefab Asset itself. For example, if you open Prefab Mode in Context via a Prefab instance in a Scene, then you can see the surroundings in that Scene while you edit the Prefab. The Prefab is also shown with the same lighting conditions as in the Scene.

A Prefab opened in Prefab Mode in Context, with the surrounding context displayed in gray scale

If you have a Prefab instance that you do not want to open in context, but want to open in isolation, hold down the **Alt** key and click the **Open** button or the arrow button to open Prefab Mode. You can also set up a custom shortcut in the **Shortcuts** window for the command **Stage > Edit Prefab in Isolation**.

## Undo

When you make changes to a Prefab Asset while in Prefab Mode, you can only undo those changes while still in Prefab Mode. Once you exit Prefab Mode for a given Prefab Asset, your edits relating to that Prefab Asset are no longer available in the undo history.

## Editing Environment

You can assign a Scene as an **editing environment** to be used with Prefab Mode in Isolation. This allows you to edit your Prefab against a backdrop of your choosing rather than an empty Scene. This can be useful to see how your Prefab looks against a specific scenery of your choice. Unity only uses this editing environment when you open Prefab Mode in Isolation.

You cannot select the GameObjects in the Scene that you assign as the editing environment when in Prefab Mode, nor do they show in the Hierarchy. This is so you can focus on editing your Prefab without accidentally selecting other unrelated GameObjects, and without having a cluttered Hierarchy window.

To set a Scene as the editing environment, open the Editor window (top menu: **Edit > Project Settings**, then select the **Editor** category) and go to the **Prefab Editing Environment** section. Use the **Regular Environment** setting for “non-UI” Prefabs, and the **UI Environment** setting for UI Prefabs. UI Prefabs are those which have a Rect Transform component on the root, rather than a regular Transform component. “non-UI” Prefabs are those which have a regular Transform component.

Prefab editing environment settings in the Editor Project Settings