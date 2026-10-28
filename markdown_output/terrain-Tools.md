---
title: "Terrain tools"
category: "General"
source_file: "terrain-Tools.html"
doc_type: "manual"
---

# Terrain tools

To access the **Terrain** painting tools, click on a Terrain object in the **Hierarchy** window and open an **Inspector** painting tools, click on a Terrain object in the **Hierarchy** window and open an **Inspector** window. In the Inspector, click the **Paint Terrain** (paintbrush) icon to reveal the list of Terrain tools.

Terrain tools drop-down menu

The Terrain component provides six distinct tools:

  * **Raise or Lower Terrain** : paint the **heightmap** with a paintbrush tool.
  * **Paint Holes** : hide portions of the Terrain.
  * **Paint Texture** : apply surface textures.
  * **Set Height** : adjust the heightmap toward a specific value.
  * **Smooth Height** : smooth the heightmap to soften Terrain features.
  * **Stamp Terrain** : stamp a brush shape on top of the current heightmap.

## Additional terrain tools

The Terrain Tools package, when you install it, brings additional functionality on top of the built-in terrain tools listed above. It includes erosion tools, sculpting tools, brush mask filters, and a Terrain Toolbox which provides preset file management and heightmap import features, among others.

## Custom terrain tools

The Unity API allows you to create your own custom Terrain tools to complete or override the existing tools, including the ones of the Terrain Tools package.

For more information about Terrain tool API, refer to TerrainAPI.TerrainPaintTool, and to create a custom Terrain tool with overlay support, refer to TerrainAPI.TerrainPaintToolWithOverlays.

The Terrain Tools package documentation also provides several Terrain API use case examples.

* * *

  * 2019–10–22 Page amended 

  * Updated screenshot to match the new UI and added the Paint Holes tool.