---
title: "Optimize the physics system for memory usage"
category: "General"
source_file: "physics-optimization-memory.html"
doc_type: "manual"
---

# Optimize the physics system for memory usage

You can optimize how the Unity physics system uses memory resources by managing **collision** callback allocations and optimizing various physics queries. Efficient memory usage helps reduce garbage collection overhead and ensures smoother gameplay.

Use the guidance in these pages to maintain your target frame rate and ensure smooth, responsive gameplay. The instructions in these pages address issues identified by Unity Editor diagnostic tools. Before you apply these optimizations described in the documentation in this section and throughout your development, you must be familiar with these diagnostic tools:

  * **The Unity Profiler**
  * **The Memory Profiler**
  * **The Physics Debug window**

**Topic** | **Description**  
---|---  
**Optimize collision callbacks** | Reduce memory allocations caused by frequent collision events.  
**Optimize raycasts and other physics queries** | Optimize physics query performance and reduce garbage collection overhead by using efficient query versions and batch processing.  
  
## Additional resources

  * Unity Profiler
  * Built-in 3D Physics
  * Memory Profiler
  * Physics Project Settings