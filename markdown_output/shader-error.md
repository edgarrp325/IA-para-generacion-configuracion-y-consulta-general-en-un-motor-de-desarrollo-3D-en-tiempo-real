---
title: "Error and loading shaders"
category: "General"
source_file: "shader-error.html"
doc_type: "manual"
---

# Error and loading shaders

Sometimes, Unity can’t render objects with regular **shaders**. When this happens, Unity renders the objects with special shaders:

  * The default error shader
  * The loading shader
  * The Streaming Virtual Texturing error material

The special shader that Unity uses depends on the reason that Unity can’t use the original shader.

## The default error shader

Unity renders an object with the default error shader when there’s a problem with that object’s material or shader; for example, if no material is assigned, if the shader doesn’t compile, or if the shader isn’t supported.

Unity uses the default error shader in the Unity Editor, and in builds.

The default error shader is magenta (bright pink).

The magenta error shader.

When you use the BatchRendererGroup API, Unity doesn’t display the default error shader. Use BatchRendererGroup.SetErrorMaterial to set a material to use instead.

If your project uses the Universal Rendering Pipeline (URP), Unity might render an object using the default error shader if the object uses a shader from the Built-In **Render Pipeline**. Refer to Converting your shaders for more information.

## The loading shader

Unity renders an object with the loading shader to indicate that Unity is compiling the shader variant needed to display that object.

Unity shows the loading shader in the Unity Editor when asynchronous shader compilation is enabled, or in a **development build**

The loading shader is cyan (bright blue).

The cyan loading shader.

When you use the BatchRendererGroup API, Unity doesn’t display the loading shader. Use BatchRendererGroup.SetLoadingMaterial to set a material to use instead.

## The Virtual Texturing error material

If your project uses Streaming Virtual Texturing  (SVT), Unity uses a special material to indicate problems in your SVT setup. For more information, see Virtual Texturing error material.