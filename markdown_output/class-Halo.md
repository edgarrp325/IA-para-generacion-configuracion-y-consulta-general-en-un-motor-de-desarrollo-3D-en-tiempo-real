---
title: "Halo component"
category: "General"
source_file: "class-Halo.html"
doc_type: "manual"
---

# Halo component

Halos are glowing areas around light sources. Use them to give the impression of small dust particles in the air, and add atmosphere to your **scene**. 

A Light with a separate Halo **Component**

**Note:** This workflow is compatible only with the Built-in Render Pipelne. For similar functionality in other **render pipelines** , see Lens flares and halos.

## Using Halo components

Add a Halo component to a **GameObject** with a Light component. Then set its size and color properties to give the desired glowing effect.

**Note:** A Light can also display a halo without a separate Halo component by enabling its _Draw Halo_ property, but you cannot configure its size and color.

To see Halos in the scene view, check **Fx** button in the **Scene View** **Toolbar** **Toolbar**.

To override the **shader** used for Halos, open the Graphics window and set **Light Halo** to the shader that you would like to use as the override.

## Halo component refence

**_Property:_** | **_Function:_**  
---|---  
**Color** | Color of the Halo.  
**Size** | Size of the Halo.  
  
Halo