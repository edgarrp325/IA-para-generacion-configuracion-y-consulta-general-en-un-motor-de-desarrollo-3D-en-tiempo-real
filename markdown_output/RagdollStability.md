---
title: "Joint and Ragdoll stability"
category: "General"
source_file: "RagdollStability.html"
doc_type: "manual"
---

# Joint and Ragdoll stability

This page provides tips for improving Joint and Ragdoll stability.

  * Avoid small Joint angles of **Angular Y Limit** and **Angular Z Limit**. Depending on your setup, the minimum angles should be around 5 to 15 degrees in order to be stable. Instead of using a small angle, try setting the angle to zero. This locks the axis and provide a stable simulation.
  * Uncheck the Joint’s **Enable Preprocessing** property. Disabling preprocessing can help prevent Joints from separating or moving erratically if they are forced into situations where there is no possible way to satisfy the Joint constraints. This can occur if Rigidbody components connected by Joints are pulled apart by static **collision** components connected by Joints are pulled apart by static **collision** geometry (for example, spawning a Ragdoll partially inside a wall).
  * Under extreme circumstances (such as spawning partially inside a wall or pushed with a large force), the joint solver is unable to keep the Rigidbody components of a Ragdoll together. This can result in stretching. To handle this, enable projection on the Joints using either ConfigurableJoint.projectionMode or CharacterJoint.enableProjection.
  * If Rigidbody components connected with Joints are jittering, open the Physics window (**Edit** > **Project Settings**
  * If Rigidbody components connected with Joints are not accurately responding to bounces, open the Physics window (**Edit** > **Project Settings** , then select the **Physics__category) and try increasing the** Default Solver Velocity Iterations__ value to between 10 and 20.
  * Never use direct Transform access with Kinematic Rigidbody components connected by Joints to other Rigidbody components. Doing so skips the step where PhysX computes internal velocities of corresponding Rigidbody components, making the solver provide unwanted results. A common example of bad practice is using direct Transform access in 2D projects to flip characters, by altering Transform.TransformDirection on the root bone of the rig. This behaves much better if you use Rigidbody2D.MovePosition and Rigidbody2D.MoveRotation instead.
  * Avoid large differences in the masses between Rigidbody components connected by Joints. It’s okay to have one Rigidbody with twice as much mass as another, but when one mass is ten times larger than the other, the simulation can become jittery.
  * Try to avoid scaling different from 1 in the Transform containing Rigidbody or the Joint. The scaling might not be robust in all cases.
  * If Rigidbody components are overlapping when inserted into the world, and you cannot avoid the overlap, try lowering the Rigidbody.maxDepenetrationVelocity to make the Rigidbody components exit each other more smoothly.