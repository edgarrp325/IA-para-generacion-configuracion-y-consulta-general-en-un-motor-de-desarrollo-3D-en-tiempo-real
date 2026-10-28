---
title: "Image"
category: "General"
source_file: "script-Image.html"
doc_type: "manual"
---

# Image

The **Image** control displays a non-interactive image to the user. You can use this for purposes such as decorations or icons, and you can change the image from a script to reflect changes in other controls. The control is similar to the Raw Image control, but offers more options for animating the image and accurately filling the control rectangle. However, the Image control requires its Texture to be a Sprite control, but offers more options for animating the image and accurately filling the control rectangle. However, the Image control requires its Texture to be a Sprite, while the Raw Image can accept any Texture.

An Image control

## Properties

**_Property:_** | **_Function:_**  
---|---  
**Source Image** | The Texture that represents the image to display (which must be imported as a Sprite).  
**Color** | The color to apply to the image.  
**Material** | The Material to use for rendering the image.  
**Raycast Target** | Enable **Raycast Target** if you want Unity to consider the image a target for raycasting.  
**Preserve Aspect** | Ensure the image retains its existing dimension.  
**Set Native Size** | Set the dimensions of the image box to the original **pixel** size of the Texture.  
  
You must import the image to display as a Sprite to work with the Image control. 

Image