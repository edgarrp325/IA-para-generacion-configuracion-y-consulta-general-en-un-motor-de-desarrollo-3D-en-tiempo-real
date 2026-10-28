---
title: "WinRT API in C# scripts for UWP"
category: "General"
source_file: "windowsstore-scripts.html"
doc_type: "manual"
---

# WinRT API in C# scripts for UWP

You can use the WinRT API directly in Unity **scripts** when you have Windows Runtime support enabled. For information on how to use the WinRT API and enable Windows Runtime support, refer to Windows Runtime support.

You need to meet the following requirements to use WinRT API in your Unity scripts:

  * Your scripts must be written in C#.
  * Your API compatibility level must be set to .NET 4.6 or .NET Standard 2.0 in the Player settings.
  * All the code that uses WinRT API must be under the `ENABLE_WINMD_SUPPORT` directive. This is necessary because the Editor uses Mono, which doesn’t support WinRT APIs.

This code example demonstrates how to get advertising using WinRT API directly:
    
    
    using UnityEngine;
    public class WinRTAPI : MonoBehaviour 
    {
        void Update() 
        {
            auto adId = GetAdvertisingId();
            // ...
        }
    
        string GetAdvertisingId() 
        {
            #if ENABLE_WINMD_SUPPORT
                return Windows.System.UserProfile.AdvertisingManager.AdvertisingId;
            #else
                return "";
            #endif
        }
    }
    

## Additional resources

  * Windows Runtime support
  * Microsoft documentation on WinRT APIs with Unity for HoloLens