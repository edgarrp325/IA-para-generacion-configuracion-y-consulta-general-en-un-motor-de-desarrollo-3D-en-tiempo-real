---
title: "XR SDK Stats interface"
category: "General"
source_file: "xrsdk-stats.html"
doc_type: "manual"
---

# XR SDK Stats interface

The **XR** SDK Stats interface is used for registering and managing statistics data.

**Note:** The Unity XR SDK is no longer available as we have focused our investments towards OpenXR.

## Overview

Use the XR Stats interface to record stats among the various subsystems. The only supported stat primitive is a floating point number.

Use the `UnityPluginLoad` entry point method to acquire a pointer to the XRStats interface:
    
    
    IUnityXRStats* sXRStats = nullptr;
    
    extern "C" void UNITY_INTERFACE_EXPORT UnityPluginLoad(IUnityInterfaces* unityInterfaces)
    {
        sXRStats = (IUnityXRStats*)unityInterfaces->GetInterface(UNITY_GET_INTERFACE_GUID(IUnityXRStats));
        //...
    }
    

## Usage

Register your subsystem and individual stat definitions with the stats interface:
    
    
    static UnityXRStatId m_GPUFrameTimeID;
    static UnityXRStatId m_DroppedFrameCountID;
    static UnityXRStatId m_WorkThreadStat;
    
    static UnitySubsystemErrorCode ExampleDisplayProvider_Start(UnitySubsystemHandle handle)
    {
        if (sXRStats)
        {
            sXRStats->RegisterStatSource(handle);
            m_GPUFrameTimeID = sXRStats->RegisterStatDefinition(handle, "Example.GPUTime", kUnityXRStatOptionNone);
            m_DroppedFrameCountID = sXRStats->RegisterStatDefinition(handle, "Example.DroppedFrame", kUnityXRStatOptionNone);
            m_WorkThreadStat = sXRStats->RegisterStatDefinition(handle, "Example.WorkerThreadStat", kUnityXRStatOptionNone);
        }
    
        return kUnitySubsystemErrorCodeSuccess;
    }
    

Update stats on the Gfx Thread:
    
    
    extern float GetLastGPUTime(); //provided by your runtime
    static void ExampleDisplayProvider_GfxThreadCall(UnitySubsystemHandle handle)
    {
        sXRStats->SetStatFloat(m_GPUFrameTimeID, GetLastGPUTime());
        // Do gfx thread things
    }
    
    

Update stats on the main thread:
    
    
    extern float GetDroppedFrameCount(); //provided by your runtime
    
    static void ExampleDisplayProvider_MainThreadCall(UnitySubsystemHandle handle)
    {
        sXRStats->SetStatFloat(m_DroppedFrameCountID, GetDroppedFrameCount());
        // Do main thread things
    }
    

Update stats on your own threads, but be sure to call `IncrementStatFrame` to keep the current frame for that thread in sync with the other threads (this is managed internally for the main and graphics threads):
    
    
    extern float GetWorkerThreadStat(); //provided by your runtime
    static void ExampleDisplayProvider_MyWorkerThread(UnitySubsystemHandle handle)
    {
        sXRStats->IncrementStatFrame();
        sXRStats->SetStatFloat(m_WorkThreadStat, GetWorkerThreadStat());
        // Do worker thread things
    }
    

Unregister the stat source when the subsystem stops:
    
    
    static void ExampleDisplayProvider_Stop(UnitySubsystemHandle handle)
    {
        sXRStats->UnregisterStatSource(handle);
    }
    
    

## Thread safety

Updating stats via `SetStatFloat` is thread safe. However, registering and unregistering stat sources is not thread safe and should only be done on the main thread during the Start and Stop functions of the stat source’s lifecycle.

## Limitations

The queue size for processing stats is 2000. This queue is shared amongst all threads and all subsystems and is only serviced upon frame completion. For this reason, you should keep the number of calls to `SetStatFloat` low to avoid filling up the queue.

**Note:** Any stat recorded when the queue is full will be lost.

## Exposing stats to users

In the `UnityEngine.XR.Provider` namespace, use `public static bool TryGetStat(Experimental.IntegratedSubsystem xrSubsystem, string tag, out float value)` to get stats registered and updated with your provider:
    
    
    using UnityEngine.XR.Provider;
    using System.Collections.Generic;
    using UnityEngine.Experimental.XR;
    using UnityEngine.Experimental;
    using UnityEngine;
    
    public static class ExampleProviderStats
    {
        public static float GPUFrameTime()
        {
            float tmp;
            XRStats.TryGetStat(GetFirstDisplaySubsystem(), "Example.GPUTime", out tmp);
            return tmp;
        }
    
        public static int DroppedFrameCount()
        {
            float tmp;
            XRStats.TryGetStat(GetFirstDisplaySubsystem(), "Example.DroppedFrame", out tmp);
            return (int)tmp;
        }
    
        public static float MyWorkerThreadStat()
        {
            float tmp;
            XRStats.TryGetStat(GetFirstDisplaySubsystem(), "Example.WorkerThreadStat", out tmp);
            return tmp;
        }
    
        // etc...
        private static IntegratedSubsystem GetFirstDisplaySubsystem()
        {
            List<XRDisplaySubsystem> displays = new List<XRDisplaySubsystem>();
            SubsystemManager.GetInstances(displays);
            if (displays.Count == 0)
            {
                Debug.Log("No display subsystem found.");
                return null;
            }
            return displays[0];
        }
    }
    

Writing public accessor methods such as the example above can help users acquire stats without the need to sift through provider documentation and find the subsystem with which stats are registered.

Additionally, some subsystems have predefined stat tags. Your provider can provide stats for the predefined stats APIs that Unity exposes by registering subsystem specific stat tags (for example: `Headers/XR/UnityXRDisplayStats.h`).