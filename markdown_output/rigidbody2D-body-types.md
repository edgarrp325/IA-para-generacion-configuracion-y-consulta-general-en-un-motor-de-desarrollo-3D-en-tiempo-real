---
title: "Rigidbody 2D body types"
category: "General"
source_file: "rigidbody2D-body-types.html"
doc_type: "manual"
---

# Rigidbody 2D body types

There are three options for **Body Type** which define the behavior of the **Rigidbody** which define the behavior of the **Rigidbody** 2D. Any **Collider** 2D. Any **Collider** 2D attached to that Rigidbody 2D inherits the Rigidbody 2D’s Body Type as well. 

The selected Body Type defines the Rigidbody 2D’s movement behavior (position and rotation) and Collider interactions. When a Body Type changes, Unity recalculates various mass-related internal properties, and all existing contacts for the Collider 2Ds attached to the Rigidbody 2D need to be re-evaluated during the **GameObject** ’s next FixedUpdate. Depending on how many contacts and Collider 2Ds are attached to the body, changing the Body Type can cause variations in performance.

The properties of the Rigidbody 2D component in its **Inspector** window differs depending on which Body Type you have selected. You can refer to the following pages for detailed information about the property settings for each Body Type:

**Topic** | **Description**  
---|---  
**Body Type: Dynamic** | Use the Dynamic Body Type to design your Rigidbody 2D to move under simulation.  
**Body Type: Kinematic** | Use the Kinematic Body Type to design your Rigidbody 2D to move under simulation only with explicit user control.  
**Body Type: Static** | Use the Static Body Type to design your Rigidbody 2D to not move under simulation.  
  
## Additional resources

  * API documentation on Rigidbody2D