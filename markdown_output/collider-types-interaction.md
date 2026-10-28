---
title: "Interaction between collider types"
category: "General"
source_file: "collider-types-interaction.html"
doc_type: "manual"
---

# Interaction between collider types

This page describes which event functions Unity generates based on the configuration of each **collider** in a **collision** in a **collision** pair.

## Collision generates collision detection messages

When a pair of colliders make contact, they generate **collision detection** messages if the following are both true:

  * There is at least one dynamic collider.
  * The other collider is a static collider, a kinematic collider, or another dynamic collider.

The following table describes each combination of collider types. A “Y” indicates a combination that can generate collision detection and collision messages. 

**Collision detection occurs and messages are sent upon collision**  
---  
| Static collider | Dynamic collider | Kinematic collider | Static trigger collider | Dynamic trigger collider | Kinematic trigger collider  
Static collider |  | Y |  |  |  |   
Dynamic collider | Y | Y | Y |  |  |   
Kinematic collider |  | Y |  |  |  |   
Static trigger collider |  |  |  |  |  |   
Dynamic trigger collider |  |  |  |  |  |   
Kinematic trigger collider |  |  |  |  |  |   
  
Remember that Unity only applies physics forces to collider **GameObjects** that have a physics body (a Rigidbody or ArticulationBody). When a physics body collider collides with a static collider, only the physics body collider behavior changes as a result of the collision (for example, it might bounce or slow down as a result of the collision).

## Collision generates trigger messages

Trigger messages occur in the following circumstances:

  * A dynamic or kinematic trigger collider collides with any collider type.
  * A static trigger collider collides with any dynamic or Kinematic collider.

The following table describes each combination of collider types. A “Y” indicates a combination that can generate trigger messages from any trigger collider in the pair. 

**Trigger messages are sent upon collision**  
---  
| Static collider | Dynamic collider | Kinematic collider | Static trigger collider | Dynamic trigger collider | Kinematic trigger collider  
Static collider |  |  |  |  | Y | Y  
Dynamic collider |  |  |  | Y | Y | Y  
Kinematic collider |  |  |  | Y | Y | Y  
Static trigger collider |  | Y | Y |  | Y | Y  
Dynamic trigger collider | Y | Y | Y | Y | Y | Y  
Kinematic trigger collider | Y | Y | Y | Y | Y | Y