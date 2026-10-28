---
title: "Model tab"
category: "General"
source_file: "FBXImporter-Model.html"
doc_type: "manual"
---

# Model tab

The **Import Settings** for a **Model file** appear in the **Model** appear in the **Model** tab of the **Inspector** tab of the **Inspector** window when you select the Model. These settings affect various elements and properties stored inside the Model. Unity uses these settings to import each Asset, so you can adjust any settings to apply to different Assets in your Project.

Import settings for the Model

This section provides information about each of the sections on the Model tab:

**(A)** Scene-level properties, such as whether to import Lights and Cameras, and what scale factor to use.

**(B)** Properties specific to Meshes.

**(C)** Geometry-related properties, for dealing with topology, UVs, and normals.

## Scene

**Property** | **Function**  
---|---  
**Scale Factor** | Set this value to apply a global scale on the imported Model whenever the original file scale (from the Model file) does not fit the intended scale in your Project. Unity’s physics system expects 1 meter in the game world to be 1 unit in the imported file.  
**Convert Units** | Enable this option to convert the Model scaling defined in the Model file to Unity’s scale.  
**Bake Axis Conversion** | Enable this property to bake the results of axis conversion directly into your application’s asset data (for example, vertex or animation data) when you import a Model that uses a different axis system than Unity. Disable this property to compensate the **Transform component** of the root **GameObject** of the root **GameObject** at runtime to simulate axis conversion.  
**Import BlendShapes** | Enable this property to allow Unity to import blend shapes with your Mesh. See Importing blend shapes below for details.  
  
**Note** : Importing blend shape normals requires smoothing groups in the FBX file.  
**Import Visibility** | Import the FBX settings that define whether or not MeshRenderer components are enabled (visible). See Importing Visibility below for details.  
**Import Cameras** | Import cameras from your .FBX file. See Importing Cameras below for details.  
**Import Lights** | Import lights from your .FBX file. See Importing Lights below for details.  
**Preserve Hierarchy** | Always create an explicit prefab root, even if this model only has a single root. Normally, the FBX Importer strips any empty root nodes from the model as an optimization strategy. However, if you have multiple FBX files with portions of the same hierarchy you can use this option to preserve the original hierarchy.   
  
For example, file1.fbx contains a rig and a Mesh and file2.fbx contains the same rig but only the animation for that rig. If you import file2.fbx without enabling this option, Unity strips the root node, the hierarchies don’t match, and the animation breaks.  
**Sort Hierarchy By Name** | Enable this property to sort GameObjects by alphabetical order within the hierarchy. Disable this property to preserve the hierarchy order defined in the FBX file.  
  
### Importing blend shapes

Unity supports blend shapes (morphing) and can import blend shapes from FBX and DAE files exported from 3D modeling applications. You can also import animation from FBX files. Unity supports vertex-level animation for blend shapes on vertices, normals and tangents.

Skin and blend shapes can affect Meshes at the same time. When Unity imports Meshes containing blend shapes, it uses the SkinnedMeshRenderer component (instead of the MeshRenderer component), regardless of whether it has skin or not.

Unity imports blend shape animation as part of regular animation: it animates blend shape weights on SkinnedMeshRenderers.

Choose either of these methods to import blend shapes with normals:

  * Set the Blend Shape Normals property to **Import** so that Unity uses the normals from the FBX file. For more information, see the documentation for the Blend Shape Normals property below.

_OR_

  * Set the Blend Shape Normals property to **Calculate** so that Unity uses the same logic to calculate normals on a **Mesh**

**Note:** If you want tangents on your blend shapes then set the Tangents import setting to **Calculate**.

### Importing visibility

Unity can read visibility properties from FBX files with the **Import Visibility** property. Values and **animation curves** can enable or disable MeshRenderer components by controlling the Renderer.enabled property.

Visibility inheritance is true by default but can be overridden. For example, if the visibility on a parent Mesh is set to 0, all of the renderers on its children are also disabled. In this case, one animation curve is created for each child’s `Renderer.enabled` property.

Some 3D modeling applications either do not support or have limitations regarding visibility properties. For more information, see:

  * Limitations on importing Models into Unity from Autodesk® Maya®
  * Limitations on importing Models into Unity from Blender

### Importing cameras

Unity supports the following properties when importing Cameras from an .FBX file:

**Property:** | **Function:**  
---|---  
**Projection** mode | Orthographic or perspective. Does not support animation.  
**Field of View** | Supports animation.  
All **Physical Camera** properties | If you import a Camera with Physical Properties (for example, from Maya), Unity creates a Camera with the **Physical Camera** property enabled and the **Focal Length** , **Sensor Type** , **Sensor Size** , **Lens Shift** , and **Gate Fit** values from the FBX file.  
**_Note:_** Not all 3D modeling applications have a concept of _Gate Fit_. When not supported by the 3D modeling application, the default value in Unity is **None**.  
**Near** and **Far** **Clipping Plane** distance | Unity does not import any animation on these properties. When exporting from 3ds Max, enable the **Clip Manually** setting; otherwise the default values are applied on import.  
**Target Cameras** | If you import a Target Camera, Unity creates a camera with a LookAt constraint using the target object as the source.  
  
