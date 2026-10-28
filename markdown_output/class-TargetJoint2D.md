---
title: "Target Joint 2D"
category: "General"
source_file: "class-TargetJoint2D.html"
doc_type: "manual"
---

# Target Joint 2D

Switch to Scripting

This **joint** connects to a specified target, rather than another **Rigidbody** connects to a specified target, rather than another **Rigidbody** object as other joints do. This behaves in a similar way to a spring type joint.

Property | Function  
---|---  
**Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to this **GameObject**.  
**Target** | Define where (in terms of x, y-coordinates in world space) the other end of the joint attempts to move.  
**Auto Configure Target** | Enable this property to automatically set the other end of the joint to the current position of the GameObject. **Note:** When this option is enabled, the target changes as you move the GameObject but the target will not change if the option is not enabled.  
**Max Force** | Set the force that the joint can apply when attempting to move the object to the **target position**. The higher the value, the higher the maximum force.  
****Damping Ratio**** | Set the degree to suppress spring oscillation. In the range 0 to 1, the higher the value, the less movement.  
**Frequency** | Set the frequency at which the spring oscillates while the GameObjects are approaching the separation distance you want (measured in cycles per second). In the range 0 to 1,000,000 - the higher the value, the stiffer the spring. **Note:** Setting **Frequency** to zero will create the stiffest spring type joint possible.  
**Break Action** | Set the action taken when either the force or torque threshold is exceeded.  
**Break Force** | Set the force threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
  
## Using this joint

Use this joint to connect a Rigidbody GameObject to a point in space. The aim of this joint is to keep zero linear distance between two points: An anchor point on a Rigidbody object and a world space position, called the “**Target** ”. The joint applies linear force to the Rigidbody object, it does not apply torque (angular force).

The joint uses a simulated spring. You can set the spring’s stiffness and movement by adjusting its settings. For example, to set a stiff and barely moving spring:

  * Set a high (1,000,000 is the highest) **Frequency** == a stiff spring.

  * Set a high (1 is the highest) **Damping Ratio** == a barely moving spring.

To simulate a looser and more freely moving spring, you would use the following settings:

  * Set a low **Frequency** == a loose spring.

  * Set a low **Damping Ratio** == a moving spring.

When the spring applies its force between the Rigidbody object and target, it tends to overshoot the distance you have set between them, and then rebound repeatedly, giving in a continuous oscillation. The **Damping Ratio** sets how quickly the Rigidbody object stops moving. The **Frequency** sets how quickly the Rigidbody object oscillates either side of the distance you have specified.

This joint has one constraint:

  * Maintain a zero linear distance between the anchor point on a Rigidbody object and a world space position (**Target**).

You can use this joint to construct physical objects that need to move to designated target positions and stay there until another target position is selected or the target is cleared. For example:

  * A game where players pick up cakes, using a mouse-click, and drag them into to a plate. You can use this joint to move each cake to the plate.

You could also use the joint to allow objects to hang: If the anchor point is not the **center of mass** , then the object will rotate. Such as:

  * A game where players pick up boxes. If they use a mouse-click to pick a box up by its corner and drag it, it will hang from the cursor.

## Additional resources

  * Refer to Joints 2D for more information about other 2D Joints.

TargetJoint2D