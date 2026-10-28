---
title: "Using shader keywords with the material Inspector"
category: "General"
source_file: "shader-keywords-material-inspector.html"
doc_type: "manual"
---

# Using shader keywords with the material Inspector

In the Unity Editor, when you view a material in the material **Inspector** , you can enable and disable its local **shader** , you can enable and disable its local **shader** keywords. This is useful for two reasons:

  * It allows artists to easily set different keyword values for different materials, without needing to use code.
  * When you enable a keyword using the `[KeywordEnum]` MaterialPropertyDrawer, Unity automatically disables the other keywords in a set. This ensures that exactly one keyword from a set is enabled at any time.

As with any shader settings or data, shader keywords are only available in the material Inspector when they are declared as material properties in the shader source file.

For shaders created in Shader Graph, keywords are material properties by default. This means that these settings are automatically available in the material Inspector. To change this, open the Blackboard, and change the **Exposed** property.

For hand-coded shaders, you must ensure that your **ShaderLab** code defines a material property that represents the keyword set. The material property must have a type of `Float`, and must use the `[Toggle]`, `[ToggleOff]`, or `[KeywordEnum]` MaterialPropertyDrawer attribute to expose it correctly to the Inspector.

The following example adds a toggle called **Make Red** , which enables and disables the keyword `_RED_ON`.
    
    
    Shader "Unlit/ToggleRed"
    {
        Properties
        {
            [Toggle] _RED ("Make red", Float) = 0
        }
        SubShader
        {
            Tags { "RenderType"="Opaque" }
    
            Pass
            {
                HLSLPROGRAM
                #pragma vertex vert
                #pragma fragment frag
    
                // Add the keyword RED_ON, for when the toggle is on
                // Unity automatically adds a keyword for when the toggle is off 
                #pragma shader_feature _RED_ON
    
                #include "UnityCG.cginc"
    
                struct appdata
                {
                    float4 vertex : POSITION;
                };
    
                struct v2f
                {
                    float4 vertex : SV_POSITION;
                };
    
                v2f vert (appdata v)
                {
                    v2f o;
                    o.vertex = UnityObjectToClipPos(v.vertex);
                    return o;
                }
    
                fixed4 frag (v2f i) : SV_Target
                {
                    // Return red if the toggle is on
                    #if _RED_ON
                        return fixed4(1, 0, 0, 1);
                    #else
                        return fixed4(0, 0, 0, 1);
                    #endif
                }
                ENDHLSL
            }
        }
    }
    

For more information and examples, see the documentation for the MaterialPropertyDrawer API.