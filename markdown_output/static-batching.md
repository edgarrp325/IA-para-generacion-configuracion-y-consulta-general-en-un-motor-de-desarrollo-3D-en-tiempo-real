---
title: "Static batching"
category: "General"
source_file: "static-batching.html"
doc_type: "manual"
---

# Static batching

Static batching is a draw call batching method that combines meshes that don’t move to reduce draw calls. It transforms the combined meshes into world space and builds one shared vertex and index buffer for them. Then Unity performs a single draw call that uses this combined mesh to draw all objects in the batch at once. **Static batching**

Static batching is more efficient than dynamic batching because static batching doesn’t transform vertices on the CPU. For more information about the performance implications for static batching, see Performance implications.

## Requirements and compatibility

This section includes information about the **render pipeline** compatibility of static batching.

### Render pipeline compatibility

**Feature** | **Built-in Render Pipeline** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)**  
---|---|---|---|---  
**Static Batching** | Yes | Yes | Yes | Yes  
  
## Using static batching

Unity can perform static batching at build time and at runtime. As a general rule, if the **GameObjects** exist in a **scene** exist in a **scene** before you build your application, use the Editor to batch your GameObjects at build time. If you create the GameObjects and their meshes at runtime, use the runtime API. 

When you use the runtime API, you can change the transform properties of the root of a static batch. This means that you can move, rotate, or scale the entire combination of meshes that make up a static batch. You can’t change the transform properties of the individual meshes. 

To use static batching for a set of GameObjects, the GameObjects must be eligible for static batching. In addition to the criteria described in the common usage information, make sure that:

  * The GameObject is active.
  * The GameObject has a Mesh Filter component, and that component is enabled.
  * The Mesh Filter component has a reference to a Mesh.
  * The mesh has a vertex count greater than 0.
  * The mesh has not already been combined with another Mesh.
  * The GameObject has a Mesh Renderer component, and that component is enabled.
  * The Mesh Renderer component does not use any Material with a **shader** that has the `DisableBatching` tag set to true.
  * Meshes you want to batch together use the same vertex attributes. For example Unity can batch meshes that use vertex position, vertex normal, and one UV with one another, but not with meshes that use vertex position, vertex normal, UV0, UV1, and vertex tangent.

**Note** : To use runtime static batching you must also set the mesh to have read/write enabled.

For information about the performance implications for static batching, see Performance implications.

### Static batching at build time

You can enable static batching at build time in the Editor.

To perform static batching at build time:

  1. Go to **Edit** > **Project Settings** > **Player**.
  2. In **Other Settings** , enable **Static Batching**.
  3. In the Scene view or Hierarchy, select the GameObject that you want to batch and view it in the Inspector.  
**Tip** : You can select multiple GameObjects at the same time to enable static batching for all of them.
  4. In the GameObject’s Static Editor Flags, enable **Batching Static**.

Unity automatically batches the specified static meshes into the same draw call if they fulfill the criteria described in the common usage information.

The Static Editor Flags checkbox in the Inspector for a GameObject.

**Note** : If you perform static batching at build time, Unity doesn’t use any CPU resources at runtime to generate the mesh data for the static batch.

### Static batching at runtime

To batch static meshes at runtime, Unity provides the StaticBatchingUtility class. The static StaticBatchingUtility.Combine method combines the GameObjects you pass in and prepares them for static batching. This is especially useful for meshes that you procedurally generate at runtime. 

Unlike static batching at build time, batching at runtime doesn’t require you to enable the **Static Batching** Player Setting. For information on how to use this API, see StaticBatchingUtility.

## Performance implications

Using static batching requires additional CPU memory to store the combined geometry. If multiple GameObjects use the same mesh, Unity creates a copy of the mesh for each GameObject, and inserts each copy into the combined mesh. This means that the same geometry appears in the combined mesh multiple times. Unity does this regardless of whether you use the editor or runtime API to prepare the GameObjects for static batching. If you want to keep a smaller memory footprint, you might have to sacrifice rendering performance and avoid static batching for some GameObjects. For example, marking trees as static in a dense forest environment can have a serious memory impact.

**Note** : There are limits to the number of vertices a static batch can include. Each static batch can include up to 64000 vertices. If there are more, Unity creates another batch.