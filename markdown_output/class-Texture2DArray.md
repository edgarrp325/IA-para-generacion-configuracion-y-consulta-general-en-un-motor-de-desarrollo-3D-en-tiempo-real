---
title: "Texture arrays"
category: "General"
source_file: "class-Texture2DArray.html"
doc_type: "manual"
---

# Texture arrays

Switch to Scripting

A texture array is a collection of same size/format/flags 2D textures that look like a single object to the GPU, and can be sampled in the **shader** with a texture element index. They are useful for implementing custom **terrain** with a texture element index. They are useful for implementing custom **terrain** rendering systems or other special effects where you need an efficient way of accessing many textures of the same size and format. Elements of a 2D texture array are also known as slices, or layers.

## Platform Support

Texture arrays need to be supported by the underlying graphics API and the GPU. They are available on:

  * Direct3D 11/12 (Windows)
  * OpenGL Core (Mac OS X, Linux)
  * Metal (iOS, Mac OS X)
  * OpenGL ES 3.0 (Android, WebGL 2.0)

Other platforms do not support texture arrays (OpenGL ES 2.0 or WebGL 1.0). Use SystemInfo.supports2DArrayTextures to determine texture array support at runtime.

## Importing texture arrays

You can import texture arrays from source texture files that are divided into cells. These are called flipbook textures. To do this:

  1. Import the source texture into your Unity Project.
  2. In your Project view, select the resulting Texture Asset. Unity displays the Texture import settings in the **Inspector**.
  3. In the Inspector, set **Texture Shape** to **2D Array**. Unity displays the Columns and Rows properties.
  4. Set **Columns** and **Rows** to the appropriate values for your flipbook texture.
  5. Click **Apply**.

For more information, see Texture import settings.

## Creating and manipulating texture arrays using scripts

To create a texture array from a C# script, use the Texture2DArray class to initialize the texture and set **pixel**

Normally, texture arrays are used purely within GPU memory, but you can use Graphics.CopyTexture, Texture2DArray.GetPixels and Texture2DArray.SetPixels to transfer pixels to and from system memory.

## Using texture arrays as render targets

Texture array elements may also be used as render targets. Use RenderTexture.dimension to specify in advance whether the render target is to be a 2D texture array. The **depthSlice** argument to Graphics.SetRenderTarget specifies which mipmap level or cube map face to render to. On platforms that support “layered rendering” (i.e. geometry shaders), you can set the **depthSlice** argument to –1 to set the whole texture array as a render target. You can also use a geometry shader to render into individual elements.

## Using texture arrays in shaders

Since texture arrays do not work on all platforms, shaders need to use an appropriate compilation target or feature requirement to access them. The minimum shader model compilation target that supports texture arrays is `3.5`, and the feature name is `2darray`.

Use these macros to declare and sample texture arrays:

  * UNITY_DECLARE_TEX2DARRAY(name) declares a texture array sampler variable inside HLSL code.
  * UNITY_SAMPLE_TEX2DARRAY(name,uv) samples a texture array with a **float3** UV; the z component of the coordinate is an array element index.
  * UNITY_SAMPLE_TEX2DARRAY_LOD(name,uv,lod) samples a texture array with an explicit mipmap level.

## Examples

The following shader example samples a texture array using object space vertex positions as coordinates:
    
    
    Shader "Example/Sample2DArrayTexture"
    {
        Properties
        {
            _MyArr ("Tex", 2DArray) = "" {}
            _SliceRange ("Slices", Range(0,16)) = 6
            _UVScale ("UVScale", Float) = 1.0
        }
        SubShader
        {
            Pass
            {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                // texture arrays are not available everywhere,
                // only compile shader on platforms where they are
                #pragma require 2darray
                
                #include "UnityCG.cginc"
    
                struct v2f
                {
                    float3 uv : TEXCOORD0;
                    float4 vertex : SV_POSITION;
                };
    
                float _SliceRange;
                float _UVScale;
    
                v2f vert (float4 vertex : POSITION)
                {
                    v2f o;
                    o.vertex = mul(UNITY_MATRIX_MVP, vertex);
                    o.uv.xy = (vertex.xy + 0.5) * _UVScale;
                    o.uv.z = (vertex.z + 0.5) * _SliceRange;
                    return o;
                }
                
                UNITY_DECLARE_TEX2DARRAY(_MyArr);
    
                half4 frag (v2f i) : SV_Target
                {
                    return UNITY_SAMPLE_TEX2DARRAY(_MyArr, i.uv);
                }
                ENDCG
            }
        }
    }
    

## See Also

  * Introduction To Textures in Direct3D documentation.
  * Array Textures in OpenGL Wiki.

Texture2DArray