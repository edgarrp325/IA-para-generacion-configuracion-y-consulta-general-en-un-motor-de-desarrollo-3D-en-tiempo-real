---
title: "Edge Collider 2D"
category: "General"
source_file: "class-EdgeCollider2D.html"
doc_type: "manual"
---

# Edge Collider 2D

Switch to Scripting

The **Edge**Collider** 2D** component is a Collider that interacts with the 2D physics system. The Collider’s shape is a freeform edge made of line segments that you can adjust to fit the shape of a **Sprite** 2D component is a Collider that interacts with the 2D physics system. The Collider’s shape is a freeform edge made of line segments that you can adjust to fit the shape of a **Sprite** or any other shape. The Collider’s start and end points do not need to meet or completely enclose an area to function (unlike the Polygon Collider 2D), and can form a straight line or other single edge shape.

Property | Function |   
---|---|---  
**Edit Collider** | Select Edit Collider  to make the collider outline editable. See Editing in Edit Collider mode for the actions and shortcuts available when **Edit Collider** is enabled.  
**Material** | Select the Physics Material 2D that determines properties of **collisions** that determines properties of **collisions** , such as friction and bounce.  
**Is Trigger** | Enable this if you want this Collider 2D to behave as a trigger. The physics system ignores this Collider when this is enabled.  
**Used by Effector** | Enable this if you want the Collider 2D to be used by an attached Effector 2D.  
**Offset** | Set the local offset values of the Collider 2D geometry.  
**Edge Radius** | Set a value that forms a radius around the edge of the Collider. This results in a larger Collider 2D with rounded convex corners. The default value is 0 (no radius).  
**Points** | Expand to view read-only information about the complexity of the generated Collider.  
**Use Adjacent Start Point** | Enable this property to calculate the collision response using the **Adjacent Start Point** to form the collision normal when a collision occurs at the Edge Collider’s start point.  
| **Adjacent Start Point X/Y** | Set the x and y-coordinates of the **Adjacent Start Point**.  
**Use Adjacent End Point** | Enable this property to calculate the collision response using the **Adjacent End Point** to form the collision normal when a collision occurs at the Edge Collider’s end point.  
| **Adjacent End Point X/Y** | Set the x and y-coordinates of the Adjacent End Point.  
**Layer Overrides** | Expand for the Layer override settings.  
| **Layer Override Priority** | Assign the decision priority that this Collider2D uses when resolving conflicting decisions on whether a contact between itself and another Collision2D should happen or not. Refer to its API page for more information.  
| **Include Layers** | Select the additional Layers that this Collider 2D should include when deciding if a contact with another Collider2D should happen or not. Refer to its API documentation for more information.  
| **Exclude Layers** | Select the additional Layers that this Collider 2D should exclude when deciding if a contact with another Collider2D should happen or not. Refer to its API documentation for more information.  
| **Force Send Layers** | Select the Layers that this Collider 2D is allowed to send forces to during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Force Receive Layers** | Select the Layers that this Collider 2D can receive forces from during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Contract Capture Layers** | Select the Layers of other Collider 2D, involved in contacts with this Collider2D, that will be captured. Refer to its API documentation for more information.  
| **Callback Layers** | Select the Layers that this Collider 2D, during a contact with another Collider2D, will report collision or trigger callbacks for. Refer to its API documentation for more information.  
  
## Editing in Edit Collider mode 

The actions and shortcuts available when **Edit Collider** is enabled.

Action | Function  
---|---  
Click and drag vertex or edge. | Move the selected vertex and edge to a different position.  
Click anywhere along an edge. | Create a new vertex by clicking an empty space along the edge.  
Hold the Ctrl(macOS:Cmd) key and select a vertex or edge. | Deletes the selected vertex or edge.  
  
EdgeCollider2D