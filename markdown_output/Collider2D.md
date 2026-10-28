---
title: "Collider 2D"
category: "General"
source_file: "Collider2D.html"
doc_type: "manual"
---

# Collider 2D

Collider 2D components define the shape of a 2D **GameObject** for the purposes of physical **collisions** for the purposes of physical **collisions**. A **collider**. A **collider** , which is invisible, doesn’t need to be the exact same shape as the GameObject’s **mesh** , which is invisible, doesn’t need to be the exact same shape as the GameObject’s **mesh** ; a rough approximation is often more efficient, with no noticeable difference in gameplay.

Colliders for 2D GameObjects all have names ending with 2D. A collider that doesn’t have 2D in its name can only be used on a 3D GameObject. You can’t use 3D GameObjects with 2D colliders, or 2D GameObjects with 3D colliders.

**Note:** On the **Rigidbody** 2D component, select the **Use Auto Mass** checkbox to automatically set the Rigidbody 2D’s mass to the same value as the Collider 2D’s mass. You can use this in conjunction with the Buoyancy Effector 2D.

You can use the following Collider 2D types with Rigidbody 2D:

**Topic** | **Description**  
---|---  
**Circle Collider 2D** | Use Circle Collider 2D for circular collision areas.  
**Box Collider 2D** | Use **Box Collider** 2D for square and rectangle collision areas.  
**Polygon Collider 2D** | Use Polygon Collider 2D for freeform collision areas.  
**Edge Collider 2D** | Use Edge Collider 2D freeform collision areas and areas which aren’t fully enclosed (such as rounded convex corners).  
**Capsule Collider 2D** | Use **Capsule Collider** 2D for circular or lozenge-shaped collision areas.  
**Composite Collider 2D** | Use Composite Collider 2D for merging Box Collider 2Ds and Polygon Collider 2Ds.  
**Custom Collider 2D** | Use Custom Collider 2D for collision areas with customizable geometry.  
  
## Additional resources

  * API documentation on Collider2D