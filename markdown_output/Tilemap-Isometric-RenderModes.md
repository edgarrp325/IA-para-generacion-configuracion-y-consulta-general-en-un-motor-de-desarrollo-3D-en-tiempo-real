---
title: "Tilemap Renderer Modes"
category: "General"
source_file: "Tilemap-Isometric-RenderModes.html"
doc_type: "manual"
---

# Tilemap Renderer Modes

The **Tilemap Renderer** component renders the Tilemap in the **Scene** in the **Scene**. Unity creates Tilemaps with the Tilemap Renderer attached by default. The Tilemap Renderer can:

  * Render in batches with **Chunk Mode**
  * Render individually with **Individual Mode**

The Render Mode affects the sorting of Tilemap **Sprites** when rendered.

## Rendering in batches with Chunk Mode

**Chunk Mode** is the default rendering mode of the Tilemap Renderer:

When set to **Chunk Mode** , the Tilemap Renderer handles Sprites on a Tilemap in batches and renders them together. They’re treated as a single sort item when sorted in the 2D Transparent Queue. While this reduces draw calls, other renderers can’t render between any part of the Tilemap, preventing other rendered Sprites from interweaving with Tilemap Sprites.

### Using the Sprite Atlas for Sorting (Chunk Mode only)

In **Chunk Mode** , the Tilemap Renderer isn’t able to sort Tiles from multiple textures individually and doesn’t render the tile sprites consistently (refer to the example below).

Pack all the individual Sprites that make up the Tilemap into a single Sprite Atlas to solve this issue. To do this:

  1. Create a **Sprite Atlas** from the Assets menu (go to: **Atlas > Create > Sprite Atlas**).

  2. Add the Sprites to the Sprite Atlas by dragging them to the **Objects for Packing** list in the Atlas’ **Inspector** window. 

  3. Click **Pack Preview**. Unity packs the Sprites into the Sprite Atlas during Play mode, and correctly sorts and renders them. This is only visible in the Editor during Play mode. 

### Rendering individually with Individual Mode

In **Individual Mode** , the Tilemap Renderer sorts and renders the Sprites on a Tilemap with consideration of other Renderers in the Scene, such as the Sprite Renderers and Mesh Renderers and Mesh Renderers. Use this mode if other Renderers interact with Sprites and objects on the Tilemap.

In this mode, the Tilemap Renderer sorts sprites based on their position on the Tilemap and the sorting properties set in the Tilemap Renderer. For example, this allows a character sprite to go in-between obstacle sprites (refer to the example below).

In Individual Mode, the character can be rendered behind the tower Sprites, and also appear above the ground Sprites.

Using the same example in **Chunk Mode** , character sprites might get hidden behind ground sprites:

The same Scene rendered in **Chunk Mode**.

Using **Individual Mode** might reduce performance as there is more overhead when rendering each sprite individually on the Tilemap.

### Custom Axis Sorting Mode for a Z as Y Tilemap in Individual Mode

To sort and render tile sprites on an **Isometric Z as Y** Tilemap, set the Transparency Sort Axis to a **Custom Axis**. To do this:

  1. Set the Tilemap Renderer component **Mode** to **Individual**.
  2. Navigate to **Edit** > **Project Settings** > **Graphics**.
  3. Set **Transparency Sort Mode** to **Custom Axis**.
  4. Set the **Transparency Sort Axis** Y-value to 1 and the Z-value to –0.26.

Refer to the page on Creating an Isometric Tilemap for more information about the **Transparency Sort Axis** settings.