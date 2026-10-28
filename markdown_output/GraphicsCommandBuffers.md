---
title: "Extending the Built-in Render Pipeline with CommandBuffers"
category: "General"
source_file: "GraphicsCommandBuffers.html"
doc_type: "manual"
---

# Extending the Built-in Render Pipeline with CommandBuffers

This page contains information on using CommandBuffers in the Built-in **Render Pipeline**. For information on using CommandBuffers in render pipelines based on the Scriptable Rendering Pipeline, see Scheduling and executing rendering commands in the Scriptable Rendering Pipeline.

## CommandBuffer fundamentals

A CommandBuffer holds a list of rendering commands (such as setting the render target, or drawing a given mesh). You can instruct Unity to schedule and execute those commands at various points in the Built-in Render Pipeline, which allows you to customize and extend Unity’s rendering functionality.

Blurry refraction, using Command Buffers.

You can execute CommandBuffers immediately using the Graphics.ExecuteCommandBuffer API, or you can schedule them so that they occur at a given point in the render pipeline. To schedule them, use the Camera.AddCommandBuffer API with the CameraEvent enum, and the Light.AddCommandBuffer API with the LightEvent enum. To see when Unity executes CommandBuffers that you schedule in this way, see CameraEvent and LightEvent order of execution.

For a full list of the commands that you can execute using CommandBuffers, see the CommandBuffer API documentation. Note that some commands are supported only on certain hardware; for example, the commands relating to **ray tracing** are supported only in DX12.

## Command Buffer examples

Decals, using Command Buffers.

The Unity blog post Extending Unity 5 rendering pipeline: Command Buffers introduces CommandBuffers in the Built-in Render Pipeline. It describes how to use CommandBuffers to achieve several different effects, and contains a sample project and example code. The project was created for an older version of Unity, but the principles are the same.

## CameraEvent and LightEvent event order of execution

### CameraEvent

The order of execution for CameraEvents depends on the rendering path that your Project uses.

**Deferred rendering path**

  * BeforeGBuffer
  * Unity renders opaque geometry
  * AfterGBuffer
  * Unity resolves depth.
  * BeforeReflections
  * Unity renders default reflections, and **Reflection Probe** reflections.
  * AfterReflections
  * Unity copies reflections to the Emissive channel of the G-buffer.
  * BeforeLighting
  * Unity renders shadows. See LightEvent order of execution.
  * AfterLighting
  * BeforeFinalPass
  * Unity processes the final pass.
  * AfterFinalPass
  * BeforeForwardOpaque (only called if there is opaque geometry that cannot be rendered using deferred)
  * Unity renders opaque geometry that cannot be rendered with deferred rendering.
  * AfterForwardOpaque (only called if there is opaque geometry that cannot be rendered using deferred)
  * BeforeSkybox
  * Unity renders the **skybox**.
  * AfterSkybox
  * Unity renders halos.
  * BeforeImageEffectsOpaque
  * Unity applies opaque-only **post-processing** effects.
  * AfterImageEffectsOpaque
  * BeforeForwardAlpha
  * Unity renders transparent geometry, and **UI** Canvases with a Rendering Mode of **Screen Space -**Camera** Canvases with a Rendering Mode of **Screen Space -**Camera****.**
  * AfterForwardAlpha
  * BeforeHaloAndLensFlares
  * Unity renders **lens flares**.
  * AfterHaloAndLensFlares
  * BeforeImageEffects
  * Unity applies post-processing effects.
  * AfterImageEffects
  * AfterEverything
  * Unity renders UI Canvases with a Rendering Mode that is not **Screen Space - Camera**.

**Forward rendering path**

  * BeforeDepthTexture
  * Unity renders depth for opaque geometry.
  * AfterDepthTexture
  * BeforeDepthNormalsTexture
  * Unity renders depth normals for opaque geometry.
  * AfterDepthNormalsTexture
  * Unity renders shadows. See LightEvent order of execution.
  * BeforeForwardOpaque
  * Unity renders opaque geometry.
  * AfterForwardOpaque
  * BeforeSkybox
  * Unity renders the skybox.
  * AfterSkybox
  * Unity renders halos.
  * BeforeImageEffectsOpaque
  * Unity applies opaque-only post-processing effects.
  * AfterImageEffectsOpaque
  * BeforeForwardAlpha
  * Unity renders transparent geometry, and UI Canvases with a Rendering Mode of **Screen Space - Camera**.
  * AfterForwardAlpha
  * BeforeHaloAndLensFlares
  * Unity renders lens flares.
  * AfterHaloAndLensFlares
  * BeforeImageEffects
  * Unity applies post-processing effects.
  * AfterImageEffects
  * AfterEverything
  * Unity renders UI Canvases with a Rendering Mode that is not **Screen Space - Camera**.

### LightEvent order of execution

During the “render shadows” stage above, for each shadow-casting Light, Unity performs these steps:

  * BeforeShadowMap
  * BeforeShadowMapPass
  * Unity renders all shadow casters for the current Pass
  * AfterShadowMapPass
  * Unity repeats the last three steps, for each Pass
  * AfterShadowMap
  * BeforeScreenSpaceMask
  * Unity gathers the shadow map into a screen space buffer and performs filtering
  * AfterScreenSpaceMask