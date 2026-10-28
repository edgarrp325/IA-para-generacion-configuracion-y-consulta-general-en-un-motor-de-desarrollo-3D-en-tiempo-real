---
title: "Visualizing lightmap UVs"
category: "General"
source_file: "LightingGiUvs-visualizing.html"
doc_type: "manual"
---

# Visualizing lightmap UVs

It is important to be able to view the lightmap UVs that are being used, and Unity has a visualization tool to help you with this. First, open the Lighting window (menu: **Window** > **Rendering** > **Lighting**) and tick the **Auto** checkbox at the bottom. This ensures that your bake and precompute are up-to-date, and outputs the data that is needed to view the UVs. Wait for the process to finish (this can take some time for large or complex Scenes).

### Visualizing real-time lightmap UVs

To see the UVs for the Realtime **Global Illumination** system:

  * Select a **GameObject** with a ****Mesh** with a ****Mesh** Renderer** component.**
  * In the ****Mesh Renderer**** component, under **Lightmapping** , open the **Realtime**Lightmap**** component, under **Lightmapping** , open the **Realtime**Lightmap**** dropdown.
  * Double-click a lightmap texture to open the **Viewer** window.
  * In the **Viewer** window, open the dropdown and select **UV Charts**.

This displays the UV layout for the real-time lightmap of the selected instance of this Mesh. 

  * The charts are indicated by the different colored areas in the Preview (show in the image above on the right-hand side).
  * The UVs of the selected instance are laid over the charts, as a wireframe representation of the GameObject’s Mesh.
  * Dark gray texels show unused areas of the lightmap.

Multiple instances can be packed into a real-time lightmap, so some of the charts you see might actually belong to other GameObjects.

### Visualizing baked lightmap UVs

To see the UVs for the Baked Global Illumination system:

  * Select a GameObject with a **Mesh Renderer** component.
  * In the **Mesh Renderer** component, under **Lightmapping** , open the **Baked Lightmap** dropdown.
  * Double-click a lightmap texture to open the **Viewer** window.
  * In the **Viewer** window, open the dropdown and select **Baked UV Charts**.

As you can see, the baked UVs are very different to the precomputed real-time UVs. This is because the requirements for baked and precomputed real-time UVs are different.