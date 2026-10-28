---
title: "Optimizing draw calls"
category: "General"
source_file: "optimizing-draw-calls.html"
doc_type: "manual"
---

# Optimizing draw calls

To draw geometry on the screen, Unity issues draw calls to the graphics API. A draw call tells the graphics API what to draw and how to draw it. Each draw call contains all the information the graphics API needs to draw on the screen, such as information about textures, **shaders** , and buffers. Draw calls can be resource intensive, but often the preparation for a draw call is more resource intensive than the draw call itself. 

To prepare for a draw call, the CPU sets up resources and changes internal settings on the GPU. These settings are collectively called the render state. Changes to the render state, such as switching to a different material, are the most resource-intensive operations the graphics API performs.

Because render-state changes are resource intensive, it is important to optimize them. The main way to optimize render-state changes is to reduce the number of them. There are two ways to do this:

  * Reduce the total number of draw calls. When you decrease the number of draw calls, you also decrease the number of render-state changes between them.
  * Organize draw calls in a way that reduces the number of changes to the render state. If the graphics API can use the same render state to perform multiple draw calls, it can group draw calls together and not need to perform as many render-state changes.

Optimizing draw calls and render-state changes has a number of benefits for your application. Mainly, it improves frame times, but it also:

  * Reduces the amount of electricity your application requires. For battery-powered devices, this reduces the rate at which batteries run out. It also reduces the amount of heat a device produces when running your application.
  * Improves maintainability of future development on your application. When you optimize draw calls and render-state changes earlier and maintain them at an optimized level, you can add more **GameObjects** to your **scene** to your **scene** without producing large performance overheads.

There are several methods you can use in Unity to optimize and reduce draw calls and render-state changes. Some methods are more suited for certain scenes than others. The following methods are available in Unity:

  * GPU instancing: Render multiple copies of the same **mesh**
  * Draw call batching: Combine meshes to reduce draw calls. Unity provides the following types of built-in draw call batching: 
    * Static batching: Combine meshes of static GameObjects in advance. Unity sends the combined data to the GPU, but renders each mesh in the combination individually. Unity can still cull the meshes individually but each draw call is less resource-intensive since the state of the data never changes.
    * Dynamic batching: Transforms mesh vertices on the CPU, groups vertices that share the same configuration, and renders them in one draw call. Vertices share the same configuration if they store the same number and type of attributes. For example, `position` and `normal`.
  * Manually combining meshes: Manually combine multiple meshes into a single mesh, using the Mesh.CombineMeshes function. Unity renders the combined mesh in a single draw call instead of one draw call per mesh.
  * SRP Batcher: If your Project uses a Scriptable **Render Pipeline**

## Optimization priority

You can use multiple draw call optimization methods in the same scene but be aware that Unity prioritizes draw call optimization methods in a particular order. If you mark a GameObject to use more than one draw call optimization method, Unity uses the highest priority method. The only exception to this is the SRP Batcher. When you use the SRP Batcher, Unity also supports static batching for GameObjects that are SRP Batcher compatible. Unity prioritizes draw call optimizations in the following order:

  1. SRP Batcher and static batching
  2. GPU instancing
  3. Dynamic batching

If you mark a GameObject for static batching and Unity successfully batches it, Unity disables GPU instancing for that GameObject, even if the renderer uses an instancing shader. When this happens, the **Inspector** window displays a warning message that suggests that you disable static batching. Similarly, if Unity can use GPU instancing for a mesh, Unity disables dynamic batching for that mesh.