---
title: "Shader keywords"
category: "General"
source_file: "shader-keywords.html"
doc_type: "manual"
---

# Shader keywords

Shader keywords allow you to use conditional behavior in your **shader**

You can use shader keywords with dynamic branching, or with Shader variants

This page contains the following information:

  * Using shader keywords
    * Declaring shader keywords
    * Making behavior conditional with shader keywords
    * Enabling and disabling shader keywords
  * Unity’s predefined shader keywords
  * Shader keyword limits

## Using shader keywords

### Declaring shader keywords

You declare shader keywords in sets. A set contains mutually exclusive keywords.

For example, the following set contains three keywords:

  * COLOR_RED
  * COLOR_GREEN
  * COLOR_BLUE

    
    
    #pragma shader_feature RED GREEN
    

**Note:** In Shader Graph, the terminology is different: a set of keywords is called a **Keyword** , and the keywords in a set are called **states**. Internally, the functionality is the same: Unity compiles them in the same way, you work with them the same way with C# **scripts** , and so on.

The way that you declare shader keywords affects a number of things:

  * The type affects whether and how Unity uses the keywords to generate shader variants, or whether it uses them for dynamic branching.
  * The scope affects whether the keywords are local or global. This determines their behavior at runtime.
  * The stage affects which shader stage the keywords affect (where applicable).

#### Definition type: “multi compile”, “shader feature”, or “dynamic branch”

When you declare a set of keywords, you choose whether to use them with shader variants or with dynamic branching. If you choose shader variants, you must also choose how Unity defines the keywords internally; this affects the number of variants that Unity compiles.

  * “dynamic branch”: Use this to create a set of keywords for use with dynamic branching. Internally, Unity uses these keywords to create uniform variables.
  * “multi compile” or “shader feature”: Use this to create a set of keywords for use with shader variants. Internally, Unity uses these keyword to create `#define` preprocessor directives. 
    * “multi compile” declares a set of keywords for use with shader variants.  
  
Unity compiles shader variants for all keywords in the set.
    * “shader feature” declares a set of keywords for use with shader variants, and also instructs the compiler to compile variants where none of these keywords are enabled.  
  
Unity examines the state of your project at build time, and only compiles variants for keywords that are in use. A keyword is in use if a material that is included in the build has that keyword enabled.

Whether to choose “multi compile” or “shader feature” depends on how you use the keywords. If you use the keywords to configure materials in your project and do not change their value from C# scripts at runtime, then you should use “shader feature” to reduce the number of shader keywords and variants in your project. If you enable and disable keywords at runtime using C# scripts, then you should use “multi compile” to prevent variants being stripped in error. For more information on shader stripping, see Shader variant stripping.

**Note:** If you add a shader to the list of **Always Included Shaders** in the Graphics settings window, Unity includes all keywords from all sets in the build, even if they were declared with “shader feature”.

To set this value, see the following documentation:

  * In hand-coded shaders, see Declaring and using shader keywords in HLSL
  * In Shader Graph, see Keywords. **Note:** The “dynamic branch” option is not available in Shader Graph. You can only use shader keywords with shader variants in Shader Graph.

#### Local or global scope

When you declare a set of keywords, you choose whether the keywords in the set have local or global **scope**. This determines whether you can override the state of this keyword at runtime using a global shader keyword.

By default, you declare keywords with global scope. This means that you can override the state of this keyword at runtime using a global shader keyword. If you declare keywords with local scope, this means that you cannot override the state of this keyword at runtime using a global shader keyword. For more information and a code example, see Using shader keywords with C# scripts.

**Note:** If a keyword with the same name exists in a shader source file and its dependencies, the scope of the keyword in the source file overrides the scope in the dependencies. Dependencies comprise all Shaders that are included via the Fallback command, and Passes that are included via the UsePass command.

To set this value, see the following documentation:

  * In hand-coded shaders, see Declaring and using shader keywords in HLSL
  * In Shader Graph, see Keywords

#### Stage-specific keywords

By default, Unity generates keyword variants for each stage of your shader. For example, if your shader contains a vertex stage and a fragment stage, Unity generates variants for every keyword combination for both the vertex and the fragment shader programs. If a set of keywords is only used in one of those stages, this results in identical variants for the other stage. Unity automatically identifies and deduplicates identical variants so that they do not increase build size, but they still result in wasted compilation time, increased shader loading times, and increased runtime memory usage. 

To avoid this problem, when you declare a set of keywords in a hand-coded shader, you can instruct Unity to compile them only for a given shader stage. You are then responsible for ensuring that the keywords are only used in the specified shader stages. 

**Note:** The following graphics APIs do not fully support stage-specific keywords. In OpenGL and Vulkan, at compile time, Unity automatically converts all stage-specific keyword directives to regular keyword directives. In Metal, any keyword targeting vertex stages also affects tessellation stages, and vice versa. 

To set this value:

  * In hand-coded shaders, see Declaring and using shader keywords in HLSL
  * In Shader Graph, you cannot set this value. By default, all keywords affect all stages.

### Making behavior conditional with shader keywords

You can use shader keywords to make parts of your shader conditional, so that certain behaviors only execute when a given keyword is in a given state.

To do this:

  * In hand-coded shaders, see Defining and using shader keywords.
  * In Shader Graph, see Shader Graph: Keyword Node.

### Enabling and disabling shader keywords

You can enable or disable shader keywords. When you enable or disable a shader keyword, the shader displays the appropriate conditional behavior. Depending on whether the keyword work with shader variants or dynamic branching, this means that either Unity renders the appropriate shader variant, or the GPU executes the appropriate branch.

There are two ways to enable and disable shader keywords:

  * Use scripts, either at runtime or in the Unity Editor. For more information, see Using shader keywords with C# scripts.
  * Use the Material **Inspector** in the Unity Editor. For more information, see Using shader keywords with the Material Inspector.

## Unity’s predefined shader keywords

Unity uses predefined sets of shader keywords to generate shader variants that enable common functionality.

Unity adds the following sets of shader variant keywords at compile time:

  * By default, Unity adds this set of keywords to all graphics shader programs: STEREO_INSTANCING_ON, STEREO_MULTIVIEW_ON, STEREO_CUBEMAP_RENDER_ON, UNITY_SINGLE_PASS_STEREO. You can strip these keywords using an Editor script. For more information, see Shader variant stripping.
  * By default, Unity adds this set of keywords to the Standard Shader: LIGHTMAP_ON, DIRLIGHTMAP_COMBINED, DYNAMICLIGHTMAP_ON, LIGHTMAP_SHADOW_MIXING, SHADOWS_SHADOWMASK. You can strip these keywords using the Graphics settings window.
  * In the Built-in **Render Pipeline** , if your project uses tier settings that differ from each other, Unity adds this set of keywords to all graphics shaders: UNITY_HARDWARE_TIER1, UNITY_HARDWARE_TIER2, UNITY_HARDWARE_TIER3. For more information, see Graphics tiers: Graphics tiers and shader variants.

## Shader keyword limits

Unity can use up to 4,294,967,294 global shader keywords. Individual shaders and compute shaders can use up to 65,534 local shader keywords. These totals include keywords used for variants, and keywords used for dynamic branching.

Every keyword declared in the shader source file and its dependencies count towards this limit. Dependencies include Passes that the shader includes with UsePass, and fallbacks.

If Unity encounters a shader keyword with the same name multiple times, it only counts towards the limit once.

If a shader uses more than 128 keywords in total, it incurs a small runtime performance penalty; therefore, it is best to keep the number of keywords low. Unity always reserves 4 keywords per shader.