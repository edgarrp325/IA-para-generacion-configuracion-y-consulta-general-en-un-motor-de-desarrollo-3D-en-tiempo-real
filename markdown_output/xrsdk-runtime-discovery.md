---
title: "Runtime discovery and activation of subsystems"
category: "General"
source_file: "xrsdk-runtime-discovery.html"
doc_type: "manual"
---

# Runtime discovery and activation of subsystems

**Note:** The Unity **XR** SDK is no longer available as we have focused our investments towards OpenXR.

Add the following script to your project in order to scan for and create or start a Display subsystem with the `id` of `Display0`. You can change the `match` variable if you want to load other Display subsystems:
    
    
    using System;
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Experimental.XR;
    using UnityEngine.XR;
    
    public class Display : MonoBehaviour
    {
        public string match = "Display0";
    
        // Use this for initialization
        void Start ()
        {
            List<XRDisplaySubsystemDescriptor> displays = new List<XRDisplaySubsystemDescriptor>();
            SubsystemManager.GetSubsystemDescriptors(displays);
            Debug.Log("Number of display providers found: " + displays.Count);
    
            foreach (var d in displays)
            {
                Debug.Log("Scanning display id: " + d.id);
    
                if (d.id.Contains(match))
                {
                    Debug.Log("Creating display " + d.id);
                    XRDisplaySubsystem dispInst = d.Create();
    
                    if (dispInst != null)
                    {
                        Debug.Log("Starting display " + d.id);
                        dispInst.Start();
                    }
                }
            }
        }
    }
    

The XR Management package is the user-facing **UI**

If your **plug-in** fails to load, see the troubleshooting section below.

## Troubleshooting plug-in discovery at runtime

To troubleshoot the initialization or starting of your subsystem Provider, check the editor log or player output log for lines that start with `[XR]` or `[Subsystems]`.

## No subsystems found in C#

If you just added a .json and plug-in files, make sure you relaunch Unity. Currently, Unity only discovers these files at start-up. Also, make sure that the Provider uses the correct file layout.

## Errors finding and parsing the UnitySubsystemsManifest.json file

**Error** | **Description**  
---|---  
[XR] 3 ‘displays’ descriptors matched in Assets/UnityXRDisplayExample/UnitySubsystemsManifest.json | Unity successfully found display descriptors and registers three different `id`s for this plug-in.  
[XR] No descriptors matched for inputs in Assets/UnityXRDisplayExample/UnitySubsystemsManifest.json. | The .json file contains no input descriptors. This is normal if you’re not implementing an input subsystem.  
If you were expecting Unity to find descriptors in your .json file, they could be malformed. See documentation on UnitySubsystemsManifest.json for the correct format to use.  
[XR] Failed to parse json header for Assets/UnityXRDisplayExample/UnitySubsystemsManifest.json (did you forget to include name or libraryName fields?) | This likely means you have a malformed .json file. Run it through a validation tool, such as json linter.  
  
## Errors finding and loading the provider plug-in

**Error** | **Description**  
---|---  
[XR] PluginName failed to register Provider for DisplayId (json name or id doesn’t match?) | This means that the first two arguments to `RegisterLifecycleProvider` don’t match the .json file.  
The first argument, `pluginName`, should match the `name` field in the .json file.  
The second argument, `id`, should match the `id` field of the subsystem in the .json file.  
[XR] Unable to load plugin PluginName for subsystem DisplayId | Your plug-in couldn’t be found, it was built for the wrong architecture, or it has missing dependencies that need to be loaded. In the later case, you can use the Dependency Walker tool to find out if there are missing dependencies.  
  
## Errors initializing the provider

**Error** | **Description**  
---|---  
[XR] Failed to initialize subsystem DisplayId [error: 1] | Unity called out to your `Initialize` method, but it returned `kUnitySubsystemErrorCodeFailure`. Double-check the implementation of your `Initialize` method.