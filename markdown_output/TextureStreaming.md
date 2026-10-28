---
title: "The Mipmap Streaming system"
category: "General"
source_file: "TextureStreaming.html"
doc_type: "manual"
---

# The Mipmap Streaming system

The Mipmap Streaming system gives you control over how Unity loads mipmaps.

This page contains the following information:

  * Overview
  * Getting started
    * Enabling Mipmap Streaming
    * Making textures work with the Mipmap Streaming system
    * Making lightmaps work with the Mipmap Streaming system
  * Configuring Mipmap Streaming
    * Setting the memory budget
    * Configuring Cameras
    * Configuring Editor streaming settings
  * Debugging
  * How Unity calculates the required mipmap level
  * Limitations

For information about using the API to extend the functionality of this system, see Mipmap Streaming system API.

## Overview

This system forces Unity to only load the mipmap levels needed to render the current **Camera** position, instead of loading all of them by default. It trades a small amount of CPU resources to save a potentially large amount of GPU memory.

You can set a total memory limit for all textures in an application, and the system automatically reduces mipmap levels to stay within this budget.

In Unity’s Viking Village demo project, the Mipmap Streaming system saves 25–30% of texture memory, depending on Camera location.

## Getting started

### Enabling Mipmap Streaming

To enable Mipmap Streaming, go to Unity’s Quality Settings (**Edit** > **Project Settings** > **Quality**) and enable the **Texture Streaming** checkbox.

When you enable this setting, the Quality settings window reveals the settings specific to the Mipmap Streaming system. For details on each setting, see documentation on Quality Settings.

By default, this enables Mipmap Streaming for all Cameras in your project.

### Making textures work with the Mipmap Streaming system

Now you can set up Mipmap Streaming on individual textures. Select a texture asset, navigate to the **Inspector** window and view the Texture Import settings. Open the **Advanced** settings, and enable the **Mip Streaming** checkbox.

If you’re developing for Android, you also need to open the Build Settings and set the **Compression Method** to **LZ4** or **LZ4HC**. Unity requires one of these **compression** methods for asynchronous Texture loading, which the Mipmap Streaming system relies upon.

Unity loads mipmap levels at the highest resolution possible while observing the memory budget. You can configure the priority of a texture with the **Mip Streaming** > **Priority** setting in the Texture Import Settings.

Unity uses this setting to determine:

  * Which textures to prioritize when assigning resources.
  * As a mipmap bias value when choosing a mipmap level that fits in the memory budget. For example, with a priority of 2, the mipmap streaming system tries to use a mipmap two levels higher than Textures with a priority of 0.

Positive numbers give higher priority. Valid values range from –128 to 127.

### Streaming Lightmaps

You can use the Mipmap Streaming system to stream mipmap levels for **lightmaps**.

You can edit the Mip Map Streaming settings of the lightmap assets in the same way that you can any other texture, but they reset to their default values when Unity regenerates the lightmaps. To solve this, you can tell Unity to apply these values when it generates the lightmaps. The Player Settings (**Edit** > **Project Settings** > **Player**) provide two controls to set streaming and priority for generated lightmaps: **Lightmap Streaming Enabled** and **Streaming Priority**.

Enabling Mip Map Streaming and configuring priority work in the same way for lightmaps as for regular textures.

## Configuring Mipmap Streaming

You can configure default settings in the Unity Editor, and then use the Mipmap Streaming API to override these settings if required.

### Setting the memory budget

The **Memory Budget** property determines the maximum amount of memory Unity uses for textures. If your memory budget is too small, Unity lowers the resolution of textures in your **scene**. This can cause textures to pop or load slowly. However, the memory budget should be as small as possible to allow memory for other resources.

Set the memory budget in the Quality Settings window, with the **Texture Streaming** > **Memory Budget** property.

When the memory budget is full, Unity discards mipmaps it’s not using, to make room for those it needs to use. You can control how many unused mipmaps it discards with the **Max Level Reduction**.

This value is also the mipmap level that the Mipmap Streaming system initially loads at startup. For example, when this is set to 2, Unity skips the two highest mipmaps on first load.

Set this value in the Quality Settings window, with the **Texture Streaming** > **Max Level Reduction** property.

**Note:** Unity prioritises the **Max Level Reduction** value over the memory budget. It never discards more mipmaps than the **Max Level Reduction** value, even if this causes the textures memory to exceed the budget.

The memory budget includes textures that do not use Mipmap Streaming. For example, if your budget is 100MB and you have 90MB of textures that don’t use Mipmap Streaming, Unity tries to fit all the streaming mipmaps in the remaining 10MB. If it can’t, it loads them at a lower resolution. Unity always loads textures that don’t use Mipmap Streaming at full resolution, even if that exceeds the budget.

To figure out what your memory budget should be:

  1. Look at the Texture.desiredTextureMemory value when your project is running.
  2. Set the **Memory Budget** value slightly higher than the Texture.desiredTextureMemory value.

