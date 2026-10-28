---
title: "Memory in Unity"
category: "General"
source_file: "performance-memory-overview.html"
doc_type: "manual"
---

# Memory in Unity

To ensure your application runs with no performance issues, it’s important to understand how Unity uses and allocates memory. This section of the documentation explains how memory works in Unity, and is intended for readers who want to understand how they can improve the memory performance of their application.

Unity uses three memory management layers to handle memory in your application: 

  * Managed memory: A controlled memory layer that uses a managed heap and a garbage collector to automatically allocate and assign memory.
  * C# unmanaged memory: A layer of memory management that you can use in conjunction with the Unity Collections namespace and package. This memory type is called “unmanaged” because it doesn’t use a garbage collector to manage unused parts of memory.
  * Native memory: C++ memory that Unity uses to run the engine. In most situations, this memory is inaccessible to Unity users, but it’s useful to be aware of it if you want to fine-tune certain aspects of the performance of your application.

## Managed memory

Mono and IL2CPP’s scripting virtual machines (VMs) implement the **managed memory** system, which is sometimes referred to as the scripting memory system. These VMs offer a controlled memory environment divided into the following different types:

  * **The managed heap** : A section of memory that the VM automatically controls with a garbage collector (GC). Because of this, the memory allocated on the managed heap is referred to as **GC Allocation**. The Profiler
  * **The scripting stack:** This is built up and unwound as your application steps into and out of any code scopes.
  * **Native VM memory:** Contains memory related to Unity’s scripting layer. Most of the time, you won’t need to manipulate the native VM memory, but it’s useful to know that it includes memory related to the executable code that your code generates, in particular around the use of generics, type meta data that Reflection uses, and the memory required to run the VM.

Because the managed memory system uses VMs, it has a controlled environment that automatically tracks the references of allocations to manage their lifetime. This means that it’s less likely for your application to release memory too early, while other code is trying to access it. It also means that you have some safeguard against memory leaks that happen when memory is inaccessible from code, or from unused memory piling up.

Using managed memory in Unity is the easiest way to manage the memory in your application; but it has some disadvantages. The garbage collector is convenient to use, but it’s also unpredictable in how it releases and allocates memory, which might lead to performance issues such as stuttering, which happens when the garbage collector has to stop to release and allocate memory. To work around this unpredictability, you can use the C# unmanaged memory layer.

For more information on how managed memory works, refer to the section on Managed memory.

## C# unmanaged memory

The **C# unmanaged memory layer** allows you to access the native memory layer to fine-tune memory allocations, with the convenience of writing C# code.

You can use the `Unity.Collections`namespace (including NativeArray) in the Unity core API, and the data structures in the Unity Collections package to access C# unmanaged memory. If you use Unity’s C# Job system, or Burst, you must use C# unmanaged memory. For more information about this, see the documentation on the Job system and Burst.

## Native memory

The Unity engine’s internal C/C++ core has its own memory management system, which is referred to as **native memory**. In most situations, you can’t directly access or modify this memory type.

Unity stores the **scenes** in your project, assets, graphics APIs, graphics drivers, subsystem and **plug-in** in your project, assets, graphics APIs, graphics drivers, subsystem and **plug-in** buffers, and allocations inside native memory, which means that you can indirectly access the native memory via Unity’s C# API. This means that you can manipulate the data for your application in a safe and easy way, without losing the benefits of the native and performant code that’s at Unity’s native core.

Most of the time, you won’t need to interact with Unity’s native memory, but you can see how it affects the performance of your application whenever you use the Profiler, through Profiler markers