---
title: "Relative Joint 2D"
category: "General"
source_file: "class-RelativeJoint2D.html"
doc_type: "manual"
---

# Relative Joint 2D

Switch to Scripting

The **Relative**Joint** 2D** connects two **GameObjects** 2D connects two **GameObjects** controlled by **Rigidbody** controlled by **Rigidbody** physics to maintain in a position based on each other’s location. Use this joint to keep two objects offset from each other, at a position and angle you decide.

Refer to Comparing Fixed and Relative joints 2D for the differences between **Relative Joint2D** and **FixedJoint2D**.

Property | Function  
---|---  
**Enable**Collision**** | Enable this property to enable collisions between the two connected GameObjects.  
**Connected Rigid Body** | Specify the other object this joint connects to. Leave this as **None** to have the other end of the joint fixed at a point in space defined by the **Connected Anchor** property. Select the circle icon to the right to view a list of GameObjects to connect to.  
**Max Force** | Set the linear (or straight line) movement between joined GameObjects. A high value (up to 1,000) uses high force to maintain the offset.  
**Max Torque** | Set the angular (or rotation) movement between joined GameObjects. A high value (up to 1000) uses high force to maintain the offset.  
**Correction Scale** | Tweak the joint to correct its behavior if required. Increasing the **Max Force** or **Max Torque** may affect the joint’s behavior such that the joint doesn’t reach its target, requiring you to correct it by adjusting this setting. The default setting is 0.3.  
**Auto Configure Offset** | Enable this property to automatically set and maintain the distance and angle between the connected objects. You do not need to manually enter the **Linear Offset** and **Angular Offset** when you enable this property.  
**Linear Offset** | Enter local space coordinates to specify and maintain the distance between the connected objects.  
**Angular Offset** | Enter local space coordinates to specify and maintain the angle between the connected objects.  
**Break Action** | Set the action taken when either the force or torque threshold is exceeded.  
**Break Force** | Set the force threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
**Break Torque** | Set the torque threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
  
## Using this joint

The aim of this joint is to maintain a relative linear and angular distance (offset) between two points. Those two points can be two **Rigidbody2D** components or a **Rigidbody2D** component and a fixed position in the world. **Note:** Connect to a fixed position in the world by setting **Connected Rigidbody** to None.

The joint applies a linear and angular (torque) force to both connected Rigidbody objects. It uses a simulated motor that is preconfigured to be quite powerful: It has a high **Max Force** and **Max Torque** limit. You can lower these values to make the motor less powerful motor or turn-off it off completely.

This joint has two simultaneous constraints:

  * Maintain the specified linear offset between the two Rigidbody objects.
  * Maintain the starting angular offset between the two Rigidbody objects.

You can use this joint to construct physical objects that need to:

  * Keep a distance apart from each other, as if they are unable to move further away from each other or closer together. (You decide the distance they are apart from each other. The distance can change in real-time.)
  * Rotate with respect to each other only at particular angle. (You decide the angle.)

Some uses may need the connection to be flexible, such as: A space-shooter game where the player has extra gun batteries that follow them. You can use the Relative Joint to give the trailing gun batteries a slight lag when they follow, but make them rotate with the player with no lag.

Some uses may need a configurable force, such as: A game where the **camera** follows a player using a configurable force to keep track.

## Comparing Fixed and Relative joints 2D 

**FixedJoint2D** is spring type joint. **RelativeJoint2D** is a motor type joint with a maximum force and/or torque. 

  * The **Fixed Joint** uses a spring to maintain the relative linear and angular offsets and the Relative joint uses a motor. You can configure a joint’s spring or motor.
  * The Fixed joint works with anchor points (it’s derived from script **AnchoredJoint2D**): It maintains the relative linear and angular offset between the anchors. The Relative joint doesn’t have anchor points (it’s derived directly from script **Joint2D**).
  * The Relative joint can modify the relative linear and angular offsets in real time: The Fixed joint cannot.

## Additional resources

  * Refer to Joints 2D for more information about other 2D Joints.

RelativeJoint2D