---
title: "Conditional compilation"
category: "General"
source_file: "PlatformDependentCompilation.html"
doc_type: "manual"
---

# Conditional compilation

Unity’s support for the C# language includes the use of **directives** , which allow you to selectively include or exclude code from compilation, based on whether certain **scripting symbols** are `defined` or `not defined`. 

You can read more broadly about how these directives work in C# in Microsoft’s user documentation on C# preprocessor directives.

Unity has a range of built-in scripting symbols which represent options that you can use in your **scripts** to selectively include or exclude portions of code from compilation.

For example, the built-in scripting symbol that’s set when a player is built for Windows standalone platform is `UNITY_STANDALONE_WIN`. You can check whether this symbol is defined using a special type of if statement using the following query:
    
    
    #if UNITY_STANDALONE_WIN
    
      Debug.Log("Standalone Windows");
    
    #endif
    

The hash (`#`) character in front of the `if` and `endif` indicates that these statements are “directives”, and they’re handled during the compilation process, rather than at runtime.

In the above example, the Debug line is only included for compilation in the Windows standalone build of the project. When compiled in the Unity Editor or in other target builds, it’s omitted entirely. This is different to using a regular `if .. then .. else` structure, which might only bypass the `execution` of certain part of code at runtime. 

There are a number of built-in scripting symbols which allow you to selectively compile or omit code based on the selected Platform, the Editor Version, and other miscellaneous system environment scenarios. These built-in scripting symbols are listed below.

In addition, you can define your own scripting symbols either using the Unity Editor **UI** , via scripting, or via an asset file, which allows you to control compilation of portions of your code based on arbitrary definitions. For more information, check Custom scripting symbols.

*Note: **Scripting symbols** are sometimes referred to as `define symbols`,`preprocessor defines`, or just `defines`.

## Platform scripting symbols

Unity automatically defines certain scripting symbols based on the authoring and build target platform. These are as follows:

**Define** | **Function**  
---|---  
**UNITY_EDITOR** | Scripting symbol to call Unity Editor scripts from your game code.  
**UNITY_EDITOR_WIN** | Scripting symbol for Editor code on Windows.  
**UNITY_EDITOR_OSX** | Scripting symbol for Editor code in macOS.  
**UNITY_EDITOR_LINUX** | Scripting symbol for Editor code on Linux.  
**UNITY_EMBEDDED_LINUX** | Scripting symbol for embedded Linux.  
**UNITY_QNX** | Scripting symbol for QNX.  
**UNITY_STANDALONE_OSX** | Scripting symbol to compile or execute code specifically for macOS (including Universal, PPC and Intel architectures).  
**UNITY_STANDALONE_WIN** | Scripting symbol for compiling/executing code specifically for Windows standalone applications.  
**UNITY_STANDALONE_LINUX** | Scripting symbol for compiling/executing code specifically for Linux standalone applications.  
**UNITY_SERVER** | Scripting symbol for compiling/executing code for a dedicated server (macOS, Windows or Linux).  
**UNITY_IOS** | Scripting symbol for compiling/executing code for the iOS platform.  
**UNITY_IPHONE** | Deprecated. Use **UNITY_IOS** instead.  
**UNITY_VISIONOS** | Scripting symbol for compiling/executing code for the visionOS platform.  
**UNITY_ANDROID** | Scripting symbol for the Android platform.  
**UNITY_TVOS** | Scripting symbol for the Apple TV platform.  
**UNITY_WSA** | Scripting symbol for Universal Windows Platform. Additionally, **NETFX_CORE** is defined when compiling C# files against .NET Core and using .NET **scripting backend**.  
**UNITY_WSA_10_0** | Scripting symbol for Universal Windows Platform. Additionally **WINDOWS_UWP** is defined when compiling C# files against .NET Core.  
**UNITY_WEBGL** | Scripting symbol for **WebGL**.  
**UNITY_ANALYTICS** | Scripting symbol for calling Unity **Analytics** methods from your game code. Version 5.2 and above.  
**UNITY_ASSERTIONS** | Scripting symbol for assertions control process.  
**UNITY_64** | Scripting symbol for 64-bit platforms.  
**UNITY_CLOUD_BUILD** | Scripting symbol for Cloud builds.  
  
## Editor version Scripting symbols

Unity automatically defines certain scripting symbols based on the version of the Unity Editor that you’re currently using.

Given a version number **X.Y.Z** (for example, 2019.4.14), Unity exposes three global scripting symbols in the following formats: **UNITY_X** , **UNITY_X_Y** and **UNITY_X_Y_Z**.

Here is an example of scripting symbols exposed in Unity 2019.4.14:

**Define** | **Function**  
---|---  
**UNITY_2019** | Scripting symbol for the release version of Unity 2019, exposed in every 2019.Y.Z release.  
**UNITY_2019_4** | Scripting symbol for the major version of Unity 2019.4, exposed in every 2019.4.Z release.  
**UNITY_2019_4_14** | Scripting symbol for the minor version of Unity 2019.4.14.  
  
You can also compile code selectively based on the earliest version of Unity required to compile or execute a section of code snippet. Following the same version format as above (**X.Y**), Unity exposes one global `#define` in the format **UNITY_X_Y_OR_NEWER** , that you can use for this purpose.

