---
title: "Creating Tilemaps"
category: "General"
source_file: "Tilemap-CreatingTilemaps.html"
doc_type: "manual"
---

# Creating Tilemaps

A Tilemap is a GameObject you place your selected Tiles on. Create a default (rectangular) **Tilemap** by going to **GameObject > 2D Object > Tilemap**. If you do not have these options, then the **2D Tilemap Editor** package may not be installed. If so, download the **2D Tilemap Editor** package from the Package Manager. 

Select the ‘Tilemap’ option to create the default rectangular Tilemap. Refer to the respective pages for Hexagonal and Isometric Tilemaps for more information on their uses and their options.

After selecting the **Tilemap** option, a new Grid GameObject is created with a child **Tilemap** GameObject in the **scene**

The child Tilemap is comprised of a **Tilemap** component and Tilemap Renderer component. The Tilemap GameObject is where the Tiles are painted on.

Create additional Tilemaps by selecting the Grid GameObject or the Tilemap GameObject, and then go to the menu: **GameObject** > **2D Object** > **2D Object** > **Tilemaps** , or right-click on the selected GameObject and go to **2D Object** > **Tilemap** to add another Tilemap as a child to the same parent Grid.

Once the Tilemap(s) are created, adjust the Grid property settings to adjust the properties of its Tilemap children, such as Cell Size or the type of layout of the child Tilemaps. These also affects attached components such as the Tilemap Renderer and Tilemap Collider 2D components.

## Additional resources

  * Tilemap class (Scripting API)