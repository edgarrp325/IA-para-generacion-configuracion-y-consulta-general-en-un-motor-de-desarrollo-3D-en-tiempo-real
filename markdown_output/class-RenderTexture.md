---
title: "Render Texture"
category: "General"
source_file: "class-RenderTexture.html"
doc_type: "manual"
---

# Render Texture

Switch to Scripting

A **Render Texture** is a type of Texture that Unity creates and updates at run time. To use a Render Texture, create a new Render Texture using **Assets > Create > Render Texture** and assign it to **Target Texture** in your Camera that Unity creates and updates at run time. To use a Render Texture, create a new Render Texture using **Assets > Create > Render Texture** and assign it to **Target Texture** in your Camera component. Then you can use the Render Texture in a **Material** component. Then you can use the Render Texture in a **Material** just like a regular Texture.

## Properties

The **Render Texture** **inspector** is similar to the Texture Inspector.

The Render Texture Inspector is almost identical to the Texture Inspector

The Render Texture inspector displays the current contents of Render Texture in real-time and can be an invaluable debugging tool for effects that use render textures.

**_Property:_** | **_Function:_**  
---|---  
**Dimension** | The dimensionality (type) of the render texture.  
| **2D** | The render texture is two-dimensional.  
| **Cube** | The render texture is a cube map.  
| **3D** | The render texture is three-dimensional.  
**Size** | The size of the render texture in **pixels**. You can only enter power-of-two values, such as 128 and 256.  
**Anti-Aliasing** | The number of anti-aliasing samples. You can select **None** , **2 samples** , **4 samples** , or **8 samples**. If you select **None** , Unity does not apply anti-aliasing.  
**Enable Compatible Color Format** | Enable this checkbox to make Unity apply a compatible format to the render texture if the defined **Color Format** is not supported by the platform.  
**Color Format** | The color format of the render texture.  
**Depth Buffer** | The format of the depth buffer. You can select **No depth buffer** , **At least 16 bits depth (no stencil)** , or **At least 24 bits depth (with stencil)**. The **stencil buffer** is a general purpose buffer that allows you to store an additional unsigned 8-bit integer (0–255) for each pixel drawn to the screen.  
**Enable Mip Maps** | Check this box to make the render texture generate mipmaps.  
**Auto generate Mip Maps** | Check this box to automatically fill the generated mipmaps with relevant data. If you don’t enable this, you’ll have to use the `GenerateMips` function to fill those mipmaps manually. Alternatively, choose which mipmap level to render into when you call the various `SetRenderTarget` functions. For more information about the `SetRenderTarget` functions, see `Graphics.SetRenderTarget` and `Rendering.CommandBuffer.SetRenderTarget`.  
**Dynamic Scaling** | Check this box to let dynamic resolution scaling resize the render texture. If you don’t enable this, the render texture maintains the same size regardless of the **Dynamic Resolution**  
**Wrap Mode** | Controls how the texture is wrapped:  
| **Repeat** | Tiles the texture to create a repeating pattern.  
| **Clamp** | Stretches the edges of the texture. This is useful for preventing wrapping artifacts when you map an image onto an object and you don’t want the texture to tile.  
| **Mirror** | Tiles the texture to create a repeating pattern that mirrors the texture at every integer boundary.  
| **Mirror Once** | Mirrors the texture once, and then falls back to clamping.  
| **Per-axis** | Lets you set different wrap modes for the **U axis** and the **V axis**. The available options are also **Repeat** , **Clamp** , **Mirror** and **Mirror Once**. For example, when you use latitude-longitude environment maps for **reflection probes** , it is useful to have **Clamp** on the vertical coordinate (**V axis**), but **Repeat** on the horizontal coordinate (**U axis**).  
**Filter Mode** | Controls how the sampling of the texture uses nearby pixels. The options are:  
| **Point** | Uses the nearest pixel. This makes the texture appear pixelated.  
| **Bilinear** | Uses a weighted average of the four nearest texels. This makes the texture appear blurry when you magnify it.  
| **Trilinear** | Uses a weighted average of the two nearest mipmap levels, which are bilinearly filtered. This creates a soft transition between mipmap levels, at the cost of a slightly more blurry appearance.  
**Aniso Level** | Anisotropic filtering level of the texture. This increases texture quality when you view the texture at a steep angle. Good for floor, ground, or road textures.  
**Shadow Sampling Mode** | Select the sampling technique the GPU uses if the render texture is used as a shadow map. This property is only visible if **Depth Stencil Format** is not set to **None** , and only has an effect if you set **Color Format** to **None**.  
| **None** | The GPU doesn’t sample the shadow map.  
| **Compare Depths** | The GPU uses a hardware comparison filter to sample the shadow map.  
  
## Example

To create a live arena camera in your game:

  1. Create a new Render Texture asset using **Assets >Create >Render Texture**.
  2. Create a new Camera using **GameObject > Camera**.
  3. Assign the Render Texture to the **Target Texture** of the new Camera.
  4. Create a new 3D cube using **GameObject > 3D Object > Cube**.
  5. Drag the Render Texture onto the cube to create a Material that uses the render texture.
  6. Enter Play Mode, and observe that the cube’s texture is updated in real-time based on the new Camera’s output.

Render Textures are set up as demonstrated above

* * *

  * 2019–04–11 Page amended 

  * Render Texture inspector changed in Unity 2017.2

  * Ability to apply any GPU format to Render Textures added in Unity 2019.1

RenderTexture