This makes sure there is enough texture memory available for the most resource-intensive areas of your scene and prevents textures from dropping to a lower resolution. If you have extra memory available, you can set a larger memory budget so that Unity can keep texture data that is not visible in your scene in the streaming cache.

### Configuring Cameras

By default, when you enable the Mipmap Streaming system, Unity enables it for all cameras. You can disable this setting if you like.

Control whether Unity enables mipmap Streaming for all Cameras in the Quality Settings window, with the **Texture Streaming** > **Add All Cameras** property.

If you want to exclude a specific Camera, add a Streaming Controller component to that Camera and then disable it.

If you disable **Add All Cameras** , then you must enable mipmap Streaming per-Camera. To do this, add a Streaming Controller component to the same **GameObject**

This component also allows you to adjust the mipmap bias setting per-Camera.

The Streaming Controller component

### Configuring Editor streaming settings

The streaming settings found in **Edit** > **Project Settings** > **Editor**

Mipmap Streaming (also known as texture streaming) in the Editor is enabled by default, but only takes effect if you have enabled **Texture Streaming** in Quality Settings, and have enabled **Mipmap Streaming** on one or more of your texture asset’s import settings.

You can control whether Unity uses Mipmap Streaming in the Editor in both Play Mode and Edit Mode independently. To do this, go to **Project Settings** > **Editor** > **Streaming Settings**.

If you enable Mipmap Streaming in the Editor for one mode but not the other, entering and exiting Play mode takes slightly longer. Enabling Mipmap Streaming for both modes prevents Unity from unloading and reloading mipmap data, and increases the speed of entering and exiting Play Mode.

The “Load texture data on demand” setting enables further optimizations in the Editor for textures which have mipmap streaming enabled, which:

  * Asynchronously loads texture data to memory from disk
  * Only loads the mipmap levels required by current camera views
  * Attempts to work within the Texture Streaming Memory Budget for the current Quality setting

These optimizations avoid some stalls, make loading slightly faster, and reduce the amount of CPU memory used. However, this setting can cause mipmapped textures to temporarily appear at a lower resolution than they should while a higher resolution version is loaded in. This feature incurs some overhead on the CPU, so you might want to leave this disabled if your textures all fit in memory at once, or you don’t have any textures set up to stream.

## Debugging Mipmap Streaming

Unity has a built-in Mipmap Streaming debugging view mode. To access it, click the Scene view control drop-down and select **Texture Streaming**. This view mode tints GameObjects the following colours, depending on their status in the Mipmap Streaming system:

  * **Green** for Textures that have reduced mipmaps due to the Mipmap Streaming system.
  * **Red** for Textures that have fewer mipmaps because the Mipmap Streaming system does not have enough resources to load them all.
  * **Blue** for Textures that are not set to stream, or if there is no renderer calculating the mipmap levels.

You can also write your own custom debug tools and visualizations using the Debugging API

**Important** : When the main texture is set using the MainTexture attribute, it is not visible in the game view when you use the texture streaming debugging view mode or a custom debug tool.

## How Unity calculates the required mipmap level

For textures that use Mipmap Streaming, Unity calculates the correct mipmap level using one of the following methods:

  * If you assign the texture to a material that is used by a Unity Renderer componennt, Unity calculates the mipmap level automatically.
  * Otherwise, you must request mipmap levels manually using Texture2D.requestedMipmapLevel.

If you don’t do this, Unity can’t calculate the correct mipmap level, and it loads the texture using low-resolution mipmap levels. These can appear blurry.

**Note:** The following systems don’t use standard Renderer components. This means you must manually set the requested mipmap levels for these systems:

  * Decal projector textures.
  * **Reflection probe** textures: Lower resolution mipmap levels are a lookup table for roughness. Therefore, if Unity uses a lower mipmap level, it renders materials using the wrong roughness.
  * **Shaders** that use UV texture coordinates in a channel other than Mesh.uv (also called UV0), or change texture coordinates in the shader. The only exceptions are changes to scale and translation (see below).

## Limitations

  * Unity does not support Mipmap Streaming on **Terrain** textures. This is because Terrain Textures need to be available at full resolution at all times to allow Unity to tile and blend the textures.
  * When a Renderer component is active, its mesh requires valid UV distribution metrics to calculate the desired mipmap level. Unity calculates distribution metrics automatically as part of the mesh importing process.  
  
If you create a mesh from code, Unity does not calculate distribution metrics automatically and therefore it loads the wrong mipmap levels. To manually trigger the UV distribution metric calculation use Mesh.RecalculateUVDistributionMetrics.
  * When Unity renders a streamed Texture directly with an API (such as Graphics.DrawMeshNow) the system has no renderer bounds or other information to calculate the mipmap level. This means you need to set the Texture mipmap level manually or disable Mipmap Streaming on this Texture. See Texture2D.requestedMipmapLevel for more details on how to manually set which mipmap level Unity loads.
  * When Unity calculates the miplevel for a texture it looks for the scale and translation of that texture in a `_ST` value with the same name as the texture flagged in your shader. For example, if you reference your textures are in the shader using `_MainTex`, Unity will look for `_MainTex_ST`.