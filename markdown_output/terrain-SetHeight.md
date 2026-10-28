---
title: "Set Height"
category: "General"
source_file: "terrain-SetHeight.html"
doc_type: "manual"
---

# Set Height

Use the **Set Height** tool to adjust the height of an area on the **Terrain** to a specific value. To access the tool, click on the **Paint Terrain** icon, and select the **Set Height** tool from the drop-down menu.

Set Height tool in the Terrain Inspector

When you paint with the **Set Height** tool, it lowers areas of the Terrain currently above the target height, and raises areas below that height. **Set Height** is useful for creating flat, level areas in a **Scene** , such as plateaus or man-made features like roads, platforms, and steps.

Choose a property from the **Space** drop-down menu to specify whether the height offset is relative to **Local** or **World** space.

**Property** | **Description**  
---|---  
**World** | Select this to set the height offset to the value you enter in the **Height** field. However, be aware that the **Set Height** tool cannot lower a Terrain below its Transform Position Y coordinate, even if you enter a value lower than the Y coordinate.  
**Local** | Select this to set the height offset relative to the Terrain. For example, if you enter 100 in the **Height** field, the height offset is the sum of the Terrain’s Transform Position Y coordinate and 100 (`terrain.transform.position.y` \+ 100). The **Height** value you enter must range from 0 to the **Terrain Height** value in the Terrain settings.  
  
Enter a numerical value in the **Height** field, or use the **Height** property slider, to manually set a height. Alternatively, press Shift and click on the Terrain to sample the height at the cursor position, similar to how you would use the Eyedropper tool in an image editor.

If you press the **Flatten Tile** button under the **Height** field, it levels the whole Terrain tile to the height you specified. This is useful to set a raised ground level if, for example, you want the landscape to include both hills above the ground level and valleys below it. If you press the **Flatten All** button, it levels all Terrain tiles in the Scene.

The **Brush Size** value determines the size of the Brush to use, while the **Opacity** value determines how quickly the height of the area you’re painting reaches the set target height.

You can also use **heightmaps** to edit the height of your Terrain. For more information, see Working with Heightmaps.

* * *

  * 2019–10–22 Page amended 

  * Updated content to match the new UI and added information about the Space option.