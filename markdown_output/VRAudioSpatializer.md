---
title: "Audio spatializers in XR"
category: "General"
source_file: "VRAudioSpatializer.html"
doc_type: "manual"
---

# Audio spatializers in XR

Audio spatializers use physical characteristics of a **scene** , such as the distance and angle between an AudioListener and an AudioSource, to modify the properties of sound transmitted to the user. Spatialization can improve the perception that a sound originates from a specific location in a scene.

The Unity audio system supports spatialization through **plug-ins** built with the Unity Audio Spatializer SDK. Unity doesn’t provide any built-in spatializer plug-ins itself, but several plug-in implementations are available in third-party 3D audio SDKs. These audio SDKs typically provide additional Unity components and tools for 3D audio. Refer to the following sections to understand the available third-party audio SDKs and how to enable them in Unity.

## Audio spatializer reference

The following is a non-comprehensive list of third-party audio SDKs that provide Unity audio spatialization plug-ins:

Maker | Name | Platforms | Documentation  
---|---|---|---  
Microsoft | Microsoft Spatializer | Windows, Android |  Spatial sound in Unity (Microsoft learn)  
Meta | Meta XR Audio SDK | Windows, Android |  Meta XR Audio SDK Unity Plugin (Meta developer documentation)  
Qualcomm | Qualcomm 3D Audio Plugin for Unity | Windows, Android |  3D Audio Plugin for Unity (Qualcomm documentation)  
Steam | Steam Audio | Windows, macOS, Linux, Android |  Steam Audio Unity Integration (Valve GitHub)  
Vive | 3DSP Audio SDK | Windows, Android |  VIVE 3DSP Audio SDK Developer Guide (Vive)  
Google (now open source) | Resonance Audio | Android, iOS, Web |  Developer Guide for Resonance Audio for Unity (Resonance audio GitHub)  
Apple | PHASE | iOS, macOS |  PHASE (Apple developer documentation)  
  
Some XR provider plug-in include spatializer plug-ins for an associated **XR**

**Note:** Although many spatializer plug-ins were developed for use with **VR** devices, their use isn’t limited to VR games or applications.

## Enable an audio spatializer plug-in

After you have added the package containing an **audio spatializer** plug-in to your project, you can enable the plug-in in the project audio settings.

To enable a plug-in:

  1. Open the Project Settings window (menu: **Edit > Project Settings**).
  2. Select the **Audio** category.
  3. Choose the plug-in from the **Spatializer Plugin** dropdown menu.

## Additional resources

  * Audio overview