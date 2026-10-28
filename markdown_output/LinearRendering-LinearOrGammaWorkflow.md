---
title: "Linear or gamma workflow"
category: "General"
source_file: "LinearRendering-LinearOrGammaWorkflow.html"
doc_type: "manual"
---

# Linear or gamma workflow

The Unity Editor offers both linear and gamma workflows. The linear workflow has a color space crossover where Textures that were authored in gamma color space can be correctly and precisely rendered in linear color space. See documentation on Linear rendering overview for more information about gamma and linear color space.

For further reading, see documentation on:

  * Linear rendering overview for background information on linear and gamma color space.
  * Gamma Textures with linear rendering for information on gamma Textures in a linear workflow.
  * Linear Textures for information on working with linear Textures.

Textures tend to be saved in gamma color space, while Shaders expect linear color space. As such, when Textures are sampled in Shaders, the gamma-based values lead to inaccurate results. To overcome this, you can set Unity to use an sRGB sampler to cross over from gamma to linear sampling. This ensures a linear workflow with all inputs and outputs of a **Shader** in the correct color space, resulting in a correct outcome. 

To specify a gamma or linear workflow, go to **Edit** > **Project Settings** , then select the **Player** category, navigate to the **Other Settings** , open the **Rendering** section, and change the **Color Space** to **Linear** or **Gamma** , depending on your preference.

Player settings showing the Color Space setting

## Gamma color space workflow

While a linear workflow ensures more precise rendering, sometimes you may want a gamma workflow (for example, on some platforms the hardware only supports the gamma format).

To do this, set **Color Space** to **Gamma** in the **Player** settings (menu: **Edit** > **Project Settings** , then select the **Player** category). Unity uses the gamma color space for color calculations, and keeps imported textures in the gamma color space. Unity also makes sure shaders keep textures in gamma color space, calculate in gamma color space, and write to a framebuffer that doesn’t reapply gamma correction.

Texture Import Settings might show textures as being in linear format, because this avoids shaders recognising the textures as being in gamma color space and automatically removing the gamma correction.

Note that you can choose to bypass sRGB sampling in **Color Space: Gamma** mode by unchecking the **sRGB (Color Texture)** checkbox in the Inspector window for the Texture.

## Linear color space workflow

Working in linear color space gives more accurate rendering than working in gamma color space. 

To do this, set **Color Space** to **Linear** in the **Player** settings (menu: **Edit** > **Project Settings** , then select the **Player** category).

You can work in linear color space if your Textures were created in linear or gamma color space. Gamma color space Texture inputs to the linear color space Shader program are supplied to the Shader with gamma correction removed from them.

**Note** : The **Texture preview** window in Texture Import Settings displays Textures using gamma blending even if you are working in linear color space.

### Linear Textures

  * Selecting **Color Space:** **Linear** assumes your Textures are in gamma color space. Unity uses your GPU’s sRGB sampler by default to crossover from gamma to linear color space. If your Textures are authored in linear color space, you need to bypass the sRGB sampling. See documentation on Working with linear Textures for more information.

### Gamma Textures

  * Crossing over from gamma color space to linear color space requires some tweaking. See documentation on Gamma Textures with linear rendering for more information.

#### Notes

For colors, this conversion is applied implicitly, because the Unity Editor already converts the values to floating point before passing them to the GPU as constants. When sampling Textures, the GPU automatically removes the gamma correction, converting the result to linear space. 

These inputs are then passed to the Shader, with lighting calculations taking place in linear space as they normally do. When writing the resulting value to a framebuffer, it is either gamma-corrected straight away or left in linear space for later gamma correction - this depends on the current rendering configuration. For example, in high dynamic range (HDR), rendering results are left in linear space and gamma corrected later.

## Differences between linear and gamma color space

When using linear rendering, input values to the lighting equations are different to those in gamma space. This means differing results depending on the color space. For example, light striking surfaces has differing response curves, and Image Effects behave differently.

### Light fall-off

The fall-off from distance and normal-based lighting differs in two ways:

  * When rendering in linear mode, the additional gamma correction that is performed makes a light’s radius appear larger. 

  * Lighting edges also appear more clearly. This more correctly models lighting intensity fall-off on surfaces.

Left: Lighting a sphere in linear space. Right: Lighting a sphere in gamma space

### Linear intensity response

When you are using gamma rendering, the colors and Textures that are supplied to a Shader already have gamma correction applied to them. When they are used in a Shader, the colors of high luminance are actually brighter than they should be compared to linear lighting. This means that as light intensity increases, the surface gets brighter in a nonlinear way. This leads to lighting that can be too bright in many places. It can also give models and **scenes** a washed-out feel. When you are using linear rendering, the response from the surface remains linear as the light intensity increases. This leads to much more realistic surface shading and a much nicer color response from the surface.

The Infinite 3D Head Scan image below demonstrates different light intensities on a human head model under linear lighting and gamma lighting.

Infinite 3D Head Scan by Lee Perry-Smith, licensed under a Creative Commons Attribution 3.0 Unported License (available from www.ir-ltd.net)

### Linear and gamma blending

When blending into a framebuffer, the blending occurs in the color space of the framebuffer. 

When you use gamma space rendering, nonlinear colors get blended together. This is not the mathematically correct way to blend colors, and can give unexpected results, but it is the only way to do a blend on some graphics hardware. 

When you use linear space rendering, blending occurs in linear color space: This is mathematically correct and gives precise results.

The image below demonstrates the different types of blending:

Top: Blending in linear color space produces expected blending results  
Bottom: Blending in gamma color space results in over-saturated and overly-bright blends