---
title: "Sprite Atlas"
category: "General"
source_file: "sprite-atlas.html"
doc_type: "manual"
---

# Sprite Atlas

A 2D project uses **sprites** and other graphics to create the visuals of its **scenes** and other graphics to create the visuals of its **scenes**. This means a single project can contain many texture files. Unity typically issues a draw call for each texture in the scene; however, in a project with many textures, multiple draw calls become resource-intensive and can negatively impact the performance of your project.

A **Sprite Atlas** is an asset that consolidates several textures into a single combined texture. Unity can call this single texture to issue a single draw call instead of multiple draw calls to access the packed textures all at once at a smaller performance overhead. You can use the Sprite Atlas API to control loading the Sprite Atlases at your project’s runtime.

**Topic** | **Description**  
---|---  
**Sprite Atlas properties reference** | Refer to the properties of the Sprite Atlas.  
**Master and Variant Sprite Atlases** | Choose the Type property for a Sprite Atlas.  
**Sprite Atlas Workflow** | Follow the general workflow to create a Sprite Atlas.  
**Preparing Sprite Atlases for distribution** | Learn how to distribute Sprite Atlases.  
**Sprite Packer** | Use the legacy **Sprite Packer**.  
**Sprite Packer Modes** | Choose the default packing behavior for a Sprite Atlas.  
**Sprite Atlas V2** | Use the Sprite Atlas V2 mode.