---
title: "Framebuffer orientation"
category: "General"
source_file: "vulkan-swapchain-pre-rotation.html"
doc_type: "manual"
---

# Framebuffer orientation

If your application’s framebuffer orientation doesn’t match the device’s native display orientation (portrait, for most devices), Android rotates the application’s framebuffer to match the device’s display every frame. Depending on the device’s hardware capabilities, this additional rotation can negatively affect performance. If your application uses the Vulkan Graphics API and the device supports Vulkan, Unity can apply this rotation during rendering which reduces the performance impact of the rotation. This is called pre-rotation.

## Using pre-rotation in Unity

To make Unity apply pre-rotation, you can use C# **scripts** or the Unity editor:

  * Through C# scripts: Set PlayerSettings.vulkanEnablePreTransform to `true`.

  * Through the Unity Editor:

  *     1. Select **Edit** > **Project Settings**.
  * In the Project settings window, select the **Player** tab, then open Android Player Settings:  

  * In the **Other Setting** s section, enable **Apply display rotation during rendering**.

## How Unity applies pre-rotation

Unity applies pre-rotation when it renders directly to the device’s backbuffer, not when it renders to a Render Texture. To apply the rotation, Unity modifies the projection matrix which affects the `UNITY_MATRIX_MVP` and `UNITY_MATRIX_P` Built-in shader variables. This means that Unity applies the rotation in the vertex **shader**. To apply the rotation, Unity modifies the projection matrix which affects the `UNITY_MATRIX_MVP` and `UNITY_MATRIX_P` Built-in shader variables. This means that Unity applies the rotation in the vertex **shader**.

Using pre-rotation doesn’t affect the behavior of Unity’s C# API. For example, you can still use `Screen.width` to access the width of the screen. The same applies to **viewports** and scissor rects. Unity adjusts these as needed, and also handles readback operations from the backbuffer such as Grab Pass, ReadPixels, or Screenshot.

Unity provides utility macros to handle special cases in shaders (for more information, see the Limitations section below).

The macro UNITY_PRETRANSFORM_TO_DISPLAY_ORIENTATION is only defined if all of the following conditions are true (otherwise, it’s undefined):

  * `preTransform` is enabled in the Player Settings
  * the platform is set to Android
  * the graphics API is set to Vulkan

UNITY_DISPLAY_ORIENTATION_PRETRANSFORM is a constant that is set to the current `preTransform` rotation. Its value is one of the following:

  * `UNITY_DISPLAY_ORIENTATION_PRETRANSFORM_0`
  * `UNITY_DISPLAY_ORIENTATION_PRETRANSFORM_90`
  * `UNITY_DISPLAY_ORIENTATION_PRETRANSFORM_180`
  * `UNITY_DISPLAY_ORIENTATION_PRETRANSFORM_270`

If UNITY_PRETRANSFORM_TO_DISPLAY_ORIENTATION is undefined, or when rendering to a Render Texture, the value of UNITY_DISPLAY_ORIENTATION_PRETRANSFORM is UNITY_DISPLAY_ORIENTATION_0.

UNITY_DISPLAY_ORIENTATION_PRETRANSFORM is translated into a Vulkan specialization constant, which makes it efficient to use in if or switch statements.

## Limitations

In the following cases, it’s likely that enabling preTransform requires additional modifications to your Unity Project before you can use it:

  * Shaders that don’t use Unity’s projection matrix
  * Shaders that depend on the current **pixel** position in the fragment shader (`SV_Position`)
  * Shaders that use screen space derivatives (ddx, ddy)
  * Native rendering plugins that use the Vulkan swapchain image might need to be modified
  * Use of backbuffer with Unity RenderPass API in an MRT setup together with other Render Textures

These cases only apply when rendering directly to the backbuffer.

## Additional resources

  * Vulkan Design Guidelines on the Android developer website.
  * Vulkan Mobile Best Practice - Appropriate Use of Surface Rotation on the arm community website.