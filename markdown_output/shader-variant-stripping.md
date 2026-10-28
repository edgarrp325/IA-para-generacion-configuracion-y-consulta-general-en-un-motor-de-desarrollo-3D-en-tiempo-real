---
title: "Shader variant stripping"
category: "General"
source_file: "shader-variant-stripping.html"
doc_type: "manual"
---

# Shader variant stripping

You can prevent shader variants from being compiled. This is called **stripping**. Stripping unneeded variants can greatly reduce build times, file size, **shader** from being compiled. This is called **stripping**. Stripping unneeded variants can greatly reduce build times, file size, **shader** loading times, and runtime memory usage. In larger projects, or projects with complex shaders, this is a very important consideration.

If you strip a shader variant that a Material needs at runtime, Unity tries to choose a similar shader variant that’s available. To avoid this, use the following approaches:

  * If you use a `shader_feature` keyword, don’t use the keyword to change which code branch executes at runtime.
  * Check what shader variants you have to help you see which shader variants and keyword combinations Materials need at runtime.
  * Add shaders to the **Always Included Shaders** list in Graphics settings.

## Limiting shader variants when you declare shader keywords

The way that you declare shader keywords can limit the number of variants that they produce:

  * Use `shader_feature` instead of `multi_compile` where possible - see conditionals in shaders.
  * Ensure that you don’t define unused keywords with `multi_compile`.

For information on declaring keywords in hand-coded shaders, see Declaring and using shader keywords in HLSL. For information on declaring keywords in Shader Graph, see Shader Graph: Blackboard.

### Indicate which shader keywords affect which shader stage

When you declare a keyword, Unity assumes all stages of the shader contain conditional code for that keyword.

You can add the following suffixes to indicate that only certain stages contain conditional code for a keyword, so that Unity doesn’t generate unneeded shader variants.

  * `_vertex`
  * `_fragment`
  * `_hull`
  * `_domain`
  * `_geometry`

For example, use `#pragma shader_feature_fragment RED GREEN BLUE` to indicate that you use the 3 keywords to create conditional code in the fragment stage only.

You can’t add these suffixes to `#pragma dynamic_branch` because `dynamic_branch` doesn’t create variants.

These suffixes might behave differently or have no effect, depending on the graphics API. For example:

  * The suffixes have no effect on OpenGL, OpenGL ES or Vulkan.
  * The `_geometry` and `_raytracing` suffixes have no effect on Metal. Metal treats `_vertex`, `_hull` and `_domain` as a single stage.

### Use preprocessor macros to limit variants by platform

In Unity 2021.3 and above, you can create conditional shader code using a target platform preprocessor macro, so you can limit variants on platforms with limited memory.

The code sample does the following:

  * If you build for a `SHADER_API_DESKTOP` platform, Unity builds variants for every possible keyword combination.
  * If you build for another platform, Unity builds only variants for keyword combinations the Materials in your build use.

    
    
    #ifdef SHADER_API_DESKTOP
       #pragma multi_compile _ RED GREEN BLUE WHITE
    #else
       #pragma shader_feature RED GREEN BLUE WHITE
    #endif
    

You can use target platform preprocessor macros to select between `shader_feature`, `multi_compile` and `dynamic_branch`. For more information on when to use each type of conditional, see Shader Conditionals.

### Create user-controlled quality settings

When you build for console and mobile platforms that have limited memory, you can limit shader variants by only allowing users to switch between a small number of quality settings.

For example, if you use the keywords `DYNAMIC_LIGHTING`, `SOFT_SHADOWS` and `HIGH_QUALITY_LIGHTMAPS`, you can create the following:

  * A ‘low quality’ setting that turns on `DYNAMIC_LIGHTING`.
  * A ‘high quality’ setting that turns on `DYNAMIC_LIGHTING`, `SOFT_SHADOWS` and `HIGH_QUALITY_LIGHTMAPS`.

This means Unity won’t create shader variants for `DYNAMIC_LIGHTING` when it’s off, or the many different combinations of the 3 keywords being on and off.

You can use target platform preprocessor macros to conditionally create fewer quality settings and fewer variants on platforms with limited memory. For example the following code sample will allow users to switch between 8 permutations of settings on `SHADER_API_DESKTOP` platforms, but only 2 on `SHADER_API_MOBILE` platforms.
    
    
    #if SHADER_API_DESKTOP
       #pragma multi_compile SHADOWS_LOW SHADOWS_HIGH
       #pragma multi_compile REFLECTIONS_LOW REFLECTIONS_HIGH
       #pragma multi_compile CAUSTICS_LOW CAUSTICS_HIGH
    #elif SHADER_API_MOBILE
       #pragma multi_compile QUALITY_LOW QUALITY_HIGH
       #pragma shader_feature CAUSTICS // Uses shader_feature, so Unity strips variants that use CAUSTICS if there are no Materials that use the keyword at build time.
    #endif
    

## Stripping shader variants in the Editor UI

There are several places in the Unity Editor **UI** where you can configure shader stripping:

  * In the Graphics Settings window, configure the settings in the **Shader stripping** section:

  * Ensure that no unneeded shaders are included in the **Always-included shaders** setting.

  * Strip variants relating to GPU instancing, lightmapping, and fog.

  * In the Built-in **Render Pipeline** , if it is not important that your Tier settings are different, ensure that they are identical to each other. For more information, see Graphics tiers.

  * In the Universal Render Pipeline (URP), disable unused features in the URP Asset. For more information, see Shader stripping.

If you use the Universal Render Pipeline you can also do the following:

  * In the Universal Render Pipeline Asset, disable rendering any features your project doesn’t use.
  * Enable shader stripping.

If you use the High Definition Render Pipeline you can also do the following:

  * In the High Definition Render Pipeline Asset, disable any rendering features your project doesn’t use.
  * In the Miscellaneous section of the HDRP Global Settings Window, disable **Runtime Debug Shaders**.

## Stripping shader variants using Editor scripts

For shader variants that you can’t strip in other ways, you can use the following APIs in an Editor script to perform build-time stripping:

  * IPreprocessShaders.OnProcessShader: receive a callback before Unity compiles a graphics shader Pass into a build.
  * IPreprocessComputeShaders.OnProcessComputeShader: receive a callback before Unity compiles a compute shader into a build.

For more information on this subject, see the Unity blog post Stripping scriptable shader variants