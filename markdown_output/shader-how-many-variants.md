---
title: "Check how many shader variants you have"
category: "General"
source_file: "shader-how-many-variants.html"
doc_type: "manual"
---

# Check how many shader variants you have

You can use logging and profiling tools to check how many **shader** variants Unity compiles, and identify ways you can remove (strip) variants to improve build times and reduce memory usage. You can do the following:

  * Get a list of shader variants the Editor uses
  * Get a list of shader variants Unity creates at build time
  * Get a list of shader variants Unity compiles at runtime
  * Check how much memory shaders use at runtime
  * Highlight missing shaders at runtime

## Get a list of shader variants the Editor uses

You can generate a list of shader variants that the Editor uses in the **Scene** view and the Game view. To do this:

  1. Go to **Edit > Project Settings > Graphics**.
  2. Under **Shader Loading** , you can see how many shaders and shader variants you have next to **Currently tracked:**.
  3. Select **Save to asset…** to create a shader variant collection asset.

## Get a list of shader variants Unity creates at build time

After you build your project, open the `Editor.log` log file and search for `Compiling shader` to see which variants Unity compiles and strips. For example:
    
    
    Compiling shader "Universal Render Pipeline/Lit" pass "ForwardLit" (fp)
    320 / 786432 variants left after stripping, processed in 6.77 seconds
    starting compilation...
    finished in 29.72 seconds. Local cache hits 202 (0.24s CPU time), remote cache hits 0 (0.00s CPU time), compiled 118 variants (582.41s CPU time), skipped 0 variants
    

If you’re using the Universal Render Pipeline (URP) or the High Definition Render Pipeline (HDRP), you can also log how many variants Unity compiles and strips in total. Select a logging level other than **Disabled** under **Shader Stripping > Shader Variant Log Level** in the following:

  * The Universal Render Pipeline Asset if you’re using URP.
  * The Global Settings Window if you’re using HDRP.

This adds `Total` logging to `Editor.log`. For example:
    
    
    STRIPPING: Universal Render Pipeline/Lit (ForwardLit pass) (Fragment) - Remaining shader variants = 640/5760 = 11.11111% - Total = 2657/10169 = 26.12843%
    

See log files for the location of `Editor.log`.

## Get a list of shader variants Unity compiles at runtime

  1. Go to **Edit > Project Settings > Graphics**.
  2. Under **Shader Loading** , enable **Log Shader Compilation**.
  3. When you build your project, enable ****Development Build**** in the build settings.
  4. In the Console Window, select **Editor** and enable **Full Log [Developer Mode Only]**.
  5. Start the application you built.

Unity prints a `Compiled shader` message in the Console Window when it compiles a shader for the GPU.

## Check how much memory shaders use at runtime

Use the Memory Profiler module or the Memory Profiler package to check how much memory shaders are using at runtime. If a shader uses a lot of memory, you can experiment with stripping its variants.

## Highlight missing shaders at runtime

In Unity 2022.2 and above, you can force Unity to show a pink error shader during runtime, when a Material tries to use a missing shader variant.

  1. Go to **Edit > Project Settings > Player**.
  2. Under **Other Settings** , in the **Shader Settings** section, select **Strict shader variant matching**.

You can also enable this in C# **scripts** using `strictShaderVariantMatching`.

When you do this, Unity shows a warning in the console with the missing variant and its keywords. You can use this during stripping to check you don’t remove shader variants your project needs.