---
title: "Fixed Joint 2D"
category: "General"
source_file: "class-FixedJoint2D.html"
doc_type: "manual"
---

# Fixed Joint 2D

Switch to Scripting

Use the **Fixed**Joint** 2D** to connect two **GameObjects** 2D to connect two **GameObjects** controlled by **Rigidbody** controlled by **Rigidbody** 2D physics to keep them in a position relative to each other, so the GameObjects are always offset at a given position and angle. It is a spring-type 2D joint for which you don’t need to set maximum forces. You can set the spring to be rigid or soft.

Refer to Fixed Joint 2D and Relative Joint 2D for the differences between ****Fixed Joint** 2D** and ****Relative Joint 2D****.

Property | Function  
---|---  
**Enable**Collision**** | Enable this property to enable collisions between the two connected GameObjects.  
**Connected Rigid Body** | Specify the other object this joint connects to. Leave this as **None** to have the other end of the joint fixed at a point in space defined by the **Connected Anchor** property. Select the circle icon to the right to view a list of GameObjects to connect to.  
**Auto Configure Connected Anchor** | Enable this property to automatically set the anchor location for the other object this joint connects to. You do not need to enter coordinates for the **Connected Anchor** property if you enable this property.  
**Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to this GameObject.  
**Connected Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to the other GameObject.  
****Damping Ratio**** | Set the degree to suppress spring oscillation. In the range 0 to 1, the higher the value, the less movement.  
**Frequency** | Set the frequency at which the spring oscillates while the GameObjects are approaching the separation distance you want (measured in cycles per second). In the range 0 to 1,000,000 - the higher the value, the stiffer the spring. **Note:** Setting **Frequency** to zero will create the stiffest spring type joint possible.  
**Break Action** | Set the action taken when either the force or torque threshold is exceeded.  
**Break Force** | Set the force threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
**Break Torque** | Set the torque threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
  
## Using this joint

The aim of this joint is to maintain a relative linear and angular offset between two points. Those two points can be two **Rigidbody 2D** components or a **Rigidbody 2D** component and a fixed position in the world. (Connect to a fixed position in the world by setting **Connected Rigidbody** to None). 

The linear and angular offsets are based upon the relative positions and orientations of the two connected points, so you change the offsets by moving the connected GameObjects in your **Scene** view. 

The joint applies both linear and torque forces to connected Rigidbody 2D GameObjects. It uses a simulated spring that is pre-configured to be as stiff as the simulation can provide. You can change the spring’s value to make it weaker using the **Frequency** setting.

When the spring applies its force between the GameObjects, it tends to overshoot the desired distance between them and then rebound repeatedly, resulting in a continuous oscillation. The damping ratio determines how quickly the oscillation reduces and brings the GameObjects to rest. The frequency is the rate at which it oscillates either side of the target distance; the higher the frequency, the stiffer the spring.

Fixed Joint 2D has two simultaneous constraints:

  * Maintain the linear offset between two anchor points on two Rigidbody 2D GameObjects.
  * Maintain the angular offset between two anchor points on two Rigidbody 2D GameObjects.

You can use this joint to construct physical GameObjects that need to react as if they are rigidly connected. They can’t move away from each other, they can’t move closer together, and they can’t rotate with respect to each other, such as a bridge made of sections which hold rigidly together.

You can also use this joint to create a less rigid connection that flexes - for example, a bridge made of sections which are slightly flexible.

## Comparing Fixed and Relative joints 2D 

It is important to know the major differences between **Fixed Joint 2D** and Relative Joint 2D:

  * **Fixed Joint 2D** is a spring-type joint. **Relative Joint 2D** is a motor-type joint with a maximum force and/or torque.
  * **Fixed Joint 2D** uses a spring to maintain the relative linear and angular offsets. **Relative Joint 2D** uses a motor. You can configure a joint’s spring or motor.
  * **Fixed Joint 2D** works with anchor points (it’s derived from script **Anchored Joint 2D**); it maintains the relative linear and angular offset between the anchors. **Relative Joint 2D** doesn’t have anchor points (it’s derived directly from script **Joint 2D**).
  * **Fixed Joint 2D** cannot modify the relative linear and angular offsets in real time. **Relative Joint 2D** can.

## Additional resources

  * Refer to Joints 2D for more information about other 2D Joints.

FixedJoint2D