---
title: "Stamp Terrain"
category: "General"
source_file: "terrain-StampTerrain.html"
doc_type: "manual"
---

# Stamp Terrain

Use the **Stamp Terrain** tool to stamp a brush shape on top of the current heightmap. In the **Terrain Inspector** , click on the **Paint Terrain** icon and select **Stamp Terrain** from the drop-down menu.

Stamp Terrain tool in the Terrain Inspector

**Stamp Terrain** is useful if you create a custom brush using a Texture that represents a heightmap with a specific geological feature, such as a hill.

With the **Stamp Terrain** tool, you can choose an existing brush and apply it with a single click. Each click raises the **Terrain** to the set **Stamp Height** in the shape of the selected brush. To multiply the **Stamp Height** by a percentage, move the **Opacity** slider to change its value. For example, a **Stamp Height** of 200 and an **Opacity** of 50% sets the height of each stamp to 100.

The **Max <–> Add** slider lets you choose whether to pick the maximum height, or add the height of your stamp to the Terrain’s current height.

  * If you set the **Max <–> Add** value to 0, then stamp onto the Terrain, Unity compares the height of your stamp to the current height of the stamped area, and sets the final height to the value that is higher.

  * If you set the **Max <–> Add** value to 1, then stamp onto the Terrain, Unity adds the height of your stamp to the current height of the stamped area, so that the final height is the sum of both values.

Enable the **Subtract** checkbox to subtract the height of any stamps you apply to the Terrain from the existing height of the stamped area. Note that **Subtract** works only if your **Max <–> Add** value is greater than zero, for example, if you set the **Max <–> Add** value to 1. If the stamp height exceeds the current height of the stamped area, the system levels the height to zero.

* * *

  * 2019–04–18 Page published 

  * Updated content to reflect new UI and options