## Other scripting symbols

The other scripting symbols Unity defines are:

**Define** | **Function**  
---|---  
**CSHARP_7_3_OR_NEWER** | Defined when building scripts with support for C# 7.3 or newer.  
**ENABLE_MONO** | Scripting backend #define for Mono.  
**ENABLE_IL2CPP** | Scripting backend #define for **IL2CPP**.  
**ENABLE_VR** | Defined when the target build platform supports **VR**. Doesn’t imply that VR is currently enabled or that the necessary **plug-ins**. Doesn’t imply that VR is currently enabled or that the necessary **plug-ins** and packages needed to support VR are installed.  
**NET_2_0** | Defined when building scripts against .NET 2.0 API compatibility level on Mono and IL2CPP.  
**NET_2_0_SUBSET** | Defined when building scripts against .NET 2.0 Subset API compatibility level on Mono and IL2CPP.  
**NET_LEGACY** | Defined when building scripts against .NET 2.0 or .NET 2.0 Subset API compatibility level on Mono and IL2CPP.  
**NET_4_6** | Defined when building scripts against .NET 4.x API compatibility level on Mono and IL2CPP.  
**NET_STANDARD_2_0** | Defined when building scripts against .NET Standard 2.0 API compatibility level on Mono and IL2CPP.  
**NET_STANDARD_2_1** | Defined when building scripts against .NET Standard 2.1 API compatibility level on Mono and IL2CPP.  
**NET_STANDARD** | Defined when building scripts against .NET Standard 2.1 API compatibility level on Mono and IL2CPP.  
**NETSTANDARD2_1** | Defined when building scripts against .NET Standard 2.1 API compatibility level on Mono and IL2CPP.  
**NETSTANDARD** | Defined when building scripts against .NET Standard 2.1 API compatibility level on Mono and IL2CPP.  
**ENABLE_WINMD_SUPPORT** | Defined when Windows Runtime support is enabled on IL2CPP. For more information, refer to Windows Runtime Support.  
**ENABLE_INPUT_SYSTEM** | Defined when the Input System package is enabled in **Player Settings**.  
**ENABLE_LEGACY_INPUT_MANAGER** | Defined when the legacy **Input Manager** is enabled in Player Settings.  
**DEVELOPMENT_BUILD** | Defined when your script is running in a Player which was built with the **Development Build** option enabled.  
  
This define only reflects whether the development build option was enabled at the time of the build. To know whether your script is running in the development build mode, use Debug.isDebugBuild. `__DEVELOPMENT\_BUILD__` isn’t sufficient to determine whether you’re currently running in a development build because most platforms allow changing between development and non-development build without rebuilding the project. However, on some platforms, Unity doesn’t support switching between development and non-development builds in the Editor and requires you to switch after the build is complete. For example, on Windows, you can choose the **Create Visual Studio solution** option to choose whether you want a development or non-development build in Visual Studio. Switching in Visual Studio doesn’t recompile your scripts and therefore, it won’t re-evaluate scripting defines. You can also switch from the final game build to a development build by swapping `UnityPlayer.dll` in the game build with the one from a development build for debugging live game builds.  
  
## Test precompiled code

The following example shows how to test your precompiled code. It also prints a message based on the platform you’ve selected for your target build.

To test the compiled code:

  1. Open the **Build Settings** window (menu: File > Build Settings).
  2. Choose the target platform you want to test your code against and click **Switch Platform**.
  3. Create a script and copy/paste the following code:

    
    
      using UnityEngine;
      using System.Collections;
      public class PlatformDefines : MonoBehaviour {
      void Start () {
    
        #if UNITY_EDITOR
          Debug.Log("Unity Editor");
        #endif
    
        #if UNITY_IOS
          Debug.Log("iOS");
        #endif
    
        #if UNITY_STANDALONE_OSX
            Debug.Log("Standalone OSX");
        #endif
    
        #if UNITY_STANDALONE_WIN
          Debug.Log("Standalone Windows");
        #endif
    
      }          
      }
    

  1. To test the code, click **Play Mode**. Confirm that the code works by checking for the relevant messages in the Unity console, depending on the platform you selected. For example, if you choose **iOS** , the messages Unity Editor and Unity iOS will appear in the console.

**Note:** In C# you can use a `CONDITIONAL` attribute which is a more clean, less error-prone way of stripping out functions. For more information, refer to ConditionalAttribute Class. Common Unity callbacks such as `Start()`, `Update()`, `LateUpdate()`, `FixedUpdate()`, `Awake()` aren’t affected by this attribute because they’re called directly from the engine and, for performance reasons, it doesn’t take them into account.

In addition to the basic `#if` compiler directive, you can also use a multiway test in C#:
    
    
    #if UNITY_EDITOR
    
        Debug.Log("Unity Editor");
    
    #elif UNITY_IOS
    
        Debug.Log("Unity iOS");
    
    #else
    
        Debug.Log("Any other platform");
    
    #endif
    

## Additional resources

  * How to create and use scripts in Unity
  * Custom scripting symbols