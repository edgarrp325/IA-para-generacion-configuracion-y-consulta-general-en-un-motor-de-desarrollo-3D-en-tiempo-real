---
title: "Texture Import Settings"
category: "General"
source_file: "class-TextureImporter.html"
doc_type: "manual"
---

# Texture Import Settings

Switch to Scripting

The **Texture Import Settings** window defines how Unity imports images from your project’s `Assets` folder into the Unity Editor.

To access this window, select the image file in the **Project window**. The **Texture Import Settings** window appears in the **Inspector**. The **Texture Import Settings** window appears in the **Inspector**.

**Note:** Some of the less commonly used properties are hidden by default. Expand the Advanced section in the Inspector window to view these properties.

The Texture Import Settings window

There are several sections on the Texture Import Settings window:

  * **(A)** Texture Type. Select the type of Texture you want to create.
  * **(B)** Texture Shape. Select the shape and set properties specific to that shape in this area.
  * **(C)** Type-specific and advanced properties. Depending on what **Texture Type** value you select, extra properties might appear in this area.
  * **(D)** Platform-specific overrides panel. Use the **Platform-specific overrides** panel to set default options and their overrides for a specific platforms.
  * **(E)** **Texture preview**. You can preview the Texture and adjust its values here.

## Texture Type

Use the **Texture Type** property to select the type of Texture you want to create from the source image file. The other properties in the Texture Import settings window change depending on the value you set.

**Property** | **Function**  
---|---  
**Default** | This is the most common setting used for all Textures. It provides access to most of the properties for Texture importing. For more information, see the Default Texture type.  
**Normal map** | The **Normal map** texture type formats the texture asset so it’s suitable for real-time normal mapping. For more information, see the Normal map texture type documentation.   
  
For more information on normal mapping in general, see Importing Textures.  
**Editor GUI and Legacy GUI** | The **Editor GUI and Legacy GUI** texture type formats the texture asset so it’s suitable for HUD and GUI controls. For more information, see the Editor GUI and Legacy GUI texture type documentation.  
**Sprite (2D and UI)** | The **Sprite (2D and UI)** texture type formats the texture asset so it’s suitable to use in 2D applications as a Sprite. For more information, see the Sprite (2D and UI) texture type documentation.  
**Cursor** | The **Cursor** texture type formats the texture asset so it’s suitable to use as a custom mouse cursor. For more information, see the Cursor texture type documentation.  
**Cookie** | The **Cookie** texture type formats the texture asset so it’s suitable to use as a light cookie in the Built-in **Render Pipeline**  
**Lightmap** | The **Lightmap** texture type formats the texture asset so it’s suitable to use as a Lightmap. This option enables encoding into a specific format (RGBM or dLDR depending on the platform) and a **post-processing**  
**Directional Lightmap** | The **Directional Lightmap** texture type formats the texture asset so it’s suitable to use as a directional Lightmap. For more information, see the Directional Lightmap texture type documentation.  
**Shadowmask** | The **Shadowmask** texture type formats the texture asset so it’s suitable to use as a shadowmask. For more information, see the Shadowmask texture type documentation.  
**Single Channel** | The **Single Channel** texture type formats the texture asset so it only has one channel. For information on the properties available only for the this type, see the Single Channel texture type documentation.  
  
## Texture Shape

Use the **Texture Shape** property to select and define the shape and structure of the Texture. There are four shape types:

  * **2D** is the most common setting for all Textures; it defines the image file as a 2D Texture. These are used to map Textures to 3D Meshes and GUI elements, among other Project elements.
  * **Cube** defines the Texture as a cubemap. You could use this for Skyboxes or **Reflection Probes**
  * **2D Array** defines the Texture as a 2D array texture. This is commonly used as an optimization for some rendering techniques, where many textures of the same size & format are used.
  * **3D** defines the Texture as a 3D texture. 3D textures are used by some rendering techniques to represent volumetric data.

### Cubemap mapping

You can further refine **Cubemap** shape textures with the following properties:

**Property:** | **Function:**  
---|---  
**Mapping** | Use **Mapping** to specify how the Texture is projected onto your **GameObject**. This is set to **Auto** by default.  
| **Auto** | Unity tries to create the layout from the Texture information.  
| **6 Frames Layout (Cubic Environment)** | The Texture contains six images arranged in one of the standard cubemap layouts: cross, or sequence (+x -x +y -y +z -z). The images can be orientated either horizontally or vertically.  
| **Latitude Longitude (Cylindrical)** | Maps the Texture to a 2D Latitude-Longitude representation.  
| **Mirrored Ball (Sphere Mapped)** | Maps the Texture to a sphere-like cubemap.  
**Convolution Type** | Choose the type of pre-convolution (filtering) that you want to use for this Texture. The result of pre-convolution is stored in mipmaps.   
This property is only available for the Default Texture type.  
| **None** | The Texture has no pre-convolution (no filtering). This is the default.  
| **Specular (Glossy Reflection)** | Select this to use cubemaps as Reflection Probes. The Texture mipmaps are pre-convoluted (filtered) with the engine BRDF. For more information, see Wikipedia’s page on Bidirectional reflectance distribution function.  
| **Diffuse (Irradiance)** | The Texture is convoluted (filtered) to represent irradiance. This is useful if you use the cubemap as a **Light Probe**.  
**Fixup Edge Seams** | This option is only available with the **None** or **Diffuse** convolution (filter). Use this on low-end platforms as a work-around for filtering limitations, such as cubemaps incorrectly filtered between faces.  
  
