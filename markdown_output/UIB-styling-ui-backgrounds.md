---
title: "Set background images"
category: "General"
source_file: "UIB-styling-ui-backgrounds.html"
doc_type: "manual"
---

# Set background images

You can use either the Image element or the `VisualElement.style.backgroundImage` property to add visual content to your **UI**

## Set background images with an image asset

You can use an imported or built-in image asset to set a background image. When you set the background image, you must select a supported background image type:

  * Textures
  * Sprites
  * Render textures
  * SVG Vector images

**Note** : 

  * To use an SVG image as a background image, you must install the `com.unity.vectorgraphics` package.
  * When you import an image to your project, define the image import settings for the most intuitive results.

You can set the background image in UI Builder, directly in USS, or in C# files. 

**USS example** :
    
    
    MyElement {
        background-image: url("path/to/imageFile.png");
    }
    

**C# example** :
    
    
    // Use the AssetDatabase method to load the texture.
    myElement1.style.backgroundImage = AssetDatabase.LoadAssetAtPath<Texture2D>("path/to/imageFile.png");
    
    // Use the AssetDatabase method to load the sprite.
    myElement2.style.backgroundImage = new StyleBackground(AssetDatabase.LoadAssetAtPath<Sprite>("path/to/spriteAssetFile.png"));
    
    // Load the texture from the project's Resources folder.
    myElement3.style.backgroundImage = Resources.Load<Texture2D>("imageFile");
    
    // Load the sprite from the project's Resources folder.
    myElement4.style.backgroundImage = new StyleBackground(Resources.Load<Sprite>("spriteAssetFile"));
    
    // Use the Unity Editor's default resources.
    myElement5.style.backgroundImage = EditorGUIUtility.FindTexture("CloudConnect");
    myElement6.style.backgroundImage = EditorGUIUtility.IconContent("FolderOpened Icon").image;
    

## Set the scale mode for a background image

Scale mode for a background image defines how the image scales to fit the **visual element**.

Slice modes

The supported scale modes for a background image.   
A: `stretch-to-fill` that stretches the image to fill the entire area of the visual element.   
B: `scale-and-crop` that scales the image to fit the visual element. If the image is larger than the visual element, the image is cropped.   
C: `scale-to-fit` that scales the image to fit the visual element. It’s similar to the stretch-to-fill mode, but the **aspect ratio** of the image is preserved.

You can set the scale mode in UI Builder, or directly in USS. 

**USS example:**
    
    
    MyElement {
        -unity-background-scale-mode: scale-and-crop;
    }
    

## 9-Slice images with UI Toolkit

Generally, you can apply the 9-slice technique to a regular 2D Sprite. However, with UI Toolkit, you can apply the 9-slice technique to Texture, Render Texture, and SVG Vector images.

To apply 9-slice, set the following:

  * **Slice values** : The slice values are the **pixel** values for the left, right, top, and bottom slices of the image. The values are relative to the image’s pivot point. For example, if the pivot point is in the center of the image, the left slice value is the number of pixels from the left edge of the image to the pivot point.
  * **Slice scale** : The slice scale is a multiplier that’s applied to the image after the 9-slice technique is applied. Note that for sprites, Unity adjusts the `-unity-slice-scale` by the sprite’s `pixels-per-unit` value in relation to the panel’s `reference sprite pixels per unit value`, which is by default `100`. For example, if the sprite’s `pixels-per-unit` is `16`, the scale is adjusted by `16/100 = 0.16`. Therefore, if you set the scale to `2px`, the final scale is `2px * 0.16px = 0.32px`. For texture and vector images, Unity doesn’t make additional adjustments to the slice scale value you set.

You can set the slice values and slice scale with UI Builder, or directly in USS, or in C# files. For a sprite image, you can also set the values in the Sprite Editor.

**UI Builder** :

Use the **Slice** fields in the **Background** section to set the slice values and slice scale.

UI Builder 9-slice

**USS example** : 
    
    
    MyElement {
        -unity-slice-left: 10px;
        -unity-slice-right: 10px;
        -unity-slice-top: 10px;
        -unity-slice-bottom: 10px;
        -unity-slice-scale: 2px;
    }
    

**C# example** :
    
    
    MyElement.style.unitySliceLeft = 10px;
    MyElement.style.unitySliceRight = 10px;
    MyElement.style.unitySliceTop = 10px;
    MyElement.style.unitySliceBottom = 10px;
    MyElement.style.unitySliceScale = 2px;
    

**Important** : 

  * Slice values set with USS apply only to the image in the associated visual element. The values don’t apply to the same image used in other visual elements, in other UI documents, or in a **scene**.
  * Unset slice value is zero. For example, if you set the Top, Bottom, and Right slice attributes but leave the Left slice empty, the Left slice is zero.
  * Slice values set in USS override slice values set in the Sprite Editor.

## Additional resources

  * UXML element Image
  * Image import settings
  * `EditorGUIUtility`