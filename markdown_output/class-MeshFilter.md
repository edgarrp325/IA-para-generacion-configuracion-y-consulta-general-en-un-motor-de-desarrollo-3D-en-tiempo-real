---
title: "Mesh Filter component"
category: "General"
source_file: "class-MeshFilter.html"
doc_type: "manual"
---

# Mesh Filter component

Switch to Scripting

A **Mesh Filter** component holds a reference to a mesh. It works with a Mesh Renderer component on the same **GameObject** component on the same **GameObject** ; the Mesh Renderer renders the mesh that the Mesh Filter references.

To render a deformable mesh, use a Skinned Mesh Renderer instead. A Skinned Mesh Renderer component does not need a Mesh Filter component.

## Mesh Filter Inspector reference

**_Property:_** | **_Function:_**  
---|---  
**Mesh** | A reference to a mesh asset.  
  
To change the mesh asset that the Mesh Filter component references, use the picker (circle icon) next to the mesh’s name.  
  
**Note:** The settings for other components on this GameObject don’t change when you change the mesh that the Mesh Filter references. For example, a Mesh Renderer doesn’t update its settings, which might cause Unity to render the mesh with unexpected properties. If this happens, adjust the settings of the other components as needed.  
  
Corresponds to the MeshFilter.mesh property.  
  
MeshFilter