### 2D Array and 3D columns and rows

The source texture files for **2D Array** and **3D** Textures are divided into cells; these textures are called flipbook textures. When Unity imports flipbook textures, it places the contents of each cell into its own 2D array layer or 3D texture slice.

When you set the **Texture Shape** property to **2D Array** or **3D** , Unity displays the **Columns** and **Rows** properties. Use these to tell Unity how to divide the flipbook texture into cells.

**Property:** | **Function:**  
---|---  
**Columns** | The number of columns that the source flipbook texture is divided into.  
**Rows** | The number of rows that the source flipbook texture is divided into.  
  
For example, an image with 8x8 cells of smoke effect frames looks like this as a default 2D texture:

Flipbook image as a 2D shape

But when you correctly import is as a 3D texture with 8 Columns and 8 Rows, it looks like this:

Flipbook image as a 3D shape

## Type-specific and advanced properties

Depending on which **Texture Type** you select, different properties can appear in the Texture Import Settings window. Some of these properties are specific to the Texture Type itself, such as **Sprite Mode** available with the Sprite (2D and UI) type.

Use Advanced settings to make finer adjustments to the way Unity handles the Texture. The order and availability of these settings can vary depending on the **Texture Type** you choose.

For information on the properties for each texture type, refer to the documentation for that texture type:

  * Default
  * Normal map
  * Editor GUI and Legacy GUI
  * Sprite (2D and UI)
  * Cursor
  * Cookie
  * Lightmap
  * Directional Lightmap
  * Shadowmask
  * Single Channel

## Platform-specific overrides panel

To set the size and format of the imported texture, use the platform-specific overrides panel.

### Default tab

The **Default** tab lets you set the final size and format of the imported texture on all platforms.

**Property:** | **Function:**  
---|---  
**Max Size** | Sets the maximum dimensions of the imported texture in **pixels**.  
**Resize Algorithm** | Sets the algorithm Unity uses to downscale the texture, if the texture file has larger dimensions than **Max Size**.  
| **Mitchell** | Resizes the texture using the Mitchell algorithm. This is the default.  
| **Bilinear** | Resizes the texture using bilinear interpolation. This setting might preserve more small, sharp details than **Mitchell**.  
**Format** | Sets the number of channels and the data type of the final texture, except for platforms you override in the platform-specific override tabs. The default is **Automatic** , where Unity selects a value based on the number of channels in the texture, and the **Compression** setting. For more information, refer to the Default formats section.  
**Compression** | Sets the compression of the final texture. Unity uses this setting to select an appropriate **texture format**. This setting is only available if you set **Format** to **Automatic**. For more information, refer to the Default formats section.  
| **None** | Don’t compress the texture.  
| **Low Quality** | Compresses the texture using a low-quality texture format. The compressed texture might use less memory than **Normal Quality**.  
| **Normal Quality** | Compresses the texture using a standard texture format.  
| **High Quality** | Compresses the texture using a high-quality texture format. The compressed texture might use more memory than **Normal Quality**.  
**Use Crunch Compression** | Compresses the texture using the Crunch compression library, which helps Unity use the lowest possible amount of space. This setting is only available if you set **Format** to **Automatic**. Unity decompresses the texture to DXT or ETC format on the CPU, then uploads them to the GPU at runtime. If you enable this setting, textures might take a long time to compress, but decompression at runtime is fast.  
**Compressor Quality** | Sets the image quality of the compressed texture, if you enable **Use Crunch Compression**. A higher value might use more memory and increase compression time.  
  
### Platform-specific overrides tabs

The platform-specific override tabs let you override the settings in the **Default** tab for specific platforms. For more information about build platforms, refer to Build Profiles window reference.

