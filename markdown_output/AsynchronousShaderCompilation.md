---
title: "Asynchronous shader compilation"
category: "General"
source_file: "AsynchronousShaderCompilation.html"
doc_type: "manual"
---

# Asynchronous shader compilation

Asynchronous **shader** compilation is an Editor-only feature that can improve your workflow when you have complex **Shader objects** compilation is an Editor-only feature that can improve your workflow when you have complex **Shader objects** with lots of shader variants.

This page contains the following information:

  * Overview
  * How asynchronous shader compilation works
  * Enabling and disabling asynchronous shader compilation for your project
  * Enabling and disabling asynchronous shader compilation for specific rendering calls
  * Disabling asynchronous shader compilation for a specific Shader object
  * Detecting asynchronous shader compilation in the Unity Editor
  * Advanced rendering in the Editor and asynchronous shader compilation
  * Custom Editor tools and asynchronous shader compilation

## Overview

Shader objects can contain of hundreds or thousands of shader variants. If the Editor compiled all variants when loading a Shader object, the import process would be very slow. Instead, the Editor compiles shader variants on-demand, the first time it encounters them.

Compiling these shader variants can cause the Editor to stall for milliseconds or even seconds, depending on the graphics API and the complexity of the Shader object. To avoid these stalls, you can use asynchronous shader compilation to compile the shader variants in the background, and use placeholder Shader objects in the meantime.

## How asynchronous shader compilation works

Asynchronous shader compilation works like this:

  1. When the Editor first encounters an uncompiled shader variant, it adds the shader variant to a compilation queue on a job thread. The progress bar in the bottom right corner of the Editor shows the status of the compilation queue.
  2. While the shader variant is loading, Editor renders the geometry with a placeholder shader, which appears as a plain cyan color.
  3. When the Editor has finished compiling the shader variant, it renders the geometry using the shader variant.

Unity renders shader variants that are still compiling with a cyan dummy Shader until compilation has finished. The bottom right progress bar indicates the compilation queue progress.

### Exceptions

The following exceptions apply:

  * If you draw geometry using `DrawProcedural` or `CommandBuffer.DrawProcedural`, the Editor doesn’t use a placeholder shader. Instead, the Editor just skips rendering this geometry until it has compiled the shader variant.
  * The Unity Editor does not use asynchronous shader compilation with **Blit** operations. This is to guarantee correct output in the most common use cases.

## Enabling and disabling asynchronous shader compilation for your project

Asynchronous shader compilation is enabled by default.

To enable or disable asynchronous shader compilation:

  1. Go to **Edit > Project Settings > Editor**.
  2. At the bottom of the Editor settings, under **Shader Compilation** , check or uncheck the **Asynchronous Shader Compilation** checkbox.

You can find the check box for **Asynchronous Shader Compilation** under the **Project Settings > Editor > Shader Compilation**.

**Note:** Enabling and disabling asynchronous shader compilation in this way affects only the **Scene** and Game views by default. If you want to use it in other parts of the Editor, see Custom Editor tools and asynchronous shader compilation.

## Enabling and disabling asynchronous shader compilation for specific rendering calls

You can enable or disable asynchronous shader compilation for specific rendering commands in your C# **scripts**.

The following instructions show you how to enable or disable the feature in an immediate scope, and a CommandBuffer scope.

#### In an immediate scope

In an immediate scope, you can use `ShaderUtil.allowAsyncCompilation`.

To do this:

  1. Store the current state of `ShaderUtil.allowAsyncCompilation` in a variable.
  2. Before you call the rendering commands, set `ShaderUtil.allowAsyncCompilation` to `false`.
  3. Call the rendering commands.
  4. After calling the rendering commands, restore `ShaderUtil.allowAsyncCompilation` back to its previous state.

