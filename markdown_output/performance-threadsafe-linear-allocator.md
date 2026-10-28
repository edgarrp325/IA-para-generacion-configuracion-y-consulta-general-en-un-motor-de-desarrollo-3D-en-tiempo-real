---
title: "Thread-safe linear allocator"
category: "General"
source_file: "performance-threadsafe-linear-allocator.html"
doc_type: "manual"
---

# Thread-safe linear allocator

The worker threads in Unity use a round robin first in, first out (FIFO) algorithm for fast, lock-free allocations of work buffers for jobs. The jobs dispose of the buffers when done.

This allocator allocates blocks of memory, then linearly allocates memory within those blocks. Available blocks are held in a pool. When one block is full, the allocator fetches a new block from the pool. When the allocator no longer needs the memory in a block, it clears the block, and the block returns to the pool of available blocks. It is important to clear allocations quickly to make blocks available again, so a job should not stay allocated for more than a few frames.

You can customize the block size. The allocator allocates up to 64 blocks, as needed.

Default value for Fast Thread Shared Temporary Allocators for the Editor

If all blocks are in use, or an allocation is too big for a block, the allocation falls back to the main heap allocator, which is much slower than the job allocator. A few overflow allocations are fine: 1 to 10 in a frame, or a few hundred, especially during load. If the overflow count grows with every frame, you can increase the block size to avoid fallback allocations. However, if you increase the block size too much (for example, to match peak use in events such as scene loading), you might leave a lot of memory unavailable during play.

For example:
    
    
    [ALLOC_TEMP_JOB_4_FRAMES (JobTemp)]
      Initial Block Size 0.5 MB
      Used Block Count 64
      Overflow Count (too large) 0
      Overflow Count (full) 50408
    

In this example usage report, the 0.5MB block size was too small to accommodate the job memory that the application needed, and the full allocator caused a large number of allocations to overflow.

To check whether your build’s frame overflow is sufficient, run it for a short time and then for a longer time. If the overflow count remains steady, the overflow is a high watermark that occurs during load. If the overflow count increases with a longer run, the build is processing a per-frame overflow. In both cases, you can increase the blocksize to reduce the overflow, but the overflow is less critical during load than per frame.