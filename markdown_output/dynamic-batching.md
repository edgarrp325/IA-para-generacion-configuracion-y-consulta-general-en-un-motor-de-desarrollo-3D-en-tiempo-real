---
title: "Dynamic batching"
category: "General"
source_file: "dynamic-batching.html"
doc_type: "manual"
---

# Dynamic batching

Dynamic batching is a draw call batching method that batches moving **GameObjects** to reduce draw calls. **Dynamic batching** works differently between meshes and geometries that Unity generates dynamically at runtime, such as particle systems works differently between meshes and geometries that Unity generates dynamically at runtime, such as particle systems. For information about the internal differences between meshes and dynamic geometries, see Dynamic batching for meshes and Dynamic batching for dynamically generated geometries.

**Note** : Dynamic batching for meshes was designed to optimize performance on old low-end devices. On modern consumer hardware, the work dynamic batching does on the CPU can be greater than the overhead of a draw call. This negatively affects performance. For more information, see Dynamic batching for meshes.

## Requirements and compatibility

This section includes information about the **render pipeline** compatibility of dynamic batching.

### Render pipeline compatibility

**Feature** | **Built-in Render Pipeline** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)**  
---|---|---|---|---  
**Dynamic Batching** | Yes | Yes | No | Yes  
  
## Using dynamic batching

Unity always uses dynamic batching for dynamic geometry such as Particle Systems

To use dynamic batching for meshes:

  1. Go to **Edit** > **Project Settings** > **Player**.
  2. In **Other Settings** , enable **Dynamic Batching**.

Unity automatically batches moving meshes into the same draw call if they fulfill the criteria described in the common usage information.

## Dynamic batching for meshes

Dynamic batching for meshes works by transforming all vertices into world space on the CPU, rather than on the GPU. This means dynamic batching is only an optimization if the transformation work is less resource intensive than doing a draw call. 

The resource requirements of a draw call depend on many factors, primarily the graphics API. For example, on consoles or modern APIs like Apple Metal, the draw call overhead is generally much lower, and often dynamic batching doesn’t produce a gain in performance. To determine whether it’s beneficial to use dynamic batching in your application, profile your application with and without dynamic batching.

Unity can use dynamic batching for shadows casters, even if their materials are different, as long as the material values Unity needs for the shadow pass are the same. For example, multiple crates can use materials that have different textures. Although the material assets are different, the difference is irrelevant for the shadow caster pass and Unity can batch shadows for the crate GameObjects in the shadow render step.

### Limitations

In the following scenarios, Unity either can’t use dynamic batching at all or can only apply dynamic batching to a limited extent:

  * Unity can’t apply dynamic batching to meshes that contain more than 900 vertex attributes and 300 vertices. This is because dynamic batching for meshes has an overhead per vertex. For example, if your **shader** uses vertex position, vertex normal, and a single UV, then Unity can batch up to 300 vertices. However, if your shader uses vertex position, vertex normal, UV0, UV1, and vertex tangent, then Unity can only batch 180 vertices.
  * If GameObjects use different material instances, Unity can’t batch them together, even if they are essentially the same. The only exception to this is shadow caster rendering.
  * GameObjects with lightmaps have additional renderer parameters. This means that, if you want to batch lightmapped GameObjects, they must point to the same **lightmap** location.
  * Unity can’t fully apply dynamic batching to GameObjects that use multi-pass shaders. 
    * Almost all Unity shaders support several lights in **forward rendering**. To achieve this, they process an additional render pass for each light. Unity only batches the first render pass. It can’t batch the draw calls for the additional per-pixel lights.

## Dynamic batching for dynamically generated geometries

The following renderers dynamically generate geometries, such as particles and lines, that you can optimize using dynamic batching:

  * Built-in Particle Systems
  * Line Renderers
  * Trail Renderers

Dynamic batching for dynamically generated geometries works differently than it does for meshes:

  1. For each renderer, Unity builds all dynamically batchable content into one large vertex buffer.
  2. The renderer sets up the material state for the batch.
  3. Unity then binds the vertex buffer to the GPU.
  4. For each Renderer in the batch, Unity updates the offset in the vertex buffer and submits a new draw call.

This approach is similar to how Unity submits draw calls for static batching.