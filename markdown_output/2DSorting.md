---
title: "2D Sorting"
category: "General"
source_file: "2DSorting.html"
doc_type: "manual"
---

# 2D Sorting

## Overview

Unity sorts Renderers according to a priority order that depends on their types and usages. You can specify the render order of Renderers through their Render Queue. In general, there are two main queues: the Opaque queue and the Transparent queue. 2D Renderers are mainly within the Transparent queue, and include the Sprite Renderer

## Transparent Queue Sorting Order by Priority

2D Renderers within the Transparent Queue generally follow the priority order below:

  1. Sorting Layer and Order in Layer
  2. Specify Render Queue
  3. Distance to Camera
     * Perspective
     * Orthographic
     * Custom Axis sort mode
     * Sprite Sort Point
  4. Sorting Group
  5. Material/Shader
  6. Tiebreaker

There are other factors which can cause the sorting order to differ from the regular priority order. These factors vary from project to project.

## Sorting Layer and Order in Layer

The Sorting Layer and **Order in Layer** (in the Renderer’s **Property** settings) are available to all 2D Renderers through the **Inspector**

## Specify Render Queue

You can specify the Render Queue type of the Renderer in its Material settings or in the **Shader** settings of its Material. This is useful for grouping and sorting Renderers which are using different Materials. Refer to documentation on ShaderLab: SubShader Tags for more details.

## Distance to Camera

The Camera component sorts Renderers based on its **Projection** setting. The two options are **Perspective** and **Orthographic**. 

### Perspective

In this mode, the sorting distance of a Renderer is the direct distance of the Renderer from the **Camera** ’s position.

### Orthographic

The sorting distance of a Renderer is the distance between the position of the Renderer and the Camera along the Camera’s view direction. For the default 2D setting, this is along the (0, 0, 1) axis.

When you set the Camera component to **Perspective** or **Orthographic,** Unity automatically sets the Camera’s TransparencySortMode to match the selected mode. You can set the Transparency Sort Mode manually in two ways: 

  * Open the ****Project Settings**** and go to Graphics, then under **Camera Settings** use Transparent Sort Mode
  * Set the Camera’s TransparencySortMode via the Scripting API.

The Camera **Transparency Sort Mode** settings are under the **Graphics** category in the **Project Settings** (main menu: **Edit** > **Project Settings** > **Graphics**). When this is set to **Default** , a Camera component’s Projection setting take priority. When this is set to an option other than **Default** , the Camera component’s Projection setting remains the same, but the Camera’s **Transparency Sort Mode** changes to that option. 

An additional option available through the Project settings and via the Scripting API is the Custom Axis sort mode.

### Custom Axis sort mode

Select this mode to sort Renderers based on their distance along the custom axis you set in the Project settings (main menu: **Edit** > **Project Settings** > **Graphics** > **Transparency Sort Axis**). This is commonly used in projects with Isometric Tilemaps to sort and render the Tile Sprites correctly on the Tilemap. Refer to Creating an Isometric Tilemap for further information.

**Note:** If your project is a 2D Universal **Render Pipeline** (URP) project, the **Transparency Sort Mode** isn’t available in the **Project Settings** , and is instead configured in the 2D Renderer asset properties. Refer to the Configure the 2D Renderer Asset documentation for more information.

### Sprite Sort Point

By default, a **Sprite** ’s **Sort Point** is set to its **Center** , and Unity measures the distance between the camera’s Transform position and the Center of the Sprite to determine their render order during sorting. An alternate option is to set a Sprite’s **Sort Point** to its **Pivot** position in World Space. Select the **Pivot** option in the Sprite’s Sprite Renderer property settings and edit the Sprite’s Pivot position in the Sprite Editor.

## Sorting Group

The Sorting Group is a component that groups Renderers which share a common root together for sorting purposes. All Renderers within the same Sorting Group share the same **Sorting Layer, Order in Layer,** and **Distance to Camera**. Refer to documentation on the Sorting Group component and its settings for more details.

## Material/Shader

Unity sorts Renderers with the same Material settings together for more efficient rendering performance, such as with dynamic batching

## Tiebreaker

When multiple Renderers have identical sorting priority, the tiebreaker is the order that Unity places the Renderers in the Render Queue. Because this is an internal process that you have no control over, you should use the sorting options (such as **Sorting Layers** and **Sorting Groups**) to make sure all Renderers have distinct sorting priorities.