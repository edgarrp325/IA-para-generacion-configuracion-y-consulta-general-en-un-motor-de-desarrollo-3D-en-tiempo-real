---
title: "Tilemap Renderer"
category: "General"
source_file: "class-TilemapRenderer.html"
doc_type: "manual"
---

# Tilemap Renderer

The **Tilemap Renderer** component is part of the Tilemap GameObject. It determines how **Tiles** set on the **Tilemap** are rendered.

Property | Function  
---|---  
**Sort Order** | Set the direction that Tiles on the selected Tilemap are sorted from.  
**Mode** | Set the rendering mode of the Renderer.  
Chunk | The Renderer groups Tiles by location, and batches their **Sprites** together for rendering. Select this mode for the best rendering performance with Tilemap.  
Individual | The Renderer renders each Tile individually, taking into account their location and sorting order. This mode enables the Sprites on the Tiles to interact with other Renderers in the **scene** or with a Custom Sorting Axis.  
**Detect Chunk Culling Bounds** | Determines how the Render detects the bounds used for the culling of Tilemap chunks. These bounds expand the boundary of Tilemap chunks to ensure that oversized Sprites will not be clipped during culling.  
Auto | The Renderer automatically inspects the Sprites used by the Tiles to determine the expanded culling bounds to use.  
Manual | The values used to extend the bounds for culling of the Tilemap chunks are manually set instead of with the Editor’s automatic detection.  
**Chunk Culling Bounds** | Enabled when Manual is selected above. Enter the values (in Unity units) that the culling bounds are extended by.  
**Sorting Layer** | Set the Sorting Layer of the Tilemap. Select an existing Sorting Layer from the drop-down box, or create a new Sorting Layer.  
**Order in Layer** | Set the render priority of the Tilemap within its Sorting Layer. Lower numbered layers are rendered first. Higher numbered layers overlap those below.  
**Mask Interaction** | Set how the Tilemap Renderer behaves when it interacts with a Sprite Mask.  
None | The Tilemap Renderer does not interact with any Sprite Mask in the Scene. This is the default option.  
Visible Inside Mask | The Tilemap Renderer only renders areas of the Tilemap that the Sprite Mask overlays.  
Visible Outside Mask | The Tilemap Renderer renders the Tilemap entirely but subtracts the areas the Sprite Mask overlays.  
  
## Additional resources

  * TilemapRenderer class (Scripting API)