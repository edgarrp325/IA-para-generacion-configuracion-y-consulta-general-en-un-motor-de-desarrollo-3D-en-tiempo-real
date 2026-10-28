---
title: "Preparing Sprite Atlases for distribution"
category: "General"
source_file: "SpriteAtlasDistribution.html"
doc_type: "manual"
---

# Preparing Sprite Atlases for distribution

Ensure that the source Texture of the **Sprite** is always uncompressed. While packing **Sprite Atlas** is always uncompressed. While packing **Sprite Atlas** , **pixel** , **pixel** data is read from the source texture and if it uses any compressed format, it may result in loss of precision as it must be uncompressed first before packing. If a Sprite is packed to a Sprite Atlas, only the Sprite Atlas Texture needs to be compressed.

A Project can have multiple Sprite Atlases for different purposes (for example, Variant Atlases with lower-resolution Textures for hardware with different limitations). If you enable all available Sprite Atlases, you might encounter conflicts (refer to Resolving different Sprite Atlas scenarios for more information). 

To prevent these issues, properly prepare Sprite Atlases for distribution with the following steps:

  1. Disable ‘Include in Build’ in the Sprite Atlas properties.
  2. Choose a method to distribute the Atlas.
  3. Load the Atlas via Late Binding with a script.

## Disable ‘Include in Build’

Unity includes Sprite Atlases in a Project’s build by default, and automatically loads them at run time. Clear the **Include in Build** setting of the selected Sprite Atlas to disable this behavior.

If ‘Include in Build’ is disabled, Unity still packs the Sprite Atlas into a *.spriteatlas file in the Project’s Assets folder. However, Sprites which reference Textures in a disabled Sprite Atlas appear invisible as the reference Texture is not available or loaded. Unity does not include the disabled Sprite Atlas in the Project’s published build, and does not automatically load it at run time. To do so, a script is required to load the Sprite Atlas via Late Binding.