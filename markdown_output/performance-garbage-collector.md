---
title: "Garbage collector overview"
category: "General"
source_file: "performance-garbage-collector.html"
doc_type: "manual"
---

# Garbage collector overview

Unity uses a garbage collector to reclaim memory from objects that your application and Unity are no longer using. When a script tries to make an allocation on the managed heap but there isn’t enough free heap memory to accommodate the allocation, Unity runs the garbage collector. When the garbage collector runs, it examines all objects in the heap, and marks for deletion any objects that your application no longer references. Unity then deletes the unreferenced objects, which frees up memory. 

The garbage collector handles subsequent requests in the same way until there is no free area large enough to allocate the required block size. In this situation, it’s unlikely that all allocated memory is still in use. Unity’s **scripting backends** can only access a reference item on the heap as long as there are still reference variables that can locate it. If all references to a memory block are missing (if the reference variables have been reassigned or if they’re local variables that are now out of scope) then the garbage collector can reallocate the memory it occupied.

To determine which heap blocks are no longer in use, the garbage collector searches through all active reference variables and marks the blocks of memory that they refer to as “live.” At the end of the search, the garbage collector considers any space between the “live” blocks empty and marks them for use for subsequent allocations. The process of locating and freeing up unused memory is called **garbage collection** (GC).

**Note:** The garbage collector works differently in **WebGL**. For more information, refer to Garbage collection considerations.

In Unity, the garbage collector has the following modes:

  * Incremental garbage collection: Enabled by default (**Project Settings > Player > Configuration**), this mode spreads out the process of garbage collection over multiple frames.
  * Incremental garbage collection disabled: If you disable the **Incremental GC** Player Setting, the garbage collector stops running your application to inspect and process objects on the heap.
  * Disable automatic garbage collection: Use the GarbageCollector.GCMode API to take full control of when Unity should run the garbage collector.

## Tracking allocations

Unity has the following tools to keep track of memory allocations: 

  * Unity Profiler’s CPU Usage module: Provides details of the **GC Alloc** per frame
  * Unity Profiler’s Memory module: Provides high-level memory usage frame by frame
  * The Memory Profiler package: A separate Unity package which provides detailed information about memory usage during specific frames in your application

In the CPU Usage module, the Hierarchy view contains a **GC Alloc** column. This column displays the number of bytes that Unity allocated on the managed heap in a specific frame. It also displays the amount of memory that the garbage collector managed, and it includes memory that Unity might have allocated and reused in subsequent frames. This means that the sum of the GC Alloc over all frames doesn’t total how much the managed memory grew in that time.

To get the most accurate information, you should always profile your application on a **development build** on the target platform or device you want to build to. The Unity Editor works in a different way to a build, and this affects the profiling data; for example, the `GetComponent` method always allocates memory when it’s executed in the Editor, but not in a built project.

You can also use the Call Stacks mode in the **Profiler**