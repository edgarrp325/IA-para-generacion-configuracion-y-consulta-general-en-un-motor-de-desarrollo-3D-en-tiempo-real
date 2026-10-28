---
title: "Panel Settings properties reference"
category: "General"
source_file: "UIE-Runtime-Panel-Settings.html"
doc_type: "manual"
---

# Panel Settings properties reference

The following tables describe the Panel Settings asset properties:

**Property** | **Description**  
---|---  
**Theme Style Sheet** | Apply a default TSS file to every UIDocument that the panel renders.  
**Text Settings** | Set the Panel Text Settings asset for this panel. If this asset isn’t set, **UI**  
**Target Texture** | Set the render texture for the panel.  
  
For a 3D game, display UI on 3D geometry in the scene.  
**Target Display** | Set the display for the panel. Only set this if the target texture isn’t set, as the target texture takes precedence over the target display.  
**Sort Order** | Set the order that the UI System draws panels in if the **Scene** uses more than one panel. Panels with higher **Sort Order** values are drawn on top of panels with lower values.  
**Scale Mode** | Set how the panel’s UI scales when the screen size changes.  
**Scale Mode Parameters** | Display different properties depending on the **Scale Mode** setting.  
**Dynamic Atlas Settings** | Specify the settings that the dynamic atlas system uses. This property has the following options:  

  * **Min Atlas Size** : Set the minimum size (width/height) of the atlas texture, in pixels.
  * **Max Atlas Size** : Set the maximum size (width/height) of the atlas texture, in pixels.
  * **Max Sub Texture Size** : Set the maximum size (width/height) of a texture that can be added to the atlas.
  * **Active Filters** : Set the filters that the dynamic atlas system uses to exclude textures from the texture atlas.

  
**Clear Settings** | Set how the panel clears before rendering. Choose from the following options:  

  * **Clear Color** : Set whether the panel clears the color buffer before rendering.
  * **Clear Color Value** : Set the color that the panel uses to clear the color buffer.
  * **Clear Depth Stencil** : Set whether the panel clears the depth stencil before rendering.
  * **Buffer Management** : Set how the panel manages its buffers.
  * **Vertex budget** : Set the approximate number of vertices the panel uses. This helps initialize vertex buffers with the right size which can reduce draw calls. A value of `0` uses the default value for UI rendering.

  
  
## Scale Mode parameters

The following tables describe the parameters for each scale mode:

### Constant Pixel Size

Set elements to stay the same size, in **pixels** , regardless of screen size.

**Parameter** | **Description**  
---|---  
**Scale** | Multiply element sizes by this value. Must be greater than 0.  
  
### Constant Physical Size

Set elements stay the same physical size regardless of screen size and resolution.|

**Parameters** | **Description**  
---|---  
**Reference DPI** | Set the **Reference DPI** value to the screen density that your UI was designed for. When the system renders your UI, it tries to find the actual DPI value of the screen, and compares it to the **Reference DPI**. If they’re different, the system scales the UI accordingly.  
**Fallback DPI** | Use this value if the UI system can’t determine the screen DPI.  
  
### Scale with Screen Size

Set elements to grow or shrink depending on the screen size.

**Parameters** | **Description**  
---|---  
**Screen Match Mode** | Set how to scale elements when the screen resolution is different from the **Reference Resolution** :  
  

  * **Match Width or Height** : Scale the canvas area with the width or the height as reference, or a linear interpolation between the width and the height.
  * **Shrink** : Crop the canvas area either horizontally or vertically, so the size of the canvas is smaller than the reference. 
  * **Expand** : Expand the canvas area either horizontally or vertically, so the size of the canvas is larger than the reference.

  
**Reference Resolution** | Set the resolution that this panel’s UI is designed for. If the screen resolution is larger than the reference resolution, the UI scales up. If it’s smaller, the UI scales down. How the UI scales depends on the **Screen Match Mode**.  
**Screen Match Mode Parameters** | When **Screen Match Mode** is set to **Match Width or Height** , the **Match** value controls whether the UI system scales the UI to match the screen width, the screen height, or a mix of the two.   
  
For example, if the value is `0`, it matches the width; if the value is `1`, it matches the height; if the value is `0.4`, it linearly interpolates between width and height by `40%`.  
  
## Active Filters

You can apply more than one filter at a time. The following table describes each active filter. 

**Filter** | **Description**  
---|---  
**Nothing** | Disable all the filters.  
**Everything** | Apply all the filters.  
**Readability** | Exclude textures that `Texture2D.isReadable` is set to `true`.   
Unity can’t automatically update the dynamic atlas when you add a texture through APIs like `Texture2D.SetPixels`. You can use `RuntimePanelUtils.SetTextureDirty` to force the atlas to update its content for a given texture.  
**Size** | Exclude textures that are larger than the **Max Sub Texture Size** setting.   
Large textures can saturate the atlas quickly. If you don’t want to add large textures to the atlas, select this filter and adjust **Max Sub Texture Size** to fit your needs. By default, textures larger than `64x64` aren’t allowed into the atlas.  
**Format** | Store sRGB-encoded data with 8-bits per channel precision, and excludes sub-textures that would lose precision or be truncated when added to the atlas, such as an R16G16B16A16_FLOAT texture.  
**Color Space** | Exclude R8G8B8A8_UNORM content when the project is in a linear color space.   
In a linear color space, the format of the `RenderTexture` of the dynamic atlas is R8G8B8A8_SRGB. The data stored in the `RenderTexture` is sRGB-encoded. When read from, it’s linearized, and when written to, it’s encoded to sRGB. Because of the limited precision of the format, R8G8B8A8_UNORM content stored in the atlas could cause banding to occur.  
**Filter Mode** | Exclude textures for which the sub-texture filter mode, such as Point or Bilinear, doesn’t match the atlas filter mode. This prevents the mismatch between the sub-texture filter mode and the atlas filter mode. The mismatch could cause unexpected blurriness or blockiness.  
  
## Additional resources

  * Get started with runtime UI
  * Render UI in the Game view
  * Runtime event system
  * FAQ for input and event systems with UI Toolkit
  * Performance consideration for runtime UI
  * `PanelSettings`