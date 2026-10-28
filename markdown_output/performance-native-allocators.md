---
title: "Native memory"
category: "General"
source_file: "performance-native-allocators.html"
doc_type: "manual"
---

# Native memory

> **Note** : The information on allocators in this section applies to **native memory only** and is **not** applicable to the managed heap, which is covered in the Managed memory section. This section assumes you have a general understanding of native memory management and allocators.

An application uses memory allocators to balance performance and available memory space. If an application has a lot of spare memory, it can favour faster, memory-heavy allocators when it loads **scenes** and frames. However, if the application has limited memory, it needs to use that memory efficiently, even if that means using slower allocators. To help you get the best performance for different projects, you can customize Unity’s allocators to fit the size and requirements of each application. 

Unity has five allocator types. Each type has a different algorithm for fitting allocations into blocks of memory, and is therefore useful for different allocations. The important difference between allocations is usually persistence, or allocation lifespan, which determines where an allocation should go. For example, a long-lived (persistent) allocation goes to the heap and bucket allocators, while short-lived allocations go to the threadsafe linear and TLS allocators.

This table lists the algorithm and uses of each allocator type:

**Allocator type** | **Algorithm** | **Used for**  
---|---|---  
Dynamic heap | Two Level Segregated Fit (TLSF) | • Main allocator  
• Gfx allocator  
• Typetree allocator  
• File cache allocator  
• Profiler allocator  
• Editor Profiler allocator (on Editor only)  
Bucket | Fixed size lock-free allocator | As a shared allocator for small allocations for:  
  
• Main allocator  
• Gfx allocator  
• Typetree allocator  
• File cache allocator  
Dual thread | Redirects allocations based on size and thread ID | • Main allocator  
• Gfx allocator  
• Typetree allocator  
• File cache allocator  
Thread Local Storage (TLS) stack | LIFO stack | Temporary allocations  
Threadsafe linear | Round robin FIFO | Buffers for passing data to jobs  
  
> **Note** : The examples in this documentation use the memory usage reports that are written to the log when you close the Player or Editor if you have used the `-log-memory-performance-stats` command line argument. To find your log files, follow the instructions on the log files page.