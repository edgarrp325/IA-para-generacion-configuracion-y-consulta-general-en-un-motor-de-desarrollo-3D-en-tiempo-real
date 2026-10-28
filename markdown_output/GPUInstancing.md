---
title: "GPU instancing"
category: "General"
source_file: "GPUInstancing.html"
doc_type: "manual"
---

# GPU instancing

GPU instancing is a draw call optimization method that renders multiple copies of a **mesh** with the same material in a single draw call. Each copy of the mesh is called an instance. This is useful for drawing things that appear multiple times in a **scene** , for example, trees or bushes.

GPU instancing renders identical meshes in the same draw call. To add variation and reduce the appearance of repetition, each instance can have different properties, such as **Color** or **Scale**. Draw calls that render multiple instances appear in the Frame Debugger as **Render Mesh (instanced)**.

## Requirements and compatibility

This section includes information about the platform, **render pipeline** , and SRP Batcher compatibility of GPU instancing.

### Platform compatibility

GPU instancing is available on every platform except **WebGL** 1.0.

### Render pipeline compatibility

**Feature** | **Built-in Render Pipeline** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)**  
---|---|---|---|---  
**GPU instancing** | Yes | Yes (1) | Yes (1) | Yes (1)  
  
**Notes** :

  1. Only if the shader isn’t compatible with the SRP Batcher.

### SRP Batcher

GPU instancing isn’t compatible with the SRP Batcher. The SRP Batcher takes priority over GPU instancing. If a **GameObject**

If your project uses the SRP Batcher and you want to use GPU instancing for a GameObject, you can do one of the following:

  * Use Graphics.RenderMeshInstanced. This API bypasses the use of GameObjects and uses the specified parameters to directly draw a mesh on screen.
  * Manually remove SRP Batcher compatibility. For information on how to do this, see Intentionally removing compatibility.

## Using GPU instancing

Unity uses GPU instancing for GameObjects that share the same mesh and material. To instance a mesh and material:

  * The material’s shader must support GPU instancing. Unity’s Standard Shader supports GPU instancing, as do all surface shaders must support GPU instancing. Unity’s Standard Shader supports GPU instancing, as do all surface shaders. To add GPU instancing support to any other shader, see Creating shaders that support GPU instancing.
  * The mesh must come from one of the following sources, grouped by behavior: 
    * A MeshRenderer component or a Graphics.RenderMesh call.   
Behavior: Unity adds these meshes to a list and then checks to see which meshes it can instance.   
Unity does not support GPU instancing for SkinnedMeshRenderers or MeshRenderer components attached to GameObjects that are SRP Batcher compatible. For more information, see SRP Batcher compatibility.
    * A Graphics.RenderMeshInstanced or Graphics.RenderMeshIndirect call. These methods render the same mesh multiple times using the same shader. Each call to these methods issues a separate draw call. Unity does not merge these draw calls.

To use GPU instancing for a material, select the **Enable GPU Instancing** option in the **Inspector**.

The Enable GPU Instancing option as it appears in the material Inspector.

### Lighting

GPU instancing supports Unity’s Baked Global Illumination system. Unity Standard Shaders and surface shaders support GPU instancing and Unity’s Baked **Global Illumination** system by default.

Each GPU instance supports global illumination from one of the following sources:

  * Any number of Light Probes.
  * One lightmap.   
**Note** : An instance can use multiple atlas regions in the lightmap.
  * One Light Probe Proxy Volume(LPPV) component.   
**Note** : You must bake the LPPV for the space volume that contains all the instances.

GPU instancing automatically works with:

  * Dynamic Mesh Renderers affected by Light Probes.
  * Static Mesh Renderers you bake to the same lightmap texture. A Mesh Renderer is static in this context if it includes **Contribute GI** in its Static Editor Flags.

To enable Light Probe rendering for `Graphics.RenderMeshInstanced`, provide a MaterialPropertyBlock that includes the Probe data. For more information and code examples, see LightProbes.CalculateInterpolatedLightAndOcclusionProbes.

Alternatively, you can pass an LPPV component reference and LightProbeUsage.UseProxyVolume to `Graphics.RenderMeshInstanced`. When you do this, all instances sample the volume for the L0 and L1 bands of the Light Probe data. If you want to supplement L2 data and occlusion data, use a `MaterialPropertyBlock`. For more information, see Light Probes: Technical Information.

## Performance implications

Meshes that have a low number of vertices can’t be processed efficiently using GPU instancing because the GPU can’t distribute the work in a way that fully uses the GPU’s resources. This processing inefficiency can have a detrimental effect on performance. The threshold at which inefficiencies begin depends on the GPU, but as a general rule, don’t use GPU instancing for meshes that have fewer than 256 vertices.

If you want to render a mesh with a low number of vertices many times, best practice is to create a single buffer that contains all the mesh information and use that to draw the meshes.

* * *

  * 2017–10–24 Page amended 

  * Enable instancing checkbox guidance, DrawMeshInstancedIndirect, #pragma multi-compile added in 5.6

  * Shader warm up for GPU instancing added in 2017.3 NewIn20173

  * Global Illumination (GI) support in GPU instancing added in 2018.1 NewIn20181