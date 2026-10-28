---
title: "Optimize raycasts and other physics queries"
category: "General"
source_file: "physics-optimization-raycasts-queries.html"
doc_type: "manual"
---

# Optimize raycasts and other physics queries

Optimize physics query performance and reduce garbage collection overhead by using efficient query versions and batch processing.

## Use non-allocating query versions

Standard physics queries, such as `Physics.Raycast`, `Physics.SphereCast`, or `Physics.OverlapSphere`, allocate memory on the heap for their results. This allocation can contribute to garbage collection pauses, especially if they are called frequently.

Instead, use the non-allocating counterparts of these queries that write their results into a pre-allocated array that you provide. Non-allocating counterparts can include:

  * `Physics.RaycastNonAlloc`
  * `Physics.SphereCastNonAlloc`
  * `Physics.OverlapSphereNonAlloc`

For example:
    
    
    int hitCount = Physics.RaycastNonAlloc(ray, preAllocatedHitsArray, distance, layerMask);
    

When you use non-allocating queries, you must provide a pre-allocated array. For example, `RaycastHit[] preAllocatedHitsArray = new RaycastHit[10];`. 

Size this array appropriately: make it large enough to capture the maximum expected hits in typical scenarios, but not so large as to waste memory. If the number of actual **colliders** found exceeds the size of your buffer array, only the results up to the array’s capacity are returned, and the rest are ignored.

**Tip:** Choose a buffer size that balances typical needs with memory considerations. Profile your game to understand common hit counts.

## Use batch queries for multiple operations

Running many individual physics queries (for example, many raycasts per frame) can reduce performance because of the overhead of each call. If you need to perform many queries simultaneously, batch them using APIs like `RaycastCommand`, `SpherecastCommand`, or `BoxcastCommand` in conjunction with the job system.

This approach leverages multi-threading to process queries in parallel, significantly improving performance for bulk query operations. This is particularly powerful when you have many independent raycasts (or other queries) that can be processed in parallel.

To use batch queries, follow these steps:

  1. Create and populate a `NativeArray<RaycastCommand>` with the parameters for all your raycasts.
  2. Allocate a `NativeArray<RaycastHit>` to store the results.
  3. Schedule the batch processing using `RaycastCommand.ScheduleBatch`, which returns a `JobHandle`.
  4. You can then perform other work, and later ensure the job is complete using `jobHandle.Complete` before you access the results. For example, ensure the job is complete at the start of the next frame or when needed.

## Additional resources

  * Unity Profiler
  * Memory Profiler
  * Physics Project Settings
  * RaycastCommand
  * Collections package