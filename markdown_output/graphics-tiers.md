---
title: "Graphics tiers"
category: "General"
source_file: "graphics-tiers.html"
doc_type: "manual"
---

# Graphics tiers

In the Built-in **Render Pipeline** , you can use **graphics tiers** to apply different graphics settings when your application runs on hardware with different capabilities. You can use Unity’s built-in **tier settings** to configure common settings, or you can define custom behaviors in your own **shader** , you can use **graphics tiers** to apply different graphics settings when your application runs on hardware with different capabilities. You can use Unity’s built-in **tier settings** to configure common settings, or you can define custom behaviors in your own **shader** code or C# code. 

**Note:** This feature is only supported in the Built-in Render Pipeline. In other render pipelines, Unity still examines the hardware on startup and stores its value in Graphics.activeTier; however, the value of this field has no effect, and Unity does not perform any other operations relating to graphics tiers.

## Graphics tiers overview

When Unity first loads your application, it examines the hardware and graphics API and determines which graphics tier the current environment corresponds to. 

The graphics tiers are:

**Value** | **Hardware** | **CorrespondingGraphicsTier enum value** | **Correspondingshader keyword **  
---|---|---|---  
1 | Android: devices that only support OpenGL ES 2  
iOS: iPhones before iPhone 5S (not including 5S, but including 5C), iPods up to and including 5th generation, iPads up to 4th generation, iPad mini first generation  
Desktop: DirectX 9  
XR: HoloLens | Tier1 | `UNITY_HARDWARE_TIER1`  
2 | Android: devices that support OpenGL ES 3, devices that support Vulkan  
iOS: iPhones starting from iPhone 5S, iPad Air, iPad mini 2nd generation, iPod 6th generation, AppleTV  
WebGL: all devices | Tier2 | `UNITY_HARDWARE_TIER2`  
3 | Desktop: OpenGL, Metal, Vulkan, DirectX 11+ | Tier3 | `UNITY_HARDWARE_TIER3`  
  
## Using graphics tiers with C# scripts

Unity stores the value of the current graphics tier in Graphics.activeTier, represented by a GraphicsTier enum. To add custom behavior based on the current graphics tier, you can test against this value.

To override the value of `Graphics.activeTier`, set it directly. Note that you must do this before Unity loads any shaders that vary based on graphics tier. A good place to set this value is in a pre-loading **scene** , before you load your main scene.

## Tier settings

In the Unity Editor, you can configure **tier settings**. Tier settings allow you to enable or disable graphics features for each tier.

Tier settings work by changing `#define` preprocessor directives in Unity’s internal shader code. These changes automatically affect prebuilt shaders for the Built-in Render Pipeline (such as the Standard Shader), and the internal shader library code for Surface Shaders

The default tier settings are suitable for most use cases. You should only change them if you are experiencing performance issues, or if you want to enable features on lower-end devices that are not enabled by default.

You can configure different tier settings for each graphics tier of a given build target. You can change tier settings in the following ways:

  * Use the Graphics Settings window, in the **Tier Settings** section.
  * Use these APIs in an Editor script: 
    * EditorGraphicsSettings
    * TierSettings

You can test tier settings in the Editor. To do this, navigate to **Edit > Graphics Tier** and choose the tier that you want the Unity Editor to use.

## Graphics tiers and shader variants

In the Built-in Render Pipeline, Unity can generate shader variants that correspond to graphics tiers.

**Note:** These tier shader variants work differently to regular shader variants. At runtime, when Unity loads a **Shader object** into CPU memory, it only loads the variants for the active tier; it does not load the variants for other tiers. This helps to reduce the runtime impact of tier variants.

To generate tier shader variants, Unity adds this set of shader keywords to all graphics shaders:
    
    
    UNITY_HARDWARE_TIER1
    UNITY_HARDWARE_TIER2
    UNITY_HARDWARE_TIER3
    

You can use these keywords in your HLSL code to write conditional behavior for lower or higher-end hardware, the same way that you would for any shader keywords. For example:
    
    
    #if UNITY_HARDWARE_TIER1
    // Put code for tier 1 devices here
    #else
    // Put code for other devices here
    #endif
    

For more information on working with shader keywords in HLSL code, see Declaring and using shader keywords in HLSL.

Unity automatically generates tier shader variants based on the tier settings for the current build target, like this:

  * If all settings for all tiers are identical, Unity does not generate any tier shader variants.
  * If any of the settings for different tiers differ in any way, Unity generates all tier shader variants.

After generating all tier shader variants, Unity identifies and deduplicates identical tier shader variants. This means that if the settings for two tiers are identical (for example, if tier 1 is different but tier 2 and tier 3 are identical to one another), then these variants do not add to the file size of your application, and the way that Unity loads tier variants means that they do not affect loading times or runtime memory usage. However, this still results in redundant compilation work.

If you want to use different settings for different tiers, but you also know that this will result in redundant work - for example, if you know that your application will only ever run on tier 1 and tier 2 devices - you can use a script to strip unneeded tier variants from compilation, the same as for any other variants. For more information, see Shader variant stripping.

In addition to the automatic behavior, you can also force Unity to generate tier shader variants on a per-shader basis. This is useful if you use these constants in your HLSL code and you want to be certain that Unity will compile the required variants, regardless of whether the tier settings for the current build differ from each other

To manually force Unity to generate tier shader variants for a given shader, use the `#pragma hardware_tier_variants` preprocessor directive in your HLSL code, and specify the graphics APIs for which you want to generate per-tier variants:
    
    
    #pragma hardware_tier_variants gles3
    

For a list of valid graphics API names that you can use with this directive, see Targeting graphics APIs. For general information on `#pragma` directives, see pragma directives.