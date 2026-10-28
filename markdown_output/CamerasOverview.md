---
title: "Cameras"
category: "General"
source_file: "CamerasOverview.html"
doc_type: "manual"
---

# Cameras

A Unity **scene** represents **GameObjects** represents **GameObjects** in a three-dimensional space. Since the viewer’s screen is two-dimensional, Unity needs to capture a view and “flatten” it for display. It does this using cameras. In Unity, you create a **camera** by adding a Camera component to a GameObject.

## Defining what a camera sees

What a camera sees is defined by its transform and its Camera component. The transform position defines the viewpoint, its forward (Z) axis defines the view direction, and its and upward (Y) axis defines the top of the screen. Settings on the Camera component define the size and shape of the region that falls within the view. With these parameters set up, the camera can display what it currently “sees” to the screen. As the GameObject moves and rotates, the displayed view moves and rotates accordingly.

## Perspective and orthographic cameras

The same scene shown in perspective mode (left) and orthographic mode (right) 

A camera in the real world, or indeed a human eye, sees the world in a way that makes objects look smaller the farther they are from the point of view. This well-known _perspective_ effect is widely used in art and computer graphics and is important for creating a realistic scene. Naturally, Unity supports perspective cameras, but for some purposes, you want to render the view without this effect. For example, you might want to create a map or information display that is not supposed to appear exactly like a real-world object. A camera that does not diminish the size of objects with distance is referred to as _orthographic_ and Unity cameras also have an option for this. The perspective and orthographic modes of viewing a scene are known as camera _projections_. _(scene above fromBITGEM)_

## The shape of the viewed region

Both perspective and orthographic cameras have a limit on how far they can “see” from their current position. The limit is defined by a plane that is perpendicular to the camera’s forward (Z) direction. This is known as the _far clipping plane_ since objects at a greater distance from the camera are “clipped” (ie, excluded from rendering). There is also a corresponding _near clipping plane_ close to the camera - the viewable range of distance is that between the two planes.

Without perspective, objects appear the same size regardless of their distance. This means that the viewing volume of an orthographic camera is defined by a rectangular box extending between the two **clipping planes**.

When perspective is used, objects appear to diminish in size as the distance from camera increases. This means that the width and height of the viewable part of the scene grows with increasing distance. The viewing volume of a perspective camera, then, is not a box but a pyramidal shape with the apex at the camera’s position and the base at the **far clipping plane**. The shape is not exactly a pyramid, however, because the top is cut off by the **near clipping plane** ; this kind of truncated pyramid shape is known as a _frustum_. Since its height is not constant, the frustum is defined by the ratio of its width to its height (known as the _aspect ratio_) and the angle between the top and bottom at the apex (known as the _field of view_ or _FOV_). See the page about understanding the view frustum for a more detailed explanation.

## The background to the camera view

You can set what a camera does with the background you see in the empty areas between objects, before it renders the scene.

For example, you can choose to fill the background with a flat color before rendering the scene on top of it, or draw the sky or a distant background, or even leave the contents of the previous frame there. For information on configuring this setting, see the _Background_ property in the Camera Inspector reference. For information on drawing sky, see Sky.