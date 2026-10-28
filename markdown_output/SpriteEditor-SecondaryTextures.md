---
title: "Sprite Editor: Secondary Textures"
category: "General"
source_file: "SpriteEditor-SecondaryTextures.html"
doc_type: "manual"
---

# Sprite Editor: Secondary Textures

The **Sprite** Editor’s **Secondary Textures** module can associate additional Textures with edited Sprites. A **Shader** Editor’s **Secondary Textures** module can associate additional Textures with edited Sprites. A **Shader** can then sample these secondary Textures to apply additional effects on the Sprite, such as normal mapping. Secondary Textures are currently only supported by **Sprite Renderers** can then sample these secondary Textures to apply additional effects on the Sprite, such as normal mapping. Secondary Textures are currently only supported by **Sprite Renderers** and are not available for other Renderer components.

To use this functionality, select the **Secondary Textures** module from the drop-down menu at the top left of the **Sprite Editor** window.

## Adding a Secondary Texture

To add a new Secondary Texture entry, select the ‘‘+’’ at the bottom right of the **Secondary Textures** panel. You can add a maximum of eight Secondary Textures to each Sprite or Sprite Sheet. Each added Secondary Texture appears as an entry on the list, with two fields: Name and Texture.

You can enter a custom name for the Secondary Texture in the Name field. Some Unity packages suggest Texture names that can be used with their Shaders. The drop-down arrow to the right of the Name field displays a list of valid suggested names. Suggested names remain in the drop-down menu even after their associated packages are uninstalled.

To select the Texture used by the Secondary Texture, drag the Texture Asset directly onto the Texture field, or open the **Object Picker** window by selecting the circle to the right of the field.

Secondary Textures are sampled with the same UV coordinates as the main Sprite Texture. Align the Secondary Textures with the main Sprite Texture to ensure that additional Texture effects are displayed correctly.

To preview the Secondary Texture in the **Sprite Editor** window with the main Sprite Texture hidden, select an entry in the list. Click outside of the Secondary Textures list to deselect the entry, and the main Sprite Texture is visible again.

## Deleting a Secondary Texture

To delete a Secondary Texture from the list, select it and then select the ‘-’ button at the bottom right of the window.

## Applying the Changes

To apply your changes to the edited Sprites, select Apply on the **toolbar**. Entries without a Name or selected Texture are considered invalid and are automatically removed when changes are applied.