---
title: "Optimize physics performance"
category: "General"
source_file: "physics-optimization.html"
doc_type: "manual"
---

# Optimize physics performance

Optimize physics system performance in the Unity Editor. 

Use the guidance in these pages to optimize the physics system so you can maintain your target frame rate and ensure smooth, responsive gameplay. The instructions in these pages address issues identified by Unity Editor diagnostic tools. Before you apply the optimizations described in the documentation in this section and throughout your development, you must be familiar with these diagnostic tools:

  * **The Unity Profiler**: The Profiler is the primary tool to measure CPU performance. The Profiler helps identify bottlenecks in your project, particularly in areas such as `Physics.FixedUpdate` and `Physics.Simulate`, and in its detailed breakdowns of physics phases such as broad phase and narrow phase processing. To open the Profiler window, go to **Window > Analysis > Profiler**.
  * **The Memory Profiler**: Use the Memory **Profiler** to identify and optimize memory allocations caused by physics operations, such as excessive `RaycastHit` arrays or frequent **collision** data creation. You can use this information to reduce your garbage collection overhead.
  * **The Physics Debug** window: Use this tool to visually diagnose physics-related performance issues. It displays collision shapes, contacts, broad phase bounding boxes, and Rigidbody component sleep states. This helps you identify areas like overly complex colliders, unnecessary interactions, or objects failing to sleep, all of which contribute to performance bottlenecks. To open the Physics Debug window, select **Window > Analysis > Physics Debug**.

**Topic** | **Description**  
---|---  
**Optimize the physics system for CPU usage** | Optimize Unity’s physics system’s CPU usage by adjusting simulation frequency, managing **colliders** , and configuring **Rigidbody** , and configuring **Rigidbody** components.  
**Optimize the physics system for memory usage** | Optimize Unity’s physics system’s memory usage by controlling collision callbacks and optimizing physics queries.  
  
## Additional resources

  * Unity Profiler
  * Built-in 3D Physics
  * Memory Profiler
  * Physics Project Settings