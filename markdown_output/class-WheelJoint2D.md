---
title: "Wheel Joint 2D"
category: "General"
source_file: "class-WheelJoint2D.html"
doc_type: "manual"
---

# Wheel Joint 2D

Switch to Scripting

Use the **Wheel**Joint** 2D** to simulate a rolling wheel, on which an object can move. You can apply motor power to the joint. The wheel uses a suspension spring to maintain its distance from the main body of the vehicle.

## Properties

Property | Function |   
---|---|---  
**Enable**Collision**** | Enable this property to enable collisions between the two connected **GameObjects**.  
**Connected Rigid Body** | Specify the other GameObject this joint connects to. If you leave this as **None** , the other end of the joint is fixed to a point in space defined by the **Connected Anchor** setting. Select the circle icon to the right to view a list of GameObjects to connect to.  
**Auto Configure Connected Anchor** | Enable this property to automatically set the anchor location for the other GameObject this **Hinge Joint** 2D connects to. You do not need to enter coordinates for the **Connected Anchor** property if you enable this property.  
**Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to this GameObject.  
**Connected Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to the other GameObject.  
**Suspension** | Select this to expand this property’s settings.  
| ****Damping Ratio**** | Set the degree to suppress spring oscillation. In the range 0 to 1, the higher the value, the less movement.  
| **Frequency** | Set the frequency at which the spring oscillates while the GameObjects are approaching the separation distance you want (measured in cycles per second). In the range 0 to 1,000,000 - the higher the value, the stiffer the spring. **Note:** Setting **Frequency** to zero will create the stiffest spring type joint possible.  
| **Angle** | Set the world movement angle for the suspension.  
**Use Motor** | Enable this to apply motor force to the joint.  
**Motor** | Select this to expand this property’s settings.  
| **Motor Speed** | Target speed (degrees per second) for the motor to reach.  
| **Maximum Motor Force** | Set the maximum torque (or rotation) the motor can apply when attempting to reach the target speed.  
**Break Action** | Set the action taken when either the force or torque threshold is exceeded.  
**Break Force** | Set the force threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
**Break Torque** | Set the torque threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
  
## Using this joint

Use this joint to simulate wheels and suspension. The aim of the joint is to keep the position of two points on a line that extends to infinity, whilst at the same time making them overlap. Those two points can be two **Rigidbody2D** components or a **Rigidbody2D** component and a fixed position in the world. (Connect to a fixed position in the world by setting **Connected Rigidbody** to None). 

Wheel Joint 2D acts like a combination of a Slider Joint 2D (without its motor or limit constraints) and a Hinge Joint 2D (without its limit constraint).

The joint applies a linear force to both connected rigid body objects to keep them on the line, an angular motor to rotate the objects on the line, and a spring to simulate wheel suspension.

Set the **Maximum Motor Speed** and **Maximum Motor Force** (torque, in this joint) to control the angular motor speed, and make the two rigid body objects rotate.

You can set the wheel suspension stiffness and movement in order to simulate different degrees of suspension. For example, to simulate a stiff, barely moving suspension:

  * Set a high (1,000,000 is the highest) **Frequency** == stiff suspension.

  * Set a high (1 is the highest) **Damping Ratio** == barely moving suspension.

To simulate a looser and more freely moving suspension, you would use the following settings:

  * Set a low **Frequency** == loose suspension.

  * Set a low **Damping Ratio** == moving suspension.

It has two simultaneous constraints:

  * Maintain a zero relative linear distance away from a specified line between two anchor points on two rigid body objects.
  * Maintain an angular speed between two anchor points on two rigid body objects. (Set the speed via the **Maximum Motor Speed** option and maximum torque via **Maximum Motor Force**.)

You can use this joint to construct physical objects that need to react as if they are connected with a rotational pivot but cannot move away from a specified line. Such as:

  * Simulating wheels with a motor to drive the wheels and a line defining the movement allowed for the suspension.

## Behavior difference to the Wheel Collider

Unlike the Wheel Collider used with 3D physics, the Wheel Joint 2D uses a separate ****Rigidbody**** used with 3D physics, the Wheel Joint 2D uses a separate ****Rigidbody**** object for the wheel, which rotates when the force is applied. (The Wheel Collider, by contrast, simulates the suspension using a raycast and the wheel’s rotation is purely a graphical effect). The wheel object will typically be a Circle Collider 2D with a Physics Material 2D object for the wheel, which rotates when the force is applied. (The Wheel Collider, by contrast, simulates the suspension using a raycast and the wheel’s rotation is purely a graphical effect). The wheel object will typically be a Circle Collider 2D with a Physics Material 2D that gives the right amount of traction for your gameplay.

## Additional resources

  * Refer to Joints 2D for more information about other 2D Joints.

WheelJoint2D