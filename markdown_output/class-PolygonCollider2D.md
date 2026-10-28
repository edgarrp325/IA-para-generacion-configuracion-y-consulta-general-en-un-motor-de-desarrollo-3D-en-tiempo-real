---
title: "Polygon Collider 2D reference"
category: "General"
source_file: "class-PolygonCollider2D.html"
doc_type: "manual"
---

# Polygon Collider 2D reference

Switch to Scripting

The **Polygon**Collider** 2D** is a Collider 2D component that interacts with the 2D physics system. It’s shape is a freeform edge of line segments that you can adjust to fit the shape of a **sprite** 2D is a Collider 2D component that interacts with the 2D physics system. It’s shape is a freeform edge of line segments that you can adjust to fit the shape of a **sprite** or any other shape. **Note:** The edge must enclose an area for the collider to work.

Property | Description |   
---|---|---  
**Edit Collider** | Select this to edit the collider’s geometry by editing and moving its vertices.  
**Material** | Select the Physics Material 2D that determines properties of **collisions** that determines properties of **collisions** , such as friction and bounce.  
**Is Trigger** | Enable this if you want this Collider 2D to behave as a trigger. The physics system ignores this Collider when this is enabled.  
**Used by Effector** | Enable this if you want the Collider 2D to be used by an attached Effector 2D.  
**Used by Composite** | Enable this if you want this Collider to be used by an attached Composite Collider 2D.  
  
**Note:** When you enable **Used by Composite** , other properties disappear from the Box Collider 2D component as they are now controlled by the attached Composite Collider 2D. The properties that disappear from the Box Collider 2D are **Material** , **Is Trigger** , **Used By Effector** , and **Edge Radius**.  
**Auto Tiling** | Enable this if the Sprite Renderer component for the selected Sprite has the **Draw Mode** set to **Tiled**. This enables automatic updates to the shape of the Collider 2D, allowing the shape to automatically readjust when the Sprite’s dimensions change. If you don’t enable **Auto Tiling** , the Collider 2D geometry doesn’t automatically repeat.  
**Offset** | Set the local offset values of the Collider 2D geometry.  
**Use Delaunay**Mesh**** | Enable this property to include an additional Delaunay triangulation step to produce the Collider mesh.  
**Points** | Expand to view information about the complexity of the generated collider.  
**Layer Overrides** | Expand for the Layer override settings.  
| **Layer Override Priority** | Assign the decision priority that this Collider2D uses when resolving conflicting decisions on whether a contact between itself and another Collision2D should happen or not. Refer to its API page for more information.  
| **Include Layers** | Select the additional Layers that this Collider 2D should include when deciding if a contact with another Collider2D should happen or not. Refer to its API documentation for more information.  
| **Exclude Layers** | Select the additional Layers that this Collider 2D should exclude when deciding if a contact with another Collider2D should happen or not. Refer to its API documentation for more information.  
| **Force Send Layers** | Select the Layers that this Collider 2D is allowed to send forces to during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Force Receive Layers** | Select the Layers that this Collider 2D can receive forces from during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Contract Capture Layers** | Select the Layers of other Collider 2D, involved in contacts with this Collider2D, that will be captured. Refer to its API documentation for more information.  
| **Callback Layers** | Select the Layers that this Collider 2D, during a contact with another Collider2D, will report collision or trigger callbacks for. Refer to its API documentation for more information.  
**Info** | Expand for read-only physics system related information about the collider.  
  
## Edit the collider’s geometry

You can edit a collider’s geometry manually or have Unity generate its shape automatically. Unity automatically generates a collider’s geometry when you drag a sprite into the **scene** and add a Collider 2D component to it. The generated collider shape matches the outline of the sprite as close as possible.

To edit the collider’s shape:

  1. Select **Edit Collider** in the Inspector window to edit the collider’s geometry. You can also access the collider’s editing mode from the Tools overlay in the Scene view window.  

  2. To move an existing vertex, select and hold it, then move it to a new location.
  3. To create a new vertex, hover your cursor over the outline of the collider’s shape. A dot shows the position of the cursor on the collider’s geometry. Click on the dot to create a new vertex at that position.
  4. To remove a vertex, hold Ctrl (macOS:Cmd) while hovering your cursor over the edges of the collider’s geometry, which turn red. Click the red edges to remove the vertex that connects them.
  5. Exit the collider editing mode by selecting **Edit Collider** in the **Inspector** window or Tools overlay again.

PolygonCollider2D