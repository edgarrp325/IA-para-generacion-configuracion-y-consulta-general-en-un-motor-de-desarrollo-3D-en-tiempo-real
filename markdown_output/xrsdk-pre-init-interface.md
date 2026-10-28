---
title: "XR SDK PreInit interface"
category: "General"
source_file: "xrsdk-pre-init-interface.html"
doc_type: "manual"
---

# XR SDK PreInit interface

This interface allows you to configure the graphics device before it’s created. Common use cases include choosing a specific GPU in multi-GPU scenarios, enabling graphics extensions, and modifying buffer creation.

**Note:** The Unity **XR** SDK is no longer available as we have focused our investments towards OpenXR.

## Overview

Your provider can export the native symbol `XRSDKPreInit`, which is called early in runtime initialization, before graphics device creation. It should fill out a `UnityXRPreInitProvider` structure with the relevant entry points for providing the engine with information it might need during early initialization. Some providers need this because the graphics device is created before providers are able to initialize.

## Discovery

The Unity project build process requires the name of your provider library before it can call `XRSDKPreInit()` at engine startup. To do this, implement the `IXRLoaderPreInit.GetPreInitLibraryName` interface on your `XRLoader`:
    
    
    public string GetPreInitLibraryName(BuildTarget buildTarget, BuildTargetGroup buildTargetGroup)
    {
        return "XRSDKMyProviderLibraryName";
    }
    

When Unity starts up, it runs the code above to load the library. Then, Unity opens that library, looks for the `XRSDKPreInit` export, and calls it. At that point, `XRSDKPreInit` should register a `UnityXRPreInitProvider`.

## Registration in XRSDKPreInit

Here’s a simple example that registers all of the callbacks that you can use for early engine initialization:
    
    
    XRSDKPreInit(IUnityInterfaces * interfaces)
    {
        IUnityXRPreInit* preInit = (IUnityXRPreInit*)interfaces->GetInterface(GetUnityInterfaceGUID<IUnityXRPreInit>());
    
        UnityXRPreInitProvider provider = { 0 };
    
        provider.userData = nullptr;
        provider.GetPreInitFlags = GetPreInitFlags;
        provider.GetGraphicsAdapterId = GetGraphicsAdapterId;
        provider.GetVulkanInstanceExtensions = GetVulkanInstanceExtensions;
        provider.GetVulkanDeviceExtensions = GetVulkanDeviceExtensions;
    
        preInit->RegisterPreInitProvider(&provider);
    }
    

Set any callbacks that you don’t need to `nullptr`.

* * *

## Callbacks

### GetPreInitFlags

`GetPreInitFlags` returns a 64-bit bitfield of flags. The following flags are currently exposed:

  * `kUnityXRPreInitFlagsEGLUsePBuffer` \- On EGL platforms (Android, standalone Meta/Oculus devices, etc.), EGL should be initialized using PBuffers.
  * `kUnityXRPreInitFlagsEGLUseNoErrorContext` \- On EGL platforms, EGL should be initialized with a NO_ERROR context.

Providers shouldn’t set any undefined bits, as they might be used for future expansion.

### GetGraphicsAdapterId

`GetGraphicsAdapterId` sets the graphics adapter that the Unity runtime graphics device uses for graphics API initialization. For example, if a user plugs a headset into a different GPU than the user’s primary display device, Unity might need to initialize the graphics API that explicitly targets the secondary GPU.

### GetVulkanDeviceExtensions and GetVulkanInstanceExtensions

`GetVulkanDeviceExtensions` and `GetVulkanInstanceExtensions` are used if the provider needs Unity to initialize Vulkan with specific extensions for the device and instance. This is often used for compositor surface sharing. Both of these return a space-separated string of extensions.

* * *

## Known issues

  * Currently, `GetPreInitLibraryName` is only called on the first XRLoader in the XRManager **prefab** , so only the first Provider in the list can provide PreInit entry points at runtime.
  * PreInit requires a native library to expose the entry point during early engine initialization.
  * PreInit doesn’t apply to the Editor at this time.