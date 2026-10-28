---
title: "Customize allocators"
category: "General"
source_file: "memory-allocator-customization.html"
doc_type: "manual"
---

# Customize allocators

> **Note:** Not all platforms support this feature. Refer to platform specific documentation for further information.

To customize allocator settings you can either edit the configurable values through the Editor UI or supply them as command line arguments.

## Use the Editor

  1. Select _Project Settings_ > _Memory Settings_.
  2. Select the lock icon next to the value you want to edit.

Project Settings > Memory Settings, showing a selection of Player memory settings

> **Note** : Refer to the previous individual allocator sections to see the fields customizable through the Editor UI.

## Use command line arguments

To find the name of the allocator parameters you want to change, check the list of allocator settings the Editor and players print when they start up. For example, to change the block size of the main heap allocators, use `-memorysetup-main-allocator-block-size=<new_value>`

The allocator parameter names and their default values:

**Allocator** | **Description** | **Parameter name** | **Default value**  
---|---|---|---  
Main Allocators | The allocators Unity uses for most allocations.  
| Main Allocator | The primary allocator Unity uses for most allocations.  
|  | Main Thread Block Size | Block size of dedicated main thread allocator. | `memorysetup-main-allocator-block-size` | `16777216`  
|  | Shared Thread Block Size | Block size of shared thread allocator. | `memorysetup-thread-allocator-block-size` | `16777216`  
| Gfx Allocator | The allocator Unity uses for CPU allocations related to the Gfx system.  
|  | Main Thread Block Size | Block size of the dedicated main thread Gfx allocator. | `memorysetup-gfx-main-allocator-block-size` | `16777216`  
|  | Shared Thread Block Size | Block size of the shared thread Gfx allocator. | `memorysetup-gfx-thread-allocator-block-size` | `16777216`  
| Other Allocators  
|  | File Cache Block Size | The file cache has its own allocator to avoid fragmentation. This is its block size. | `memorysetup-cache-allocator-block-size` | `4194304`  
|  | Type Tree Block Size | The type treess have their own allocator to avoid fragmentation due to many small allocations. This is its block size. | `memorysetup-typetree-allocator-block-size` | `2097152`  
| Shared Bucket Allocator | The bucket allocator that is shared between the main allocators.  
|  | Bucket Allocator Granularity | Step size for buckets in the shared allocator. | `memorysetup-bucket-allocator-granularity` | `16`  
|  | Bucket Allocator BucketCount | Number of bucket sizes. | `memorysetup-bucket-allocator-bucket-count` | `8`  
|  | Bucket Allocator Block Size | Size of memory blocks used for buckets. | `memorysetup-bucket-allocator-block-size` |  `Editor: 8388608`  
`Player: 4194304`  
|  | Bucket Allocator Block Count | Maximum number of blocks to be allocated. | `memorysetup-bucket-allocator-block-count` |  `Editor: 8`  
`Player: 1`  
Fast Per Thread Temporary Allocators | The Thread Local Storage (TLS) allocator that handles very short-lived allocations.  
| Main Thread Block Size | The initial size for the main thread stack. | `memorysetup-temp-allocator-size-main` |  `Editor: 16777216`  
`Player: 4194304`  
| Job Worker Block Size | Size of each job worker in the Unity job system. | `memorysetup-temp-allocator-size-job-worker` | `E262144`  
| Background Job Worker Block Size | Size for each background worker. | `memorysetup-temp-allocator-size-background-worker` | `32768`  
| Preload Block Size | The preload manager stack size. | `memorysetup-temp-allocator-size-preload-manager` |  `Editor: 33554432`  
`Player: 262144`  
| Audio Worker Block Size | Each audio worker thread’s stack size. | `memorysetup-temp-allocator-size-audio-worker` | `65536`  
| Cloud Worker Block Size | Cloud worker threads stack size. | `memorysetup-temp-allocator-size-cloud-worker` | `32768`  
| Gfx Thread Blocksize | The main render threads stack size. | `memorysetup-temp-allocator-size-gfx` | `262144`  
| GI Baking Blocksize | Each GI worker thread’s stack size. | `memorysetup-temp-allocator-size-gi-baking-worker` | `262144`  
| **NavMesh** Worker Block Size | Nav **mesh** worker threads stack size. | `memorysetup-temp-allocator-size-nav-mesh-worker` | `65536`  
Fast Thread Shared Temporary Allocators | Fast linear allocator for short lived allocations shared between threads.  
| Job Allocator Block Size | The round robin linear thread allocator Unity mainly uses for the job worker threads. | `memorysetup-job-temp-allocator-block-size` | `2097152`  
| Background Job Allocator Block Size | The linear allocator for the background workers that allows longer lived allocations. | `memorysetup-job-temp-allocator-block-size-background` | `21048576`  
| Job Allocator Block Size on low memory platforms | Platforms with less than 2GB memory use this size for both the job workers and the background jobs. | `memorysetup-job-temp-allocator-reduction-small-platforms` | `262144`  
**Profiler** Allocators | Allocators that Unity uses exclusively for the Profiler so that they don’t interfere with the application’s allocation patterns.  
| Profiler Block Size | The block size for the main part of the Profiler. | `memorysetup-profiler-allocator-block-size` | `16777216`  
| Editor Profiler Block Size | Block size for the Editor part of the Profiler. This is not present on players. | `memorysetup-profiler-editor-allocator-block-size` | `1048576`  
| Shared Profiler Bucket Allocator | Shared bucket allocator for the Profiler and Editor Profiler allocators.  
  
Not present on low memory platforms.  
|  | Bucket Allocator Granularity | Step size for buckets in the shared allocator. | `memorysetup-profiler-bucket-allocator-granularity` | `16`  
|  | Bucket Allocator BucketCount | Number of bucket sizes. For example, if the value is 4, the sizes are 16, 32, 48 and 64. | `memorysetup-profiler-bucket-allocator-bucket-count` | `8`  
|  | Bucket Allocator Block Size | Size of memory blocks used for buckets. | `memorysetup-profiler-bucket-allocator-block-size` |  `Editor: 33554432`  
`Player: 4194304`  
|  | Bucket Allocator Block Count | Maximum number of blocks to be allocated. | `memorysetup-profiler-bucket-allocator-block-count` |  `Editor: 8`  
`Player: 1`  
  
> **Tip** : To ensure your settings improve performance, profile the application before and after making changes. For more information, refer to the Profiler overview page and the package documentation for the Profiler Analyzer. Profiler Analyzer enables multiframe comparison, which is especially useful for highlighting differences in allocator performance. You can also check the memory usage reports. They are available in the log when you close the Player or Editor. To find your log files, follow the instructions on the log files page.

## Storing and reading the settings

Unity stores allocator settings in `MemorySettings.asset`and these settings are applied during the build process. This means new settings take effect at every build.

In the Editor, these settings are stored in the `ProjectSettings` folder and are updated every time Unity imports or changes `MemorySettings.asset`. New values for the Editor only take effect on the next Editor startup.