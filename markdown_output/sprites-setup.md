---
title: "Import images as sprites"
category: "General"
source_file: "sprites-setup.html"
doc_type: "manual"
---

# Import images as sprites

Import images into the Unity Editor to create your own sprite assets.

Sprites are a type of asset you can use in your 2D Unity project. This page shows how to import images as sprites you can use in your 2D Unity project. This page shows how to import images as sprites.

You can import images into your project through two main methods:

  * Place images directly into your project’s `Assets` folder.
  * Import images into Unity through the Editor menu.

If you create your project with the 2D template or set the project to 2D mode, Unity automatically imports images as the Sprite (2D and UI) **Texture Type**. If you set your project mode to 3D instead, Unity imports your image as a texture.

## Prerequisites

To adjust the import settings for images imported as the Sprite (2D and UI), you must install the 2D Sprite package. You will be given the option to install the package if you select the **Sprite (2D and UI)** Texture Type without the package installed.

## Place images directly into the project folder 

  1. In your computer’s _File Explorer_ (**macOS** : _Finder_), go to your Unity project’s `Assets` folder.
  2. Place your image directly into the `Assets` folder.
  3. Unity detects the placed image and displays it in the **Project** window.

## Import an image through the Editor menu 

  1. In the Unity Editor, go to **Assets** > **Import New Asset**.
  2. Select the image you want to import from the _File Explorer_ (**macOS** : _Finder_) window. Unity makes a copy of your selected image and places it in the `Assets` folder.

Refer to Importing assets for more information on how Unity processes and organizes imported assets.

## Set the Texture Type of an imported image to Sprite (2D and UI) 

To change an asset’s **Texture Type** :

  1. Select the asset to access its **Import**Inspector****.
  2. Set the **Texture Type** to **Sprite (2D and UI)**.

For more information about the sprite **Texture Type** settings, refer to the Sprite (2D and UI) import settings reference.

## Additional resources

  * Texture Import Settings
  * Sprite Editor