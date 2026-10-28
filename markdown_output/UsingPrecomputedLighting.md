---
title: "Generating lighting data"
category: "General"
source_file: "UsingPrecomputedLighting.html"
doc_type: "manual"
---

# Generating lighting data

In Unity, precomputed lighting is generated in the background either as an automatic process or when manually initiated. It is possible to continue working in the editor while these processes run.

The Editor follows different steps to calculate **Enlighten** Realtime **Global Illumination** and Baked Global Illumination. The progress bar displays information about the current process.

The stages of lighting precomputation are listed below:

**Enlighten Realtime Global Illumination**

  1. Create Geometry
  2. Layout Systems
  3. Create Systems
  4. Create Atlas
  5. Clustering
  6. Visibility
  7. Light Transport
  8. Tetrahedralize Probes
  9. Create ProbeSet

**Probes**

  1. Ambient Probes
  2. Baked/Realtime Ref. Probes

**Enlighten Baked Global Illumination**

  1. Create Geometry
  2. Atlassing
  3. Create Baked Systems
  4. Baked Resources
  5. Bake AO
  6. Export Baked Texture
  7. Bake Visibility
  8. Bake Direct
  9. Ambient and Emissive
  10. Create Bake Systems
  11. Bake Runtime
  12. Upsampling Visibility
  13. Bake Indirect
  14. Final Gather
  15. Bake ProbesSet
  16. Compositing

## Generating data

Unity’s precomputed lighting solutions only consider static geometry. To begin the lighting precompute process, you need at least one Static ****GameObject**** in your ****Scene****.

When you manually initiate a precompute, the Unity Editor evaluates and computes all aspects of your Scene lighting. To recalculate and bake only Reflection Probes, select the **Generate Lighting** option **Reflection Probes** Lighting Window.

## Before you build

Before building your game, disable the **Auto Generate** option in the **Lighting Window** and generate the lighting data manually for all your Scenes, to ensure that you do not lose any lighting data.

When you deactivate **Auto Generate** and manually generate lighting for your Scene, Unity saves your lighting data as Asset files in your project directory. This ensures that the data you need is part of your build.

**Auto-Generate** is not recommended for multi-scene workflows.