---
title: "Mesh collider component reference"
category: "General"
source_file: "class-MeshCollider.html"
doc_type: "manual"
---

# Mesh collider component reference

Switch to Scripting

The ****Mesh** **collider** **collider**** takes a Mesh Asset and builds a collider that matches the geometry of that Mesh. It is more accurate for **collision** takes a Mesh Asset and builds a collider that matches the geometry of that Mesh. It is more accurate for **collision** detection than using primitives, and is a better option for complicated Meshes. 

Mesh colliders that are marked as **Convex** can collide with other **Mesh colliders**.

**Property** | **Description**  
---|---  
**Convex** | Enable the checkbox to make the Mesh collider collide with other Mesh colliders. **Convex** Mesh colliders are limited to 255 triangles.  
**Is Trigger** | Enable **Is Trigger** to use the collider as a trigger for events. When **Is Trigger** is enabled, other colliders pass through this collider, and trigger the messages `OnTriggerEnter`, `OnTriggerStay`, and `OnTriggerExit`.  
**Provides Contacts** | Enable **Provides Contacts** to generate contact information for this collider at all times. Usually, a collider only generates contact data if there is something to send it to; in this case, the messages `OnCollisionEnter`, `OnCollisionStay`, or `OnCollisionExit`. When **Provides Contacts** is enabled, the collider generates contact data for the physics system at all times. Contact generation is resource-intensive, so **Provides Contacts** is disabled by default.  
**Cooking Options** | Enable or disable the Mesh cooking options that affect how the **physics engine** processes Meshes. When you set the **Cooking Options** to any other value than the default settings (that is, everything enabled except **None**), the Mesh collider must use a Mesh that has an `isReadable` value of `true`. For details on Mesh cooking, see Prepare Meshes for Mesh colliders.  
| **None** | Disables all **Cooking Options**. This is disabled by default.  
| **Everything** | Enables all **Cooking Options**. This is enabled by default.  
| **Cook for Faster Simulation** | The cooking process preprocesses the Mesh data and stores it in memory to speed up run time calculations at run time. This is particularly useful for complex Meshes in the **scene**. When this setting is disabled, the physics engine uses a faster cooking time, but retrieves the mesh data more slowly at run time. This is enabled by default.  
| **Enable Mesh Cleaning** | The cooking process attempts to clear the Mesh of degenerate triangles on the Mesh (that is, triangles in which all three points are collinear, and do not form a triangle shape) and other geometrical artifacts. This results in a Mesh that is better suited for use in **collision detection** , and tends to produce more accurate contact points. When this setting is disabled, the physics engine uses a faster cooking time but implements less optimization. This is enabled by default.  
| **Weld Colocated Vertices** | The cooking process combines vertices that have the same position. This results in a Mesh that is better suited for use in collision detection, and tends to produce more accurate contact points. When this setting is disabled, the physics engine uses a faster cooking time but implements less optimization. This is enabled by default.  
| **Use Fast Midphase** | The cooking process uses the fastest mid-phase acceleration structure and algorithm available for your output platform. The fastest algorithm doesn’t require any R-Trees for spatial access. If you encounter midphase issues at runtime, disable this option; Unity then uses the slower legacy midphase algorithm instead. This is enabled by default.  
**Material** | Reference to the Physics Material that determines how this collider interacts with others.  
**Mesh** | Reference to the Mesh to use for collisions.  
  
## Layer overrides

The Layer Overrides section provides properties that allow you to override the project-wide Layer-based collision detection settings for this collider. 

**Property** | **Description**  
---|---  
**Layer Override Priority** | Define the priority of this collider override. When two colliders have conflicting overrides, the settings of the collider with the higher value priority are taken.   
For example, if a collider with a **Layer Override Priority** of 1 collides with a Collider with a **Layer Override Priority** of 2, the physics system uses the settings for the Collider with the **Layer Override Priority** of 2.  
**Include Layers** | Choose which Layers to include in collisions with this collider.  
**Exclude Layers** | Choose which Layers to exclude in collisions with this collider.