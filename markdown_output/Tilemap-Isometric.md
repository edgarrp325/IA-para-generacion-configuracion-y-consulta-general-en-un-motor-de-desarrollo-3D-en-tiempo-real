---
title: "Isometric Tilemaps"
category: "General"
source_file: "Tilemap-Isometric.html"
doc_type: "manual"
---

# Isometric Tilemaps

In addition to Hexagonal Tilemaps, Unity enables you to create **Isometric Tilemaps**. The isometric perspective displays all three X, Y, and Z axes, so you can add pseudo-depth and height to a **Tilemap**

Isometric tilemaps are popular in strategy games, as the isometric perspective allows you to simulate 3D gameplay elements such as different elevations and line-of-sight. This lets players make tactical decisions regarding movement and positioning during gameplay.

## Isometric Tilemap workflow

  1. Import and prepare Sprites for an Isometric Tilemap.
  2. Create an Isometric Tilemap.
  3. Create an Isometric Tile Palette.
     * Adjust the Z Position Editor while painting the Tilemap.
  4. Set the Tilemap Renderer Mode and settings. 
     * Set up Chunk Mode sorting with **Sprite**
     * Set the Custom Axis Sort mode.
  5. Customize Scriptable Brushes to handle Z position changes.

* * *

  * Isometric Tilemaps added in 2018.3 NewIn20183