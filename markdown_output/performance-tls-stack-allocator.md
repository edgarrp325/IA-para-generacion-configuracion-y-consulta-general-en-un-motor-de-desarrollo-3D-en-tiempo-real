---
title: "Thread Local Storage (TLS) stack allocator"
category: "General"
source_file: "performance-tls-stack-allocator.html"
doc_type: "manual"
---

# Thread Local Storage (TLS) stack allocator

Each thread uses its own fast stack allocator for temporary allocations. These allocations are very fast, with a lifespan of less than a frame. The allocator uses a last in, first out (LIFO) stack.

The default block size for the temporary allocator is 4MB for the platforms and 16MB for the Unity Editor. You can customize these values.

> **Note** : If the allocator use exceeds the configured block size, Unity increases the block size. The limit for this increase is twice the original size.

Main Thread Block Size custom value in the Fast Per Thread Temporary Allocators

If a thread’s stack allocator is full, allocations fall back to the threadsafe linear allocator. A few overflow allocations are fine: 1 to 10 in a frame, or a few hundred during load. However, if the numbers grow on every frame, you can increase the block sizes. 

The information in the usage report can help you select a block size that is appropriate for your application. For example, in the following main thread usage report, the load peaks at 2.7MB, but the remaining frames are below 64KB. You can reduce the block size from 4MB to 64KB and allow the loading frame to spill over the allocations:
    
    
    [ALLOC_TEMP_TLS] TLS Allocator
      StackAllocators :
        [ALLOC_TEMP_MAIN]
          Peak usage frame count: [16.0 KB-32.0 KB]: 802 frames, [32.0 KB-64.0 KB]: 424 frames, [2.0 MB-4.0 MB]: 1 frames
          Initial Block Size 4.0 MB
          Current Block Size 4.0 MB
          Peak Allocated Bytes 2.7 MB
          Overflow Count 0
        [ALLOC_TEMP_Job.Worker 18]
    

In this second example, the worker thread is not used for large temporary allocations. To save memory, you can reduce the worker’s block size to 32KB. This is especially useful on a multi-core machine, where each worker thread has its own stack:
    
    
    [ALLOC_TEMP_Job.Worker 14]
          Initial Block Size 256.0 KB
          Current Block Size 256.0 KB
          Peak Allocated Bytes 18.6 KB
          Overflow Count 0