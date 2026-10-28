---
title: "Creating an XR provider"
category: "General"
source_file: "xrsdk-provider-setup.html"
doc_type: "manual"
---

# Creating an XR provider

An **XR** provider is part of a Unity project and minimally consists of a manifest file and one or more native **plug-ins** provider is part of a Unity project and minimally consists of a manifest file and one or more native **plug-ins**. It can also include other assets such as **scripts**. It can also include other assets such as **scripts** and images. As long as these are in your project when you launch the Editor, Unity discovers them.

You must relaunch Unity whenever you change a provider’s manifest or Editor **native plug-in**.

**Note:** The Unity XR SDK is no longer available as we have focused our investments towards OpenXR.

## File layout

Native plug-ins must be in a subfolder relative to the manifest file, `UnitySubsystemsManifest.json`, and no more than two folders below the manifest itself. 

## UnitySubsystemsManifest.json

This manifest contains information about your provider, including the subsystems it offers and the plug-in name. It’s important to note that the `xreditorsubsystem` keyword should be included in the `package.json` file of any package that defines subsystems in `UnitySubsystemsManifest.json` and requires these subsystems to function within the Unity Editor. The presence of this keyword is essential for ensuring that the Unity Editor recognizes and properly discovers these subsystems. Without this keyword, subsystems intended for editor usage may not perform as expected, though this does not impact the player build process.

For more information, refer to the UnitySubsystemsManifest.json page.

## Building a provider plug-in

To learn how to build a native plug-in for your targeted platform, refer to documentation on the Unity native plug-in interface. After you get your dynamic library into Unity, ensure that all the options (such as the target platform in the Plug-in Settings) are correct.

You need to register a lifecycle handler for the subsystems that you intend to implement. For example:
    
    
    extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
    UnityPluginLoad(IUnityInterfaces* unityInterfaces)
    {
      s_XrDisplay = unityInterfaces->Get<IUnityXRDisplayInterface>();
      UnityLifecycleProvider displayLifecycleHandler =
      {
        NULL, // This can be any object you want to pass as userData to the following functions
        &Lifecycle_Initialize,
        &Lifecycle_Start,
        &Lifecycle_Stop,
        &Lifecycle_Shutdown
      };
      s_XrDisplay->RegisterLifecycleProvider("Provider Plugin Name", "Display0", &displayLifecycleHandler);
    
      // Register with other subsystems
    }
    

**Note:** The parameters passed to `RegisterLifecycleProvider` must match the `name` and `id` fields in your manifest file.

When you call your `Initialize` method at a later point, you get an instance handle you can use to call methods that take a `UnitySubsystemHandle`. Example:
    
    
    /// Callback executed when a subsystem should initialize in preparation for becoming active.
    static UnitySubsystemErrorCode UNITY_INTERFACE_API Lifecycle_Initialize(UnitySubsystemHandle handle, void* data)
    {
      // Register for callbacks on the graphics thread.
      UnityXRDisplayGraphicsThreadProvider gfxThreadProvider = { NULL, NULL, &GfxThread_WaitForNextFrameDesc, NULL };
      s_XrDisplay->RegisterProviderForGraphicsThread(handle, &gfxThreadProvider);
    
      return kUnitySubsystemErrorCodeSuccess;
    }
    

The SDK package includes an example project that builds sample plug-ins.

## Loading in Unity

For more information about loading your provider in Unity, refer to the Runtime discovery and activation of subsystems page.