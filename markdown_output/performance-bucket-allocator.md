---
title: "Bucket allocator"
category: "General"
source_file: "performance-bucket-allocator.html"
doc_type: "manual"
---

# Bucket allocator

The bucket allocator is a fast lock-free allocator that performs small allocations. Usually, the bucket allocator is used as a first step to speed up small allocations, before they go to the heap allocator.

The allocator reserves blocks of memory for allocations. Each block is divided into **subsections** of 16KB. This is not configurable, and does not appear in the user interface. Each subsection is divided into **allocations**. The allocation size is a multiple of a configured fixed size, called **granularity**.

## Example configuration

The following example configuration demonstrates the process of reserving blocks for allocations:

Shared Bucket Allocator for the Windows, Mac and Linux Player

In this setup, the total **block** size (**Bucket Allocator Block Size**) is 4MB, and the granularity of allocations (**Bucket Allocator Granularity**) is 16B. The first allocation is 16B, the second is 32B (2*16), then 48B, 64B, 80B, 96B, 112B, and 128B, for a total of eight buckets (**Bucket Allocator BucketCount**).

Each subsection contains a different number of buckets. To calculate the number of buckets in a subsection, divide the subsection size (16KB) by the granularity size. For example:

  * When the allocation granularity is 64B, 256 buckets fit in a subsection.
  * When the allocation granularity is 16B, 1,024 buckets fit in a subsection.

## Development and release build comparison

Bucket allocators produce different usage reports for a **development build** and a release build because in a development build each allocation has an additional 40B header. The following diagram demonstrates the difference between development and release builds for 16B and 64B allocations:

Development and Release builds comparison

The header is the reason the allocator reports being full after allocating only 2MB of its 4MB:
    
    
    [ALLOC_BUCKET]
          Large Block size 4.0 MB
          Used Block count 1
          Peak Allocated bytes 2.0 MB
          Failed Allocations. Bucket layout:
            16B: 64 Subsections = 18724 buckets. Failed count: 3889
            32B: 17 Subsections = 3868 buckets. Failed count: 169583
            48B: 31 Subsections = 5771 buckets. Failed count: 39674
            64B: 28 Subsections = 4411 buckets. Failed count: 9981
            80B: 17 Subsections = 2321 buckets. Failed count: 14299
            96B: 6 Subsections = 722 buckets. Failed count: 9384
            112B: 44 Subsections = 4742 buckets. Failed count: 5909
            128B: 49 Subsections = 4778 buckets. Failed count: 8715
    

In a release build for the same project, the allocator block size is enough:
    
    
    [ALLOC_BUCKET]
          Large Block size 4.0 MB
          Used Block count 1
          Peak Allocated bytes 3.3 MB
    

If the bucket allocator is full, the allocation falls back to another allocator. The usage report displays usage statistics, including how many allocations failed. If the report displays a fail count that increases linearly, it is likely that the failed allocations happen when calculating the frames, not the load. Fallback allocations are not a problem for a **scene** load, but they can impact performance if they happen when calculating frames. 

To prevent these fallback allocations, increase the block size, and limit the new block size to match the frames’ peak usage, rather than the scene load peak usage. This prevents the block from becoming so large that it reserves a lot of memory which is then not available at runtime.

> **Tip** : The Profiler allocators share an instance of a bucket allocator. You can customize this shared instance in the Profiler Shared Bucket Allocator.