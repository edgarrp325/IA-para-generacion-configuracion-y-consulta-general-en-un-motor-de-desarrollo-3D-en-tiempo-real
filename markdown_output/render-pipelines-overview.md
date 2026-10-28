---
title: "Introduction to render pipelines"
category: "General"
source_file: "render-pipelines-overview.html"
doc_type: "manual"
---

# Introduction to render pipelines

A **render pipeline** takes the objects in a **scene** takes the objects in a **scene** and displays them on-screen.

## How a render pipeline works

A render pipeline follows these steps:

  1. Culling, where the pipeline decides which objects from the scene to display. This usually means it removes objects that are outside the **camera** view (frustum culling) or hidden behind other objects (occlusion culling view (frustum culling) or hidden behind other objects (occlusion culling).
  2. Rendering, where the pipeline draws the objects with their correct lighting into **pixel** buffers.
  3. **Post-processing** , where the pipeline modifies the pixel buffers to generate the final output frame for the display. Example of modifications include color grading, bloom, and **depth of field** , where the pipeline modifies the pixel buffers to generate the final output frame for the display. Example of modifications include color grading, bloom, and **depth of field**.

A render pipeline repeats these steps each time Unity generates a new frame.

## Render pipelines in Unity

In Unity, you can use one of the following pre-built render pipelines for your project.

The Built-In Render Pipeline is Unity’s default render pipeline. It’s a general purpose render pipeline with limited options for customization.

The Universal Render Pipeline (URP) is a Scriptable Render Pipeline that you can customize. It lets you create scalable graphics across a wide range of platforms.

The High Definition Render Pipeline (HDRP) is a Scriptable Render Pipeline that lets you create cutting-edge, high-fidelity graphics on high-end platforms.

The Scriptable Render Pipelines let you inspect and change how culling, rendering, and post-processing work directly in C#. This level of customization is also possible in the Built-In Render Pipeline when you purchase access to the Unity engine’s source code in C++.

If you’re an experienced graphics developer with advanced customization needs, you can also create your own custom render pipeline using Unity’s Scriptable Render Pipeline API.

Refer to Choose a render pipeline for more information about choosing the right pipeline for your project.

## Additional resources

  * Introduction to Lighting and Rendering tutorial