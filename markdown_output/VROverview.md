---
title: "VR and MR development in Unity"
category: "General"
source_file: "VROverview.html"
doc_type: "manual"
---

# VR and MR development in Unity

Get started with **virtual reality** and **mixed reality** development in Unity.

Virtual Reality (VR) and Mixed Reality (MR) both refer to extended reality experiences where specialized devices provide a way for the user to interact with a virtual environment.

In **VR** experiences, the environment is closed. This means that the user can’t see their surrounding environment, and can only see virtual content displayed on the screen. The user can only interact with virtual content, rather than their physical environment. VR experiences are often achieved with a headset (a Head-Mounted Display [HMD]), where a screen within the headset displays the virtual environment. VR experiences are fully immersive, and so are a good choice for creating immersive, story-driven experiences and gameplay.

MR combines elements of the real and virtual environments, enabling users to see and interact with both simultaneously. MR relies on devices that are able to display a real-time view of the user’s surroundings, and blend the real-world view with virtual content. Some headsets, such as the Meta Quest 3, achieve MR through passthrough cameras, which capture the surrounding environment and display it on the screen. Other devices achieve MR without passthrough cameras, for example the Microsoft HoloLens devices are transparent glasses which project virtual content directly onto the lenses. MR is useful in situations where real-world integration is beneficial, such as training or educational experiences. You can also use MR to create social gaming experiences, or to enhance gameplay with locational information.

**Note:** On some modern devices, you can develop an app that has both **MR** and VR modes to allow the user to toggle between these modes within your app.

## Considerations for VR and MR development

VR and MR development shares common workflows and design considerations with any real-time 3D development in Unity. However, distinguishing factors include:

  * **Richer user input** : in addition to traditional button and joystick controllers, VR devices provide spatial head, controller, and hand and finger tracking (on supported platforms).
  * **More intimate interaction with the environment** : in conjunction with the possibilities of richer input, VR raises the expectations of much closer and physical interaction with the environment than typical 3D games and applications. Users expect to be able to pick things up and interact with objects in the environment. With head tracking, the **camera** can get much closer to the walls and other boundaries of the environment and can even pass through them.
  * **User comfort concerns** : many people experience motion sickness in VR when camera movement doesn’t match the movement of their head. You can mitigate the causes of motion sickness by maintaining a high frame rate, offering a range of locomotion options so that users can choose a mode they are comfortable with, and avoiding moving the camera independently of the user’s head tracking.

To get started with VR development, use the XR Plug-in Management system to install and enable XR provider plug-ins for the devices you want to support. Refer to XR Project set up for more information.

## Basic VR and MR scene elements

A basic VR or MR **scene** should contain an XR Origin, which defines the 3D origin for tracking data. This collection of **GameObjects** should contain an XR Origin, which defines the 3D origin for tracking data. This collection of **GameObjects** and components also contains the main scene Camera and the GameObjects representing the user’s controllers. Refer to Set up an XR scene for instructions on setting up a basic VR scene.

You typically need a way for the user to move around and to interact with the 3D world you have created. The XR Interaction Toolkit provides components for creating interactions like selecting and grabbing objects. It also provides a customizable locomotion system. You can use the Input System in addition to or instead of the **XR**

## VR packages

Most of the features and APIs used for VR development in Unity are provided through packages. These packages include:

  * Provider plug-ins
  * XR Interaction Toolkit
  * XR Core Utilities
  * Input System
  * VR project template
  * Hand tracking

### VR and MR provider plug-ins

VR and MR platforms are available as provider plug-ins by the XR **Plug-in** Management system. To understand how to use the XR Plug-in Management system to add and enable provider plug-ins for your target platforms, refer to XR Project set up.

The following table describes the plug-ins available for VR and MR development, and the devices that they support:

**Plug-in** | **MR/VR** | **Supported devices**  
---|---|---  
Apple visionOS XR Plugin | MR and VR | Apple Vision Pro  
Oculus Plug-in | VR | Oculus Rift, Meta Quest 2, Meta Quest 3, Meta Quest 3s, Meta Quest Pro  
OpenXR | MR and VR |  Devices with an OpenXR runtime including Meta Quest devices, Valve SteamVR, HoloLens  
Unity OpenXR: Meta OpenXR | MR and VR | Meta Quest devices  
PlayStation VR | VR | PlayStation VR and VR2. (Requires Sony Developer registration.)  
Mock HMD | VR | Simulates a VR headset in the Unity Editor Play mode  
  
**Note:** Many headset makers are working toward using the OpenXR runtime as a standard. However, this process isn’t complete and there can be feature discrepancies between OpenXR and a headset maker’s own provider plug-in or SDK.

### XR Interaction Toolkit

The XR Interaction Toolkit can make it easier and faster to develop VR applications. The XR Interaction Toolkit provides:

  * An XR Origin set up with controllers.
  * XR controller setups with Input System presets for basic interactions like select and grab.
  * Interactor and Interactable components for creating object manipulation.
  * A configurable locomotion system.
  * XR UI input.

### XR Core Utilities

The XR Core Utilities package contains software utilities used by other Unity XR plug-ins and packages. Typically, this package gets installed in your project as a dependency of other XR packages.

### Input System

The Unity Input System package not only supports accessing user input from VR controller buttons and joysticks, but also provides access to XR tracking data and haptics. The Input System package is required if you use the XR Interaction Toolkit or the OpenXR provider plug-in.

## VR and MR templates

Unity provides templates for VR and MR development. These templates are accessible from the Unity Hub, and provide a sample scene pre-configured with the relevant packages and components to get started with VR and MR development.

The available VR and MR templates are:

  * VR Template
  * VR Multiplayer Template
  * MR Template

To learn more about creating an XR project from a template, refer to Create an XR project.

## Hand tracking

Hand tracking is a feature that allows users to interact with a VR application using their hands. Hand tracking is supported by the XR Hands package.

The Hands package provides:

  * A standard hand data model.
  * An API for accessing hand tracking data.
  * The XR Hand Skeleton Driver component, which maps a set of Transforms to their corresponding hand **joints**
  * The XR Hand Mesh Controller, which enables and disables a **mesh**
  * A HandVisualizer sample that demonstrates how to use the hand tracking API.

## Additional resources

  * Create virtual and mixed reality experiences in Unity (E-book)
  * Make a VR multiplayer game, Part 1 | Unity (YouTube)