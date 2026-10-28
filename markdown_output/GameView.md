---
title: "The Game view"
category: "General"
source_file: "GameView.html"
doc_type: "manual"
---

# The Game view

The Game view is rendered from the Camera(s) in your application. It shows how the final, built application looks. You need to use one or more **Cameras** to control what the player sees when they are using your application. For more information about Cameras, see the Camera Component page.

Unity lets you switch between the Game view and the Simulator view. The Simulator view shows how your built application looks on a mobile device.

## Play mode

The Play mode lets you run your project and see how it works as it would in a built application. Use the buttons in the **Toolbar** to control the Play mode. In Play mode, any changes you make are temporary, and are reset when you exit Play mode. When you enter the Play mode, Unity darkens parts of the interface outside the Game view.

## Using the Simulator view

Use the Simulator view to preview how your built application looks on a mobile device. To switch between Game and Simulator views, in the **Game/Simulator** tab, select the appropriate option from the **Game/Simulator** menu. 

Alternatively, you can go to **Window > General**, and select **Game** or **Device Simulator** from the menu to open the required window. If there are no instances of Game or Simulator windows open, by default they’ll open as a floating window. However, if one of the windows is already open somewhere in the interface, then trying to open it from the menu will bring it into focus.

## Game view Control Bar

**Button** | **Function**  
---|---  
**Game/Simulator** | Use this menu to enable the **Game** or **Simulator** view.  
**Display** | If you have multiple Cameras in the **Scene** , select the appropriate option to switch between them. By default, this is set to **Display 1**. You can assign Displays to Cameras in the Camera module, under **Target Display**.  
**Aspect ratio** | Select from the available values to test how your game looks on monitors with different aspect ratios. By default, this is set to **Free Aspect**.  
| **Low Resolution Aspect Ratios** | Enable **Low Resolution Aspect Ratios** to emulate the **pixel** density of older displays, which reduces the resolution of the Game view when an aspect ratio is selected. It is always enabled when the Game view is on a non-Retina display.  
**Scale slider** | Scroll right to zoom in and examine areas of the Game screen in more detail. This slider lets you zoom out to see the entire screen where the device resolution is higher than the Game view window size. You can also use the scroll wheel and middle mouse button to do this while the application is stopped or paused.  
**Play Mode behavior** | This section describes the play mode behavior based on your selection below.  
| **Focused** | Enable Focused to shift focus on the selected Game view while the Editor is in Play mode.   
Only one Game view can be in focus when you enter the Play mode. Using Maximized mode implies focus on the Maximized Game view. Enabling Focused on a Game view disables it on other Game views.  
| **VSync (Game view only)** | Enable **VSync (Game view only)** to allow syncing, which is useful when recording a video, for example. Unity attempts to render the Game view at the monitor refresh rate, though this is not guaranteed. When this option is enabled, it is still useful to maximize the Game view in Play mode to hide other views and reduce the number of views that Unity renders.  
**Enter Play Mode:** | Choose from the options below to determine the settings for the Editor when it enters the Play mode.  
| **Normally** | Select this to view the Game view without forcing focus or maximizing any views to full screen.  
| **Maximized** | When this option is selected, Unity runs the Play mode with the Game view maximized to 100% of the Editor window.  
**Mute audio** | Click to enable: use this to mute any in-application audio when you enter the Play mode.  
**Unity Shortcuts** | Disable Editor keyboard shortcuts from triggering during Play mode when the Game view window is in focus. Shortcuts still trigger when the focus is on any other part of the Editor.  
**Stats** | Click this to show or hide the Statistics overlay, which contains Rendering Statistics about your application’s audio and graphics. The overlay lets you monitor the performance of your application while in Play mode.  
**Gizmos** | Click this to show or hide the visibility of Gizmos. To only show certain types of Gizmos in the Play mode, from the **Gizmos** menu, only enable the Gizmo types you want to see.  
  
## Gizmos menu

The Gizmos menu contains options for how Unity displays gizmos for **GameObjects** and other items in the **Scene view** and other items in the **Scene view** and Game view. This menu is available in both the Scene view and the Game view. For more information see Gizmos Menu.

## Advanced options

Right-click the **Game** tab to display advanced Game view options.

**Warn if No Cameras Rendering** : This option is enabled by default. It causes Unity to display a warning if no Cameras are rendering to the screen; e.g., for diagnosing problems such as accidentally deleting or disabling a Camera. Leave this enabled unless you are intentionally not using Cameras to render your application.

**Clear Every Frame in Edit Mode** : This option is enabled by default. It causes Unity to clear the Game view from every frame when your application is not playing. This prevents smearing effects while you are configuring your application. Leave this enabled unless you are depending on the previous frame’s contents when not in the Play mode.

* * *

  * **Low Resolution Aspect Ratios** Game view option available on Windows from 2018.2 NewIn20182