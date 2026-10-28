---
title: "Hexagonal Tilemaps"
category: "General"
source_file: "Tilemap-Hexagonal.html"
doc_type: "manual"
---

# Hexagonal Tilemaps

In addition to regular Tilemaps, Unity provides both **Hexagonal Point Top** and **Hexagonal Flat Top** Tilemaps. Hexagonal tiles are often used in strategic tabletop games, because they have consistent distance between their centres and any point on their edge, and neighboring tiles always share edges. This makes them ideal for constructing almost any kind of large play area and allows players to make tactical decisions regarding movement and positioning.

The Hexagonal Tilemap uses an offset coordinate system, where alternative rows or columns are offset by half a cell when aligning the cells to the hexagonal grid. For Hexagonal Point Top Tilemaps, every odd row is offset to the right by half a cell’s width. For Hexagonal Flat Top Tilemaps, every odd column is offset to the top by half a cell’s height.

Example: Hexagonal Point Top Tilemap. Offset rows are colored in yellow. Example: Hexagonal Flat Top Tilemap. Offset columns are colored in yellow.

## Creating a Hexagonal Tilemap

To create a **Hexagonal Tilemap** , follow the same steps to create a regular Tilemap (menu: **GameObject > 2D Object**) but choose one of the **Hexagonal** options in the **2D Object**

Hexagonal Tilemap options in the 2D Object menu

Select the **Hexagonal Tilemap** option that matches the orientation of the hexagonal Tiles you are using. The following are examples of a **Hexagonal Point Top Tilemap** and a **Hexagonal Flat Top Tilemap**.

Example of hexagonal Tiles oriented with points facing top Example of hexagonal Tiles oriented with flat sides facing top

When creating the **Tile Palette** for a Hexagonal Tilemap, set the **Grid** setting of the **Tile Palette** to **Hexagon** and select the **Hexagon Type** that matches the Tilemap and Tiles you are using, as shown below.

**Hexagon Type** must match the orientation of the hexagonal Tiles

* * *

  * Hexagonal Tilemaps added in 2018.2 NewIn20182