---
title: "Grid component reference"
category: "General"
source_file: "class-Grid.html"
doc_type: "manual"
---

# Grid component reference

Switch to Scripting

The **Grid** component is a guide which helps to align **GameObjects** , such as Tiles, such as Tiles, based on a selected layout. The component transforms Grid cell positions to the corresponding **local coordinates** of the GameObject. The Transform component then converts these local coordinates to world space or **global coordinates**.

Grid component settings window Property | Function  
---|---  
**Cell Size** | The size of a cell on this Grid.  
**Cell Gap** | Enter the size (in Unity units) of gaps between cells on this Grid. If a negative number with an absolute value higher than the **Cell Size** is entered, then Unity will automatically change the absolute value to match the **Cell Size** instead.  
For example, if **Cell Size** is (1, 1, 0) and **Cell Gap** is set to (–2, –2, 0), the Editor will automatically change the **Cell Gap** values to (–1, –1, 0) instead.  
**Cell Layout** | Select an option from the drop-down menu to define the shape and arrangement of cells on this Grid.  
**Rectangle** | Cells are rectangular.  
**Hexagon** | Cells are hexagonal.  
**Isometric** | Cells are rhombus-shaped for an isometric layout.  
**Isometric Z as Y** | Similar to the **Isometric Grid** layout, but Unity converts the Z position of cells to their local Y coordinate.  
**Cell Swizzle** | Select the order that Unity reorders the XYZ cell coordinates to for transform conversions. See the Wikipedia article on Swizzling for more details.  
XYZ | The Grid component uses the default XYZ cell coordinates.  
XZY | The Grid component reorders the XYZ coordinates to XZY.  
YXZ | The Grid component reorders the XYZ coordinates to YXZ.  
YZX | The Grid component reorders the XYZ coordinates to YZX.  
ZXY | The Grid component reorders the XYZ coordinates to ZXY.  
ZYX | The Grid component reorders the XYZ coordinates to ZYX.  
  
* * *

  * Page content and screenshots updated for 2020.1 NewIn20201
  * Tilemaps added in 2017.2 NewIn20172

Grid