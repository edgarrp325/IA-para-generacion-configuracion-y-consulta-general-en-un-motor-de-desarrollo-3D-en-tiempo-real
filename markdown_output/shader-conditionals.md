---
title: "Conditionals in shaders"
category: "General"
source_file: "shader-conditionals.html"
doc_type: "manual"
---

# Conditionals in shaders

Sometimes, you want the same **shader** to do different things under different circumstances. For example, you might want to configure different settings for different materials, define functionality for different hardware, or dynamically change the behavior of shaders at runtime. You might also want to avoid executing computationally expensive code when it’s not needed, such as texture reads, vertex inputs, interpolators, or loops.

You can use conditionals to define behavior that the GPU only executes under certain conditions.

## Different types of conditionals

To use conditionals in your shader, you can use the following approaches:

  * Static branching: the shader compiler evaluates conditional code at compile time.
  * Dynamic branching: the GPU evaluates conditional code at runtime.
  * Shader variants: Unity uses static branching to compile the shader source code into multiple shader programs. Unity then uses the shader program that matches the conditions at runtime.

## When to use which type of conditional

There is no “one size fits all” approach to conditionals in shaders, and you should consider the advantages and disadvantages of each approach for a given shader, in a given project.

Which conditional to use depends on when you need the shader to switch to a different code branch:

  * Only while you’re editing.
  * During runtime.

### Switch code branch while you’re editing

If you don’t need a shader to switch to a different code branch at runtime, you can use conditionals that Unity only evaluates while you’re editing.

For example you can set up a property in a Material’s **Inspector** window to make a shader do the following:

  * Add specular reflections to some instances of a material but not others.
  * Add a different look to certain objects, such as objects that appear in underwater **scenes**.

If you use this approach, shader code is simpler to write and maintain, and less likely to affect build time, file size and performance.

To do this, use one of the following:

  * Shader variants: Use `shader_feature` to declare keywords and evaluate them in `if` statements.
  * Static branching: Use preprocesser constants and macros.

If you use the `shader_feature` keyword definition, Unity keeps shader variants used by Materials in your build, and removes (‘strips’) other shader variants. This keeps build times low and file sizes small.

Avoid using a C# script to enable or disable `shader_feature` keywords at runtime, because if a Material uses a shader variant that’s missing, Unity chooses a different available variant instead. If you do need to enable or disable keywords at runtime, use one of the following approaches to make sure your build includes all the variants you need:

  * Include a shader variant collection with the shader variants you need in the list of preloaded shaders.
  * Include a Material in your build for every combination of `shader_feature` keywords you want to use.

### Switch code branch at runtime

If you need to use C# scripting to make the shader switch to a different code branch at runtime, you can use conditionals that Unity evaluates both while you’re editing and at runtime.

For example you can use a C# script to make a shader do the following:

  * Change a Material dynamically so it has snow on it at certain times.
  * Change a Material when a user changes quality settings, for example to give users dynamic control over whether fog appears.

To do this, use one of the following:

  * Shader variants: Use `multi_compile` to declare keywords and evaluate them in `if` statements.
  * Dynamic branching.

If you use the `multi_compile` keyword definition, Unity builds a shader variant for every possible combination of shader code branches, including combinations that aren’t used by Materials in your build. This means you can enable and disable keywords at runtime, but it might also greatly increase build time, file size, load times and memory usage. See shader variants.

Dynamic branching doesn’t create shader variants, but may mean your shaders run more slowly on the GPU, especially if any of the following are true:

  * Your shaders run on a less capable GPU.
  * Your conditional code has ‘asymmetric branches’, where one branch is longer or more complex code than the other.

You can check how many shader variants you have to see whether you can use dynamic branching without affecting GPU performance too much. See shader branching for more on the advantages and disadvantages of dynamic branching.