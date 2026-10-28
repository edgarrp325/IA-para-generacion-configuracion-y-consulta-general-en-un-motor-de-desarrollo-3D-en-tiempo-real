---
title: "Draw call batching"
category: "General"
source_file: "DrawCallBatching.html"
doc_type: "manual"
---

# Draw call batching

Draw call batching is a draw call optimization method that combines meshes so that Unity can render them in fewer draw calls. Unity provides two built-in draw call batching methods:

  * Static batching: For static **GameObjects**
  * Dynamic batching: For small enough meshes, this transforms their vertices on the CPU, groups similar vertices together, and renders them in one draw call.

Unity’s built-in draw call batching has several advantages over manually merging meshes; most notably, Unity can still cull meshes individually. However, it also has some downsides; static batching incurs memory and storage overhead, and dynamic batching incurs some CPU overhead.

## Requirements and compatibility

This section includes information about the **render pipeline** compatibility of Unity’s built-in draw call batching methods.

### Render pipeline compatibility

**Feature** | **Built-in Render Pipeline** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)**  
---|---|---|---|---  
**Static Batching** | Yes | Yes | Yes | Yes  
**Dynamic Batching** | Yes | Yes | No | Yes  
  
## Using draw call batching

The following usage information is relevant for both static and dynamic batching. For information specific to each draw call batching method, such as how to enable and use each method, see Static batching and Dynamic batching.

Mesh Renderers, Trail Renderers, Trail Renderers, Line Renderers, Line Renderers, Particle Systems, Particle Systems, and Sprite Renderers, and Sprite Renderers are supported for draw call batching. Other types of rendering components, including Skinned **Mesh** are supported for draw call batching. Other types of rendering components, including Skinned **Mesh** Renderers Cloth, are not supported. Unity only batches Renderers with other Renderers of the same type; for example, Mesh Renderers with Mesh Renderers.

Unity batches draw calls of GameObjects that use the same material. This means to get the best results from draw call batching, share materials among as many GameObjects as possible. If you have two material assets that are identical apart from their textures, you can combine the textures into a single, larger texture. This process is called texture atlasing. For more information, see the Wikipedia article on texture atlasing. When textures are in the same atlas, you can use a single material asset instead.

In the Built-in Render Pipeline, you can use a MaterialPropertyBlock to change material properties without breaking draw call batching. The CPU still needs to make some render-state changes, but using a `MaterialPropertyBlock` is faster than using multiple materials. If your project uses a Scriptable Render Pipeline, don’t use a `MaterialPropertyBlock` because they remove SRP Batcher compatibility for the material.

Transparent **shaders** often require Unity to render meshes in back-to-front order. To batch transparent meshes, Unity first orders them from back to front and then tries to batch them. Since Unity must render the meshes back-to-front, it often can’t batch as many transparent meshes as opaque meshes.

Unity can’t apply dynamic batching to GameObjects that contain mirroring in their **Transform component**. For example, if one GameObject has a scale of **1** and another GameObject has a scale of **–1** , Unity can’t batch them together.

If you are not able to use draw call batching, manually combining meshes that are close to each other can be a good alternative. For more information on combining meshes, see Combining meshes.

**Warning** : When you access shared material properties from a C# script, make sure to use Renderer.sharedMaterial and not Renderer.material. `Renderer.material` creates a copy of the material and assigns the copy back to the Renderer. This stops Unity from batching the draw calls for that Renderer.

* * *

  * 2017–10–26 Page amended 

  * Added note on dynamic batching being incompatible with graphics jobs in 2017.2