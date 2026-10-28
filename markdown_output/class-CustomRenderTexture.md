---
title: "Custom Render Textures"
category: "General"
source_file: "class-CustomRenderTexture.html"
doc_type: "manual"
---

# Custom Render Textures

Switch to Scripting

**Custom Render Textures** are a special type of texture that allow you to update a texture with a **shader**. They are an extension to Render Textures. They are an extension to Render Textures. You can use Custom Render Textures to create complex simulations like caustics, ripple simulation for rain effects, and liquid splatters.

The Custom Render Textures feature provides a scripting and Shader framework to help with complicated configuration like varying update frequency, partial or multi-pass updates.

To use this framework you need to assign a Material to the Custom Render Texture asset. Custom Render Textures require a compatible Material. For more information, see Writing a shader for a Custom Render Texture.

To assign a compatible material to a Custom Render Texture asset:

  1. Create a new Custom Render Texture asset.
  2. Assign a compatible Material to it in the **Material** property in the **Custom Render Texture** asset.

This Material updates the content of a texture according to its parameters.

This page contains the following information:

  * Render Pipeline Compatibility

  * Properties

    * Render Texture
    * Custom Render Texture
  * Exporting Custom Render Texture to a file

  * Update Zones

  * Controlling Custom Render Texture from Script

  * Double Buffered Custom Render Textures

  * Chaining Custom Render Textures

  * Writing a shader for a Custom Render Texture

## Render Pipeline Compatibility

The following table describes the compatibility between the **Custom Render Textures** feature and each **render pipeline** :

Feature | Built-in Render Pipeline | Universal Render Pipeline (URP) | High Definition Render Pipeline (HDRP) | Custom Scriptable Render Pipeline (SRP)  
---|---|---|---|---  
Custom Render Textures | Yes (1) | Yes (1) | Yes (1) | Yes (1)  
  
**Note:**

  1. Currently, you can’t create Materials that update and initialize **Custom Render Textures** in Shader Graph. You can only create shaders that operate on Custom Render Textures by writing ShaderLab

## Properties

The **Custom Render Textures** **Inspector** window displays many of the same properties as the Render Texture Inspector, and some properties specific to **Custom Render Textures**.

### Render Texture:

Property: | Function:  
---|---  
**Dimension** | Dimension of the Render Texture.  
2D | Makes the Render Texture two-dimensional.  
Cube | Makes the Render Texture a cube map.  
3D | Makes the Render Texture three-dimensional.  
**Size** | The size of the Render Texture in **pixels**.  
**Color Format** | The format of the Render Texture.  
**sRGB (Color Render Texture)** | Enable to allow the Render Texture to use sRGB read/write conversions (Read Only).  
**Enable Mip Maps** | Enable this property to allow the Render Texture to use mipmaps.  
**Auto generate Mip Maps** | Enable this property to automatically generate mipmaps.  
**Wrap Mode** | Defines how the Texture behaves when tiled.  
Repeat | The Texture repeats itself as a tile.  
Clamp | Unity stretches the edges of the Texture.  
**Filter Mode** | Defines how Unity filters the Texture when it is stretched by 3D transformations.  
Point | The Texture becomes blocky up close.  
Bilinear | The Texture becomes blurry up close.  
Trilinear | Like Bilinear, but the Texture also blurs between different mipmap levels.  
**Aniso Level** | Increases Texture quality when viewing the texture at a steep angle. Good for floor and ground textures.  
  
### Custom Texture:

These properties are exclusive to Custom Render Textures. Custom Texture parameters are separated into three categories:

  * **Material** : Defines what shader is used to update the texture.

  * **Initialization** : Controls how the texture is initialized before the shader performs any updates.

  * **Update** : Controls how the shader updates the texture.

