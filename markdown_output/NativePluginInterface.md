---
title: "Low-level native plug-in interface"
category: "General"
source_file: "NativePluginInterface.html"
doc_type: "manual"
---

# Low-level native plug-in interface

Native Plug-ins in Unity can receive callbacks when certain events happen. You can use this to implement low-level rendering in your **plug-in** in Unity can receive callbacks when certain events happen. You can use this to implement low-level rendering in your **plug-in** so it can work with Unity’s multithreaded rendering.

## Interface Registry

To handle main Unity events, a plug-in must export `UnityPluginLoad` and `UnityPluginUnload` functions. IUnityInterfaces enables the plug-in to access these functions, which you can find in `IUnityInterface.h` in the plug-in API:
    
    
    #include "IUnityInterface.h"
    #include "IUnityGraphics.h"
    // Unity plugin load event
    extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
        UnityPluginLoad(IUnityInterfaces* unityInterfaces)
    {
        IUnityGraphics* graphics = unityInterfaces->Get<IUnityGraphics>();
    }
    

## Access to the graphics device

Use the `IUnityGraphics` interface, which you can find in `IUnityGraphics.h`, to give a plug-in access to generic graphics device functionality. This script demonstrates how you can use the `IUnityGraphics` interface to register a callback:
    
    
    #include "IUnityInterface.h"
    #include "IUnityGraphics.h"
        
    static IUnityInterfaces* s_UnityInterfaces = NULL;
    static IUnityGraphics* s_Graphics = NULL;
    static UnityGfxRenderer s_RendererType = kUnityGfxRendererNull;
        
    // Unity plugin load event
    extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
        UnityPluginLoad(IUnityInterfaces* unityInterfaces)
    {
        s_UnityInterfaces = unityInterfaces;
        s_Graphics = unityInterfaces->Get<IUnityGraphics>();
            
        s_Graphics->RegisterDeviceEventCallback(OnGraphicsDeviceEvent);
            
        // Run OnGraphicsDeviceEvent(initialize) manually on plugin load
        // to not miss the event in case the graphics device is already initialized
        OnGraphicsDeviceEvent(kUnityGfxDeviceEventInitialize);
    }
        
    // Unity plugin unload event
    extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
        UnityPluginUnload()
    {
        s_Graphics->UnregisterDeviceEventCallback(OnGraphicsDeviceEvent);
    }
        
    static void UNITY_INTERFACE_API
        OnGraphicsDeviceEvent(UnityGfxDeviceEventType eventType)
    {
        switch (eventType)
        {
            case kUnityGfxDeviceEventInitialize:
            {
                s_RendererType = s_Graphics->GetRenderer();
                //TODO: user initialization code
                break;
            }
            case kUnityGfxDeviceEventShutdown:
            {
                s_RendererType = kUnityGfxRendererNull;
                //TODO: user shutdown code
                break;
            }
            case kUnityGfxDeviceEventBeforeReset:
            {
                //TODO: user Direct3D 9 code
                break;
            }
            case kUnityGfxDeviceEventAfterReset:
            {
                //TODO: user Direct3D 9 code
                break;
            }
        };
    }
    

## Plug-in callbacks on the rendering thread

You can use multithreading to render in Unity, if the platform and number of available CPUs allows for it. 

**Note** : When you use multithreaded rendering, the rendering API commands happen on a thread that is completely separate from the thread that runs MonoBehaviour **scripts**. The communication between the main thread and the render thread means that your plug-in might not start rendering immediately, depending on how much work the main thread has pushed to the render thread.

To render from the plug-in, call GL.IssuePluginEvent from your **managed plug-in** script. This causes Unity’s rendering pipeline to call the native function from the render thread, as demonstrated in the code example below. For example, if you call GL.IssuePluginEvent from the **Camera** ’s OnPostRender function, the function will call a plug-in callback immediately after the camera has finished rendering.

Native plugin code:
    
    
    // Plugin function to handle a specific rendering event
    static void UNITY_INTERFACE_API OnRenderEvent(int eventID)
    {
        // User rendering code
    }
        
    // Freely defined function to pass a callback to plugin-specific scripts
    extern "C" UnityRenderingEvent UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API
        GetRenderEventFunc()
    {
        return OnRenderEvent;
    }
    

Managed plug-in code:
    
    
    #if UNITY_IPHONE && !UNITY_EDITOR
    [DllImport ("__Internal")]
    #else
    [DllImport("RenderingPlugin")]
    #endif
    private static extern IntPtr GetRenderEventFunc();
        
    // Queue a specific callback to be called on the render thread
    GL.IssuePluginEvent(GetRenderEventFunc(), 1);
    

The signature for the `UnityRenderingEvent` callback is provided in IUnityGraphics.h in the Native Rendering Plugin sample.

## Plug-in using the OpenGL graphics API

There are two kinds of OpenGL objects: 

  * **Objects shared across OpenGL contexts** , such as texture, buffer, renderbuffer, samplers, query, **shader** , and program objects.
  * **Per-OpenGL context objects** , such as vertex array, framebuffer, program pipeline, transform feedback, and sync objects.

Unity uses multiple OpenGL contexts. When initializing and closing the Editor and the Player, Unity relies on a master context, but when rendering it uses dedicated contexts. This means you can’t create per-context objects during `kUnityGfxDeviceEventInitialize` and `kUnityGfxDeviceEventShutdown` events.

## Plug-in using the Vulkan graphics API

When developing a native graphics plug-in that uses the Vulkan graphics API, you can enable debugging through the validation layers. To enable the validation layers, ensure the following to prevent crashes during plug-in execution:

  * Add a validation layer plug-in in the same directory as the native graphics plug-in.
  * Configure identical **Load on Startup** settings for both the native and the Vulkan validation layer plug-ins in the plug-in Inspector window.

## Additional resources

  * Vulkan validation layers on Android

* * *

• 2017–05–16 Page amended