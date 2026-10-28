---
title: "Manually combining meshes"
category: "General"
source_file: "combining-meshes.html"
doc_type: "manual"
---

# Manually combining meshes

You can manually combine multiple meshes into a single **mesh** as a draw call optimization technique. Unity renders the combined mesh in a single draw call instead of one draw call per mesh. This technique can be a good alternative to draw call batching in cases where the meshes are close together and don’t move relative to one another. For example, for a static cupboard with lots of drawers, it makes sense to combine everything into a single mesh.

**Warning** : Unity can’t individually cull meshes you combine. This means that if one part of a combined mesh is onscreen, Unity draws the entire combined mesh. If the meshes are static and you want Unity to individually cull them, use static batching instead.

There are two main ways to combine meshes:

  * In your asset generation tool while authoring the mesh.
  * In Unity using Mesh.CombineMeshes.