---
title: "Creating and editing Terrains"
category: "General"
source_file: "terrain-UsingTerrains.html"
doc_type: "manual"
---

# Creating and editing Terrains

To add a Terrain GameObject to your Scene, select **GameObject > 3D Object > Terrain** from the menu. This also adds a corresponding Terrain Asset to the Project view. When you do this, the landscape is initially a large, flat plane. The Terrain’s Inspector window provides a number of tools to create detailed landscape features.

Terrain editing tools in the Inspector

Terrain editing tools in the Inspector

The **toolbar** provides five options to adjust your Terrain: 

  * Create adjacent Terrain tiles.
  * Sculpt and paint your Terrain.
  * Add trees.
  * Add details such as grass, flowers, and rocks.
  * Change general settings for the selected Terrain.

For more information about each of these icons, see Create Neighbor Terrains, Terrain tools, Trees

Select the paintbrush icon to access painting tools, which allow you to modify the Terrain. Use the cursor to sculpt the height of the Terrain, or paint texture onto the Terrain. Choose from several built-in Brush shapes, or define your own Brush using a texture. You can also change the size and opacity (the strength of the applied effect) of the Brush. Once you’ve defined the properties, your cursor takes the shape of the selected Brush. Click or drag on the Terrain to create different shapes and textures.

Similar to how you paint with a Brush on the Terrain, you can add textures, trees, and details like grass, flowers, and rocks. You can also create additional connected Terrain tiles, change the height of an entire tile, and even write custom Brushes with complex effects.

## Terrain keyboard shortcuts

The Terrain **Inspector** has the following keyboard shortcuts enabled by default.

Keys | Function  
---|---  
Comma ( , ) and Period ( . ) | Cycle through the available Brushes  
Shift-Comma ( < ) and Shift-Period ( > ) | Cycle through the available objects for trees, textures, and details  
Open Bracket ( [ ) and Close Bracket ( ] ) | Decrease and increase the Brush Size  
Minus ( - ) and Equal ( = ) | Decrease and increase Brush Opacity  
  
To set your own custom shortcuts, use the **Shortcuts Manager**. 

  * On Windows and Linux, select **Edit > Shortcuts**.
  * On macOS, select **Unity > Shortcuts**.

Under **Category** , select **Terrain** to display Terrain-related shortcut assignments. For more information about setting and modifying shortcuts, see the Shortcuts Manager page.

List of Terrain shortcuts

Additionally, the standard F keystroke works slightly differently for Terrain. As Terrains are typically very large, when you press the F key, the **Scene** view focuses on the area where you position the cursor. This provides a very quick and intuitive way to jump to the Terrain area you want to edit. If you press F while the cursor is not over a Terrain tile, it uses the standard framing behavior, framing the selection around the whole **GameObject** view focuses on the area where you position the cursor. This provides a very quick and intuitive way to jump to the Terrain area you want to edit. If you press F while the cursor is not over a Terrain tile, it uses the standard framing behavior, framing the selection around the whole **GameObject** when you place the cursor over the **Scene view** when you place the cursor over the **Scene view**.

## Additional resources

  * Scripting Reference for custom Terrain tools

* * *

  * 2019–04–17 Page amended 

  * Updated content to match new UI and added information about keyboard shortcuts