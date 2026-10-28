---
title: "Disabling garbage collection"
category: "General"
source_file: "performance-disabling-garbage-collection.html"
doc_type: "manual"
---

# Disabling garbage collection

You can use the GarbageCollector.GCMode to disable garbage collection at run time. This prevents CPU spikes, but the memory usage of your application never decreases, because the garbage collector doesn’t collect objects that no longer have any references.

**Warning:** Disabling the garbage collector requires careful memory management. If you don’t manage memory carefully, the managed heap continuously expands until your application runs out of memory, and the operating system shuts it down. 

You can use the following APIs to fine-tune control over the automatic garbage collector:

  * `System.GC.Collect`: Performs a full, blocking garbage collection.
  * GarbageCollector.Mode.Disabled: Fully disables the garbage collector. Using `System.Gc.Collect` in this mode has no effect.
  * GarbageCollector.Mode.Manual: Disables automatic invocations of the garbage collector, but you can still use `System.GC.Collect` to run a full collection.
  * `GarbageCollection.CollectIncremental`: Runs the garbage collector incrementally.

You should only disable garbage collection during short, performance-critical parts of your application, when you are able to calculate and control how much memory you need to allocate. You should immediately enable the garbage collector afterward, and profile your project often to ensure that you don’t trigger additional managed allocation which might cause the managed heap to get too big. 

When you disable the garbage collector, it doesn’t stop your application to perform a garbage collection. Calling `System.GC.Collect` has no effect and doesn’t start a collection. To avoid increased memory usage over time, you must take care when managing memory. Ideally, you should allocate all memory before you disable the garbage collector and avoid additional allocations while it is disabled.

It’s best practice to only disable the garbage collector for long-lived allocations. For example, you might want to allocate all required memory for a level of your game before it loads, and then disable the garbage collector to avoid performance overhead during the level. After the level is completed and all memory is released, you can then enable the garbage collector again and use `System.GC.Collect` to reclaim memory before loading the next level.

For more details on how to enable and disable garbage collection at run time, see the GarbageCollector Scripting API page.