### Importing lights

The following Light types are supported:

  * Omni
  * Spot
  * Directional
  * Area

The following Light properties are supported:

**Property:** | **Function:**  
---|---  
**Range** | The **FarAttenuationEndValue** is used if **UseFarAttenuation** is enabled. **FarAttenuationEndValue** does not support animation.  
**Color** | Supports animation.  
**Intensity** | Supports animation.  
**Spot Angle** | Supports animation. Only available for Spot Lights.  
  
**Note** : In 3ds Max, the exported default value is the value of the property at the current selected frame. To avoid confusion, move the playhead to frame 0 when exporting.

#### Limitations

Some 3D modeling applications apply scaling on light properties. For instance, you can scale a Spot Light by its hierarchy and affect the light cone. Unity does not do this, which may cause lights to look different in Unity.

The FBX format does not define the width and height of area lights. Some 3D modeling applications don’t have this property and only allow you to use scaling to define the rectangle or disc area. Because of this, area lights always have a size of 1 when imported.

Targeted light animations are not supported unless their animation is baked.

## Meshes property section

**Property** | **Function**  
---|---  
**Mesh Compression** | Set the level of compression ratio to reduce the file size of the Mesh. Increasing the compression ratio lowers the precision of the Mesh by using the mesh bounds and a lower bit depth per component to compress the mesh data.  
  
It’s best to turn it up as high as possible without the Mesh looking too different from the uncompressed version. This is useful for optimizing game size.  
| **Off** | Don’t use **compression**.  
| **Low** | Use a low compression ratio.  
| **Medium** | Use a medium compression ratio.  
| **High** | Use a high compression ratio.  
**Read/Write Enabled** | When you enable this option, Unity uploads the Mesh data to GPU-addressable memory, but also keeps it in CPU-addressable memory. This means that Unity can access the Mesh data at run time, and you can access it from your scripts. For example, you might want to do this if you’re generating a Mesh procedurally, or if you want to copy some data from a Mesh.   
  
When this option is disabled, Unity uploads the Mesh data to GPU-addressable memory, and then removes it from CPU-addressable memory.   
  
By default, this option is disabled. In most cases, to save runtime memory usage, leave this option disabled. For information on when to enable Read/Write Enabled, see Mesh.isReadable.  
**Optimize Mesh** | Determine the order in which triangles are listed in the Mesh for better GPU performance.  
| **Nothing** | No optimization.  
| **Everything** | Let Unity reorder the vertices and indices for both polygons and vertices. This is the default.  
| **Polygon Order** | Reorder only the polygons.  
| **Vertex Order** | Reorder only the vertices.  
**Generate Colliders** | Enable to import your Meshes with Mesh **Colliders** automatically attached. This is useful for quickly generating a **collision** automatically attached. This is useful for quickly generating a **collision** Mesh for environment geometry, but should be avoided for geometry you are moving.  
  
## Geometry properties section

**Property** | **Function**  
---|---  
**Keep Quads** | Enable this to stop Unity from converting polygons that have four vertices to triangles. For example, if you are using Tessellation Shaders, you may want to enable this option because tessellating quads may be more efficient than tessellating polygons.   
  
Unity can import any type of polygon (triangle to N-gon). Polygons that have _more_ than four vertices are always converted to triangles regardless of this setting. However, if a mesh has quads and triangles (or N-gons that get converted to triangles), Unity creates two submeshes to separate quads and triangles. Each submesh contains either triangles only or quads only.   
  
**Tip:** If you want to import quads into Unity from 3ds Max, you have to export it as an Editable Poly.  
**Weld Vertices** | Combine vertices that share the same position in space, provided that they share the same properties overall (including, UVs, Normals, Tangents, and VertexColor).   
  
This optimizes the vertex count on Meshes by reducing their overall number. This option is enabled by default.   
  
In some cases, you might need to switch this optimization off when importing your Meshes. For example, if you intentionally have duplicate vertices which occupy the same position in your Mesh, you may prefer to use scripting to read or manipulate the individual vertex and triangle data.  
**Index Format** | Define the size of the Mesh index buffer.   
  
