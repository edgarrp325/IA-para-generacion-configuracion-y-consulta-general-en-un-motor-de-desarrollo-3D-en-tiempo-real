---
title: "Smooth Height"
category: "General"
source_file: "terrain-SmoothHeight.html"
doc_type: "manual"
---

# Smooth Height

The **Smooth Height** tool smooths the heightmap and softens **Terrain** and softens **Terrain** features. In the Terrain **Inspector** features. In the Terrain **Inspector** , click the **Paint Terrain** icon, and select **Smooth Height** from the list of Terrain tools.

Smooth Height tool in the Terrain Inspector

The **Smooth Height** tool averages out nearby areas, softens the landscape and reduces the appearance of abrupt changes; it does not significantly raise or lower Terrain height.

Smoothing is particularly useful after you paint with brushes containing high frequency patterns. These brush patterns tend to introduce sharp, jagged edges into a landscape, but you can use the **Smooth Height** tool to soften that roughness.

Adjust the **Blur Direction** value to control which areas to soften. If you set **Blur Direction** to –1, the tool softens exterior (convex) edges of your Terrain. If you set **Blur Direction** to 1, the tool softens interior (concave) edges of your Terrain. To smooth all parts of your Terrain evenly, set **Blur Direction** to 0.

The **Brush Size** value determines the size of the Brush to use, while the **Opacity** value determines how quickly the tool smooths out the area you’re painting.

* * *

  * 2019–04–17 Page published 

  * Updated content to reflect new UI and options