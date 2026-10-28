---
title: "Collision"
category: "General"
source_file: "collision-section.html"
doc_type: "manual"
---

# Collision

To configure **collision** between GameObjects in Unity, you need to use colliders. colliders define the shape of a **GameObject** between GameObjects in Unity, you need to use colliders. colliders define the shape of a **GameObject** for the purposes of physical collisions. You can then use these colliders to manage collision events. You can configure collisions via **collider** for the purposes of physical collisions. You can then use these colliders to manage collision events. You can configure collisions via **collider** components, or their corresponding C# class. 

This documentation describes how to configure collisions and collision events, and how colliders interact with each other and their environment.

**Topic** | **Description**  
---|---  
Introduction to collision | Overview of the fundamental concepts around physics collision in Unity.  
Collider types | The different collider types (static, kinematic, and dynamic), and how collider behaviour differs depending on the collider’s physics body configuration.  
Collider shapes | The different collider shapes available, and how collider shape complexity affects performance.  
Collider surfaces | How PhysX handles friction and bounciness on a collider’s surface, and how to configure surface properties for each collider.  
Collider interactions and events | How collisions can call events and functions to trigger changes at run time.  
Collision detection | How PhysX detects collisions in Unity, and how to select the right algorithm depending on your collider configuration for optimal performance.