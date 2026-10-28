---
title: "Preprocessor directives in HLSL"
category: "General"
source_file: "shader-preprocessor-directives.html"
doc_type: "manual"
---

# Preprocessor directives in HLSL

Internally, shader compilation has multiple stages. The first stage is **preprocessing** , where a program called the preprocessor prepares the code for compilation. **Preprocessor directives** are instructions for the preprocessor.

This section of the manual contains information on Unity-specific ways of working with HLSL preprocessor directives, and HLSL preprocessor directives that are unique to Unity. It does not contain exhaustive documentation on all the preprocessor directives that HLSL supports, or general information on working with preprocessor directives in HLSL. For that information, see the HLSL documentation: Preprocessor directives (HLSL).

**Page** | **Description**  
---|---  
include and include_with_pragmas directives in HLSL | Working with `#include` and the Unity-specific `#include_with_pragmas` directives in HLSL in Unity.  
pragma directives in HLSL | Working with `#pragma` directives in HLSL in Unity.  
Targeting shader models and GPU features in HLSL | Using `#pragma` directives to indicate that your **shader** requires certain GPU features.  
Targeting graphics APIs and platforms in HLSL | Using `#pragma` directives to target specific graphics API and platforms.  
Declaring and using shader keywords in HLSL | Using `#pragma` directives to declare shader keywords and `#if` directives to indicate that code depends on the state of shader keywords.