Here is a pseudo-code example:
    
    
    // Store the current state
    bool oldState = ShaderUtil.allowAsyncCompilation;
    
    // Disable async compilation
    ShaderUtil.allowAsyncCompilation = false;
    
    // Enter your rendering code that should never use the placeholder shader, for example UI elements or characters.
    Graphics.RenderMesh(...);
    
    // Restore the old state
    ShaderUtil.allowAsyncCompilation = oldState;
    

#### In a CommandBuffer scope

In a `CommandBuffer` scope, you can use `ShaderUtil.SetAsyncCompilation` and `ShaderUtil.RestoreAsyncCompilation`.

  1. Immediately before you call the rendering commands, call `ShaderUtil.SetAsyncCompilation`, and set it to `false`. Subsequent commands in the CommandBuffer won’t allow asynchronous compilation.
  2. Add the rendering commands to the CommandBuffer.
  3. After the rendering commands, call `Shader.Util.RestoreAsyncCompilation` to restore the state of asynchronous shader compilation.

Here is an example:
    
    
    // Create the CommandBuffer
    CommandBuffer cmd = new CommandBuffer();
    
    // Disable async compilation for subsequent commands
    ShaderUtil.SetAsyncCompilation(cmd, false);
    
    /// Enter your rendering commands that should never use the placeholder shader, for example UI elements or characters.
    cmd.DrawMesh(...);
    
    // Restore the old state
    ShaderUtil.RestoreAsyncCompilation(cmd);
    

## Disabling asynchronous compilation for specific Shader objects

You can disable asynchronous shader compilation for specific Shader objects by forcing the Editor to always compile them synchronously. This is a good option for data generating Shader objects that are always present at the start of your rendering, and which are relatively quick to compile. You would most likely need this if you are performing advanced rendering.

To force synchronous compilation for a Shader object, add the `#pragma editor_sync_compilation` directive to your shader source code.

**Note:** You should not force synchronous compilation for complex Shader objects that encounter new shader variants during rendering; this can stall rendering in the Editor.

## Detecting asynchronous shader compilation

You can use C# APIs to monitor the state of asynchronous shader compilation, and perform operations when this state changes.

This is most likely useful in advanced rendering; if the placeholder shader pollutes your generated data, you can wait until compilation is complete, discard the polluted data, and regenerate a new set with the correct shader variants.

If you already know which material you are interested in, you can use `ShaderUtil.IsPassCompiled` to check the compilation status of the shader variant. When the status changes _Uncompiled_ to _Compiled_ , compilation is complete.

If you do not know which material you are interested in, or if you are interested in more than one material, you can use `ShaderUtil.anythingCompiling` to detect whether Unity is compiling any shader variants asynchronously. When this changes from `true` to `false`, all current compilation is complete.

## Advanced rendering in the Editor and asynchronous shader compilation

Advanced rendering solutions rely on generating data once and reusing it in later frames. If the Editor uses a placeholder shader during this process, it might pollute the generated data. If this happens, you can see the cyan color or other rendering artifacts in your scene, even after the shader variants have finished compiling.

To avoid this, you can:

  * Disable asynchronous shader compilation completely for your project
  * Disable asynchronous shader compilation for specific rendering calls
  * Disable asynchronous shader compilation for a specific Shader object
  * Detect when the source of the data pollution has finished compiling, and then re-generate the data.

## Custom Editor tools and asynchronous shader compilation

By default, asynchronous Shader compilation works in the Game and **Scene views**. If you want to use it in custom Editor tools, you can enable it via C# for your custom tool.

To do this, you can enable asynchronous shader compilation for specific rendering calls.

### Customizing compile time rendering

You can make your custom tools draw something other than the placeholder shader for each material. This way, you can avoid rendering in plain cyan, and instead draw something else while the shader variant compiles.

To check if a specific shader variant has compiled, see Detecting asynchronous shader compilation.

To trigger compilation manually, you can use `ShaderUtil.CompilePass`. This way, you can avoid rendering with the cyan placeholder, and draw something else while the shader variant compiles.