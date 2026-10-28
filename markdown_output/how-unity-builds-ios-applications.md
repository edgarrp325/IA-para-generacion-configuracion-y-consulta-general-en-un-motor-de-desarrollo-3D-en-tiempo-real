---
title: "How Unity builds iOS applications"
category: "General"
source_file: "how-unity-builds-ios-applications.html"
doc_type: "manual"
---

# How Unity builds iOS applications

Unity uses Xcode to build iOS applications. You can use iOS Player settings to configure most aspects of the final build. However, for more granular control, building an Xcode project allows you to directly modify Xcode project files.

## The build process

  1. Unity collects project resources, code libraries, and **plug-ins** from your Unity project and uses them to create a valid Xcode project.
  2. Unity updates the Xcode project based on the Unity project’s **Player settings** and Build settings. Depending on whether you use replace or append mode, Unity replaces or preserves previous changes you made. Append mode preserves changes you previously made and only overwrites certain values. Replace mode creates a new project which overwrites any changes you previously made.
  3. Unity generates C++ source files based on your C# **scripts** and places them in the generated Xcode project. Xcode then invokes the IL2CPP and places them in the generated Xcode project. Xcode then invokes the IL2CPP program which compiles the C++ source files into libraries called `libGameAssembly.a` and `il2cpp.a`.
  4. Xcode builds the project into a standalone application and deploys and launches it on a connected device or the Xcode simulator.

## Incremental build pipeline

Unity uses the Incremental build pipeline when it generates the Xcode project for iOS. This means that Unity incrementally builds and generates files such as Information Property List (plist) files and Entitlement files. If you implement callbacks that modify or move any iOS file or asset that the incremental build pipeline uses, refer to Creating non-incremental builds.

## Additional resources

  * Build an iOS application
  * iOS Build Settings