Property: | Function:  
---|---  
**Material** | The Material that Unity uses to update the Custom Render Texture.  
Shader Pass | The Shader Pass that Unity uses to update the Custom Render Texture. The drop-down shows all passes available in your Material.  
**Initialization Mode** | The rate at which Unity initializes the texture.  
OnLoad | Unity initializes the texture once upon creation.  
Realtime | Unity initializes the texture every frame.  
OnDemand | Unity initializes the texture on demand from the script.  
**Source** | How Unity texture initializes the texture.  
Texture and Color | Unity uses a texture multiplied by a color to initialize the texture.  
Initialization Color | Defines the color that Unity uses to initialize the Custom Render Texture. If you also provide an **Initialization Texture** , Unity uses the multiplication of the color and the texture to initialize the Custom Render Texture.  
Initialization Texture | Defines the texture that Unity uses to initialize the Custom Render Texture. If you also provide an **Initialization Color** , Unity uses the multiplication of the color and the texture to initialize the Custom Render Texture.  
Material | Unity uses a Material to initialize the texture.  
Initialization Material | Defines the Material that Unity uses to initialize the Custom Render Texture.  
**Update Mode** | The rate at which the shader updates the Custom Render Texture.  
OnLoad | The shader updates the texture once upon creation.  
Realtime | The shader updates the texture every frame.  
OnDemand | The shader updates the texture on demand from script.  
**Period** | The amount of time in seconds over which Unity updates a real-time texture. A value of 0.0 updates every frame. This property is only available when the **Update Mode** to property is set to Realtime.  
**Double Buffered** | Double-buffers the texture. Each update swaps the two buffers. This allows you to read the result of the preceding update in the shader.  
**Wrap Update Zones** | Enable to allow partial update zones to wrap around the border of the texture.  
**Cubemap Faces** | (Cubemap only) Series of toggle allowing user to enable/disable update on each of the cube map faces.  
**Update Zone Space** | The coordinate system where Unity defines the update zones.  
Normalized | All coordinates and sizes are between 0 and 1 with the top-left corner starting at (0, 0).  
Pixel | All coordinates and sizes are expressed in pixels limited by the width and height of the texture. Top-left corner starting at (0, 0).  
**Update Zone List** | List of update zones for the texture. For more information, see Update Zones.  
  
## Exporting Custom Render Texture to a file:

You can export Custom Render Textures to a PNG or EXR file (depending on the texture format) in the **Export** menu.

## Update Zones:

When Unity updates a Custom Render Texture, it uses the Material to update the whole texture at once by default. The Custom Render Texture allows you to define zones of partial update. You can use this to define as many zones as you want and the order in which the zones are processed.

You can use update zones for various purposes. For example, you could have multiple small zones to splat water drops on the texture and then do a full pass to simulate the ripples. This can also be used as an optimization when you know that you don’t need to update the full texture.

Update zones have their own set of properties. The **Update Zone Space** is visible in the display. Coordinates depend on the **Dimension** of the texture: 2D for 2D and Cube textures, or 3D for 3D textures.

Property: | Function:  
---|---  
Center | The coordinates of the center of the update zone..  
Size | The size of the update zone.  
Rotation | The orientation of the update zone in degrees (unavailable for 3D textures).  
Shader Pass | Defines the Shader Pass to use for this update zone. If you set this property as default, this update zone uses the Shader Pass that you defined in the main part of the inspector. Otherwise it will use the Shader Pass you provide.  
Swap (Double Buffer) | (Only for Double Buffered textures) When you enable this property, Unity swaps the buffers before processing this update zone.  
  
## Controlling Custom Render Texture from Script

You can access most of the Custom Render Texture functionalities in the Scripting API. You can also change Material parameters, update frequency, update zones, request an update, and more using a script.

When Unity updates or initializes a Custom Render Texture, it uses the current properties to render the next frame. This guarantees that any Material that uses this texture has an up-to-date result. For example, in the following script Unity performs two updates using the second Update Zone array:

`customRenderTexture.updateZones = updateZones1;`

`customRenderTexture.Update();`

`customRenderTexture.updateZones = updateZones2;`

`customRenderTexture.Update();`

**Note:** Unity does not update or initialize a Custom Render Texture at the same time you call `Update()` or `Initialize()`. This is because Unity always updates and initializes a Custom Render Texture at the start of the next frame.

## Double Buffered Custom Textures

You can double-buffer Custom Render Textures. To do this, enable **Double Buffered** in the Custom Render Textures component, or use `CustomRenderTexture.doubleBuffered`.

Double-buffering means that inside one Custom Render Texture there are two textures which Unity can swap after each update. This allows you to read the result of the last update while writing a new result in the Custom Render Texture.

Double-buffering is particularly useful if the shader needs to use the content the Unity has already written in the texture but can’t mix the values with classic blend modes. This is also required if the shaders have to sample different pixels from the preceding result.

**Performance warning** : Double-buffering currently involves a copy of the texture at each swap which can lead to a drop in performance depending on the frequency at which it is done and the resolution of the texture.

## Chaining Custom Render Textures

You can chain Custom Render Textures together. To do this, use a Custom Render Texture as the input for a material that you have assigned to the **Material** or **Initialization Mode > Texture** in another Custom Render Texture.

You can use chained Custom Render Textures to generate a simulation with multiple steps.

Chained Custom Render Textures are dependent on each other. Unity calculates this dependency automatically so that each update happens in the right order. It does this by looking at the materials assigned to the **Material** and **Initialization Mode > Texture** properties in the **Custom Render Textures** inspector window.

