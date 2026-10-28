---
title: "Lightmapping: Getting started"
category: "General"
source_file: "Lightmapping.html"
doc_type: "manual"
---

# Lightmapping: Getting started

## Preparing the Scene and baking the lightmaps

Select **Window** > **Rendering** > **Lighting** from the Unity Editor menu to open the Lighting window. Make sure any Mesh you want to apply a lightmap to has proper UVs for lightmapping. The easiest way to do this is to open the Mesh import settings and enable the **Generate Lightmap UVs** setting.

Next, to control the resolution of the **lightmaps** , go to the **Lightmapping Settings** section and adjust the **Lightmap Resolution** value. 

To be included in your lightmap, Renderers must meet the following criteria:

  * Have a **Mesh Renderer** or **Terrain** or **Terrain** component
  * Be marked as **Contribute GI**
  * Use a built-in Unity Material, the Standard **Shader** , or a Shader with a Meta Pass

You can adjust settings for Lights in the Light Explorer. To open the Light Explorer, go to **Window** > **Rendering** > **Light Explorer**.

To generate lightmaps for your Scene:

  1. Open the Lighting window (menu: **Window** > **Rendering** > **Lighting**)

  2. At the bottom of the **Scene** tab on the Lighting window, select **Generate Lighting** (or ensure that **Auto Generate** is enabled).

  3. A progress bar appears in Unity Editor’s status bar, in the bottom-right corner.

When lightmapping is complete, Unity’s Scene and Game views update automatically and you can view the resulting lightmaps by going to the **Baked Lightmaps** tab in the Lighting Window.

When you manually generate lighting, Unity adds Lighting Data Assets, baked lightmaps and Reflection Probes to the Assets folder.

* * *

Progressive Lightmapper added in 2018.1 NewIn20181