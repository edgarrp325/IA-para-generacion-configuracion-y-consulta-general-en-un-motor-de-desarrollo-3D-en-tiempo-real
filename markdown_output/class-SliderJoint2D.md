---
title: "Slider Joint 2D"
category: "General"
source_file: "class-SliderJoint2D.html"
doc_type: "manual"
---

# Slider Joint 2D

Switch to Scripting

This **joint** allows a **GameObject** allows a **GameObject** controlled by **Rigidbody** controlled by **Rigidbody** physics to slide along a line in space. The object can freely move anywhere along the line in response to **collisions** physics to slide along a line in space. The object can freely move anywhere along the line in response to **collisions** or forces. Alternatively, it can be also be moved along by a motor force, with limits applied to keep its position within a certain section of the line.

Property | Function |   
---|---|---  
**Enable Collision** | Enable this property to enable collisions between the two connected GameObjects.  
**Connected Rigidbody** | Specify the other object this joint connects to. Leave this as **None** to have the other end of the joint fixed at a point in space defined by the **Connected Anchor** property. Select the circle icon to the right to view a list of GameObjects to connect to.  
**Auto Configure Connected Anchor** | Enable this property to automatically set the anchor location for the other object this joint connects to. You do not need to enter coordinates for the **Connected Anchor** property if you enable this property.  
**Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to this GameObject.  
**Connected Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to the other GameObject.  
**Auto Configure Angle** | Enable this property to automatically detect between the two GameObjects. The joint then keeps the same angle between the two GameObjects. You do not need to manually specify the angle when you enable this property.  
**Angle** | Enter the angle that the joint keeps between the two objects.  
**Use Motor** | Use the sliding motor? Check the box for yes.  
**Motor** | Expand for motor-related property settings.  
| **Motor Speed** | Set the target motor speed (meters/sec).  
| **Maximum Motor Force** | Set the maximum force the motor can apply while attempting to reach the target speed.  
**Use Limits** | Enable this property to set limits to the linear force.  
**Translation Limits** | Expand to set the limited distance that the translation can travel.  
| **Lower Translation** | Set the minimum distance the GameObject can be from the connected anchor point.  
| **Upper Translation** | Set the maximum distance the GameObject can be from the connected anchor point.  
**Break Action** | Set the action taken when either the force or torque threshold is exceeded.  
**Break Force** | Set the force threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
**Break Torque** | Set the torque threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
  
## Using this joint

Use this joint slide GameObjects by maintaining the position of two points on a configurable line that extends to infinity. Those two points can be two **Rigidbody2D** components, or a **Rigidbody2D** component and a fixed position in the world (by setting **Connected Rigidbody** to **None**).

The joint applies a linear force to both connected Rigidbody objects to keep them on the line. It also has a simulated linear motor that applies linear force to move the Rigidbody GameObjects along the line. You can turn the motor off or on. Although the line is infinite, you can specify just a segment of the line that you want to use, using the **Translation Limits** option.

This joint has three simultaneous constraints. All are optional:

  * Maintain a relative linear distance away from a specified line between two anchor points on two Rigidbody objects.
  * Maintain a linear speed between two anchor points on two Rigidbody objects along a specified line. (The speed is limited with a maximum force.)
  * Maintain a linear distance between two points along the specified line.

You can use this joint to construct physical objects that need to react as if they are connected together on a line. For example:

  * A platform which can move up or down. The platform reacts by moving down when something lands on it but must never move sideways. You can use this joint to ensure platform to never moves up or down beyond certain limits. Use the motor to make the platform move up.

## Additional resources

  * Refer to Joints 2D for more information about other 2D Joints.

SliderJoint2D