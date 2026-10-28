---
title: "Composite Collider 2D"
category: "General"
source_file: "class-CompositeCollider2D.html"
doc_type: "manual"
---

# Composite Collider 2D

Switch to Scripting

The Composite Collider 2D component is a Collider that interacts with the 2D physics system. Unlike most Colliders, it does not define an inherent shape. Instead, it merges the shapes of any Box Collider 2D or Polygon Collider 2D that you set it up to use. The Composite Collider 2D uses the vertices (geometry) from any of these Colliders, and merges them together into new geometry controlled by the Composite Collider 2D itself.

Property | Function |   
---|---|---  
**Material** | Select the Physics Material 2D that determines properties of **collisions** that determines properties of **collisions** , such as friction and bounce.  
**Is Trigger** | Enable this if you want this Collider 2D to behave as a trigger. The physics system ignores this Collider when this is enabled.  
**Used by Effector** | Enable this if you want the Collider 2D to be used by an attached Effector 2D.  
**Offset** | Set the local offset values of the Collider 2D geometry.  
**Geometry Type** | Select the type of geometry to merge the vertices of the selected Colliders into. Select either **Outlines** or **Polygons** from the dropdown menu.  
| **Outlines** | Select this to produce a Collider 2D with hollow outlines, identical to an Edge Collider 2D.  
| **Polygons** | Select this to produce a Collider 2D with solid polygons, identical to a Polygon Collider 2D.  
**Use Delaunay**Mesh**** | Enable this property to an additional Delaunay triangulation step to produce the Collider mesh.  
**Generation Type** | Select the geometry generation method used when either the Composite Collider 2D is changed, or when any of the Colliders composing the Composite Collider 2D is changed.  
| **Synchronous** | Select this to have Unity immediately generate new geometry when a change is made to the Composite Collider 2D or to any of the Colliders composing it.  
| **Manual** | Select this to have Unity only generate geometry generation happens when you request it. To request generation, either call the CompositeCollider2D.GenerateGeometry scripting API, or select **Regenerate Geometry** that appears under the selection.  
**Vertex Distance** | Set a value for the minimum spacing allowed for any vertices gathered from Colliders being composed. Any vertex closer than this limit is removed. This allows control over the effective resolution of the vertex compositing.  
**Offset Distance** | Set the value to offset vertices when compositing multiple physics shapes. Any vertices between physics shapes within this distance value are combined. **Note:** It’s recommended to not set this value higher than 1% of the **Sprite** ’s length, as this may result in loss of detail when too many vertices are combined together.  
**Layer Overrides** | Expand for the Layer override settings.  
| **Layer Override Priority** | Assign the decision priority that this Collider2D uses when resolving conflicting decisions on whether a contact between itself and another Collision2D should happen or not. Refer to its API page for more information.  
| **Include Layers** | Select the additional Layers that this Collider 2D should include when deciding if a contact with another Collider2D should happen or not. Refer to its API documentation for more information.  
| **Exclude Layers** | Select the additional Layers that this Collider 2D should exclude when deciding if a contact with another Collider2D should happen or not. Refer to its API documentation for more information.  
| **Force Send Layers** | Select the Layers that this Collider 2D is allowed to send forces to during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Force Receive Layers** | Select the Layers that this Collider 2D can receive forces from during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Contract Capture Layers** | Select the Layers of other Collider 2D, involved in contacts with this Collider2D, that will be captured. Refer to its API documentation for more information.  
| **Callback Layers** | Select the Layers that this Collider 2D, during a contact with another Collider2D, will report collision or trigger callbacks for. Refer to its API documentation for more information.  
  
## Composing with the Box Collider 2D and Polygon Collider 2D

Both the **Box Collider** 2D and Polygon Collider 2D components have the **Used By Composite** property, which allows them be merged and composed into a single Collider with the Composite Collider 2D. These Colliders must also be attached to the same Rigidbody 2D as the Composite Collider 2D. When you enable **Used by Composite** , other properties disappear from that component, as they are now controlled by the attached Composite Collider 2D.

Refer to the CompositeCollider2D API documentation for more information about scripting with the Composite Collider 2D.

CompositeCollider2D