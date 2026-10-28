---
title: "Image import settings"
category: "General"
source_file: "UIE-image-import-settings.html"
doc_type: "manual"
---

# Image import settings

After you have imported an image to your project, for the most intuitive results, it’s recommended that you apply certain import settings for Textures, **Sprites** , and Vector images before you use them as a background for a **visual element** , and Vector images before you use them as a background for a **visual element** in the **UI** in the **UI** Builder.

## Texture

The recommended import settings for a **Texture** image that you use as a background for a visual element are as follows.

Use the following settings for Default Texture types, and Editor GUI and Legacy GUI Texture types:

**Property** | **Value**  
---|---  
**Non-Power of 2** | None  
****Compression**** | None  
**Alpha Is Transparency** | true  
  
Use the following settings for Sprite (2D and UI) Texture types:

**Property** | **Value**  
---|---  
**Compression** | None  
**Alpha Is Transparency** | true  
**Sprite Mode** | Single  
****Mesh** Type** | Tight  
  
## Sprites

The recommended import settings for a **Sprite** image that you use as a background for a visual element:

**Property:** | **Value:**  
---|---  
**Compression** | None  
**Alpha Is Transparency** | true  
**Sprite Mode** | Multiple if file contains multiple sprites, Single otherwise.  
**Mesh Type** | Tight  
  
## Vector images

The recommended import settings for a SVG **Vector** image that you use as a background for a visual element:

**Property:** | **Value:**  
---|---  
**Generated Asset Type** | UI Toolkit Vector Image  
**Tessellation Settings** | Basic  
**Target Resolution** | Lowest value that produces satisfactory results  
  
**Tip** : 

  * You can apply default presets to Assets by folder to automatically set your desired import settings.
  * All image types are subject to dynamic atlasing if they’re not already in an atlas. (An image is in an atlas if imported as a Sprite with **Sprite Mode** set to **Multiple** , or if you have manually added it to a Sprite Atlas

## Additional resources

  * UIE-uxml-element-Image