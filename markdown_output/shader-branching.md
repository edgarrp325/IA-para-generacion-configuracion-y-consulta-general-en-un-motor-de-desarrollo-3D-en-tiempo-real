---
title: "Branching in shaders"
category: "General"
source_file: "shader-branching.html"
doc_type: "manual"
---

# Branching in shaders

Branching is one way of introducing conditional behavior into **shader** code. 

This page contains information on the following techniques:

  * Static branching
  * Dynamic branching

For a general overview of conditionals in shader code and when to use which technique, see Conditionals in shader code.

## Static branching

When a shader program includes conditionals that are evaluated at compile time, it uses static branching. The compiler excludes the code from the unused branch, so it does not appear in the compiled shader program.

Internally, Unity uses static branching when it creates shader variants. Static branching on its own does not have any of the performance disadvantages of shader variants.

### Advantages and disadvantages of static branching

The main advantage of static branching is that it has no negative impact on runtime performance. The main disadvantage of static branching is that you can only use it at compile time.

Static branching means that the compiler excludes unneeded code from the shader program. It results in small, specialized shader programs that contain only the necessary code. There is no runtime performance cost to static branching; in fact, the smaller programs are likely to result in quicker load times and lower runtime memory usage.

To use static branching, the conditions must be constant at compile time. This means that you can’t use it to execute code for different conditions at runtime.

### How to use static branching

You can use static branching in your shaders in the following ways:

  * In hand-coded shaders: 
    * Use `#if`, `#elif`, `#else`, and `#endif` preprocessor directives, or `#ifdef` and `#ifndef` preprocessor directives to create static branches.
    * Use an if statement that evaluates a compile-time constant value. Although `if` statements can also be used for dynamic branches, the compiler detects the compile-time constant value and creates a static branch instead.
    * Unity provides built-in macros for some compile-time constants that you can use with static branches.

**Note:** In Shader Graph, you can use keywords only with static branching. To use dynamic branching in a shader graph, refer to Shader keywords.

## Dynamic branching

When a shader program includes conditionals that are evaluated at runtime, it uses dynamic branching.

There are two types of dynamic branching: dynamic branching based on uniform variables, and dynamic branching based on any other runtime value. Uniform-based branching is usually more efficient, because the uniform value is constant for the whole draw call.

You can use shader keywords for dynamic branching. This allows you to use C# **scripts** and the Material **Inspector** to configure runtime branching behavior for your shaders. This results is uniform-based branching; when you do this, Unity compiles the shader keywords as uniforms.

### Advantages and disadvantages of dynamic branching

The main advantage of dynamic branching is that it allows you to use conditionals at runtime without increasing the number of shader variants in your project. The main disadvantage of dynamic branching is that it impacts GPU performance.

The GPU performance impact varies by hardware, and by shader code. The reasons are:

  * Branching based on non-uniform variables means that the GPU must either perform different operations at the same time (and therefore break parallelism), or “flatten the branch” and maintain parallelism by performing the operations for both branches and then discarding one result. Branching based on uniform variables means that the GPU must flatten the branch. Both of these approaches result in reduced GPU performance.
  * For any type of dynamic branching, the GPU must allocate register space for the worst case. If one branch is much more costly than the other, this means that the GPU wastes register space. This can lead to fewer invocations of the shader program in parallel, which reduces performance.

In general, if your code branches on uniform values and both branches have roughly similar workloads, then the impact on GPU performance is likely to be small. However, you should always profile your application and consider the advantages and disadvantages case-by-case.

**Note:** Dynamic branching can also lead to large shader programs, because the code for all conditions is compiled into the same shader program. However, the effect of these larger files on load times and memory usage is usually less significant than the impact of shader variants.

For information about other ways of using conditionals in shaders, and how to decide which technique is right for your use case, see Conditionals in shaders.

### How to use dynamic branching

You can use dynamic branching in your shaders in the following ways:

  * In hand-coded shaders: 
    * **Optional** : Set up shader keywords for use with with dynamic branching. You can use dynamic branching without shader keywords, but this provides simple set up and per-material configuration.
    * Use an if statement that evaluates the shader keywords (if used) or any other runtime state. You can use attributes to force the GPU to execute both branches, or to execute only one branch.
  * In Shader Graph, use a Branch Node. This always executes both branches.