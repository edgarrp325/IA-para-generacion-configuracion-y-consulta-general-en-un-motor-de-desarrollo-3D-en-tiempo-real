---
title: "Vertex Lit Rendering Path"
category: "General"
source_file: "RenderTech-VertexLit.html"
doc_type: "manual"
---

# Vertex Lit Rendering Path

This page describes details of the Vertex Lit rendering path in Unity’s Built-in **Render Pipeline** in Unity’s Built-in **Render Pipeline**.

The Vertex Lit path generally renders each object in one pass, with lighting from all lights calculated for each vertex.

It’s the fastest rendering path and has the widest hardware support.

Since all lighting is calculated at the vertex level, this rendering path does not support most per-pixel effects: shadows, normal mapping, light cookies, and highly detailed specular highlights are not supported.