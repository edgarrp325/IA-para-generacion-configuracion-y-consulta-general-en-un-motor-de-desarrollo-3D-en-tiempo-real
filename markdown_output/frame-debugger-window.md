---
title: "Frame Debugger window reference"
category: "General"
source_file: "frame-debugger-window.html"
doc_type: "manual"
---

# Frame Debugger window reference

The Frame Debugger window is the user interface for Unity’s Frame Debugger. It shows the rendering event information and controls the playback of the frame under construction.

The Frame Debugger window. **Label** | **Description**  
---|---  
|  **Enable/Disable** : Enables or disables the Frame Debugger.  
|  **Target selector** : Specifies the process to attach the Frame Debugger to. This is the Unity Editor by default but you can use this to attach the Frame Debugger to built applications. For more information, see Attach the Frame Debugger to a built project.  
|  **Event scrubber** : A slider you can use to move through the rendering events in the current frame linearly.  
|  **Previous event** : Selects the event previous to the one currently selected.  
|  **Next event** : Selects the event after the one currently selected.  
|  **Event Hierarchy** : Lists the sequence of rendering events that constitute the frame. For more information, see Event Hierarchy.  
|  **Event Information Panel** : Displays information about the event such as geometry details and the **shader** used for a draw call. For more information, see Event Information Panel.  
  
## Debug a frame

To debug a frame using the Frame Debugger:

  1. Open the Frame Debugger (menu: **Window** > **Analysis** > **Frame Debugger**).
  2. Use the target selector to select the process to attach the Frame Debugger to. If you want to debug a frame in the Unity Editor, set this to **Editor**. If you want to debug a frame in a built application, see Attach the Frame Debugger to a built project.
  3. Click **Enable**. When you do this, the Frame Debugger captures a frame. It populates the Event Hierarchy with the draw calls and other events that constitute the frame and renders the frame in the Game view.   
**Note** : If your application is running, the Frame Debugger pauses it.
  4. Select an event from the Event Hierarchy to view the **scene** as it appears up to and including that event. This also displays information about the event in the Event Information Panel. You can use the previous event and next event button, the arrow keys, or the event scrubber to move through the frame linearly. If you don’t know which event Unity renders the geometry you want to debug in, these navigation tools are useful to move through the events linearly until you find it.

When a draw call event corresponds to the geometry of a **GameObject** , Unity highlights that GameObject in the Hierarchy.

If an event renders into a RenderTexture, Unity displays the contents of that RenderTexture in the Game view and Frame Debugger window. This is useful for inspecting how various off-screen render targets build up. For example:

Viewing events that accumulate to produce the diffuse G-buffer during deferred rendering.

## Attach the Frame Debugger to a built project

You can change the Frame Debugger’s target process to attach the Frame Debugger to a built Unity Player. To be compatible with the Frame Debugger, the Unity Player must:

  * Use the ****Development Build**** Build Setting.
  * Support multithreaded rendering. Every Unity platform except **WebGL** supports this.
  * For desktop platforms, use the **Run In Background** Player Setting. Otherwise, when you focus the Frame Debugger window in the Unity Editor, the Unity Player loses focus and doesn’t reflect any rendering changes.

If the Unity Player fulfills the above requirements, when you next debug a frame, you can attach the Frame Debugger to the Unity Player.