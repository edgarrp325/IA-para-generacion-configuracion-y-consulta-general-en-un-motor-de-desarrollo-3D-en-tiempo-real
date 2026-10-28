---
title: "Native plug-ins"
category: "General"
source_file: "NativePlugins.html"
doc_type: "manual"
---

# Native plug-ins

Unity supports native **plug-ins** , which are libraries of native code you can write in languages such as C, C++, and Objective-C. Plug-ins allow the code you write in C# to call functions from these libraries. This feature allows Unity to integrate with middleware libraries or existing C/C++ code.

The **native plug-in** provides a simple C interface, which the C# script then exposes to your other **scripts** provides a simple C interface, which the C# script then exposes to your other **scripts**. Unity can also call functions that the native plug-in exports when certain low-level rendering events happen (for example, when you create a graphics device). See Low-level native plug-in interface for more information.

For an example of a native plugin, see Native Renderer Plugin.

## Using a native plug-in

To use a native plug-in:

  1. Write functions in a C-based language to access the features you need.
  2. Compile them into a library.
  3. In Unity, create a C# script that calls functions in the native library.

You build native plug-ins with native code compilers on the target platform. Because plug-in functions use a C-based call interface, you must declare the functions with C linkage to avoid name mangling issues.

## Example

A simple native library with a single function might have code that looks like this:

`float ExamplePluginFunction () { return 5.0F; }`

To access this code from within Unity, use the following C# script:
    
    
    using UnityEngine;
    using System.Runtime.InteropServices;
    
    class ExampleScript : MonoBehaviour {
        #if UNITY_IPHONE
        // On iOS plugins are statically linked into
        // the executable, so we have to use __Internal as the
        // library name.
        [DllImport ("__Internal")]
        #else
        // Other platforms load plugins dynamically, so pass the
        // name of the plugin's dynamic library.
        [DllImport ("PluginName")]   
        #endif
        private static extern float ExamplePluginFunction ();
    
        void Awake () {
            // Calls the ExamplePluginFunction inside the plugin
            // And prints 5 to the console
            print (ExamplePluginFunction ());
           }
        }
    

## Further information

You can learn more about using native plugins to interact with third-party code libraries, including how you can implement rendering in your plug-in, with the following pages:

  * Low-level native plug-in interface
  * Mono Interop with native libraries
  * P-invoke documentation on MSDN