---
title: "Billboard asset"
category: "General"
source_file: "class-BillboardAsset.html"
doc_type: "manual"
---

# Billboard asset

Switch to Scripting

A **Billboard** asset is a collection of pre-rendered images of a **mesh** asset is a collection of pre-rendered images of a **mesh**. Use it with the Billboard Renderer to an object that is distant from the **Camera**. Use it with the Billboard Renderer to an object that is distant from the **Camera** at a low level of detail (LOD).

The most common way to generate a Billboard Asset is to create files in SpeedTree Modeler, and then import them into Unity.

It is also possible to create your own Billboard Assets from script. For more information, see the API reference for BillboardAsset.

Property | Description  
---|---  
**Width** | The width of the billboard.  
**Height** | The height of the billboard.  
**Bottom** | The amount to offset the billboard at the bottom.  
**Images** | The texture coordinates that represent the billboard images in the texture atlas.  
**Vertices** | The vertex data of the billboard mesh.  
**Indices** | The triangle indices of the billboard mesh.  
**Material** | The material Unity uses to render the billboard.  
  
BillboardAsset