---
title: "XR Origin"
category: "General"
source_file: "xr-origin.html"
doc_type: "manual"
---

# XR Origin

The **XR** Origin serves as the center of tracking space in an XR **scene** Origin serves as the center of tracking space in an XR **scene**.

An XR Origin configuration is a set of **GameObjects** and components that work together to transform data from the XR tracking subsystems into world space. For example, the TrackedPoseDriver component on the Main **Camera** and components that work together to transform data from the XR tracking subsystems into world space. For example, the TrackedPoseDriver component on the Main **Camera** GameObject moves the Camera relative to the XR Origin using the tracking data for the user’s headset or handheld device. Refer to XR Origin for more information about the XR Origin.

XR devices provide tracking data in real-world units relative to a point chosen by the XR system at initialization. Unity aligns the XR Origin GameObject in a scene with this initial point.

GameObjects representing tracked entities, such as the user’s headset or hand-held device, are children of the XR Origin GameObject in the scene hierarchy. This means that changes in position and rotation based on tracking updates are relative to the XR Origin. As the user moves in the real world, these child GameObjects move relative to the XR Origin in the scene. The XR Origin doesn’t move on its own. However, you can move the XR Origin with a script to allow the user to teleport or move via controller input. 

## XR Origin configurations

The Unity XR packages provide a number of XR Origin configurations tailored for different types of XR applications. You can use the **GameObject > XR** menu to add an XR Origin to the current Scene. The available options depend on which packages you have added to your project.

XR type | Rig | Menu option | Package | Notes  
---|---|---|---|---  
**VR** , **MR** | XR Rig | **Convert Main Camera To XR Rig** |  XR Legacy Input Helpers (installed with the XR Plug-in Management package) | Replaces the standard Camera in a basic Unity Scene. The logic used to replace the main camera can fail in complex scenes. Unity removes this option when you install the XR Interaction Tools package. The **XR Rig** GameObject created by this menu option is slightly different than the **XR Origin** and might not be as compatible with other Unity XR features.  
VR, MR | XR Origin | **XR Origin** |  XR Core Utils (installed with the XR Interaction Toolkit package) | Does not include GameObjects for controllers.  
VR, MR | XR Origin (VR) | **XR Origin (VR)** | XR Interaction Toolkit | Includes controller GameObjects set up for action-based input.  
VR, MR | XR Origin (VR) | **Device-based > XR Origin (VR)** | XR Interaction Toolkit | Includes controller GameObjects set up for device-based input.  
**AR** , MR | XR Origin (AR) | **XR Origin (AR)** | AR Foundation | Serves as the tracking origin for hand-held AR applications. Includes controller GameObjects. This option is available if you have the XR Interaction Toolkit installed.  
AR | XR Origin (Mobile AR) | **XR Origin (Mobile AR)** | AR Foundation | Serves as the tracking origin for hand-held AR applications. Does not include controller GameObjects. This option is replaced with **XR Origin (AR)** if you have the XR Interaction Toolkit installed.  
  
**Notes:**

  * In the latest versions of the Unity XR packages, the **XR Rig** has been replaced with the **XR Origin**.
  * The `XROrigin` component also replaces the `CameraOffset` component, providing a few additional settings. See XR Origin component for more information.
  * The **AR Session Origin** configuration has been replaced with **XR Origin (Mobile)** and **XR Origin (AR)** in AR Foundation 5.0+.
  * The **XR Origin (Mobile)** and **XR Origin (AR)** configurations are not compatible with earlier versions of the AR Foundation package.