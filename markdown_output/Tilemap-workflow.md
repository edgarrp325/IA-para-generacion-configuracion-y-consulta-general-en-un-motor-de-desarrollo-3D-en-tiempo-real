---
title: "Tilemap workflow"
category: "General"
source_file: "Tilemap-workflow.html"
doc_type: "manual"
---

# Tilemap workflow

The following is the general workflow and steps for creating a Tilemap.

  1. Create a Tilemap that you will paint your Tiles on. A Grid **GameObject** is also automatically created as a parent to the Tilemap in the process.
  2. Create Tile Assets directly, or generate Tiles automatically by bringing **Sprites**
  3. Create a Tile Palette that contains your **Tile Assets** and use a variety of painting Brushes to Paint onto **Tilemaps**
  4. You can attach the Tilemap Collider 2D component to your Tilemaps to have them interact with Physics2D.

Unity also supports more specialized types of Tilemaps such as Hexagonal and Isometric Tilemaps. Refer to their respective documentation for their specific workflows and properties.

* * *

  * Tilemaps added in 2017.2 NewIn20172