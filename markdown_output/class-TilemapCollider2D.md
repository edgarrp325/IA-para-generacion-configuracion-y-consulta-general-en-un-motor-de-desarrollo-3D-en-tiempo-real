---
title: "Tilemap Collider 2D"
category: "General"
source_file: "class-TilemapCollider2D.html"
doc_type: "manual"
---

# Tilemap Collider 2D

The **Tilemap**Collider** 2D** component generates **Collider** shapes for Tiles 2D component generates **Collider** shapes for Tiles on a Tilemap on a Tilemap component on the same **GameObject** component on the same **GameObject**. When you add or remove Tiles on the Tilemap component, the Tilemap Collider 2D updates the Collider shapes during `LateUpdate`. It batches multiple Tile changes together to ensure minimal impact on performance.

## Tilemap Collider 2D properties

Tilemap Collider 2D window Property | Function |   
---|---|---  
**Max Tile Change Count** | Set the maximum number of Tile changes (such as adding/removing Tiles to the Tilemap) to accumulate before doing a full Collider rebuild instead of an incremental rebuild.  
  
**Note:** A high number of accumulated changes can cause the incremental rebuild of the **Tilemap Collider 2D** to be slower than a full rebuild. Decrease this value to resolve this issue.  
**Extrusion Factor** | Set the amount (in Unity world space units) to extrude the Collider shape of each Tile. This minimizes the gaps between the Collider shapes of neighboring Tiles and brings them to within the minimum **Vertex Distance** set in the **Composite Collider 2D** , which can then compose the Tile Colliders together.   
  
**Note:** This property isn’t available by default. It becomes available when you enable Used by Composite, and attach a Composite Collider 2D to the same GameObject.  
**Material** | Select the Physics Material 2D that determines properties of **collisions** that determines properties of **collisions** , such as friction and bounce.  
**Is Trigger** | Enable this if you want this Collider 2D to behave as a trigger. The physics system ignores this Collider when this is enabled.  
**Used by Effector** | Enable this if you want the Collider 2D to be used by an attached Effector 2D.  
**Used by Composite** | Enable this to use this Collider with an attached Composite Collider 2D.  
  
When you enable **Used by Composite** , all properties except **Offset** will no longer be available in the Tilemap Collider 2D component and the attached Composite Collider 2D component controls the Collider properties instead.  
**Offset** | Set the local offset values of the Collider 2D geometry.  
**Layer Overrides** | Expand for the Layer override settings.  
| **Layer Override Priority** | Assign the decision priority that this Collider2D uses when resolving conflicting decisions on whether a contact between itself and another Collision2D should happen or not. Refer to its API page for more information.  
| **Include Layers** | Select the additional Layers that this Collider 2D should include when deciding if a contact with another Collider2D should happen or not. Refer to its API documentation for more information.  
| **Exclude Layers** | Select the additional Layers that this Collider 2D should exclude when deciding if a contact with another Collider2D should happen or not. Refer to its API documentation for more information.  
| **Force Send Layers** | Select the Layers that this Collider 2D is allowed to send forces to during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Force Receive Layers** | Select the Layers that this Collider 2D can receive forces from during a Collision contact with another Collider2D. Refer to its API documentation for more information.  
| **Contract Capture Layers** | Select the Layers of other Collider 2D, involved in contacts with this Collider2D, that will be captured. Refer to its API documentation for more information.  
| **Callback Layers** | Select the Layers that this Collider 2D, during a contact with another Collider2D, will report collision or trigger callbacks for. Refer to its API documentation for more information.  
  
## Collider Type’s effect on Collider generation

The Collider shapes generated for each Tile in the Tilemap depend on the desired Collider type set in the Tile Asset’s properties. The component’s shape generation behavior corresponds to the Collider Types in the following ways:

Collider Type | Function  
---|---  
**None** | The Tilemap Collider 2D component does not generate any Collider shapes for this Tile.  
****Sprite**** | The Tilemap Collider 2D component generates a Collider shape based on the Sprite assigned to the Tile. The Collider shape is based on the Custom Physics Shape set for the Sprite.  
**Grid** | The Tilemap Collider 2D component generates a Collider shape based on the shape of the Grid cell, which is determined by the selected Cell Layout of the Grid component.  
  
## Tilemap and Composite Colliders

You can use the Tilemap Collider 2D component together with the Composite Collider 2D component. When you add both components to the same Tilemap, Unity composites the Collider shapes of neighboring Tiles together. This smoothens the corners and edges between Collider shapes in neighboring Tiles.

Using both components together reduces the number of individual Collider shapes involved in a physics update, which reduces the amount of calculations required, and minimizes the impact on performance.

## Scripting API tips

If you require immediate changes to happen to the Collider, use Tilemaps.TilemapCollider2D.ProcessTilemapChanges to process them immediately. You can use Tilemaps.TilemapCollider2D-hasTilemapChanges to check if any processing is required.

## Additional resources

  * Physics 2D Reference
  * Collider 2D

* * *

  * New properties added in Unity 2020.1
  * Tilemaps added in 2017.2 NewIn20172

TilemapCollider2D