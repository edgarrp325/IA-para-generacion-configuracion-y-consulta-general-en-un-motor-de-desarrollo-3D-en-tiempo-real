---
title: "Using shader keywords with C# scripts"
category: "General"
source_file: "shader-keywords-scripts.html"
doc_type: "manual"
---

# Using shader keywords with C# scripts

You can enable or disable **shader** keywords. When you enable or disable a shader keyword, the shader displays the appropriate conditional behavior. Depending on whether the keyword works with shader variants or dynamic branching, this means that either Unity renders the appropriate shader variant, or the GPU executes the appropriate branch.

This page contains the following information:

  * Local and global shader keywords
  * Shader variants or dynamic branching
  * Enabling and disabling shader keywords
  * Managing sets of keywords at runtime

## Local and global shader keywords

When Unity represents shader keywords in C#, it uses the concept of **local shader keywords** and **global shader keywords**.

Local shader keywords comprise all keywords that you declare in shader source files. Local shader keywords affect an individual shader or compute shader. Local keywords can have local or global scope, which affects whether they can be overridden by global shader keywords.

Global shader keywords act as overrides for local shader keywords. You don’t declare these in shader source files; they exist only in C# code. Global shader keywords can affect multiple shaders and compute shaders at the same time.

### Local shader keywords

When you declare a shader keyword in a shader source file, Unity represents this in C# with a LocalKeyword struct. This is called a **local shader keyword**.

The isOverridable property of a `LocalKeyword` indicates whether the keyword was declared with a global or local scope in the source file. It is `true` if the keyword was declared with global scope and can therefore be overridden by a global shader keyword with the same name. It is `false` if the keyword was declared with local scope, and therefore cannot be overridden by a global shader keyword with the same name.

Unity stores all local shader keywords that affect a shader or compute shader in a LocalKeywordSpace struct. For a graphics shader, you can access this with Shader.keywordSpace. For a compute shader, you can access this with ComputeShader-keywordSpace.

### Global shader keywords

In addition to the local shader keywords that you declared in your source files, Unity maintains a separate list of **global shader keywords**. You don’t declare these in shader source files; instead, they are runtime overrides for local shader keywords that you work with in C#. Global shader keywords can affect multiple shaders and compute shaders at the same time.

Unity represents a global shader keyword with a GlobalKeyword struct.

Setting a global shader keyword can be convenient when you need to enable or disable the same shader keyword for many materials and compute shaders. However, it has the following potential downsides:

  * Setting the global state of keywords can lead to unintended consequences if shaders accidentally define a keyword with the same name. You can guard against this by declaring keywords with local scope, or by naming keywords in a way that reduces the likelihood of clashes.
  * When you create a new `GlobalKeyword`, Unity updates its internal mapping between global and local keyword space for all shaders and compute shaders loaded at this point. This can be a CPU-intensive operation. To reduce the impact of this operation, try to create all global keywords shortly after application startup, while your application is loading.

### How local and global shader keywords interact

When a global and local shader keyword with the same name have different states, Unity uses the `isOverridable` property of a `LocalKeyword` to determine whether the keyword is enabled or disabled for an individual material or compute shader. `isOverridable` is true if the keyword was declared with global scope, and `false` if it was declared with local scope.

  * When `isOverridable` is `true`: If a global keyword with the same name exists and is enabled, Unity uses the state of the global keyword. Otherwise, Unity uses the state of the local keyword.
  * When `isOverridable` is `false`: Unity always uses the state of the local keyword.

Therefore, to understand whether a shader keyword is enabled or disabled for an individual material or compute shader, you must examine the state of the `isOverridable` property and the global and/or local keyword state.

This example demonstrates how to check whether Unity considers a keyword enabled or disabled for a material:
    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    
    public class KeywordExample : MonoBehaviour
    {
        public Material material;
    
        void Start()
        {
            CheckShaderKeywordState();
        }
    
        void CheckShaderKeywordState()
        {
            // Get the instance of the Shader class that the material uses
            var shader = material.shader;
    
            // Get all the local keywords that affect the Shader
            var keywordSpace = shader.keywordSpace;
    
            // Iterate over the local keywords
            foreach (var localKeyword in keywordSpace.keywords)
            {
                // If the local keyword is overridable (i.e., it was declared with a global scope),
                // and a global keyword with the same name exists and is enabled,
                // then Unity uses the global keyword state
                if (localKeyword.isOverridable && Shader.IsKeywordEnabled(localKeyword.name))
                {
                    Debug.Log("Local keyword with name of " + localKeyword.name + " is overridden by a global keyword, and is enabled");
                }
                // Otherwise, Unity uses the local keyword state
                else
                {
                    var state = material.IsKeywordEnabled(localKeyword) ? "enabled" : "disabled";
                    Debug.Log("Local keyword with name of " + localKeyword.name + " is " + state);
                }            
            }
        }
    }
    
    

## Shader variants or dynamic branching

In Unity, you can use shader keywords with shader variants, or you can use them with dynamic branching. You decide when you declare the keywords.

The isDynamic property of a `LocalKeyword` indicates whether the keyword was declared for use with dynamic branching in the shader source file. It is `true` if the keyword was declared for use with dynamic branching, and `false` if it was declared for use with shader variants.

## Enabling and disabling shader keywords

To check whether a local keyword is enabled for a graphics shader, use Material.IsKeywordEnabled or Material.EnableKeyword. For a compute shader, use ComputeShader.IsKeywordEnabled, or ComputeShader.EnableKeyword.

To check whether a global keyword is enabled, use Shader.IsKeywordEnabled or Shader.EnableKeyword or ComputeShader.enabledKeywords.

To enable or disable a local shader keyword for a graphics shader, use Material.SetKeyword, Material.EnableKeyword, or Material.DisableKeyword. For a compute shader, use ComputeShader.SetKeyword, ComputeShader.EnableKeyword, or ComputeShader.DisableKeyword.

To enable or disable a global shader keyword, use Shader.SetKeyword, ComputeShader.EnableKeyword, or ComputeShader.DisableKeyword.

To enable or disable a local or global keyword with a Command Buffer, use CommandBuffer.EnableKeyword, or CommandBuffer.DisableKeyword .

**Note:** When you enable or disable keywords that work with shader variants, Unity uses different shader variants. Changing shader variants at runtime can impact performance. If a change in keywords requires a variant to be used for the first time, it can lead to hitches while the graphics driver prepares the shader program. This can be a particular problem for large or complex shaders, or if a global keyword state change affects multiple shaders. To avoid this, if you use keywords with shader variants, ensure that you consider keyword variants in your shader loading and prewarming strategy. For more information, see Shader loading. 

## Managing sets of keywords at runtime

When you author your shader, you declare keywords in sets. A set contains mutually-exclusive keywords.

At runtime, Unity has no concept of these sets. It allows you to enable or disable any keyword independently, and enabling or disabling a keyword has no effect on the state of any other keyword. This means that it is possible to enable multiple keywords from the same set, or disable all the keywords in a set.

If you use keywords with shader variants, when more than one keyword in a set is enabled or no keywords in a set are enabled, Unity chooses a variant that it considers a “good enough” match. There is no guarantee about what exactly happens, and it can lead to unintended results. It is best to avoid this situation by managing keyword state carefully.

If you use keywords with dynamic branching, when more than one keyword in a set is enabled or no keywords in a set are enabled, the conditional branches execute accordingly. For example, if both `KEYWORD_A` and `KEYWORD_B` are enabled, the branches for `if (KEYWORD_A)` and `if (KEYWORD_B)` will both execute.