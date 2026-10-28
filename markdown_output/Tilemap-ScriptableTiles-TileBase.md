---
title: "TileBase"
category: "General"
source_file: "Tilemap-ScriptableTiles-TileBase.html"
doc_type: "manual"
---

# TileBase

All tiles added to a **Tilemap** component must inherit from `TileBase`. `TileBase` provides a tilemap with a fixed set of APIs to communicate its rendering properties. For most cases of the APIs, the location of the tile and the instance of the tilemap the tile is placed on is passed in as arguments of the API. You can use this to find any required attributes for setting the tile information.

## Using RefreshTile
    
    
    public void RefreshTile(Vector3Int location, ITilemap tilemap)
    

`RefreshTile` determines which tiles in the vicinity are updated as this tile is added to the tilemap. By default, the `TileBase` calls `tilemap.RefreshTile(location)` to refresh the tile at the current location. Override this to determine which tiles need to be refreshed due to the placement of the new tile. 

**Example:** There is a straight road, and you place a `RoadTile` next to it. The straight road isn’t valid anymore. It needs a T-section instead. Unity doesn’t automatically know what needs to be refreshed, so `RoadTile` needs to trigger the refresh onto itself, but also onto the neighboring road.

## Using GetTileData
    
    
    public void GetTileData(Vector3Int location, ITilemap tilemap, ref TileData tileData)
    

`GetTileData` determines what the tile looks like on the tilemap. See `TileData` below for more details.

## Using GetTileAnimationData
    
    
    public bool GetTileAnimationData(Vector3Int location, ITilemap tilemap, ref TileAnimationData tileAnimationData)
    

`GetTileAnimationData` determines whether or not the tile is animated. Return true if there is an animation for the tile, other returns false if there isn’t.

## Using StartUp
    
    
    public bool StartUp(Vector3Int location, ITilemap tilemap, GameObject go)
    

`StartUp` is called for each tile when the tilemap updates for the first time. You can run any start up logic for Tiles on the Tilemap if necessary. The argument `go` is the instanced version of the object passed in as **gameobject** when `GetTileData` was called. You may update `go` as necessary as well.