---
title: "Paint Holes"
category: "General"
source_file: "terrain-PaintHoles.html"
doc_type: "manual"
---

# Paint Holes

Use the **Paint Holes** tool to hide portions of your **Terrain**. It allows you to paint openings in the Terrain for formations such as caves and cliffs.

To access the tool, click the **Paint Terrain** icon, and select **Paint Holes** from the drop-down menu.

Paint Holes tool in the Terrain Inspector

To paint holes, click and drag the cursor across the Terrain. To erase holes from the Terrain, click and drag while holding down the Shift key. Use the **Brush Size** slider to control the size of your tool. The **Opacity** slider determines the strength of the Brush when you apply it to the Terrain.

Internally, Unity uses a Texture to define the opacity mask for a Terrain surface. When you use the **Paint Holes** tool to paint on a Terrain, it modifies this Texture. Thus, any holes you paint are visible only if the Terrain Material you use clips or discards texels based on this mask.

Because this tool uses a Texture, you might see aliased edges surrounding holes you paint. Therefore, for example, when you make a cave, you might choose to hide the aliased edges of the hole with other geometry such as rock meshes.

Terrain holes work with lighting, physics, and **NavMesh** baking. Unity discards the Terrain information in areas where you paint holes to ensure accurate lighting, Terrain **Colliders** baking. Unity discards the Terrain information in areas where you paint holes to ensure accurate lighting, Terrain **Colliders** , and baked NavMeshes.

To support physics Colliders, the resolution of the hole’s mask Texture is equal to the resolution of the Terrain’s **heightmap** \- 1.

## Additional resources

  * Digging into Terrain Paint Holes in Unity 2019.3

* * *

  * Paint Holes added in 2019.3 NewIn20193