## Writing a shader for a Custom Render Texture

To update a Custom Render Texture manually, you can write a specialized Custom Render Texture shader.

To help you write your Custom Render Texture shaders, here are two example frameworks that contain utility functions and built-in helper variables.

The following shader example fills the texture with a color multiplied by a color. When you write a shader for a Custom Render Texture, you must do the following:

  * `#include "UnityCustomRenderTexture.cginc"`.
  * Use the provided **Vertex Shader** `CustomRenderTextureVertexShader`.
  * Use the provided input structure `v2f_customrendertexture` for the pixel shader.

    
    
    Shader "CustomRenderTexture/Simple"
    {
        Properties
        {
            _Color ("Color", Color) = (1,1,1,1)
            _Tex("InputTex", 2D) = "white" {}
         }
    
         SubShader
         {
            Lighting Off
            Blend One Zero
    
            Pass
            {
                HLSLPROGRAM
                #include "UnityCustomRenderTexture.cginc"
                #pragma vertex CustomRenderTextureVertexShader
                #pragma fragment frag
                #pragma target 3.0
    
                float4      _Color;
                sampler2D   _Tex;
    
                float4 frag(v2f_customrendertexture IN) : COLOR
                {
                    return _Color * tex2D(_Tex, IN.localTexcoord.xy);
                }
                ENDHLSL
                }
        }
    }
    

The following example is a shader for a material you can use to initialize a Custom Render Texture. When you write a shader for an initialization Material, the following steps are mandatory:

  * `#include "UnityCustomRenderTexture.cginc"`

  * Use the provided Vertex Shader `CustomRenderTextureVertexShader`

  * Use the provided input structure `v2f_customrendertexture` for the pixel shader.

    
    
    Shader "CustomRenderTexture/CustomTextureInit"
    {
        Properties
        {
            _Color ("Color", Color) = (1,1,1,1)
            _Tex("InputTex", 2D) = "white" {}
        }
    
        SubShader
        {
            Lighting Off
            Blend One Zero
    
            Pass
            {
                HLSLPROGRAM
                #include "UnityCustomRenderTexture.cginc"
    
                #pragma vertex InitCustomRenderTextureVertexShader
                #pragma fragment frag
                #pragma target 3.0
    
                float4      _Color;
                sampler2D   _Tex;
    
                float4 frag(v2f_init_customrendertexture IN) : COLOR
                {
                    return _Color * tex2D(_Tex, IN.texcoord.xy);
                }
                ENDHLSL
            }
        }
    }
    

`#include "UnityCustomRenderTexture.cginc"` gives you access to a set of built-in values. This includes Global values, values from the `v2f_customrendertexture` structure and values from the `v2f_init_customrendertexture` structure.

The `v2f_customrendertexture` structure accepts the following inputs:

Name | Type | Value  
---|---|---  
`localTexcoord` | `float3` | Texture coordinates relative to the update zone being currently processed.  
`globalTexcoord` | `float3` | Texture coordinates relative to the Custom Render Texture itself  
`primitiveID` | `uint` | Index of the update zone being currently processed.  
`direction` | `float3` | For Cube Custom Render Texture, direction of the current pixel inside the **cubemap**.  
  
The `v2f_init_customrendertexture` structure accepts the following inputs:

Name | Type | Value  
---|---|---  
`texcoord` | float3 | Texture coordinates relative to the Custom Render Texture itself.  
  
The following structures are Global values:

Name | Type | Value  
---|---|---  
`_CustomRenderTextureWidth` | `float` | Width of the Custom Texture in pixels  
`_CustomRenderTextureHeight` | `float` | Height of the Custom Texture in pixels  
`_CustomRenderTextureDepth` | `float` | Depth of the Custom Texture in pixels (only for 3D textures, otherwise will always be equal to 1).  
`_CustomRenderTextureCubeFace` | `float` | The index of the current cubemap face that Unity processes (-X, +X, -Y, +Y, -Z, +Z). This only applies to cube maps.  
`_CustomRenderTexture3DSlice` | `float` | Index of the current 3D slice being processed. This only applies to 3D textures.  
`_SelfTexture2D` | `Sampler2D` | For double buffered textures: Texture containing the result of the last update before the last swap.  
`_SelfTextureCube` | `SamplerCUBE` | For double buffered textures: Texture containing the result of the last update before the last swap.  
`_SelfTexture3D` | `Sampler3D` | For double buffered textures: Texture containing the result of the last update before the last swap.  
  
* * *

  * 2017–05–18 Page published 

  * New feature in Unity 2017.1 NewIn20171

CustomRenderTexture