---
title: "Sprite Packer Modes"
category: "General"
source_file: "SpritePackerModes.html"
doc_type: "manual"
---

# Sprite Packer Modes

To enable or disable the **Sprite Atlas** default packing behavior, open the Editor settings (menu: **Edit > Project Settings > Editor**) and navigate to **Sprite Packer > Mode**. Select the Sprite Packer **Mode** to determine how Unity uses the Sprite Atlas within the Editor.

Mode | Function  
---|---  
**Disabled** | Select this mode to disable **Sprite** Atlas packing in the current Project. Sprite Atlases are not built when the Project enters Play mode or when publishing a build. **Pack Preview** is also disabled.  
****Sprite Atlas** V1 - Enabled For Builds** | Select this mode to have Unity pack Sprites into the Sprite Atlas when publishing builds only. The Editor and Play mode reference the original source Texture instead of the Texture within the Sprite Atlas.  
**Sprite Atlas V1 - Always Enabled** | This option is enabled by default. Select this mode to have Unity pack selected Textures into the Sprite Atlas, and Sprites reference the packed Textures during runtime. However, Sprites will reference the original unpacked Textures during Edit mode.  
**Sprite Atlas V2 - Enabled** | Select this mode to have Unity pack Sprites into the Sprite Atlas immediately when there are any changes. The packed Sprite Atlas is available when the project enters Play mode or when publishing a build.  
**Sprite Atlas V2 - Enabled For Builds** | Select this mode to have Unity pack Sprites into the Sprite Atlas only when publishing a build. The Editor and Play mode will reference the original unpacked Textures.