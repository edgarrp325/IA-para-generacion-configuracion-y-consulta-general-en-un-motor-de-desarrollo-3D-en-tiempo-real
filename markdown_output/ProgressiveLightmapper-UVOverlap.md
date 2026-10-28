---
title: "Fixing lightmap UV overlap"
category: "General"
source_file: "ProgressiveLightmapper-UVOverlap.html"
doc_type: "manual"
---

# Fixing lightmap UV overlap

Each **lightmap** contains a number of **charts**. At run time, Unity maps these charts onto **mesh** contains a number of **charts**. At run time, Unity maps these charts onto **mesh** faces, and uses the charts’ lighting data to calculate the final appearance. Because of the way GPU sampling works, data from one chart can bleed onto another if they are too close to each other. This usually leads to unintended artifacts such as aliasing, pixelation, and so on.

Example of graphical artifacts due to chart bleeding

To avoid light bleeding, there must be a sufficient amount of space between charts. When a GPU samples a lightmap, the lighting system calculates the final sample value from the four texels closest to the sampled point (assuming bilinear filtering is used). These four texels are called the bilinear “neighborhood” of the sampled point. Charts are too close together if they overlap - that is, if the neighbourhood of any point inside a chart overlaps with the neighborhood of any point in another chart. In the image below, the white **pixels** indicate chart neighbourhoods, and red pixels indicate overlapping neighbourhoods.

Red pixels indicate overlapping chart neighbourhoods

Determining optimal chart placements and spacing can be difficult, because it depends on several parameters (such as lightmap resolution, mesh UVs, and Importer settings). For this reason, Unity provides the ability to identify these issues easily, as outlined in the following section.

## Identification

There are three ways to identify overlaps: 

  * Keep an eye on Unity’s console. If Unity detects overlapping UVs, it prints a warning message with a list of affected **GameObjects**. 

  * Use the **UV Overlap** draw mode in the **Scene** View (see GI visualizations in the Scene View for more information). When you have this mode enabled, Unity adds a red highlight to chart texels that are too close to texels of other charts. This is especially useful if you discover an artefact in the **Scene view** View (see GI visualizations in the Scene View for more information). When you have this mode enabled, Unity adds a red highlight to chart texels that are too close to texels of other charts. This is especially useful if you discover an artefact in the **Scene view** , and want to quickly examine whether UV overlap is causing it.

Scene View using UV Overlap draw mode (see dropdown in top left)

  * Use **Baked Lightmaps Preview**. Select a GameObject and go to the Lighting window and then choose the **Baked Lightmaps** tab. Double-click the highlighted lightmap, navigate to the Preview window, and select **Baked UV Overlap** (see dropdown in upper right corner). The Preview window colours problematic texels red in this view.

The Baked Lightmaps Preview in the Lighting window’s Baked Lightmaps tab

## Solutions

There is no one single solution for UV overlap, because there are so many things that can cause it. Here are the most common solutions to consider:

  * If you provide lightmap UVs yourself, add margins using your modelling package.
  * If Unity automatically generates the lightmap UVs for a Model, you can tell Unity to increase the pack margin. The simplest way to do this is to set the **Margin Method** to **Calculate** , and set an appropriate **Min Lightmap Resolution** and **Min Object Scale**. If you prefer to set **Margin Method** to **Manual** , you can adjust the **Pack Margin** value directly. For more information on these settings, see documentation on Generating lightmapping UVs.
  * Increase the resolution of the entire lightmap. This will increase the numbers of pixels between the charts, and therefore reduce the likelihood of bleeding. The downside is that your lightmap may become too large. You can do this in the **Lighting** tab under **Lightmapper Settings**.
  * Increase the resolution of a single GameObject. This allows you to increase lightmap resolution only for GameObjects that have overlapping UVs. Though less likely, this can also increase your lightmap size. You can change a GameObject’s lightmap resolution inside its **Mesh Renderer** under **Lightmap Settings**.

Same mesh as before, but without bleeding artifacts