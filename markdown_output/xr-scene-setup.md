---
title: "Set up an XR scene"
category: "General"
source_file: "xr-scene-setup.html"
doc_type: "manual"
---

# Set up an XR scene

To set up an **XR** **scene** **scene** , add an **XR Origin**. 

These objects are collections of **GameObjects** and components that provide a frame of reference for transforming spatial tracking data into the scene, including controlling the scene **camera** and components that provide a frame of reference for transforming spatial tracking data into the scene, including controlling the scene **camera**. When you add an **XR Origin** to a scene, it controls the attached camera to track the user’s head-mounted (VR) or hand-held (AR) device. In addition, the versions of the XR Origin that contain GameObjects for controllers will move them to track the user’s controllers. 

**Notes** : 

  * The older **XR Rig** name has been changed from “rig” to “origin” to better reflect the object’s role in a Unity scene. In addition, the **XR Origin** component has replaced the **Camera Offset** component and provides a few additional settings. Refer to XR Origin component for more information.
  * The option to **Convert Camera to XR Rig** still appears in the **GameObject > XR** menu if you do not have the XR Interaction Toolkit package installed in the project. Although this option still works, Unity recommends using the appropriate **XR Origin** option from the XR Interaction Toolkit or AR Foundation packages for best compatibility with other XR features.
  * The _**AR** Session Origin_ has been replaced by the _XR Origin (AR)_ and _XR Origin (Mobile AR)_ options in version 5 of the AR Foundation package.
  * The controller GameObjects included with some **XR Origin** objects do not have **visual components** , such as a **mesh** , such as a **mesh** , and are not configured to receive user input other than tracking data. You must add 3D models and the components or **scripts** , and are not configured to receive user input other than tracking data. You must add 3D models and the components or **scripts** necessary to act upon user input, if desired. The XR Interaction Toolkit package provides components for handling user input.

Refer to XR Origin for a description of the XR Origin options available to use in a scene.

## Prerequisites

Before you can set up a scene for XR, you must first:

  * Set up the project for XR.
  * Add the AR Foundation to the project, if you are developing an AR app.
  * Add the XR Interaction Toolkit package, if you plan to use it (recommended).
  * If you use the XR Interaction Toolkit, import the **Starter Assets**. These assets contain Input System actions and presets that you can use to configure XR controller input.

## Set up a scene for XR

The basic steps to set up a scene for XR include:

  1. Create or open the scene in the Unity Editor.
  2. Add one of the **XR Origin** options to the scene with the **GameObject > XR** menu. You will see different options in the menu depending on which XR packages you have added to your project. Refer to XR Origin for a description of the available XR Origin options.
  3. Configure XR input. Refer to XR input options for more information.

Your projects might have additional setup considerations depending on the project type, platform, and Unity packages that you plan to use:

  * For AR projects, refer to Scene setup in the AR Foundation manual for additional set up steps and more detailed instructions. 

  * For **VR** projects using the XR Interaction Toolkit, refer to General Setup in the Interaction Toolkit manual for additional information.

  * For AR/**MR** projects on the Apple Vision Pro, use a Volume Camera instead of an XR Origin. Refer to PolySpatial visionOS: Starting a new visionOS project.

  * For VR projects on the Apple Vision Pro, you must add an AR Session object from the **AR Foundation** package to a scene to access head and hand tracking data. VR apps on this device also have access to additional ARKit data, such as plane detection, scene reconstruction meshes, and image tracking. Refer to Fully Immersive VR on visionOS

## Detect whether XR is enabled

If you have a scene that can be used in both XR and non-XR contexts, you can use the XRSettings.enabled property to detect whether the XR subsystems are currently loaded and active. With that information you can activate or deactivate the appropriate sets of GameObjects and components.
    
    
    public void CheckXRStatus()
    {
        if (UnityEngine.XR.XRSettings.enabled)
        {
            Debug.Log("XR is active.");
        }
        else
        {
            Debug.Log("XR is not available.");
        }
    }
    
    

**Note:** you can read the value of the XRSettings.enabled property to determine the XR status. However, setting the value is no longer supported and does nothing. For information about how to dynamically turn XR on and off at runtime, refer to Manage XR loader lifecycles.