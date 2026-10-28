---
title: "9-slicing Sprites"
category: "General"
source_file: "9SliceSprites.html"
doc_type: "manual"
---

# 9-slicing Sprites

9-slicing is a 2D technique which allows you to reuse an image at various sizes without needing to prepare multiple Assets. It involves splitting the image into nine portions, so that when you re-size the Sprite. It involves splitting the image into nine portions, so that when you re-size the Sprite, the different portions scale or tile (that is, repeat in a grid formation) in different ways to keep the Sprite in proportion. This is useful when creating patterns or Textures, the different portions scale or tile (that is, repeat in a grid formation) in different ways to keep the Sprite in proportion. This is useful when creating patterns or Textures, such as walls or floors in a 2D environment.

This is an example of a 9-sliced Sprite, split into nine sections. Each section is labelled with a letter from A to I.

The following points describe what happens when you change the dimensions of the image:

  * The four corners (A, C, G and I) do not change in size.

  * The B and H sections stretch or tile horizontally.

  * The D and F sections stretch or tile vertically.

  * The E section stretches or tiles both horizontally and vertically.

This page describes how to set 9-slicing up, and which settings to apply depending on whether you want to stretch or tile the areas shown above.

## Setting up your Sprite for 9-slicing

Before you 9-slice a Sprite, you need to ensure the Sprite is set up properly.

First, you need to make sure the **Mesh Type** is set to **Full Rect**. To apply this, select the Sprite, then in the Inspector window click the **Mesh Type** drop-down and select **Full Rect**. If the **Mesh Type** is set to **Tight** , 9-slicing might not work correctly, because of how the Sprite Renderer generates and renders the Sprite when it is set up for 9-slicing. 

The Sprite’s Inspector window. **Mesh Type** is highlighted in the red box.

Next, you need to define the borders of the Sprite via the **Sprite Editor** window. To do this, select the Sprite, then in the Inspector

The Sprite’s Inspector window. The **Sprite Editor** button is highlighted in the red box. See documentation on Sprites for information on all of the properties in the Sprite Import Settings.

Use the Sprite Editor window to define the borders of the Sprite (that is, where you want to define the tiled areas, such as the walls of a floor tile). To do this, use the Sprite control panel’s **L** , **R** , **T** , and **B** fields (left, right, top, and bottom, respectively). Alternatively, click and drag the green dots at the top, bottom, and sides.

Defining the borders of the Sprite in the Sprite Editor window

Click **Apply** in the Sprite Editor window’s top bar. Close the Sprite Editor window, and drag the Sprite from the Project window into the **Scene** into the **Scene** view to begin working on it.

## 9-slicing your Sprite

Select the Sprite in the Scene view or the Hierarchy window. In the Inspector window, navigate to the Sprite Renderer or the Hierarchy window. In the Inspector window, navigate to the Sprite Renderer component and change the **Draw Mode** property. 

It is set to **Simple** by default; to apply 9-slicing, set it to either **Sliced** or **Tiled** depending on the behavior you want. The following sections explain how each one behaves, using this Sprite:

The original Sprite used for the examples shown below

### Simple

This is the default Sprite Renderer behaviour. The image scales in all directions when its dimensions change. **Simple** is not used for 9-slicing.

### Sliced

In **Sliced** mode, the corners stay the same size, the top and bottom of the Sprite stretch horizontally, the sides of the Sprite stretch vertically, and the centre of the Sprite stretches horizontally and vertically to fit the Sprite’s size.

When a Sprite’s **Draw Mode** is set to **Sliced** , you can choose to change the size using the **Size** property on the Sprite Renderer or the Rect Transform Tool. You can still scale the Sprite using the Transform properties or the Transform Tool; however, the Transform scales the Sprite without applying the 9-slicing. 

### Tiled

In **Tiled** mode, the sprite stays the same size, and does not scale. Instead, the top and bottom of the Sprite repeat horizontally, the sides repeat vertically, and the centre of the Sprite repeats in a tile formation to fit the Sprite’s size.

When you set the **Draw Mode** to **Tiled** , an additional property called **Tile Mode** appears. See the next section in this page for more information on how **Tile Mode** works. 

See documentation on the Sprite Renderer for full details on all of the component’s properties.

## Tile Mode

When the **Draw Mode** is set to **Tiled** , use the **Tile Mode** property to control how the sections repeat when the dimensions of the Sprite change.

### 

### Continuous

**Tile Mode** is set to **Continuous** by default. When the size of the Sprite changes, the repeating sections repeat evenly in the Sprite.

### Adaptive

When **Tile Mode** is set to **Adaptive** , the repeating sections only repeat when the dimensions of the Sprite reach the **Stretch Value**. 

Use the **Stretch Value** slider to set the value between **0** and **1**. Note that **1** represents an image resized to twice its original dimensions, so if the **Stretch Value** is set at **1** , the section repeats when the image is stretched to twice its original size.

To demonstrate this, the following images show the difference between an image with the same dimension but a different **Stretch Value:**

**Stretch Value 0.1** :

**Stretch Value 0.5** :

## 9-slicing and Colliders

If your Sprite has a Collider2D attached, you need to ensure that when you change the Sprite’s dimensions, the Collider2D changes with it.

Box Collider 2D and Polygon Collider 2D are the only Collider2D components in Unity that support 9-slicing. These two Collider2Ds have an **Auto Tiling** checkbox. To make sure the Collider2D components are set up for 9-slicing, select the Sprite you are applying it to, navigate to the Collider2D in the Inspector window, and tick the **Auto Tiling** checkbox. This enables automatic updates to the shape of the Collider2D, meaning that the shape is automatically readjusted when the Sprite’s dimensions change. If you don’t enable **Auto Tiling** , the Collider2D stays the same shape and size, even when the Sprite’s dimensions change.

### Limitations and known issues

  * The only two Collider2Ds that support 9-slicing are BoxCollider2D and PolygonCollider2D.

  * You cannot edit BoxCollider2D or PolygonCollider2D when the Sprite Renderer’s **Draw Mode** is set to **Sliced** or **Tiled**. Editing in the Inspector window is disabled, and a warning appears to notify you that the Collider2D cannot be edited because it is driven by the Sprite Renderer component’s tiling properties.

  * When the shape is regenerated in **Auto Tiling** , additional edges might appear within the Collider2D’s shape. This may have an effect on **collisions**.