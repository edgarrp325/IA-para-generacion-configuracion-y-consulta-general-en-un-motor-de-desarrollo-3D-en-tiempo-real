---
title: "Recommended and supported texture formats, by platform"
category: "General"
source_file: "class-TextureImporterOverride.html"
doc_type: "manual"
---

# Recommended and supported texture formats, by platform

This page contains the following information:

  * Terminology
  * Recommended texture formats, by platform
  * Desktop
  * iOS and tvOS
  * Android
  * Texture compression formats, by quality 
  * Supported texture formats, by platform

This page doesn’t contain information about console platforms. For information about console platforms, see the platform-specific documentation.

For an overview of texture formats, see Texture formats. For information about texture import settings and how to set per-texture platform-specific overrides, see Texture import settings. Some texture import settings can also be overridden globally in Build Settings, mostly to speed up iteration time during development.

## Terminology

This page uses the following terminology:

  * **Bits per**pixel** (bpp)** is the amount of storage required for a single texture pixel. Textures with a lower bpp value have a smaller size on disk and in memory. A lower bpp value also means that the GPU can store more pixels in its cache, which results in faster texture access.
  * LDR (Low Dynamic Range) refers to most typical images where colors are conceptually between 0.0 (black) and 1.0 (white) values. The majority of image files (such as PNG and JPG) have low dynamic range.
  * **HDR** (High Dynamic Range) refers to special image and texture formats where colors can have a higher range than 0 through 1. Image file formats like .exr or .hdr are often used for HDR image data. At runtime and on the GPU, there are several HDR formats, trading off accuracy, range and memory usage.
  * **RGB** is a color model in which red, green and blue combine to reproduce an array of colors.
  * **RGBA** is a version of **RGB** with an alpha channel, which supports blending and opacity alteration.
  * **Variable bit rate (VBR)** means that bits per pixel is not a fixed value, and depends on the actual content instead. VBR only applies to **Crunch**compression**** , and only texture size on disk. The size in memory is the same as when using the underlying texture format (for example, RGB Compressed DXT1 for RGB Crunched DXT1).

## Recommended texture formats, by platform

### Desktop

For devices with DirectX 11 or better class GPUs, where support for BC7 and BC6H formats is guaranteed to be available, the recommended choice of compression formats is: RGB textures - DXT1 at four bits/pixel. RGBA textures - BC7 (higher quality, slower to compress) or DXT5 (faster to compress), both at eight bits/pixel. HDR textures - BC6H at eight bits/pixel. If you need to support DirectX 10 class GPUs on PC (NVIDIA GPUs before 2010, AMD before 2009, Intel before 2012), then DXT5 instead of BC7 would be preferred, since these GPUs do not support BC7 nor BC6H.

See the Supported texture formats reference table for detailed information about all supported formats.

### iOS and tvOS

For Apple devices that use the A8 chip (2014) or above, ASTC is the recommended texture format for RGB and RGBA textures. This format allows you to choose between texture quality and size on a granular level: all the way from eight bits/pixel (4x4 block size) down to 0.89 bits/pixel (12x12 block size). If support for older devices is needed, or you want additional Crunch compression, then Apple devices support ETC/ETC2 formats starting with A7 chip (2013). For even older devices, PVRTC is the format to use. On iOS you can configure the default texture format in the Player Settings. PVRTC gives you the broadest possible compatibility. ASTC is preferred, but is not supported on A7 devices (the very first Metal-enabled devices) and will be unpacked at runtime.

See the Supported texture formats reference table for detailed information about all supported formats.

### Android

Texture format support on Android is complicated. You might need to build several application versions with different sub-targets.

You can select the default format in Player Settings. Your options are ASTC, ETC2 and ETC (ETC1 for RGB, ETC2 for RGBA). See Texture compression settings for more details on how the different settings interact.

For LDR RGB and RGBA textures, most modern Android GPUs that support OpenGL ES 3.1 or Vulkan also support ASTC format, including: Qualcomm GPUs since Adreno 4xx / Snapdragon 415 (2015), ARM GPUs since Mali T624 (2012), NVIDIA GPUs since Tegra K1 (2014), PowerVR GPUs since GX6250 (2014).