**Note:** For bandwidth and memory storage size reasons, you generally want to keep **16 bit** indices as default, and only use **32 bit** when necessary, which is what the **Auto** option uses.  
| **Auto** | Let Unity decide whether to use 16 or 32 bit indices when importing a Mesh, depending on the Mesh vertex count. This is the default for Assets added in Unity 2017.3 and onwards.  
| **16 bit** | Use 16 bit indices when importing a Mesh. If the Mesh is larger, then it is split into <64k vertex chunks. This was the default setting for Projects made in Unity 2017.2 or previous.  
| **32 bit** | Use 32 bit indices when importing a Mesh. If you are using GPU-based rendering pipelines (for example with compute shader triangle culling), using 32 bit indices ensures that all Meshes use the same index format. This reduces **shader** complexity, because they only need to handle one format.  
**Legacy Blend Shape Normals** | Enable this option to compute normals based on the **Smoothing Angle** value.  
**Normals** | Defines if and how normals should be calculated. This is useful for optimizing game size.  
| **Import** | Import normals from the file. This is the default option. If the file doesn’t contain normals, they will be calculated.  
| **Calculate** | Calculate normals based on **Normals Mode** , **Smoothness Source** , and **Smoothing Angle** (below).  
| **None** | Disable normals. Use this option if the Mesh is neither normal mapped nor affected by real-time lighting.  
**Blend Shape Normals** | Defines if and how Unity should calculate normals for blend shapes. This value should match the value for the **Normals** property.  
  
This property is only visible when **Legacy Blend Shape Normals** is disabled.  
| **Import** | Import normals from the file. If the blend shape does not contain normals, the FBX SDK uses its own method to calculate normals, resulting in normal values that usually differ from the normal values that Unity creates with the **Calculate** option.  
| **Calculate** | Calculate normals based on **Normals Mode** , **Smoothness Source** , and **Smoothing Angle** (below).  
| **None** | The blend shape normals do not contribute to the base shape.  
**Normals Mode** | Define how the normals are calculated by Unity. This is only available when **Normals** is set to **Calculate** or **Import**.  
| **Unweighted Legacy** | The legacy method of computing the normals (prior to version 2017.1). In some cases it gives slightly different results compared to the current implementation. It is the default for all FBX **prefabs** imported before the migration of the Project to the latest version of Unity.  
| **Unweighted** | The normals are not weighted.  
| **Area Weighted** | The normals are weighted by face area.  
| **Angle Weighted** | The normals are weighted by the vertex angle on each face.  
| **Area and Angle Weighted** | The normals are weighted by both the face area and the vertex angle on each face. This is the default option.  
**Smoothness Source** | Set how to determine the smoothing behavior (which edges should be smooth and which should be hard).  
  
This property is only visible when **Legacy Blend Shape Normals** is disabled.  
| **Prefer Smoothing Groups** | Use smoothing groups from the Model file, where possible.  
| **From Smoothing Groups** | Use smoothing groups from the Model file only.  
| **From Angle** | Use the **Smoothing Angle** value to determine which edges should be smooth.  
| **None** | Don’t split any vertices at hard edges.  
**Smoothing Angle** | Control whether vertices are split for hard edges: typically higher values result in fewer vertices.   
  
**Note:** Use this setting only on very smooth organics or very high poly models. Otherwise, you are better off manually smoothing inside your 3D modeling software and then importing with the **Normals** option set to **Import** (above). Since Unity bases hard edges on a single angle and nothing else, you might end up with smoothing on some parts of the Model by mistake.  
  
Only available if **Normals** is set to **Calculate**.  
**Tangents** | Define how vertex tangents should be imported or calculated. This is only available when **Normals** is set to **Calculate** or **Import**.  
| **Import** | Import vertex tangents from FBX files if **Normals** is set to **Import**. If the Mesh has no tangents, it won’t work with normal-mapped shaders.  
| **Calculate Tangent Space** | Calculate tangents using MikkTSpace. This is the default option if **Normals** is set to **Calculate**.  
| **Calculate Legacy** | Calculate tangents with legacy algorithm.  
| **Calculate Legacy - Split Tangent** | Calculate tangents with legacy algorithm, with splits across UV charts. Use this if **normal map** lighting is broken by seams on your Mesh. This usually only applies to characters.  
| **None** | Don’t import vertex tangents. The Mesh has no tangents, so this doesn’t work with normal-mapped shaders.  
**Swap UVs** | Swap UV channels in your Meshes. Use this option if your diffuse Texture uses UVs from the **lightmap**. Unity supports up to eight UV channels but not all 3D modeling applications export more than two.  
**Generate Lightmap UVs** | Creates a second UV channel for Lightmapping. See documentation on generating lightmap UVs for more information.  
  
* * *

  * **Normals Mode** , **Light** and **Camera** import options added in Unity 2017.1 NewIn20171
  * **Materials** tab added in 2017.2 NewIn20172
  * **Index Format** property added in 2017.3 NewIn20173
  * Updated description of read/write enabled setting and reorganized properties table, to match improvements in Unity 2017.3 NewIn20173
  * Added **Legacy Blend Shape Normals** and **Sort Hierarchy By Name** properties in Unity 2019.3 NewIn20193