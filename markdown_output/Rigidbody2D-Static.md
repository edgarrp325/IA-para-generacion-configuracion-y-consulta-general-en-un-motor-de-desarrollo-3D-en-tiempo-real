---
title: "Body Type: Static"
category: "General"
source_file: "Rigidbody2D-Static.html"
doc_type: "manual"
---

# Body Type: Static

A Static **Rigidbody** 2D is designed to not move under simulation at all. If anything collides with it, a Static Rigidbody 2D behaves like an immovable object (as though it has infinite mass). It is also the least resource intensive ****Body Type** 2D is designed to not move under simulation at all. If anything collides with it, a Static Rigidbody 2D behaves like an immovable object (as though it has infinite mass). It is also the least resource intensive ****Body Type****. A Static body only collides with Dynamic Rigidbody 2Ds. **Note** : Having two Static Rigidbody 2Ds collide is not supported, since they are not designed to move.**

Due to their limited behavior, only a very limited set of properties are available for this **Body Type**.

## Available Rigidbody 2D properties

Property | Function |   
---|---|---  
**Body Type** | Select to set the movement behavior and **Collider** 2D interaction of this Rigidbody 2D’s component settings.  
| **Dynamic** | Select to set this Rigidbody 2D to the Dynamic Body Type, which is designed to move under simulation and has all Rigidbody 2D properties available. The is the default Body Type for a Rigidbody 2D  
| **Kinematic** | Select to set this Rigidbody 2D to the Kinematic Body Type, which is designed to move under simulation but only under very explicit user control. Refer to Body Type: Kinematic for more information.  
| **Static** | Select to set this Rigidbody 2D to the Static Body Type, which is designed to not move under simulation at all and behaves like an immovable object with infinite mass.  
**Material** | Set a common physics material for all Collider 2Ds attached to this Rigidbody 2D. **Note:** A Collider 2D uses its own Material property if it has one set. If there is no Material specified here or in the Collider 2D, the default option is **None (Physics Material 2D)**. This uses a default Material which you can set in the Physics 2D window.   
  
**Tip:** Use this to ensure that all Collider 2Ds attached to the same **Static** Body Type Rigidbody 2D can all use the same Material.  
**Simulated** | Enable **Simulated** to have the Rigidbody 2D and any attached Collider 2Ds and **Joint** 2Ds to interact with the physics simulation during runtime. If this is disabled, these components do not interact with the simulation. Refer to Rigidbody 2D properties: Simulated for more information. This property is enabled by default.  
**Layer Overrides** | Expand for the Layer override settings.  
| **Include Layers** | Select the additional Layers that all Collider 2Ds attached to this Rigidbody 2D should include, when deciding if a **collision** with another Collider2D should occur or not. Refer to Rigidbody2D-includeLayers for more information.  
| **Exclude Layers** | Select the additional Layers that all Collider 2Ds attached to this Rigidbody 2D should exclude, when deciding if a collision with another Collider 2D should occur or not. Refer to Rigidbody2D-excludeLayers for more information.  
  
## Creating a large number of Static Collider 2D

Aside from setting the Rigidbody 2D to the **Static** Body Type, there is another scenario where a Static Rigidbody 2D is created. This is when a **GameObject** with a Collider 2D component does not have a Rigidbody 2D component at all. All Collider 2Ds without a Rigidbody 2D component are internally considered to be attached to a single hidden **Static** Rigidbody 2D component.

This means that you are able to create a large number of Static Collider 2Ds as you do not have to add a Rigidbody 2D component for each individual GameObject. Both methods of creating Static Collider 2Ds have their advantages, depending on the scenario.

If an individual Static Collider 2D needs to be moved or reconfigured at runtime, then add a Rigidbody 2D component and set it to the **Static** Body Type, as it is faster to simulate the Collider 2D when it has its own Rigidbody 2D. If a group of Collider 2Ds needs to be moved or reconfigured at runtime, it is faster to have them all be children of the single hidden parent Rigidbody 2D than to move each GameObject individually.

**Note:** As stated above, Static Rigidbody 2Ds are designed not to move, and collisions between two Static Rigidbody **2D objects** that intersect are not registered. However, Static Rigidbody 2Ds and Kinematic Rigidbody 2Ds will interact with each other if one of their Collider 2Ds is set to be a **trigger**. There is also a feature that changes what a Kinematic body will interact with (see Use Full Kinematic Contacts for more information).