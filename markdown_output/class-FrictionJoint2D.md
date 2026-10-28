---
title: "Friction Joint 2D"
category: "General"
source_file: "class-FrictionJoint2D.html"
doc_type: "manual"
---

# Friction Joint 2D

Switch to Scripting

The **Friction**Joint** 2D** connects **GameObjects** 2D connects **GameObjects** controlled by **Rigidbody** controlled by **Rigidbody** 2D physics. The Friction Joint 2D reduces both the linear and angular velocities between the objects to zero (ie, it slows them down).

Property | Function  
---|---  
**Enable**Collision**** | Enable this property to enable collisions between the two connected GameObjects.  
**Connected Rigid Body** | Specify the other object this joint connects to. Leave this as **None** to have the other end of the joint fixed at a point in space defined by the **Connected Anchor** property. Select the circle icon to the right to view a list of GameObjects to connect to.  
**Auto Configure Connected Anchor** | Enable this property to automatically set the anchor location for the other object this joint connects to. You do not need to enter coordinates for the **Connected Anchor** property if you enable this property.  
**Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to this GameObject.  
**Connected Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to the other GameObject.  
**Max Force** | Set the linear (or straight line) movement between joined GameObjects. A high value resists the linear movement between GameObjects.  
**Max Torque** | Set the angular (or rotation) movement between joined GameObjects. A high value resists the rotation movement between GameObjects.  
**Break Action** | Set the action taken when either the force or torque threshold is exceeded.  
**Break Force** | Set the force threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
**Break Torque** | Set the torque threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
  
## Using this joint

Use the Friction Joint 2D to slow down movement between two points to a stop. This joint’s aim is to maintain a zero relative linear and angular offset between two points. Those two points can be two **Rigidbody 2D** components or a **Rigidbody 2D** component and a fixed position in the world. (Connect to a fixed position in the world by setting **Connected Rigidbody** to None).

### Resistance

The joint applies linear force (**Force**) and angle force (**Torque**) to both Rigidbody 2D points. It uses a simulated motor that is pre-configured to have a low motor power (and so, low resistance). You can change the resistance to make it weaker or stronger.

Strong Resistance:

  * A high (1,000,000 is the highest) **Max Force** creates strong linear resistance. The Rigidbody 2D GameObjects won’t move in a line relative to each other very much.
  * A high (1,000,000 is the highest) **Max Torque** creates strong angular resistance. The Rigidbody 2D GameObjects won’t move at an angle relative to each other very much.

Weak Resistance:

  * A low **Max Force** creates weak linear resistance. The Rigidbody 2D GameObjects move easily in a line relative to each other.
  * A low **Max Torque** creates weak angular resistance. The Rigidbody 2D GameObjects move easily at an angle relative to each other.

### Constraints

Friction Joint 2D has two simultaneous constraints:

  * Maintain a zero relative linear velocity between two anchor points on two Rigidbody 2Ds
  * Maintain a zero relative angular velocity between two anchor points on two Rigidbody 2Ds

You can use this joint to construct physical GameObjects that need to behave as if they have friction. They can resist either linear movement or angular movement, or both linear and angular movement. For example:

  * A platform that does rotate, but resists applied forces, making it difficult but possible for the player to move it.
  * A ball that resists linear movement. The ball’s friction is related to the GameObject’s velocity and not to any collisions. It acts like the **Linear Drag** and **Angular Drag** which is set in **Rigidbody 2D**. The difference is that Friction Joint 2D has the option of maximum **Force** and **Torque** settings.)

## Additional resources

  * Refer to Joints 2D for more information about other 2D Joints.

FrictionJoint2D