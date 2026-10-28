---
title: "Dynamic heap allocator"
category: "General"
source_file: "performance-dynamic-heap-allocator.html"
doc_type: "manual"
---

# Dynamic heap allocator

The dynamic heap allocator is the main heap allocator. It applies the algorithm Two Level Segregated Fit (TLSF) to blocks of memory.

Each platform has a default block size, which you can customize. An allocation must be smaller than half a block. An allocation of half a block or more is too large for the dynamic heap allocator and in such cases Unity uses the virtual memory API to make the allocation instead.

An example usage report for the dynamic heap allocator:
    
    
    [ALLOC_DEFAULT_MAIN]
    Peak usage frame count: [16.0 MB-32.0 MB]: 497 frames, [32.0 MB-64.0 MB]: 1 frames
    Requested Block Size 16.0 MB
    Peak Block count 2
    Peak Allocated memory 54.2 MB
    Peak Large allocation bytes 40.2 MB
    

In this example, the TLSF block size is set to 16 MB, and Unity has allocated two blocks. The peak usage of the allocator was 54.2MB. Of those 52.4MB, 40.2MB were not allocated in the TLSF block, and instead fell back to virtual memory. Most frames had 16–32MB of allocated memory, while one frame - likely the loading frame - peaked at 32–64MB of memory.

If you increased the block size the large allocation would stay in the dynamic heap rather than fall back into virtual memory. However, that block size could lead to memory waste, because the blocks might not be fully used.

> **Tip** : The type tree and file cache allocators use dynamic heap allocation. To save the memory blocks they would otherwise use under this algorithm, you can set the type tree block size and file cache block size to 0. Allocations that would have used typetree and cache will then fall back to the main allocator instead. **Note** that this comes with the risk of increased native memory fragmentation. Refer to Customize allocators for how to set these block sizes.