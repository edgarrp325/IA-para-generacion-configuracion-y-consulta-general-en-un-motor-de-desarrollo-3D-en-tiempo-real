---
title: "ShaderLab legacy functionality"
category: "General"
source_file: "shader-shaderlab-legacy.html"
doc_type: "manual"
---

# ShaderLab legacy functionality

ShaderLab includes a number of “fixed-function style” commands that allow you to write **shaders** without using any HLSL code.

**Note** : These commands are legacy, and are documented for backwards compatibility only. If your **Shader object** source file includes HLSL code, Unity ignores these commands completely. If your shader source file does not include HLSL code, Unity compiles these commands into regular shader programs on import.

  * Legacy fog
  * Legacy lighting
  * Legacy alpha testing
  * Legacy texture combining
  * Legacy vertex data channel mapping