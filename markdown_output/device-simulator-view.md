---
title: "The Simulator view"
category: "General"
source_file: "device-simulator-view.html"
doc_type: "manual"
---

# The Simulator view

The Simulator view displays your application on a simulated mobile device. Use it to see how your application appears with the screen shape, resolution, and orientation of that device.

A screenshot of the Simulator view

## Using the Simulator view

To open the Simulator view, do one of the following:

  * In the Game view, in the top left corner, use the drop-down menu to switch between the Game view and the Simulator view.
  * In the menu: **Window** > **General** > **Device Simulator**

Unity simulates the device in the Simulator view. To control the simulation, use the toolbar and the Control Panel.

### Toolbar

The toolbar is at the top of the Simulator view and contains options that, along with the Control Panel, control the simulation.

The toolbar at the top of the Simulator view. **Control** | **Description**  
---|---  
**Game/Simulator view** | Use this drop-down menu to switch between the Simulator view and the Game view.  
**Device selection drop-down menu** | Choose the device to simulate from the available device definitions.  
**Scale** | Zoom in or out on the simulated screen.  
**Fit to Screen** | Scale the display to fit inside the window.  
**Rotate** | Simulates the physical rotation of the device. The image on the device screen rotates together with the device if you enable auto-rotation and if the device supports rotation. Otherwise, if you rotate the device it causes the image to be sideways or upside down. **Note** : The Device Simulator doesn’t support gyroscope simulation.  
**Safe Area** | Indicates whether the view draws a line around the SafeArea of the current device screen.  
**Play Mode behavior** | This section describes the play mode behavior based on your selection below.  
| **Focused** | Enable Focused to shift focus on the selected Game view while the Editor is in Play mode.   
Only one game view can be in focus when you enter the Play mode. Using Maximized or Fullscreen on Display mode implies focus on the Maximized Game view. Enabling Focussed on a Game view disables it on other Game views.  
| **VSync (Game view only)** | Enable **VSync (Game view only)** to allow syncing, which is useful when recording a video, for example. Unity attempts to render the Game view at the monitor refresh rate, though this is not guaranteed. When this option is enabled, it is still useful to maximize the Game view in Play mode to hide other views and reduce the number of views that Unity renders.  
**Enter Play Mode:** | Choose from the options below to determine the settings for the Editor when it enters the Play mode.  
| **Normally** | Select this to view the Game view without forcing focus or maximizing any views to full screen.  
| **Maximized** | When this option is selected, Unity runs the Play mode with the Simulator view maximized to 100% of the Editor window.   
**Note** : This option doesn’t create a Simulator view if you disable the **Create Game View On Play** Editor preference.  
**Control Panel** | Displays and hides the Control Panel.  
  
### Control Panel

To open the Control Panel, click **Control Panel** in the top-right corner of the Toolbar. By default, the Control Panel contains settings for the Application simulated class.

The Device Simulator Control Panel. **Property** | **Description**  
---|---  
**System Language** | Specifies the value to receive from Device.Application.systemLanguage.  
**Internet Reachability** | Specifies the value to receive from Device.Application.internetReachability.  
**On Low Memory** | Calls the lowMemory event.  
  
Device Simulator plugins can change the appearance of the control panel and add content and controls. Some packages, like the Adaptive Performance package, contain Device Simulator plugins. Their **UI**