**Property:** | **Function:**  
---|---  
**Max Size** | Sets the maximum dimensions of the imported texture in pixels.  
**Resize Algorithm** | Sets the algorithm Unity uses to downscale the texture, if the texture file has larger dimensions than **Max Size**.  
| **Mitchell** | Resizes the texture using the Mitchell algorithm. This is the default.  
| **Bilinear** | Resizes the texture using bilinear interpolation. This setting might preserve more small, sharp details than **Mitchell**.  
**Format** | Sets the final texture format. The available texture formats depend on the platform, and the file type of the texture. The default is selected by Unity based on the platform and the settings in the **Default** tab. For more information, refer to the Default formats section.  
**Compressor quality** | Sets the quality of the final texture that compression produces. This setting isn’t available for all texture formats.  
| **Fast** | Compresses the texture to create a low-quality image that might use less memory than **Normal**.  
| **Normal** | Compresses the texture using the standard compression.  
| **Best** | Compresses the texture and retains a high-quality image that might use more memory than **Normal**.  
| Slider | Sets the quality of the compressed texture. This slider is only available if you select a texture that uses Crunch compression. A higher value might use more memory and increase compression time.  
**Split Alpha Channel** | Allows alpha splitting for this Texture on these platforms: **tvOS** , **iOS** , and **Android**. For more information, refer to Notes on Android for Texture compression formats.  
**Override ETC2 fallback** | ETC2 texture decompression fallback override on Android devices that don’t support ETC2.  
  
Allows to choose which texture format to decompress the texture to on Android devices that have no ETC2 texture format support. For more information, refer to Notes on Android for Texture compression formats.  
  
## Default formats

The following table lists the default **Format** Unity selects in the platform-specific override tab, based on the **Format** and **Compression** settings in the **Default** tab.

**Platform** | **Texture channels** | **Format for no compression** | **Format for Normal Quality compression** | **Format for High Quality compression** | **Format for Low Quality compression**  
---|---|---|---|---|---  
**Windows, Linux, macOS** | RGB | RGB 24 bit | RGB Compressed DXT1 | RGB(A) Compressed BC7 | RGB Compressed DXT1  
| RGBA | RGBA 32 bit | RGBA Compressed DXT5 | RGB(A) Compressed BC7 | RGBA Compressed DXT5  
| **HDR** | RGBA Half | RGB Compressed BC6H | RGB Compressed BC6H | RGB Compressed BC6H  
****WebGL** – desktop** (configurable) | RGB | RGB 24 bit | RGB Compressed DXT1 | RGB Compressed DXT1 | RGB Compressed DXT1  
| RGBA | RGBA 32 bit | RGBA Compressed DXT5 | RGBA Compressed DXT5 | RGBA Compressed DXT5  
**WebGL – mobile** (configurable) | RGB | RGB 24 bit | RGBA Compressed ASTC 6x6 block  
RGB Compressed ETC2  
RGB Compressed ETC | RGBA Compressed ASTC 4x4 block  
RGB Compressed ETC2  
RGB Compressed ETC | RGBA Compressed ASTC 8x8 block  
RGB Compressed ETC2  
RGB Compressed ETC  
| RGBA | RGBA 32 bit | RGBA Compressed ASTC 6x6 block  
RGBA Compressed ETC2 | RGBA Compressed ASTC 4x4 block  
RGBA Compressed ETC2 | RGBA Compressed ASTC 8x8 block  
RGBA Compressed ETC2  
**Android** (configurable) | RGB | RGB 24 bit | RGBA Compressed ASTC 6x6 block  
RGB Compressed ETC2  
RGB Compressed ETC | RGBA Compressed ASTC 4x4 block  
RGB Compressed ETC2  
RGB Compressed ETC | RGBA Compressed ASTC 8x8 block  
RGB Compressed ETC2  
RGB Compressed ETC  
| RGBA | RGBA 32 bit | RGBA Compressed ASTC 6x6 block  
RGBA Compressed ETC2 | RGBA Compressed ASTC 4x4 block  
RGBA Compressed ETC2 | RGBA Compressed ASTC 8x8 block  
RGBA Compressed ETC2  
**iOS** (configurable) | RGB | RGB 24 bit | RGBA Compressed ASTC 6x6 block  
RGB Compressed PVRTC 4 bits | RGBA Compressed ASTC 4x4 block  
RGB Compressed PVRTC 4 bits | RGBA Compressed ASTC 8x8 block  
RGB Compressed PVRTC 2 bits  
| RGBA | RGBA 32 bit | RGBA Compressed ASTC 6x6 block  
RGBA Compressed PVRTC 4 bits | RGBA Compressed ASTC 4x4 block  
RGBA Compressed PVRTC 4 bits | RGBA Compressed ASTC 8x8 block  
RGBA Compressed PVRTC 2 bits  
**tvOS** | RGB | RGB 24 bit | RGBA Compressed ASTC 6x6 block | RGBA Compressed ASTC 4x4 block | RGBA Compressed ASTC 8x8 block  
| RGBA | RGBA 32 bit | RGBA Compressed ASTC 6x6 block | RGBA Compressed ASTC 4x4 block | RGBA Compressed ASTC 8x8 block  
**Default** | RGBA | RGBA 32 bit | RGBA 16 bit | RGBA 16 bit | RGBA 16 bit