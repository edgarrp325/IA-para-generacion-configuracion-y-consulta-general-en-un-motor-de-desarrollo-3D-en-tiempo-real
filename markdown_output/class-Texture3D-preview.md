---
title: "Preview a 3D texture"
category: "General"
source_file: "class-Texture3D-preview.html"
doc_type: "manual"
---

# Preview a 3D texture

To preview a 3D texture, do one of the following:

  * Use the **Inspector** window.
  * Draw the 3D texture in the **Scene** view.

## Use the Inspector window

To preview a 3D texture, select the texture in the **Project** window. In the **Inspector** window, Unity displays the preview of the texture at the bottom of the **Texture Import Settings** window.

There are three different 3D texture preview modes available:

  * **Volume** mode displays the 3D texture as a translucent cube. Click and drag the cube to rotate the preview.
  * **Slice** mode displays a 2D slice of each of the three axes of the 3D texture. Use the **X** , **Y** and **Z** sliders to select the slices to preview.
  * **SDF** mode displays the 3D texture as a signed distance field (SDF) in 3D space.

Refer to 3D texture preview reference for more information.

## Draw the 3D texture in the Scene view

Use the `Handles` API to draw the 3D texture in the **Scene view**

Refer to the following for more information:

  * `Handles.DrawTexture3DVolume`
  * `Handles.DrawTexture3DSlice`
  * `Handles.DrawTexture3DSDF`