---
title: "Optimize Rigidbody component collision detection modes"
category: "General"
source_file: "physics-optimization-cpu-rigidbody-collision-modes.html"
doc_type: "manual"
---

# Optimize Rigidbody component collision detection modes

Set the ****Collision** Detection** mode on a **Rigidbody** component in the **Inspector** Detection mode on a **Rigidbody** component in the **Inspector** window to balance simulation accuracy, and prevent phenomena such as fast-moving objects from passing through other objects, against CPU performance.

When you enable **Collision Detection** modes, always profile and monitor performance. Some **Collision Detection** modes, especially **Continuous** and **Continuous Dynamic** , can significantly impact CPU usage. Apply them selectively and only where needed.

To learn more about ****Rigidbody**** component collision detection modes, refer to Rigidbody component reference.

The available collision detection modes include:

  * **Discrete** : Checks for collisions only at the discrete time points of each physics simulation step. This is the default collision detection mode and the most performant. The risk when using **Discrete** is that fast objects can tunnel if they pass entirely through another **collider** between physics steps. Use **Discrete** for most objects, especially when they aren’t exceptionally fast or where occasional tunneling is acceptable.
  * **Continuous** : Prevents tunneling through static geometry. Uses sweep-based continuous collision detection (CCD) to ensure the **GameObject**
  * **Continuous Dynamic** : Uses sweep-based CCD against both static colliders and other **Rigidbody** components that are also set to **Continuous Dynamic** or **Continuous**. **Continuous Dynamic** has the highest CPU usage and that usage increases with the number of potential interactions. Use sparingly and only for critical, very fast-moving objects that absolutely must not tunnel through other specifically-marked fast-moving dynamic objects.
  * **Continuous Speculative** : Uses a Speculative CCD approach to prevent tunneling against both static and dynamic colliders. Often the best choice for CCD. **Continuous Speculative** is generally balanced performance and simulation quality. It is often more performant than **Continuous** modes for similar or better tunneling prevention. Use **Continuous Speculative** when **Discrete** mode results in tunneling for fast-moving objects.

To determine the ideal **Collision Detection** mode for a **Rigidbody** component, the recommended best practice is to:

  * Start with the **Discrete** mode for most **Rigidbody** components. **Discrete** is the most performant and sufficient for most objects that don’t move exceptionally fast or where occasional tunneling is acceptable.
  * If tunneling occurs with fast objects, switch to **Continuous Speculative**.
  * If tunneling still occurs with **Continuous Speculative** or you want to have specific interactions with static geometry, switch to **Continuous**.
  * Set to **Continuous Dynamic** only as a last resort for critical object-on-object tunneling.

## Additional resources

  * Unity Profiler
  * Memory Profiler
  * Physics Project Settings
  * Rigidbody component reference
  * Collision detection
  * Sweep-based CCD
  * Speculative CCD