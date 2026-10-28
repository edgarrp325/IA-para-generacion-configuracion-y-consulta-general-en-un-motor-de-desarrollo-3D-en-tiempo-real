---
title: "visionOS"
category: "General"
source_file: "visionOS.html"
doc_type: "manual"
---

# visionOS

visionOS is the operating system of the Vision Pro, Apple’s latest spatial computing device. Unity developers can leverage existing 3D **scenes** and assets to build games or applications for visionOS. For more information about visionOS, see Apple’s visionOS Overview.

visionOS provides a few different modes in which apps can be displayed: Windows, Volumes or Spaces. Users can use Windows to present 2D or 3D content (without stereo), or use Volumes to present 3D content and objects. With Volumes, users have the flexibility to walk around and interact with 3D content from any angle. 

Depending on application type, visionOS apps can run in either a **Shared Space** or a **Full Space**. The Shared Space works is a multitasking environment similar to the desktop of a personal computer; in this mode, users can see and interact with Windows and Volumes from multiple applications simultaneously. For more immersive experiences, users can target their applications for a dedicated **Full Space** , which displays content exclusively from one app at time. Windowed apps run in a Shared Space by default. Fully immersive (VR) content requires a Full Space, while Immersive (MR) content supports both Shared Spaces and Full Spaces, depending on the Mode of its Volume **Camera** ’s Output Configuration.

## Requirements

Fully Immersive (VR) and Immersive (MR) apps are only available to Unity Pro, Unity Enterprise, and Unity Industry users. Learn more about these plans.

## Getting Started

All visionOS application types require that you install the visionOS module to the Unity Editor via the Unity Hub. The visionOS module is available for Unity 2022.3.5f1+.

In addition, Fully Immersive (VR) and Immersive (MR) apps further require that you install extra packages. You must add these packages by name via the Package Manager. 

For Fully Immersive (VR) apps, you need:

  * `com.unity.xr.visionos`

For Immersive (MR) apps, you need:

  * `com.unity.polyspatial.visionos` (which depends on `com.unity.xr.visionos`)
  * `com.unity.polyspatial.xr`

If you do not install these packages, you content will be built as a Windowed App by default.

Once you have done so, navigate to `Project Settings > XR Plug-in Manager > Apple visionOS > App Mode` and select between `Mixed Reality - Volume or Immersive Space` and `Virtual Reality - Fully Immersive Space` to configure build for the appropriate application mode

## Windowed Apps

Unity describes applications that live within Windows as Windowed Apps. By default, your Unity content will become Windowed Apps in visionOS if you build a Unity application targeted at the visionOS platform without enabling the PolySpatial Runtime or visionOS plugin via the **XR** Plugin Manager.

To detect interactions on the Unity application within a window component on visionOS, use the Input System package’s (com.unity.inputsystem) touch support. To learn more about designing for the window component on visionOS, visit Apple’s Human Interface Guidelines for visionOS.

## Mixed Reality (Immersive) and Virtual Reality (Fully Immersive) Apps

For more information about developing fully immersive **virtual reality** (VR) apps and immersive **mixed reality** (MR) apps for visionOS, refer to Unity’s visionOS-specific documentation.