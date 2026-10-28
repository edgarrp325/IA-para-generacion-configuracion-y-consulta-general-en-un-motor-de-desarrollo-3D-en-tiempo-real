---
title: "Branching, variants, and keywords"
category: "General"
source_file: "shader-variants-and-keywords.html"
doc_type: "manual"
---

# Branching, variants, and keywords

Sometimes, you want the same **shader** to do different things under different circumstances. When this happens, you use conditionals to define different behavior for different hardware.

This section of the manual contains information about how shader variants and keywords work, and when and how to use them.

**Page** | **Description**  
---|---  
Conditionals in shaders | An introduction to conditionals in shaders, including information on the different types of conditional, and when to use which one.  
Branching in shaders | An introduction to static and dynamic branching in shaders.  
Shader variants | An introduction to shader variants, and information on how to understand and control how many shader variants Unity compiles.  
Check how many shader variants you have | Using logging and profiling tools to check how many shader variants Unity compiles, and identify ways you can remove (strip) variants.  
Shader keywords | An introduction to shader keywords, and information on how to use them.  
Using shader keywords with C# scripts | Working with shader keywords in C# **scripts**.  
Using shader keywords with the material Inspector | Working with shader keywords in the Unity Editor, using the material **Inspector**.  
Shader variant stripping | Preventing shader variants from being compiled to reduce build times, file size, shader loading times and runtime memory usage.  
Shader variant collections | An introduction to shader variant collections, and information on how to use them.