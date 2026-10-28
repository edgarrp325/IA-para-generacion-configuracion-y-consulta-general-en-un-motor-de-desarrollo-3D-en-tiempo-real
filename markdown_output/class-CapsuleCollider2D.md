---
title: "Capsule Collider 2D"
category: "General"
source_file: "class-CapsuleCollider2D.html"
doc_type: "manual"
---

# Capsule Collider 2D

Switch to Scripting

The **Capsule**Collider** 2D** is a Collider that interacts with the 2D physics system. The capsule shape has no vertex corners and has a continuous round circumference. This shape allows the **Capsule Collider** 2D is a Collider that interacts with the 2D physics system. The capsule shape has no vertex corners and has a continuous round circumference. This shape allows the **Capsule Collider** 2D to not get easily caught in the corners of other Colliders.

**Note:** The capsule shape of the Collider is considered solid and not hollow, which means any other Collider 2Ds that are inside the Capsule Collider 2D are considered to be in contact with the Collider and are forced out of it over time.

Property | Function |   
---|---|---  
**Material** | Select the Physics Material 2D that determines properties of **collisions** that determines properties of **collisions** , such as friction and bounce.  
**Is Trigger** | Enable this if you want this Collider 2D to behave as a trigger. The physics system ignores this Collider when this is enabled.  
**Used by Effector** | Enable this if you want the Collider 2D to be used by an attached Effector 2D.  
**Offset** | Set the local offset values of the Collider 2D geometry.  
**Size** | Set the x and y values to define the size of the box region that the Capsule Collider 2D fills. Refer to Defining Size and Direction for more details.  
**Direction** | Select the orientation of the Capsule Collider 2D. This determines the position and orientation of the curved ends of the Collider shape. Refer to Defining Size and Direction for more details.  
| **Vertical** | Select this to orient the ends of the Collider shape upwards and downwards.  
| **Horizontal** | Select this to orient the ends of the Collider shape left and right.  
**Layer Overrides** | Expand for the Layer override settings.  
| **Layer Override Priority** | Assign the decision priority that this Collider2D uses when resolving conflicting decisions on whether a contact between itself and another Collision2D should happen or not. Refer to its API page for more information.  
| **Include Layers** | Select the additional Layers that this Collider 2D should include when deciding if a contact with another Collider2D should happen or not. Refer to its API documentation for more information.  
| **Exclude Layers** | Select the additional Layers that this Collider 2D should exclude when deciding if a contact with another Collider2D should happen or not. Refer to its API documentation for more information.  
| **Force Send Layers** | Select the Layers that this Collider 2D is allowed to send forces to during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Force Receive Layers** | Select the Layers that this Collider 2D can receive forces from during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Contract Capture Layers** | Select the Layers of other Collider 2D, involved in contacts with this Collider2D, that will be captured. Refer to its API documentation for more information.  
| **Callback Layers** | Select the Layers that this Collider 2D, during a contact with another Collider2D, will report collision or trigger callbacks for. Refer to its API documentation for more information.  
  
## Defining Size and Direction 

The settings that define the shape of the Capsule Collider 2D are **Size** and **Direction**. Both the Size and Direction properties refer to **X** and **Y** (horizontal and vertical, respectively) in the local space of the Capsule Collider 2D, and not in world space.

A typical way to set up the Capsule Collider 2D is to set the **Size** to match the **Direction**. For example, if the Capsule Collider 2D’s **Direction** is **Vertical** , the **Size** of **X** is 0.5 and the **Size** of **Y** is 1, this makes the vertical direction capsule taller, rather than wider.

In the example below, the **X** and **Y** are represented by the yellow lines.

An example of a Capsule Collider 2D set so the **Size** matches **Direction**

## Capsule configuration examples

You can change the Capsule Collider 2D with different configurations. Below are some examples.

Note that when the **X** and **Y** of the **Size** property are the same, the Capsule Collider 2D always approximates to a circle.

Examples of Capsule Collider 2D configurations

**Note:** A known issue in the 2D physics system is that when a **GameObject** moves across multiple Colliders, one or several of the Colliders may register a collision between the Colliders. This may occur even when the Colliders are perfectly aligned. This collision can cause the Collider to slow down or stop.

While constructing a surface with the Capsule Collider 2D can help reduce this problem, it is recommeneded to use a single Collider rather than multiple Colliders for a surface, such as the Edge Collider 2D.

CapsuleCollider2D