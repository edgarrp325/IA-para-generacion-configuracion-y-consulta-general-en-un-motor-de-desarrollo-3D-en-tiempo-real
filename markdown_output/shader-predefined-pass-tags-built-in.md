---
title: "ShaderLab: Predefined Pass tags in the Built-in Render Pipeline"
category: "General"
source_file: "shader-predefined-pass-tags-built-in.html"
doc_type: "manual"
---

# ShaderLab: Predefined Pass tags in the Built-in Render Pipeline

This page contains information on predefined Pass tags that you can use with the Built-in **Render Pipeline**.

For general information on Pass tags, including an introduction to the LightMode tag, see ShaderLab: assigning tags to a Pass. For predefined Pass tag values in the Universal Render Pipeline (URP), see URP Pass tags: LightMode.

## LightMode tag valid values

These are the valid values for the `LightMode` Pass tag in the Built-in Render Pipeline. For more information on the LightMode tag, see ShaderLab: using Pass tags.

**Value** | **Function**  
---|---  
`Always` | Always rendered; does not apply any lighting. This is the default value.  
`ForwardBase` | Used in **Forward rendering** ; applies ambient, main directional light, vertex/SH lights and **lightmaps** ; applies ambient, main directional light, vertex/SH lights and **lightmaps**.  
`ForwardAdd` | Used in Forward rendering; applies additive per-pixel lights, one Pass per light.  
`Deferred` | Used in **Deferred Shading** ; renders G-buffer.  
`ShadowCaster` | Renders object depth into the shadowmap or a depth texture.  
`MotionVectors` | Used to calculate per-object motion vectors.  
`Vertex` | Used in legacy Vertex Lit rendering when the object is not lightmapped; applies all vertex lights.  
`VertexLMRGBM` | Used in legacy Vertex Lit rendering when the object is lightmapped, and on platforms where the lightmap is RGBM encoded (PC & console).  
`VertexLM` | Used in legacy Vertex Lit rendering when the object is lightmapped, and on platforms where lightmap is double-LDR encoded (mobile platforms).  
`Meta` | This Pass is not used during regular rendering, only for lightmap baking or **Enlighten** Realtime **Global Illumination**. For more information, see Lightmapping and shaders.  
  
## PassFlags tag

In the Built-in Render Pipeline, use the `PassFlags` Pass tag to specify what data Unity provides to the Pass.

### Valid values

**Value** | **Function**  
---|---  
OnlyDirectional | Valid only in the Built-in Render Pipeline, when the rendering path is set to Forward, in a Pass with a `LightMode` tag value of `ForwardBase`.  
  
Unity provides only the main directional light and ambient/light probe data to this Pass. This means that data of non-important lights is not passed into vertex-light or spherical harmonics shader variables. See Forward rendering path for details.  
  
### PassFlag tag code examples
    
    
    Shader "Examples/ExamplePassFlag"
    {
        SubShader
        {
            Pass
            {    
                  Tags { "LightMode" = "ForwardBase" "PassFlags" = "OnlyDirectional" }
                
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## RequireOptions tag

In the Built-in Render Pipeline, the `RequireOptions` Pass tag enables or disables a Pass based on **project settings**.

### Valid values

**Value** | **Function**  
---|---  
`SoftVegetation` | Render this Pass only if QualitySettings-softVegetation is enabled.  
  
### Examples
    
    
    Shader "Examples/ExampleRequireOptions"
    {
        SubShader
        {
            Pass
            {    
                  Tags { "RequireOptions" = "SoftVegetation" }
                
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }