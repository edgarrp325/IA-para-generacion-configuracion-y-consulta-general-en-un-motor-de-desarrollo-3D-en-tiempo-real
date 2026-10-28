---
title: "ShaderLab: commands"
category: "General"
source_file: "shader-shaderlab-commands.html"
doc_type: "manual"
---

# ShaderLab: commands

This page contains information on using commands in the **ShaderLab** language.

ShaderLab commands fall into these categories:

  * Commands for setting the render state on the GPU.
  * Commands that create a Pass with a specific purpose.
  * Legacy “fixed function style” commands that allow you to create **shader** programs without writing HLSL.

You can group ShaderLab commands together with the Category block.

## Commands for setting render state

Use these commands within a Pass block to set the render state for that Pass, or within a SubShader block to set the render state for that SubShader and any Passes that it contains.

  * AlphaToMask: sets the alpha-to-coverage mode.
  * Blend: enables and configures alpha blending.
  * BlendOp: sets the operation used by the Blend command.
  * ColorMask: sets the color channel writing mask.
  * Conservative: enables and disables conservative **rasterization**.
  * Cull: sets the polygon culling mode.
  * Offset: sets the polygon depth offset.
  * Stencil: configures the stencil test, and what to write to the **stencil buffer**
  * ZClip: sets the depth clip mode.
  * ZTest: sets the depth testing mode.
  * ZWrite: sets the **depth buffer**

## Pass commands

Use these commands in a SubShader to define a Pass with a specific purpose.

  * UsePass defines a Pass that imports the contents of a named Pass from another **Shader object**
  * GrabPass creates a Pass that grabs the contents of the screen into a texture, for use in a subsequent Pass.

## Legacy “fixed function style” commands

These are documented on the page ShaderLab legacy functionality.