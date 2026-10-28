---
title: "Move static colliders to prevent performance issues"
category: "General"
source_file: "physics-optimization-cpu-static-colliders.html"
doc_type: "manual"
---

# Move static colliders to prevent performance issues

Properly manage static **colliders** when they move to avoid performance issues.

A Static collider is a **GameObject** with a Collider component but no **Rigidbody** or ArticulationBody component attached. You can use static colliders for objects that don’t move during gameplay, such as **terrain** or ArticulationBody component attached. You can use static colliders for objects that don’t move during gameplay, such as **terrain** , buildings, or other environmental features. 

When you move a static collider by changing its transform values, the physics system detects the change and updates its internal spatial structures during the next physics step or when `Physics.SyncTransforms` is called. If you want to make frequent changes to the transform values of a static collider between physics simulations steps when you execute gameplay code, use a Kinematic Rigidbody component instead.

If you want to move a static collider, the recommended best practice is that you don’t add a Rigidbody component to a static object solely to move that GameObject. If it doesn’t need a physics simulation, you’re adding an unnecessary performance burden.

## Additional resources

  * Unity Profiler
  * Memory Profiler
  * Physics Project Settings
  * Introduction to collider types