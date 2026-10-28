---
title: "Introduction to joints"
category: "General"
source_file: "Joints.html"
doc_type: "manual"
---

# Introduction to joints

A **joint** connects a **Rigidbody** to another Rigidbody or a fixed point in space. Joints apply forces that move rigid bodies, and joint limits restrict that movement. Joints give Rigidbodies the following degrees of freedom:

For details on joints in the PhysX system, including how twist and swing axes work, refer to NVidia PhysX documentation: Joints.

Unity provides the following joint components that apply different forces and limits to Rigidbody components, and give those bodies different motion:

**_Property:_** | **_Function:_**  
---|---  
Character Joint | Emulates a ball and socket joint, like a hip or shoulder. Constrains rigid body movement along all linear degrees of freedom, and enables all angular freedoms. Rigidbodies attached to a Character Joint orient around each axis and pivot from a shared origin.  
Configurable Joint | Emulates any skeletal joint, like those in a ragdoll. You can configure this joint to force and restrict rigid body movement in any degree of freedom.  
Fixed Joint | Restricts the movement of a rigid body to follow the movement of the rigid body it is attached to. This is useful when you need rigid bodies that easily break apart from each other, or you want to connect the movement of two rigid bodies without parenting in a Transform hierarchy.  
Hinge Joint | Attaches a rigid body to another rigid body or a point in space at a shared origin and allows the rigid bodies to rotate around a specific axis from that origin. Useful for emulating doors and finger joints.  
Spring Joint | Keeps rigid bodies apart from each other but lets the distance between them stretch slightly. The spring acts like a piece of elastic that tries to pull the two anchor points together to the exact same position.  
  
2D joints have **2D** at the end of the name (for example, Hinge Joint 2D). For a summary of the 2D joints , see Joints 2D documentation.

Joints also have other options that you can enable for specific effects. For example, you can set a joint to break when a Rigidbody applies a force to it that exceeds a certain threshold. Some joints allow a **drive force** to occur between the connected Rigidbodies to set them in motion automatically.

**Note:** If you want to build kinematic chains in the context of an industrial application, for example to simulate a robotic arm with realistic physics behavior, you should use physics articulations instead of the regular joints hereby described.