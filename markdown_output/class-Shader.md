---
title: "Shader assets"
category: "General"
source_file: "class-Shader.html"
doc_type: "manual"
---

# Shader assets

Switch to Scripting

A shader asset is an asset in your Unity project that defines a Shader object. It is a text file with a `.shader` extension. It contains shader code.

## Creating a new shader asset

To create a new shader asset, use **Assets** > **Create** > **Shader** > **Create** > **Shader** from the main menu or the **Project View** context menu.

### Inspector reference

When you select a shader asset in your Unity project, the **Inspector** displays basic information about the Shader object that it defines. It also provides controls for compiling, and inspecting the compiled code.

Shader inspector.

### Import settings

The Import settings section of the Inspector lets you set the default textures for a shader asset. Whenever a new Material is created with this shader, these textures are automatically assigned.

### Imported object

The Imported object section of the Inspector lets you view and edit settings related to the Shader object itself, and how the shader compiler handles it.

Shader compilation popup menu.

For Surface Shaders, the **Show generated code** button displays the code that Unity generates from your simplified source file. If you want to customize the generated code, you can just copy and paste it into your shader source file.

You can use the **Compile and show code** popup menu to:

  * Manually compile all shader variants for a selected graphics API. In the Unity Editor, the shader does not compile all shader variants for all graphics APIs until build time. You can manually force this to check for errors. For more information on what the shader compiler does and when, see Shader compilation
  * Inspect the compiled shader code for selected platforms. This is mostly useful while optimizing shaders for performance; often you do want to know how many low-level instructions are generated. You can paste the generated code into GPU shader performance analysis tools (like AMD GPU ShaderAnalyzer or PVRShaderEditor.

The **Preprocess Only** checkbox lets you view the preprocessed source for that shader asset.

Shader