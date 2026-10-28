---
title: "Terrain collider component reference"
category: "General"
source_file: "class-TerrainCollider.html"
doc_type: "manual"
---

# Terrain collider component reference

Switch to Scripting

The **Terrain**collider**** builds a collider that matches the geometry of the Terrain builds a collider that matches the geometry of the Terrain it is attached to. It is the best and most accurate collider type for Terrains. 

**Property** | **Description**  
---|---  
**Provides Contacts** | Enable **Provides Contacts** to generate contact information for this collider at all times. Usually, a collider only generates contact data if there is something to send it to; in this case, the messages `OnCollisionEnter`, `OnCollisionStay`, or `OnCollisionExit`. When **Provides Contacts** is enabled, the collider generates contact data for the physics system at all times. Contact generation is resource-intensive, so **Provides Contacts** is disabled by default.  
**Material** | Choose the Physic Material asset that determines how this collider interacts with others. If you do not choose one, the physics system uses the project-wide default settings.  
**Terrain Data** | Choose the TerrainData asset. The **Terrain collider** builds a collider shape based on the TerrainData asset properties.  
**Enable Tree Colliders** | Enable this to automatically generate colliders for any Trees on the Terrain. This makes the collider more accurate, but is more computationally demanding, so you should only use it if your **scene** on the Terrain. This makes the collider more accurate, but is more computationally demanding, so you should only use it if your **scene** requires physics interactions with the trees on the Terrain. It is enabled by default.  
  
## Layer overrides

The Layer Overrides section provides properties that allow you to override the project-wide Layer-based collision detection settings for this collider. 

**Property** | **Description**  
---|---  
**Layer Override Priority** | Define the priority of this collider override. When two colliders have conflicting overrides, the settings of the collider with the higher value priority are taken.   
For example, if a collider with a **Layer Override Priority** of 1 collides with a Collider with a **Layer Override Priority** of 2, the physics system uses the settings for the Collider with the **Layer Override Priority** of 2.  
**Include Layers** | Choose which Layers to include in **collisions** with this collider.  
**Exclude Layers** | Choose which Layers to exclude in collisions with this collider.