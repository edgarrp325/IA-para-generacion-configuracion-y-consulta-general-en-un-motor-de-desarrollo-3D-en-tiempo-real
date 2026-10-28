---
title: "Sprite Atlas properties reference"
category: "General"
source_file: "class-SpriteAtlas.html"
doc_type: "manual"
---

# Sprite Atlas properties reference

To create a Sprite Atlas in Unity, go to **Assets** > **Create** > **2D** > **Sprite Atlas**. Unity creates the Sprite Atlas in the **Assets** folder, with the file extension `.spriteatlas`.

Sprite Atlas Inspector window **Property** | **Description**  
---|---  
**Type** | Set the **Sprite** Atlas’ Type to either **Master** or **Variant**. **Master** is the default Type setting. When you set this property to **Variant** , Unity reveals additional property settings. For more information about the two types, refer to Master and Variant Sprite Atlases.  
**Include in Build** | Check this box to include the **Sprite Atlas** Asset in the current build. This option is enabled by default.  
**Allow Rotation** | Check this box to allow the Sprites to rotate when Unity packs them into the Sprite Atlas. This maximizes the density of Sprites in the combined Texture, and is enabled by default. Disable this option if the Sprite Atlas contains Canvas UI element Textures, as when Unity rotates the Textures in the Sprite Atlas during packing, it rotates their orientation in the **Scene**  
**Tight Packing** | Check this box to pack Sprites based on their Sprite outlines instead of the default rectangle outline. This maximizes the density of Sprites in the combined Texture, and is enabled by default.  
**Padding** | Defines how many pixels are between the individual Sprite Textures in the Sprite Atlas. This is a buffer to prevent **pixel** overlap between Sprites that are next to each other in the Sprite Atlas. The default value is 4 pixels.  
**Read/Write Enabled** | Check this box to enable access to the Texture data from script functions (such as Texture2D.SetPixels, and other Texture2D functions). If you enable this property, Unity creates a copy of the Texture data. This doubles the amount of memory required for Texture Assets, and can negatively affect performance. This property is disabled by default. This property is only valid for uncompressed or DXT compressed Textures as Unity can’t read other types of compressed Textures.  
**Generate Mip Maps** | Check this box to enable mipmap generation. For more information, refer to the **Generate Mip Maps** property in Sprite (2D and UI) Import Settings.  
**sRGB** | Check this box to store Textures in gamma space. For more information, refer to the **sRGB (Color Texture)** property in Sprite (2D and UI) Import Settings.  
**Filter Mode** | Select how Unity filters packed Textures when they stretch during transformations. This setting overrides the **Filter Mode** setting of any packed Sprite in the Atlas. For more information, refer to the **Filter Mode** property in Sprite (2D and UI) Import Settings.  
**Default** (Platform-specific overrides panel on the Texture Import Settings window) | Sets the resolution, the file size with associated memory size requirements, the pixel dimensions, and the quality of your Textures for each target platform of the Sprite Atlas. This panel lets you override these settings on the individual Textures that the Sprite Atlas contains. For more information, refer to Platform-specific overrides.  
**Objects For Packing** | Unity packs all items in this list into the currently selected Sprite Atlas. For more information, refer to Selecting items for the Objects for Packing list.  
  
* * *

  * New in Unity 2017.1 NewIn20171

SpriteAtlas