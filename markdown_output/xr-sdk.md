---
title: "Unity XR SDK"
category: "General"
source_file: "xr-sdk.html"
doc_type: "manual"
---

# Unity XR SDK

**Note:** The Unity **XR** SDK is no longer available as we have focused our investments towards OpenXR.

## Subsystems

A single subsystem consists of:

  * A developer-facing C# interface
  * A native interface that multiple backends (Providers) implement via dynamic libraries
  * Common engine code which handles communicating with the C# interface, the native interface, and the rest of the engine

### Subsystem descriptor

A subsystem descriptor is metadata about a subsystem which can be inspected before loading or initializing a subsystem. This comes from a manifest file and is accessed via a C# interface. A `Create` method activates the subsystem and provides an instance of it to the user’s **scripts**.

For more information, see the Runtime discovery and activation of subsystems page.

### Subsystem instance

When `Create` is called on a subsystem descriptor, this creates a subsystem instance. Scripting code interacts with these instances in order to communicate with the subsystem. The subsystem itself has its own lifecycle: it can be started, stopped, and shut down.

## Provider

A provider is the native implementation of a subsystem. One subsystem can have multiple providers. Some subsystems can allow multiple providers to be active at a time, but others might be mutually exclusive.

Provider diagram

Providers conform to the Unity native plug-in interface, with some additional lifecycle support built on top. The entry point is the `UnityPluginLoad` method. From there, the provider must register with all subsystems it intends to implement.
    
    
    extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
    UnityPluginLoad(IUnityInterfaces* unityInterfaces)
    {
        s_XrDisplay = unityInterfaces->Get<IUnityXRDisplayInterface>();
        UnityLifecycleProvider displayLifecycleHandler =
        {
            NULL, // This can be any object you want to be passed as userData to the following functions
            &Lifecycle_Initialize,
            &Lifecycle_Start,
            &Lifecycle_Stop,
            &Lifecycle_Shutdown
        };
        s_XrDisplay->RegisterLifecycleProvider("Provider Plugin Name", "Display0", &displayLifecycleHandler);
    
        // Register with other subsystems...
    }