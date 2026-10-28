---
title: "Spring Joint 2D"
category: "General"
source_file: "class-SpringJoint2D.html"
doc_type: "manual"
---

# Spring Joint 2D

Switch to Scripting

The **Spring**Joint** 2D** component allows two **GameObjects** 2D component allows two **GameObjects** controlled by **Rigidbody** controlled by **Rigidbody** physics to be attached together as if by a spring. The spring will apply a force along its axis between the two GameObjects, attempting to keep them a certain distance apart.

Property | Function  
---|---  
**Enable**Collision**** | Enable this property to enable collisions between the two connected GameObjects.  
**Connected Rigidbody** | Specify the other object this joint connects to. Leave this as **None** to have the other end of the joint fixed at a point in space defined by the **Connected Anchor** property. Select the circle icon to the right to view a list of GameObjects to connect to.  
**Auto Configure Connected Anchor** | Enable this property to automatically set the anchor location for the other object this joint connects to. You do not need to enter coordinates for the **Connected Anchor** property if you enable this property.  
**Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to the GameObject.  
**Connected Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to the other GameObject.  
**Auto Configure Distance** | Enable this property to automatically detect the distance between the two GameObjects and set it as the distance that the joint keeps between the two GameObjects.  
**Distance** | Set the distance that the spring should attempt to maintain between the two objects. (Can be set manually.)  
****Damping Ratio**** | Set the degree to suppress spring oscillation. In the range 0 to 1, the higher the value, the less movement.  
**Frequency** | Set the frequency at which the spring oscillates while the GameObjects are approaching the separation distance you want (measured in cycles per second). In the range 0 to 1,000,000 - the higher the value, the stiffer the spring. **Note:** Setting **Frequency** to zero will create the stiffest spring type joint possible.  
**Break Action** | Set the action taken when either the force or torque threshold is exceeded.  
**Break Force** | Set the force threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
  
## Using this joint

This joint behaves like a spring, while keeping a linear distance between two points. You set this via the **Distance** setting. Those two points can be two **Rigidbody2D** components or a **Rigidbody2D** component and a fixed position in the world. (Connect to a fixed position in the world by setting **Connected Rigidbody** to None). The joint applies a linear force to both rigid bodies. It doesn’t apply torque (an angle force). 

The joint uses a simulated spring. You can set the spring’s stiffness and movement:

A stiff, barely moving spring…

  * A high (1,000,000 is the highest) **Frequency** == a stiff spring.

  * A high (1 is the highest) **Damping Ratio** == a barely moving spring.

A loose, moving spring…

  * A low **Frequency** == a loose spring.

  * A low **Damping Ratio** == a moving spring.

When the spring applies its force between the objects, it tends to overshoot the distance you have set between them, and then rebound repeatedly, giving in a continuous oscillation. The **Damping Ratio** sets how quickly the objects stop moving. The **Frequency** sets how quickly the objects oscillate either side of the target distance.

This joint has one constraint:

  * Maintain a zero linear distance between two anchor points on two Rigidbody objects.

You can use this joint to construct physical objects that need to react as if they are connected together using a spring or a connection which allows rotation. For example:

  * A character who’s body is composed of multiple objects that act as if they are semi-rigid. Use the **Spring Joint** to connect the character’s body parts together, allowing them to flex to and from each other. You can specify whether the body parts are held together loosely or tightly.

**Note:** Spring Joint 2D uses a Box 2D spring-joint, which the Distance Joint 2D also uses with its frequency set to zero.

## Additional resources

  * Refer to Joints 2D for more information about other 2D Joints.

SpringJoint2D