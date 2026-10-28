---
title: "Use the Sprite Editor"
category: "General"
source_file: "sprite-editor-use.html"
doc_type: "manual"
---

# Use the Sprite Editor

When you have an image that is a single character with different parts, such as a car with wheels which each move independently, you can use the **Sprite** Editor to extract different parts from that image into separate sprites from the same texture.

**Note** : Make sure the graphic you want to edit has its **Texture Type** set to **Sprite (2D and UI)**. For more information on importing and setting up sprites, refer to Set up sprites.

Sprite textures with multiple components need the **Sprite Mode** to be set to **Multiple** in the **Inspector**.

## Open the Sprite Editor

To open the **Sprite Editor** :

  1. Select the 2D image you want to edit from the **Project View** _(Fig 1: Project View)_.   
**Note** : You can’t edit a sprite by selecting it in the **Scene View**.

  2. Click on the **Sprite Editor** button in the ****Texture Import Inspector**** _(Fig 2: Texture Import Inspector)_ and the **Sprite Editor** displays _(Fig 3: Sprite Editor)_.

**Note:** You can only see the **Sprite Editor** button if the **Texture Type** on the image you have selected is set to **Sprite (2D and UI)**.

Project View Texture Import Inspector with Sprite Editor button

**Note:** Set the **Sprite Mode** to **Multiple** in the **Texture Import Inspector** if your image has several elements.

Sprite Editor

Along with the composite image, you will see a number of controls in the bar at the top of the window. The slider at the top right controls the zoom, while the color bar button to its left chooses whether you view the image itself or its alpha levels. The right-most slider controls the pixilation (mipmap) of the Texture. Moving the slider to the left reduces the resolution of the Sprite Texture. The most important control is the **Slice** menu at the top left, which gives you options for separating the elements of the image automatically.

Select the **Apply** and **Revert** buttons to keep or discard any changes you have made in the Sprite Editor window respectively. You set these buttons to display a confirmation dialog before applying their effects in Unity’s Preferences window. In the Preferences window, go to **2D > Sprite Editor Window** to open the Sprite Editor window options.

Sprite Editor Window preference settings.

Select the respective option to have a dialog appear after selecting **Apply** or **Revert** to confirm your selection, preventing accidental saving or discarding of changes made.

## Use the Editor

The most direct way to use the editor is to identify the elements manually. If you click on the image, you will see a rectangular selection area appear with handles in the corners. You can drag the handles or the edges of the SpriteRect to resize it around a specific element. Having isolated an element, you can add another by dragging a new SpriteRect in a separate part of the image. You’ll notice that when you have a SpriteRect selected, a panel appears in the bottom right of the window:

The controls in the panel let you choose a name for the Sprite graphic and set the position and size of the SpriteRect by its coordinates. A border width, for left, top, right and bottom can be specified in **pixels**. The borders are useful when 9-Slicing Sprites. There are also settings for the Sprite’s pivot, which Unity uses as the coordinate origin and main “anchor point” of the graphic. You can choose from a number of default SpriteRect-relative positions (for example, Center, Top Right, etc) or use custom coordinates.

The **Trim** button next to the Slice menu item will resize the SpriteRect so that it fits tightly around the edge of the graphic based on transparency.

**Note:** Borders are only supported for the **UI** system, not for the 2D **Sprite Renderer** system, not for the 2D **Sprite Renderer**.