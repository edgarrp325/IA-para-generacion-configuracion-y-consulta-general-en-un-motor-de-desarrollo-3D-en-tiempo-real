---
title: "ShaderLab: adding shader programs"
category: "General"
source_file: "shader-shaderlab-code-blocks.html"
doc_type: "manual"
---

# ShaderLab: adding shader programs

In Unity, you usually write **shader** programs in HLSL. To add HLSL code to your shader asset, you put the code inside a **shader code block**. 

This page contains information about using shader code blocks. For information about writing HLSL itself, see Using HLSL in Unity.

## HLSL

`HLSLPROGRAM` and `HLSLINCLUDE` are compatible with all **render pipelines**.

**Signature** | **Function**  
---|---  
`HLSLPROGRAM`  
`[source code for shader programs]`  
`ENDHLSL` | Creates a shader program block. Unity adds the HLSL shader program to the pass that includes this shader program block.  
`HLSLINCLUDE`  
`[code that you want to share]`  
`ENDHLSL` | Creates a shader include block. Unity includes this code in all shader programs that are defined in `HLSLPROGRAM` blocks, anywhere in this source file.  
  
## CG

`CGPROGRAM` and `CGINCLUDE` are compatible only with the Built-In Render Pipeline. For most uses, use `HLSLPROGRAM` and `HLSLINCLUDE` instead, unless you write surface shaders.

If you use `CGPROGRAM`, Unity includes several of Unity’s built-in shader include files by default, enabling you to use built-in variables and functions. As a result, shaders that use `CGPROGRAM` might not work if you change the keyword to `HLSLPROGRAM`. 

**Note** : Although the shader library files in the Built-In Render Pipeline have a .cginc file extension, they contain HLSL code rather than CG code.

**Signature** | **Function**  
---|---  
`CGPROGRAM`  
`[source code for shader programs]`  
`ENDCG` | Creates a shader program block. Unity adds the shader program to the pass that includes this shader program block.  
`CGINCLUDE`  
`[code that you want to share]`  
`ENDCG` | Create a shader include block. Unity includes this code in all shader programs that are defined in `CGPROGRAM` blocks, anywhere in this source file.  
  
## Using a shader program block

  * Writing HLSL shader programs
  * Import a file from the shader library in the Built-In Render Pipeline
  * Shader methods in URP