If you need support for older devices, or you want additional Crunch compression, then all GPUs that run Vulkan or OpenGL ES 3.0 support the ETC2 format. The resulting image quality is quite high, and it supports one- to four-component texture data. OpenGL ES 2 devices do not support the ETC2 format, so Unity decompresses the texture at runtime to the format ETC2 fallback specifies. For even older devices, usually only ETC format is available. The drawback is that there is no direct alpha channel support. For **Sprites** , Unity offers an option to use ETC1 compression by splitting a texture into two ETC1 textures: one for RGB, one for alpha. To enable this, enable the Android-specific Split Alpha Channel option for the Texture when importing a Sprite Atlas, Unity offers an option to use ETC1 compression by splitting a texture into two ETC1 textures: one for RGB, one for alpha. To enable this, enable the Android-specific Split Alpha Channel option for the Texture when importing a Sprite Atlas. The sprite **shader**. The sprite **shader** samples both textures and combines them into the final result.

For older Android devices that don’t support the ASTC format, the texture is decompressed into an uncompressed RGBA 32-bit format. This increases memory usage and can slow down the decompression performed on the CPU.

For HDR textures, ASTC HDR is the only compressed format available on Android devices. ASTC HDR requires Vulkan or GL_KHR_texture_compression_astc_hdr support. ASTC is the most flexible format. If a device doesn’t support ASTC HDR the texture is decompressed at runtime to RGB9e5 or RGBA Half, depending on alpha channel usage.

For devices that don’t support ASTC HDR, all devices running Vulkan, Metal, or OpenGL ES 3.0 support RGB9e5, which is suitable for textures without an alpha channel. If an alpha channel or even wider support is needed, use RGBA Half. This takes twice as much memory as RGB9e5.

See the Supported texture formats reference table for detailed information about all supported formats.

## Texture formats, by quality

The table below shows each format available in Unity, and their quality details. 

**Texture format** | **Description** | **Channels** | **Quality** | **Bits per pixel** | **Size of 1024x1024 texture, in MB**  
---|---|---|---|---|---  
**Alpha 8** | Uncompressed single channel (A) | A | High | 8 | 1  
**R 8** | Uncompressed single channel (R) | R | High | 8 | 1  
**R 16 bit** | Uncompressed single channel (R), very high precision | R | Very high | 16 | 2  
**R Float** | HDR, uncompressed single channel (R), very high precision | R | Very high | 32 | 4  
**R Compressed BC4** | Compressed single channel (R) | R | High | 4 | 0.5  
**R Compressed EAC 4 bit** | Compressed single channel (R) | R | High | 4 | 0.5  
**RG 32 bit** | Uncompressed two channel (RG), very high precision | RG | Very high | 32 | 4  
**RG Float** | HDR, uncompressed two channel (RG), very high precision | RG | Very high | 64 | 8  
**RG Compressed BC5** | Compressed two channel (RG) | RG | High | 8 | 1  
**RG Compressed EAC 8 bit** | Compressed two channel (RG) | RG | High | 8 | 1  
**RGB + 1-bit Alpha Compressed ETC2 4 bits** | Compressed RGBA, with alpha values fully opaque or fully transparent | RGBA | Medium | 4 | 0.5  
**RGB 16 bit** | Also known as RGB 565. Quantized RGB | RGB | Medium | 16 | 2  
**RGB 24 bit** | Uncompressed RGB. Converted to RGBA 32 bit for the GPU | RGB | High | 24 disk, 32 GPU | 3 disk, 4 GPU  
**RGB 48 bit** | Uncompressed RGB, very high precision. Converted to RGBA 64 bit for the GPU | RGB | Very high | 48 disk, 64 GPU | 6 disk, 8 GPU  
**RGB Compressed BC6H** | HDR, compressed RGB, 0 to +64k range | RGB | High | 8 | 1  
**RGB Compressed DXT1** | Also known as BC1. Compressed RGB | RGB | Medium | 4 | 0.5  
**RGB Compressed ETC** | Compressed RGB | RGB | Low | 4 | 0.5  
**RGB Compressed ETC2** | Compressed RGB | RGB | Medium | 4 | 0.5  
**RGB Compressed PVRTC 2 bits** | Compressed RGB, texture required to be square | RGB | Low | 2 | 0.25  
**RGB Compressed PVRTC 4 bits** | Compressed RGB, texture required to be square | RGB | Medium | 4 | 0.5  
**RGB Crunched DXT1** | Also known as BC1. Compressed RGB, with additional on-disk Crunch compression | RGB | Low to medium | Variable | Variable  
**RGB Crunched ETC** | Compressed RGB, with additional on-disk Crunch compression | RGB | Low | Variable | Variable  
**RGB(A) Compressed ASTC HDR** | HDR, compressed RGB or RGBA, size & quality dependent on block size | RGB or RGBA | Low to High | 12x12: 0.89, 10x10: 1.28, 8x8: 2, 6x6: 3.56, 5x5: 5.12, 4x4: 8 | 12x12: 0.11, 10x10: 0.16, 8x8: 0.25, 6x6: 0.45, 5x5: 0.64, 4x4: 1.0  
**RGB(A) Compressed ASTC** | Compressed RGB or RGBA, size & quality dependent on block size | RGB or RGBA | Low to high | 12x12: 0.89, 10x10: 1.28, 8x8: 2, 6x6: 3.56, 5x5: 5.12, 4x4: 8 | 12x12: 0.11, 10x10: 0.16, 8x8: 0.25, 6x6: 0.45, 5x5: 0.64, 4x4: 1.0  
**RGB(A) Compressed BC7** | Compressed RGB or RGBA | RGB or RGBA | High | 8 | 1  
**RGB9e5 32 Bit Shared Exponent Float** | HDR, quantized RGB, 0 to +64k range | RGB | Medium | 32 | 4  
**RGBA 16 bit (4444)** | Quantized RGBA | RGBA | Medium | 16 | 2  
**RGBA 32 bit** | Uncompressed RGBA | RGBA | High | 32 | 4  
**RGBA 64 bit** | Uncompressed RGBA, very high precision | RGBA | Very high | 64 | 8  
**RGBA Float** | HDR, uncompressed RGBA, very high precision | RGBA | Very high | 128 | 16  
**RGBA Compressed ETC2** | Compressed RGBA | RGBA | Medium | 8 | 1  
**RGBA Compressed PVRTC 2 bits** | Compressed RGBA, texture required to be square | RGBA | Low | 2 | 0.25  
**RGBA Compressed PVRTC 4 bits** | Compressed RGBA, texture required to be square | RGBA | Medium | 4 | 0.5  
**RGBA Crunched DXT5** | Also known as BC3. Compressed RGBA. With additional on-disk Crunch compression | RGBA | Low to medium | Variable | Variable  
**RGBA Crunched ETC2** | Compressed RGBA, with additional on-disk Crunch compression | RGBA | Low to medium | Variable | Variable  
**RGBA Half** | HDR, half-precision (FP16) RGBA, –64k to +64k range | RGBA | High | 64 | 8  
  
