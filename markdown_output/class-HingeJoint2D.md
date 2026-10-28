---
title: "Hinge Joint 2D"
category: "General"
source_file: "class-HingeJoint2D.html"
doc_type: "manual"
---

# Hinge Joint 2D

Switch to Scripting

This **joint** allows a **GameObject** allows a **GameObject** controlled by **Rigidbody** controlled by **Rigidbody** 2D physics to be attached to a point in space around which it can rotate. The rotation can be left to happen passively (for example, in response to a collision) or can be actively powered by a motor torque provided by the Joint 2D itself. You can set limits to prevent the hinge from making a full rotation, or make more than a single rotation.

## Properties

Property | Function |   
---|---|---  
**Enable**Collision**** | Enable this property to enable collisions between the two connected GameObjects.  
**Connected Rigidbody** | Specify the other GameObject this joint connects to. If you leave this as **None** , the other end of the joint is fixed to a point in space defined by the **Connected Anchor** setting. Select the circle icon to the right to view a list of GameObjects to connect to.  
**Auto Configure Connected Anchor** | Enable this property to automatically set the anchor location for the other GameObject this **Hinge Joint** 2D connects to. You do not need to enter coordinates for the **Connected Anchor** property if you enable this property.  
**Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to this GameObject.  
**Connected Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to the other GameObject.  
**Use Motor** | Enable this to apply motor force to the joint.  
**Motor** | Select this to expand this property’s settings.  
| **Motor Speed** | Set the target motor speed (in degrees per second).  
| **Maximum Motor Force** | Set the maximum torque (or rotation) the motor can apply when attempting to reach the target speed.  
| **Use Limits** | Enable this to limit the rotation angle.  
**Angle Limits** | Select this to expand the Angle limits settings. Set the limits used when **User Limits** is enabled.  
| **Lower Angle** | Set the lower end of the rotation arc allowed by the limit.  
| **Upper Angle** | Set the upper end of the rotation arc allowed by the limit.  
**Break Action** | Set the action taken when either the force or torque threshold is exceeded.  
**Break Force** | Set the force threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
**Break Torque** | Set the torque threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
  
## Using this joint

The Hinge Joint 2D’s is used to have a joint that allows a GameObject to rotate around a particular point, for example a door hinge, wheels, or pendulums.

You can use this joint to make two points overlap. Those two points can be two **Rigidbody 2D** components, or a **Rigidbody 2D** component and a fixed position in the world space. Connect the Hinge Joint 2D to a fixed position in the world by setting **Connected Rigidbody** to **None**. The joint applies a linear force to both connected Rigidbody 2D GameObjects.

The Hinge Joint 2D has a simulated rotational motor which you can turn on or off. Set the **Maximum Motor Speed** and **Maximum Motor Force** to control the angular speed (**Torque**) and make the two Rigidbody 2D GameObjects rotate in an arc relative to each other. Set the limits of the arc using **Lower Angle** and **Upper Angle**.

### Constraints

Hinge Joint 2D has three simultaneous constraints. All are optional:

  * Maintain a relative linear distance between two anchor points on two Rigidbody 2D GameObjects.
  * Maintain an angular speed between two anchor points on two Rigidbody 2D GameObjects (limited with a maximum torque in **Maximum Motor Force**).
  * Maintain an angle within a specified arc.

You can use this joint to construct physical GameObjects that need to behave as if they are connected with a rotational pivot. For example:

  * A see-saw pivot where the horizontal section is connected to the base. Use the joint’s **Angle Limits** to simulate the highest and lowest point of the see-saw’s movement.
  * A pair of scissors connected together with a hinge pivot. Use the joint’s **Angle Limits** to simulate the closing and maximum opening of the scissors.
  * A simple wheel connected to the body of a car with the pivot connecting the wheel at its center to the car. In this example you can use the Hinge Joint 2D’s motor to rotate the wheel.

## Additional resources

  * Refer to Joints 2D for more information about other 2D Joints.

HingeJoint2D