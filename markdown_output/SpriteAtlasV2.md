---
title: "Sprite Atlas V2"
category: "General"
source_file: "SpriteAtlasV2.html"
doc_type: "manual"
---

# Sprite Atlas V2

The original version 1 of the **Sprite** Atlas system packs textures (from sprites, sprites within textures, and sprites in folders) into an Atlas Texture. It packs these textures when it enters Play mode, or when it builds the Player or an AssetBundle. AssetDatabase V1 can’t have dependencies, and has no importer support for named objects, so Unity packs its Sprite Atlases through a custom mechanism and stores the output data of textures and render data in the `Library/AtlasCache` folder.

**Note:** From Unity 2022.2 onwards, the Editor’s **Sprite Atlas** **Mode** is set to **Sprite Atlas V2 - Enabled** by default. Sprite Atlas V2 uses the functionalities exposed by AssetDatabase V2 (ADBV2) such as Cache Server support, which the original Sprite Atlas system didn’t support.

## Sprite Atlas V2 Inspector properties

There are no changes to the **Inspector** properties and settings from that of Sprite Atlas V1 except for the following. The imported Sprite Atlas object is located at the bottom of the Inspector.

  
_The Pack Preview window displayed at the bottom of the Inspector window._

## Enabling Sprite Atlas V2

Sprite Atlas V2 is automatically enabled by default by the Editor from Unity 2022.2 onwards. If you are upgrading an existing project from an earlier version that used an earlier version of Sprite Atlas, go to **Edit > Project Settings > Editor > Sprite Atlas > Mode** and select **Sprite Atlas V2 - Enabled** from the dropdown menu.

When you enable **Sprite Atlas V2** , the following effects occur:

  1. When you create new Sprite Atlases, they’re automatically set to the selected **Mode**.

  2. Unity automatically migrates all existing Sprite Atlas V1 assets to Sprite Atlas V2.

Due to the automatic migration, it’s recommended that you make a backup of your Sprite Atlases V1 before you enable Sprite Atlas V2, as assets converted to V2 are incompatible with V1, and Unity can’t revert them to their original state.

## Enabling Sprite Atlas V2 effects

The following come into effect when you select the following Sprite Atlas V2 options for the Sprite Atlas **Mode** :

  1. If you select **Sprite Atlas V2 - Enabled** , sprites will always use the Sprite Atlas as their texture source, in both Edit and Play modes.

  2. If you select **Sprite Atlas V2 - Enabled for Builds** , Unity only packs Sprite Atlases when building Players, AssetBundles, or Addressable build **scripts**. When the Editor is in Edit mode, sprites continue to use their original textures and not textures from a packed Sprite Atlas.