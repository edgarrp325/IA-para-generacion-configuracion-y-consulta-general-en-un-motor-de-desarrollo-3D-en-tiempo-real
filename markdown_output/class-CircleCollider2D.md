---
title: "Circle Collider 2D"
category: "General"
source_file: "class-CircleCollider2D.html"
doc_type: "manual"
---

# Circle Collider 2D

Switch to Scripting

The **Circle**Collider** 2D** is a collider that interacts with the 2D physics system for approximate **collision** 2D is a collider that interacts with the 2D physics system for approximate **collision** detection. The Circle Collider 2D, as the name suggests, is in circular shape with a defined position and radius within the local coordinate space of a ****Sprite** detection. The Circle Collider 2D, as the name suggests, is in circular shape with a defined position and radius within the local coordinate space of a ****Sprite****.**

Property | Function |   
---|---|---  
**Material** | Select the Physics Material 2D that determines properties of collisions, such as friction and bounce.  
**Is Trigger** | Enable this option if you want the Collider 2D to behave as a trigger. The physics system ignores the Collider 2D when you enable this option.  
**Used by Effector** | Enable this option if you want an attached Effector 2D to use this Collider 2D.  
**Offset** | Set the local offset values of the Collider 2D geometry.  
**Radius** | Set the radius of the Circle Collider 2D in local space units.  
**Layer Overrides** | Expand this option to use the Layer override settings.  
| **Layer Override Priority** | Assign the decision priority that this Collider 2D uses when resolving conflicting decisions on whether a contact between itself and another Collider 2D should happen or not. For more information, refer to its API page.  
| **Include Layers** | Select the additional Layers for this Collider 2D to include when deciding if a contact with another Collider2D should happen or not. Refer to its API documentation for more information.  
| **Exclude Layers** | Select the additional layers for this Collider 2D to exclude when deciding if a contact with another Collider 2D should happen or not. Refer to its API documentation for more information.  
| **Force Send Layers** | Select the Layers that this Collider 2D is allowed to send forces to during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Force Receive Layers** | Select the Layers that this Collider 2D can receive forces from during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Contact Capture Layers** | Select the Layers of other Collider 2D involved in contact with this Collider2D that you want to capture. Refer to its API documentation for more information.  
| **Callback Layers** | Select the Layers that this Collider 2D, during a contact with another Collider2D, will report collision or trigger callbacks for. Refer to its API documentation for more information.  
  
CircleCollider2D