## Supported texture formats, by platform

The table below shows each texture format available in Unity, and the platforms that support them. 

**Texture format** | **Windows** | **macOS** | **Linux** | **Android** | **iOS & tvOS** | ****WebGL** (Desktop Browsers)** | **WebGL (iOS and Android browser)**  
---|---|---|---|---|---|---|---  
**Alpha 8** | yes | yes | yes | yes | yes | yes | yes  
**R 8** | yes | yes | yes | partial (5) | yes | partial (5) | partial (5)  
**R 16 bit** | yes | yes | yes | partial (6) | partial (6) | **yes (14)** | yes (14)  
**R Float** | yes | yes | yes | yes | yes | yes | yes  
**R Compressed BC4** | yes | yes | yes | no | no | **yes** | no  
**R Compressed EAC 4 bit** | no | no | no | partial (9) | yes | no | yes  
**RG 32 bit** | yes | yes | yes | partial (6) | yes | no | no  
**RG Float** | yes | yes | yes | yes | yes | yes | yes  
**RG Compressed BC5** | yes | yes | yes | no | no | **yes** | no  
**RG Compressed EAC 8 bit** | no | no | no | partial (9) | yes | no | yes  
**RGB + 1-bit Alpha Compressed ETC2 4 bits** | no | no | no | partial (9) | yes | no | yes  
**RGB 16 bit** , also known as RGB 565 | yes | yes | yes | yes | yes | yes | yes  
**RGB 24 bit** | yes | yes | yes | yes | yes | yes | yes  
**RGB 48 bit** | yes | yes | yes | partial (6) | yes | no | no  
**RGB Compressed BC6H** | yes (1) | yes (1) | yes | no | no | **yes (1)** | no  
**RGB Compressed DXT1** , also known as BC1 | yes | yes | yes | no (3) | no | partial (2) | no  
**RGB Compressed ETC** | no | no | no | yes | yes | no | yes  
**RGB Compressed ETC2** | no | no | no | partial (9) | yes | no | yes  
**RGB Compressed PVRTC 2 bits** | no | no | no | no (12) | yes | no | no  
**RGB Compressed PVRTC 4 bits** | no | no | no | no (12) | yes | no | no  
**RGB Crunched DXT1** , also known as BC1 | yes | yes | yes | no (3) | no | partial (2) | no  
**RGB Crunched ETC** | no | no | no | yes | yes | no | yes  
**RGB(A) Compressed ASTC HDR** | no | no | no | partial (11) | partial (11) | no | partial (11)  
**RGB(A) Compressed ASTC** | no | no | no | partial (8) | yes (10) | no | yes (13 & 10)  
**RGB(A) Compressed BC7** | yes (1) | yes (1) | yes | no | no | **yes (1)** | no  
**RGB9e5 32 Bit Shared Exponent Float** | yes | yes | yes | partial (4) | yes | partial (4) | partial (4)  
**RGBA 16 bit** | yes | yes | yes | yes | yes | yes | yes  
**RGBA 32 bit** | yes | yes | yes | yes | yes | yes | yes  
**RGBA 64 bit** | yes | yes | yes | partial (6) | yes | no | no  
**RGBA Float** | yes | yes | yes | yes | yes | yes | yes  
**RGBA Compressed DXT5** , also known as BC3 | yes | yes | yes | no (3) | no | partial (2) | no  
**RGBA Compressed ETC2** | no | no | no | partial (9) | yes | no | yes  
**RGBA Compressed PVRTC 2 bits** | no | no | no | no (12) | yes | no | no  
**RGBA Compressed PVRTC 4 bits** | no | no | no | no (12) | yes | no | no  
**RGBA Crunched DXT5** , also known as BC3 | yes | yes | yes | no (3) | no | partial (2) | no  
**RGBA Crunched ETC2** | no | no | no | partial (9) | yes | no | yes  
**RGBA Half** | yes | yes | yes | yes | yes | yes | yes  
  
