---
title: "Unity architecture"
category: "General"
source_file: "unity-architecture.html"
doc_type: "manual"
---

# Unity architecture

The Unity engine is built with native C/C++ internally, however it has a C# wrapper that you use to interact with it. As such, you need to be familiar with some of the key concepts of scripting in C#. This section of the User Manual contains information on how Unity implements .NET and C#, and any exceptions you might encounter as you code.

For information on how to get started scripting in Unity, and the fundamentals you need to know, see the documentation on Getting started scripting in Unity.

This section covers the following topics:

**Page** | **Description**  
---|---  
Overview of .NET in Unity | How the Unity engine uses the .NET framework, and any differences you might encounter if you have used .NET outside of Unity before. This area also contains information on how Unity manages memory, and how to reference additional profiles in your Project.  
Scripting backends | Unity has two main scripting backends: Mono and **IL2CPP**. This section describes the differences between the backends and how and when to use them, plus their restrictions. It also contains information on managed code stripping, which removes unused code from your build.  
Code reloading in the Editor | Information on domain reloads and how they impact on the performance of your application. Also contains information on running code on Editor launch, and how to quickly enter and exit Play mode with Configurable Enter Play Mode.  
Script serialization | Serialization is the automatic process of transforming data structures or object states into a format that Unity can store and reconstruct later. This contains information on how to use serialization in your Project in an effective way.  
Script compilation | How Unity compiles your **scripts** and in what order. Also contains information on Assembly Definitions and best practices around using them.