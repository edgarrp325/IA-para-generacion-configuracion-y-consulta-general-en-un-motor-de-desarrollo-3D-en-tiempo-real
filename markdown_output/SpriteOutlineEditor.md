---
title: "Sprite Editor: Custom Outline"
category: "General"
source_file: "SpriteOutlineEditor.html"
doc_type: "manual"
---

# Sprite Editor: Custom Outline

Use the Sprite Editor’s **Custom Outline** option to edit the shape of the Mesh that Unity renders the Sprite texture on. The Custom Outline editor allows you to use control points to create and define the shape of the Sprite’s Mesh outline.

By default, Unity renders each Sprite on a rectangle Mesh. This Mesh might include transparent areas outside the Texture’s border, and rendering these transparent areas can negatively affect performance. When you use the Custom Outline editor to define a Mesh outline that matches the outline of the Sprite Texture, you reduce the size of the transparent areas, which improves performance.

To access the Custom Outline editor, select a Sprite and then in the Sprite’s **Inspector** window, select the Sprite Editor button. In the Sprite Editor window, open the upper-left drop-down menu and select **Custom Outline** to open the Custom Outline editor.

Select **Custom Outline** from the Sprite Editor drop-down menu.

## The Custom Outline editor

Editing a Sprite’s outline in the Custom Outline editor.

### Custom Outline editor properties

Property | Function  
---|---  
**Snap** | Snap control points to the nearest **pixel**.  
**Outline Tolerance** | Use this slider to control how tightly and accurately the generated outline follows the outline of the Sprite texture. At the minimum value (0), the Sprite Editor generates a basic outline around the Sprite. At the maximum value (1), the Sprite Editor generates an outline that follows the outline of the Sprite texture as closely as possible.  
**Generate** | When you click this button, Unity automatically creates an outline based on the **Outline Tolerance** value you set.  
**Copy** | After you have generated or set up a custom outline, click this **Copy** button to duplicate the custom outline. Leaving the Custom outline module or closing the Sprite Editor removes the copied outline from memory.  
**Paste** | Use this button to paste a copied outline to the currently selected Sprite. If you have not used the **Copy** function to copy an outline, this button is not available. To **Paste** a copied custom outline to another Sprite, in the **Project window** select the Sprite while the Custom outline editor window is open. Then click the **Paste** button to paste the copied outline to the new Sprite. When you paste the outline, if a point in the outline is larger than the Sprite’s frame, Unity clamps the point to be inside the Sprite’s frame.  
**Paste All** | Use this button to paste a copied outline to all Sprites in the Sprite Editor window, regardless of selection. If you have not used the **Copy** function to copy an outline, this button is unavailable. Use this function to apply the same outline to multiple Sprites in the same Texture (such as when a Texture has its Sprite Mode set to ‘Multiple’). When you paste the outline, if a point in the outline exceeds the Sprite’s frame, Unity clamps the point to be inside that Sprite’s frame.  
**Revert** | Undoes any unsaved recent changes made in the editor window. To save changes, click **Apply** first.  
**Apply** | Select this button to save all changes made in the editor window.  
  
## Using the Custom Outline editor

The Custom Outline editor allows you to to create or generate the Mesh of the Sprite. There are two ways to create a custom outline: have Unity automatically generate the shape, or manually creating and editing it in the editor window.

### Generating the outline 

To have Unity automatically generate an outline that follows the shape of the original Sprite texture, and that also takes into account transparent areas in the texture, click the **Generate** button. However, you can adjust how tightly the generated outline follows the Sprite texture by adjusting the **Outline Tolerance** slider.

The **Generate** button is next to the **Outline Tolerance** slider.

Adjust the **Outline Tolerance** slider to refine the outline of the Mesh that Unity generates. Increasing the value increases how closely the outline follows the shape of the Sprite texture. Leaving the slider at 0 generates a Mesh that more loosely follows the Sprite texture.

_Left_ : An automatically generated Mesh outline with a low **Outline Tolerance**. _Right_ : An automatically generated Mesh outline with a high **Outline Tolerance**.

### Editing the custom outline

You can create your own custom shape and edit it in two ways. The first way is by automatically generating an outline, and then moving the control points of the generated outline to further refine its shape. Alternatively click and drag over any space in the Custom Outline editor window to create a rectangular outline with four control points and begin refining the outline by moving the control points or adding and removing them.

You can create multiple outlines in the same texture.

Click and drag over the Sprite texture in the editor window to create rectangle outlines with four control points. Repeat this step to create multiple Mesh outlines within the Sprite. Unity only renders the areas enclosed within the Mesh outlines.

#### **Moving control points**

To adjust the shape of the Mesh outline, click and drag its control points. When you hover over a control point, it turns blue to indicate that you can select it. Click and drag the control point to different positions to adjust the shape of the Mesh outline. You can select multiple control points at once by clicking and dragging the cursor over an area to select all control points within that area. You can then re-position or remove all selected control points altogether.

Moving a control point to change the shape of the Mesh outline.

#### Adding/Removing control points 

To add a control point, place the cursor over the edge of the outline. A preview of the control point appears along the outline’s edge. Click to add a new control point at that location. To remove a control point, select it and press the **Del/Command+Del keys**.

Adding a control point to a Mesh outline

#### Moving edges

To move a section between two control points, hold the **Control/Ctrl** key to select the edges of the outline instead of its control points. To change the shape of the outline, click and drag the highlighted edge to move them into new positions.

Moving a section of Mesh outline between two control points

* * *

  * Copy and Paste editor window functions added in 2020.1 NewIn20201
  * **Edit Outline** renamed to **Custom Outline** in Unity version 2017.3.