---
title: "Dual thread allocator"
category: "General"
source_file: "performance-dual-thread-allocator.html"
doc_type: "manual"
---

# Dual thread allocator

The dual thread allocator is a wrapper that combines dynamic heap and bucket allocators. More specifically, it combines:

  * Two dynamic heap allocators: A lock-free allocator for the main thread, and an allocator that is shared by all other threads, which locks on allocation and deallocation. Unity uses these allocators for allocations that are too large for the bucket allocator. The dynamic heap allocator uses memory blocks. Allocations that are equal to or greater than half a block go to the virtual memory system instead of the dynamic heap allocator.
  * A bucket allocator for small allocations. If the bucket allocator is full, allocation spills over into the dynamic heap allocator.

You can customize the block sizes of the two dynamic heap allocators:

Main Allocator, with a custom value for Shared Thread Block Size

The usage report contains information for all three parts of the allocator. For example:
    
    
    [ALLOC_DEFAULT] Dual Thread Allocator
      Peak main deferred allocation count 135
        [ALLOC_BUCKET]
          Large Block size 4.0 MB
          Used Block count 1
          Peak Allocated bytes 3.3 MB
        [ALLOC_DEFAULT_MAIN]
          Peak usage frame count: [16.0 MB-32.0 MB]: 8283 frames, [32.0 MB-64.0 MB]: 1 frames
          Requested Block Size 16.0 MB
          Peak Block count 2
          Peak Allocated memory 53.3 MB
          Peak Large allocation bytes 40.2 MB
        [ALLOC_DEFAULT_THREAD]
          Peak usage frame count: [64.0 MB-128.0 MB]: 8284 frames
          Requested Block Size 16.0 MB
          Peak Block count 2
          Peak Allocated memory 78.3 MB
          Peak Large allocation bytes 47.3 MB
    

> **Note** : The **Peak main deferred allocation count** is the number of items in a deletion queue. The main thread must delete any allocation it made. If another thread deletes an allocation, that allocation is added to a queue. The allocation waits in the queue for the main thread to delete it. It is then counted as a deferred allocation.