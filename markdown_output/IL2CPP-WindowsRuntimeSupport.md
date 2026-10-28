---
title: "Windows Runtime support"
category: "General"
source_file: "IL2CPP-WindowsRuntimeSupport.html"
doc_type: "manual"
---

# Windows Runtime support

Unity includes Windows Runtime support for IL2CPP on Universal Windows Platform platform. Use Windows Runtime support to call into both native system Windows Runtime APIs as well as custom .winmd files directly from managed code (scripts and DLLs).

To automatically enable Windows Runtime support in IL2CPP, go to the Player settings (**Edit** > **Project Settings**

The Configuration section of the **Player** settings. The options shown above change depending on your chosen build platform.

Unity automatically references Windows Runtime APIs (such as _Windows.winmd_ on Universal Windows Platform) when it has Windows Runtime support enabled. To use custom .winmd files, import them (together with any accompanying DLLs) into your Unity project folder. Then use the Plugin Inspector to configure the files for your target platform.

Use the Plugin Inspector to configure custom .winmd files for specific platforms 

In your Unity project’s scripts you can use the `ENABLE_WINMD_SUPPORT` #define directive to check that your project has Windows Runtime support enabled. Use this before a call to .winmd Windows APIs or custom .winmd scripts to ensure they can run and to ensure any scripts not relevant to Windows ignore them. Note, this is only supported in C# scripts. See the examples below. 

**Examples**

**`C#`**
    
    
    void Start() {
      #if ENABLE_WINMD_SUPPORT
        Debug.Log("Windows Runtime Support enabled");
        // Put calls to your custom .winmd API here
      #endif
    }
    

* * *

• 2017–05–16 Page amended