**Notes:**

  1. Except on pre-DX11 level GPUs, or macOS when using WebGL or OpenGL. When not supported, BC6H textures get decompressed to RGBA Half, and BC7 get decompressed to RGBA32 at load time.
  2. With linear rendering on web browsers that don’t support sRGB DXT, textures are decompressed to RGBA32 at load time.
  3. Except on Android devices with NVIDIA Tegra GPUs; these do support DXT/BC formats.
  4. Except on OpenGL ES 2.0 / WebGL 1.
  5. When on OpenGL ES 2.0 / WebGL 1: requires GL_EXT_texture_rg extension support.
  6. Requires GL_EXT_texture_norm16 or corresponding Vulkan capability on Android.
  7. When on OpenGL ES 2.0 / WebGL 1: requires OES_texture_half_float extension support.
  8. Requires Vulkan or GL_KHR_texture_compression_astc_ldr OpenGL ES extension.
  9. Except on OpenGL ES 2.0; there ETC2 textures are decompressed into the format _ETC2 fallback_ specifies in the Android Build Settings or on the Android tab for the Platform-specific overrides.
  10. Except on Apple A7 chip devices (2013).
  11. Android: requires GL_KHR_texture_compression_astc_hdr extension. iOS: requires A13 or later chip (2019).WebGL: requires WEBGL_compressed_texture_astc extension and HDR profile. When not supported, the texture is decompressed to RGB9E5 format, losing the alpha channel.
  12. Except on Android devices with Imagination PowerVR GPUs; these do support PVRTC formats.
  13. Requires WEBGL_compressed_texture_astc extension.
  14. Requires EXT_texture_norm16 extension and WebGL 2.

## Supported texture formats in WebGL

The following table provides the supported texture formats for WebGL.

**Format** | **Description**  
---|---  
**ASTC** | Adaptive Scalable **Texture Compression** (ASTC) is an advanced lossy texture compression format. Widely used for mobile browsers / devices.  
**DXT** | Also known as S3 Texture Compression (S3TC), DXT is mainly used for desktop browsers and devices.  
**ETC2** | Ericsson Texture Compression (ETC) is an older lossy texture compression format, lower quality than ASTC, used for mobile browsers / devices.  
  
## Additional resources:

  * Default texture formats
  * Texture compression in WebGL
  * Texture Compression format in Android

TextureImporterOverride