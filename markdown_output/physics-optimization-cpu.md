---
title: "Optimize the physics system for CPU usage"
category: "General"
source_file: "physics-optimization-cpu.html"
doc_type: "manual"
---

# Optimize the physics system for CPU usage

You can optimize how the Unity physics system uses CPU resources in several ways. For example, you can adjust simulation frequency, carefully manage **collider** types, configure **Rigidbody** types, configure **Rigidbody** component behaviors, and more. Effective CPU optimization helps ensure your game maintains a high frame rate and responsive physics interactions.

Use the guidance in these pages to maintain your target frame rate and ensure smooth, responsive gameplay. The instructions in these pages address issues identified by Unity Editor diagnostic tools. Before you apply these optimizations described in the documentation in this section and throughout your development, you must be familiar with these diagnostic tools:

  * **The Unity Profiler**
  * **The Memory Profiler**
  * **The Physics Debug window**

**Topic** | **Description**  
---|---  
**Set fixed timestep to optimize physics simulation frequency** | Configure the fixed time step and manage potential performance spirals to control physics update frequency.  
**Manually set physics simulation** | Control over when physics calculations occur to align them with game performance.  
**Optimize physics for query-only or non-simulating games** | Prevent the default physics update loop from running to reduce unnecessary performance overhead.  
**Optimize transform value syncing** | Optimize the synchronization of Transform values with the physics system to improve performance and query accuracy.  
**Move static colliders** | Understand best practices for moving static colliders and when to use Kinematic **Rigidbody** components instead.  
**Use the layer collision matrix to reduce overlaps** | Reduce **collision** calculation overhead by configuring interaction rules between **GameObjects** calculation overhead by configuring interaction rules between **GameObjects** with collision layers.  
**Select a broad phase pruning algorithm** | Optimize physics performance in large **scenes** by selecting the most efficient broad phase pruning algorithm.  
**Collider types and performance** | Select the most efficient collider types for different GameObjects.  
**Configure Mesh Collider component cooking options for optimization** | Optimize physics calculations by configuring cooking options for ****Mesh** Collider** components  
**Use Rigidbody sleeping to improve physics performance** | Reduce CPU load and improve physics performance by enabling **Rigidbody** sleeping for stationary objects.  
**Adjust Rigidbody component solver iterations** | Adjust solver iteration counts for a **Rigidbody** component to improve simulation accuracy.  
**Optimize Rigidbody component collision detection modes** | Balance collision accuracy and CPU performance by choosing appropriate detection modes for **Rigidbody** components.  
  
## Additional resources

  * Unity Profiler
  * Built-in 3D Physics
  * Memory Profiler
  * Physics Project Settings