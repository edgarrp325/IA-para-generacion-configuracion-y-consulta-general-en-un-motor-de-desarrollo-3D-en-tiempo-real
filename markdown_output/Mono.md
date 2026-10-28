---
title: "Mono overview"
category: "General"
source_file: "Mono.html"
doc_type: "manual"
---

# Mono overview

The **Mono**scripting backend**** compiles code at runtime, with a technique called just-in-time compilation (JIT). Unity uses a fork of the open source Mono project.

Some platforms don’t support JIT compilation, so the Mono backend doesn’t work on every platform. Other platforms support JIT and Mono but not ahead-of-time compilation (AOT), and so can’t support the IL2CPP backend. When a platform can support both backends, Mono is the default. For more information, see Scripting restrictions.

Mono supports the debugging of managed code. For more information, see Debugging C# code in Unity.

## Building a project using Mono

You can change the scripting backend Unity uses to build your application in one of two ways:

  * Through the ****Player Settings**** menu in the Editor. Perform the following steps to change the scripting backend through the **Player** settings menu: 
    1. Go to **Edit** > **Project Settings**.
    2. Select **Player** to open the Player settings for the current platform in the Inspector
    3. Under the **Other Settings** sub-menu, navigate to **Configuration** > **Scripting Backend**.
    4. Select **Mono**.
  * Through the Editor scripting API. Use the PlayerSettings.SetScriptingBackend property to change the scripting backend that Unity uses.

The **Configuration** section of the **Player** settings

To start the build process, open the **Build Settings** window (Menu: **File** > **Build Settings**) and select **Build**.

Both the Mono and **IL2CPP** scripting backends require a new build for each platform you want to target. For example, to support both the Android and iOS platforms, you need to build your application twice and produce two binary files, one for Android and one for iOS.