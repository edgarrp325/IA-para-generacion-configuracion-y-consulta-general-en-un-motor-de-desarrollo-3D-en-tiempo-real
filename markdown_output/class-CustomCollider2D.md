---
title: "Custom Collider 2D"
category: "General"
source_file: "class-CustomCollider2D.html"
doc_type: "manual"
---

# Custom Collider 2D

Switch to Scripting

The Custom Collider 2D is a Collider that interacts with the 2D physics system. Unlike other Colliders, you do not configure the Collider in-Editor, instead you configure the Collider by assigning PhysicsShape2D geometry to it via the PhysicsShapeGroup2D API. You can further define the Collider by adding, removing and modifying the `PhysicsShape2D` shapes. Refer to the PhysicsShape2D API documentation for more information. This also means that a Custom Collider 2D can contain an unlimited number of low-level `PhysicsShape2D` and represent any type of shape, or emulate other types of Collider 2D.

Custom Collider 2D properties Property | Function |   
---|---|---  
**Material** | Select the Physics Material 2D that determines properties of **collisions** that determines properties of **collisions** , such as friction and bounce.  
**Is Trigger** | Enable this if you want this Collider 2D to behave as a trigger. The physics system ignores this Collider when this is enabled.  
**Used by Effector** | Enable this if you want the Collider 2D to be used by an attached Effector 2D.  
**Offset** | Set the local offset values of the Collider 2D geometry.  
**Custom Shape Count** (Read only) | Indicates how many `PhysicsShape2D` the Collider is using.  
**Custom Vertex Count** (Read Only) | Indicates how many vertices all `PhysicsShape2D` in the Collider are using.  
**Layer Overrides** | Expand for the Layer override settings.  
| **Layer Override Priority** | Assign the decision priority that this Collider2D uses when resolving conflicting decisions on whether a contact between itself and another Collision2D should happen or not. Refer to its API page for more information.  
| **Include Layers** | Select the additional Layers that this Collider 2D should include when deciding if a contact with another Collider2D should happen or not. Refer to its API documentation for more information.  
| **Exclude Layers** | Select the additional Layers that this Collider 2D should exclude when deciding if a contact with another Collider2D should happen or not. Refer to its API documentation for more information.  
| **Force Send Layers** | Select the Layers that this Collider 2D is allowed to send forces to during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Force Receive Layers** | Select the Layers that this Collider 2D can receive forces from during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Contract Capture Layers** | Select the Layers of other Collider 2D, involved in contacts with this Collider2D, that will be captured. Refer to its API documentation for more information.  
| **Callback Layers** | Select the Layers that this Collider 2D, during a contact with another Collider2D, will report collision or trigger callbacks for. Refer to its API documentation for more information.  
  
## Using the Custom Collider 2D

When assigning `PhysicsShape2D` to the Custom Collider 2D, you can do so either during Edit mode or Play mode. When modifying the Custom Collider 2D in Edit mode, Unity saves all assigned `PhysicsShape2D` and associated vertices in the Unity **Scene** , and the `CustomCollider2D` retains its configuration when the Scene is loaded. This makes it possible to use Edit mode authoring **scripts** , and the `CustomCollider2D` retains its configuration when the Scene is loaded. This makes it possible to use Edit mode authoring **scripts** to create custom geometry.

When modifying the Custom Collider 2D during Play mode, the Collider will not retain any changes made to assigned `PhysicsShape2D` and their associated vertices, and all changes will be lost when exiting Play mode.

CustomCollider2D