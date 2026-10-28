---
title: "UnitySubsystemsManifest.json"
category: "General"
source_file: "xrsdk-unity-subsystems-manifest-json.html"
doc_type: "manual"
---

# UnitySubsystemsManifest.json

**Note:** The Unity **XR** SDK is no longer available as we have focused our investments towards OpenXR.

`UnitySubsystemsManifest.json` contains metadata about your provider that can be queried before your **plug-in** is loaded. The values in this dictionary are used to populate specific instances of SubsystemDescriptors in C#. For example, information within the `displays` list is used to populate XRDisplaySubsystemDescriptors.

For Unity to find the a native library referenced by the `UnitySubsystemsManifest.json` file, the library must be no more than two subfolders deeper than the `UnitySubsystemsManifest.json` file.

Example .json file:
    
    
    {
        "name": "PluginName",
        "version": "1.0.0",
        "libraryName": "UnityXRDisplayExample",
    
        "displays": [
            {
                "id": "Display0",
                "supportedMirrorBlitReservedModes" : ["leftEye","rightEye", "sideBySide"]
            }
        ],
        "inputs:": [
            {
                "id": "MockHMD Head Tracking Stationary"
            },
            {
                "id": "MockHMD Head Tracking Simulated"
            }
        ]
    }
    

**Metadata** | **Description**  
---|---  
`name` | The name of your provider. Must match the first parameter of your **native plug-in** ’s `RegisterLifecycleHandler` call.  
`version` | Unused currently.  
`libraryName` | Must match the name of your provider’s native plug-in binary without the extension.  
`displays` | Collection of Display subsystem providers.  
`id` | Identifier for this display plug-in configuration. The `id` must match the string you pass into your native plug-in’s `RegisterLifecycleHandler` call for that subsystem. You can have more than one `display`, as long as your native plug-in calls `RegisterLifecycleHandler` for each.  
`inputs` | Collection of Input subsystem providers.  
  
Your manifest file can include additional fields for a display record after `id` \- subsystems specify which parameters are valid.