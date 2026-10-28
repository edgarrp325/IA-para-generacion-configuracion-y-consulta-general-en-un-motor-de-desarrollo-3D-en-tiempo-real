---
title: "Rendering Mode"
category: "General"
source_file: "StandardShaderMaterialParameterRenderingMode.html"
doc_type: "manual"
---

# Rendering Mode

A Standard Shader material with default Properties and no values or textures assigned. The Rendering Mode Property is highlighted.

The first Material Parameter in the Standard **Shader** is **Rendering Mode**. This allows you to choose whether the object uses transparency, and if so, which type of blending mode to use.

  * **Opaque** \- Is the default, and suitable for normal solid objects with no transparent areas.

  * **Cutout** \- Allows you to create a transparent effect that has hard edges between the opaque and transparent areas. In this mode, there are no semi-transparent areas, the texture is either 100% opaque, or invisible. This is useful when using transparency to create the shape of materials such as leaves, or cloth with holes and tatters.

  * **Transparent** \- Suitable for rendering realistic transparent materials such as clear plastic or glass. In this mode, the material itself will take on transparency values (based on the texture’s alpha channel and the alpha of the tint colour), however reflections and lighting highlights will remain visible at full clarity as is the case with real transparent materials.

  * **Fade** \- Allows the transparency values to entirely fade an object out, including any specular highlights or reflections it may have. This mode is useful if you want to animate an object fading in or out. It is not suitable for rendering realistic transparent materials such as clear plastic or glass because the reflections and highlights will also be faded out.

## Changing the Rendering Mode using a script

When you change the **Rendering Mode** , Unity applies a number of changes to the Material. There is no single C# API to change the Rendering Mode of a Material, but you can make the same changes in your code.

To see the changes that Unity makes when you change the **Rendering Mode** :

  1. Download the source code for Unity’s built-in shaders. See Make your own shader for instructions.
  2. Open the file _StandardShaderGUI.cs_.
  3. Locate the area of the file that looks like this, and observe the changes for each **Rendering Mode**.

    
    
    switch (blendMode)
            {
                case BlendMode.Opaque:
                   // Changes associated with Opaque Rendering Mode are here
                    break;
                case BlendMode.Cutout:
                    // Changes associated with Cutout Rendering Mode are here
                    break;
                case BlendMode.Fade:
                    // Changes associated with Fade Rendering Mode are here
                    break;
                case BlendMode.Transparent:
                    // Changes associated with Transparent Rendering Mode are here
                    break;
            }
    
    

The helmet visor in this image is rendered using the Transparent mode, because it is supposed to represent a real physical object that has transparent properties. Here the visor is reflecting the skybox in the scene.  These windows use Transparent mode, but have some fully opaque areas defined in the texture (the window frames). The Specular reflection from the light sources reflects off the transparent areas and the opaque areas. The hologram in this image is rendered using the Fade mode, because it is supposed to represent an opaque object that is partially faded out. The grass in this image is rendered using the Cutout mode. This gives clear sharp edges to objects which is defined by specifying a cut-off threshold. All parts of the image with the alpha value above this threshold are 100% opaque, and all parts below the threshold are invisible. To the right in the image you can see the material settings and the alpha channel of the texture used.