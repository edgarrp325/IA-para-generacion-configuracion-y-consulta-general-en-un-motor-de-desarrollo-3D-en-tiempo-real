---
title: "Include sprites in text"
category: "General"
source_file: "UIE-sprite.html"
doc_type: "manual"
---

# Include sprites in text

To use sprites in your rich text tags, such as emojis, you need a **sprite** asset. You create sprite assets from atlas textures asset. You create sprite assets from atlas textures that contain a set of sprites.

An example atlas texture

You can use as many sprite atlases and assets as you want. However, if you use multiple atlases per text object results in multiple draw calls for that object and consumes more system resources. As a rule, when you import multiple sprites, pack them into a single atlas to reduce draw calls. Make sure the **sprite atlas** has a suitable resolution for your target platform.

Use the `<sprite>` rich text tag to include sprites in your text.

See information for all the Sprite asset properties.

## Create a sprite asset

You create sprite assets from atlas textures. Although sprite assets and their source textures are separate entities, you must keep the source textures in the project after you’ve created the sprite assets. 

To create a sprite asset:

  1. Import the sprite atlas.

  2. Select the atlas and change the following texture options in the **Inspector** window:

     * Set the **Texture Type** to **Sprite (2D and UI)**.
     * Set the **Sprite Mode** to **Multiple**.
  3. Select **Sprite Editor** and divide the texture into individual sprites.

  4. Right-click the sprite and select **Create** > **Text** > **Sprite Asset**. This creates a new sprite asset.

  5. From the Inspector window, you can further customize the appearance and names of each glyph. See Sprite Asset properties for more information.

  6. Place the sprite asset to the path set in the Panel Text Settings.

Once you’ve created the sprite asset, you can revert the atlas texture’s **Texture Type** to its original setting.

## Use a sprite asset

To use sprites in the rich text tag, reference the sprite asset name and the sprite name as `<sprite="assetName" name="spriteName">` or by index as `<sprite="assetName" index=1>`.

You can add the `tint=1` attribute to the tag to tint the sprite with the text object’s vertex color. You can also choose a different color by adding a color attribute to the tag, for example: `<sprite="assetName" index=1 color=#55FF55FF>`.

For runtime UI, if you have set a sprite asset as the default in the Panel Text Settings, you can omit the asset name as `<sprite index=1>` (or shorthand `<sprite=1>`), or `<sprite name="spriteName">`.

## Assign and use Unicode for a sprite

You can assign a Unicode to a sprite and use the Unicode directly in your text object instead of the `<sprite>` tag.

For example, the Unicode for a smiling face emoji is `U+1F60A`. To assign it to a sprite in your sprite asset:

  1. In the sprite asset’s Inspector window, find the glyph in the **Sprite Character Table**. You can browse or search by index or name.
  2. Click the glyph to enable the edit mode.
  3. In the Unicode box, enter `+1F60A`.
  4. Click the **Unicode** label to save your changes. The Unicode changes to `0xF1F60A`.

To use the smiling face emoji in your text object, enter `\U00F1F60A`.

## Additional resources

  * Sprite asset properties
  * Rich text tags