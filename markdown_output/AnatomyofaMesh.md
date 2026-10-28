---
title: "Mesh data"
category: "General"
source_file: "AnatomyofaMesh.html"
doc_type: "manual"
---

# Mesh data

This page contains information on the data that a mesh contains, and how Unity stores that data in the Mesh class.

## Overview

A mesh is defined by these properties:

  * Vertices: A collection of positions in 3D space, with optional additional attributes.
  * Topology: The type of structure that defines each face of the surface.
  * Indices: A collection of integers that describe how the vertices combine to create the surface, based on the topology.

In addition to this, deformable meshes contain either:

  * Blend shapes: Data that describes different deformed versions of the mesh, for use with animation.
  * Bind poses: Data that describes the “base” pose of the skeleton in a skinned mesh.

## Vertex data

The elements of vertex data are called **vertex attributes**.

Every vertex can have the following attributes:

  * Position
  * Normal
  * Tangent
  * Color
  * Up to 8 texture coordinates
  * Bone weights and blend indices (skinned meshes only)

Internally, all vertex data is stored in separate arrays of the same size. If your mesh contains an array with 10 vertex positions, it also has arrays with 10 elements for each other vertex attribute that it uses.

In C#, Unity describes the available vertex attributes with the VertexAttribute enum. You can check whether an instance of the `Mesh` class has a given vertex attribute with the Mesh.HasVertexAttribute function.

### Position

The **vertex position** represents the position of the vertex in **object space**.

Unity uses this value to determine the surface of the mesh.

This vertex attribute is required for all meshes.

In the `Mesh` class, the simplest way to access this data is with Mesh.GetVertices and Mesh.SetVertices. Unity also stores this data in Mesh.vertices, but this older property is less efficient and user-friendly.

### Normal

The **vertex normal** represents the direction that points directly “out” from the surface at the position of the vertex.

Unity uses this value to calculate the way that light reflects off the surface of a mesh.

This vertex attribute is optional.

In the `Mesh` class, the simplest way to access this data is with Mesh.GetNormals and Mesh.SetNormals. Unity also stores this data in Mesh.normals, but this older property is less efficient and user-friendly.

### Tangent

The **vertex tangent** represents the direction that points along the “u” (horizontal texture) axis of the surface at the position of the vertex.

Unity stores the vertex tangent with an additional piece of data, in a four-component vector. The x,y,z components of the vector describe the tangent, and the w component of the vector describes its orientation. Unity uses the w value to compute the **binormal** , which is the cross product of the tangent and normal.

Unity uses the tangent and binormal values in normal mapping.

This vertex attribute is optional.

In the `Mesh` class, the simplest way to access this data is with Mesh.GetTangents and Mesh.SetTangents. Unity also stores this data in Mesh.tangents, but this older property is less efficient and user-friendly.

### Texture coordinates (UVs)

A mesh can contain up to eight sets of **texture coordinates**. Texture coordinates are commonly called **UVs** , and the sets are called **channels**.

Unity uses texture coordinates when it “wraps” a texture around the mesh. The UVs indicate which part of the texture aligns with the mesh surface at the vertex position.

UV channels are commonly called “UV0” for the first channel, “UV1” for the second channel, and so on up to “UV7”. The channels respectively map to the **shader** semantics `TEXCOORD0`, `TEXCOORD1`, and so on up to `TEXCOORD7`.

By default, Unity uses the first channel (UV0) to store UVs for regular textures such as diffuse maps and specular maps. Unity can use the second channel (UV1) to store baked **lightmap** UVs, and the third channel (UV2) to store input data for real-time lightmap UVs. For more information on lightmap UVs and how Unity uses these channels, see Lightmap UVs.

All eight texture coordinate attributes are optional.

In the `Mesh` class, the simplest way to access this data is with Mesh.GetUVs and Mesh.SetUVs. Unity also stores this data in the following properties: Mesh.uv, Mesh.uv2, Mesh.uv3 and so on, up to Mesh.uv8. Note that these older properties are less efficient and user-friendly.

### Color

The **vertex color** represents the base color of a vertex, if any.

This color exists independently of any textures that the mesh may use.

This vertex attribute is optional.

In the `Mesh` class, the simplest way to access this data is with Mesh.GetColors and Mesh.SetColors. Unity also stores this data in Mesh.colors, but this older property is less efficient and user-friendly.

### Blend indices and bone weights

In a skinned mesh, **blend indices** indicate which bones affects a vertex, and **bone weights** describe how much influence those bones have on the vertex.

In Unity, these vertex attributes are stored together. 

Unity uses blend indices and bone weights to deform a skinned mesh based on the movement of its skeleton. For more information, see Skinned Mesh Renderer.

These vertex attributes are required for skinned meshes.

In the past, Unity only allowed up to 4 bones to influence a vertex. It stored this data in a BoneWeight struct, in the Mesh.boneWeights array. Now, Unity allows up to 256 bones to influence a vertex. It stores this data in a BoneWeight1 struct, and you can access it with Mesh.GetAllBoneWeights and Mesh.SetBoneWeights. For more information, read the linked API documentation.

## Topology

Topology describes the type of face that a mesh has.

A mesh’s topology defines the structure of the index buffer, which in turn describes how the vertex positions combine into faces. Each type of topology uses a different number of elements in the index array to define a single face.

Unity supports the following mesh topologies:

  * Triangle
  * Quad
  * Lines
  * LineStrip
  * Points

**Note:** The Points topology doesn’t create faces; instead, Unity renders a single point at each position. All other mesh topologies use more than one index to create either faces or edges.

In the `Mesh` class, you can get the topology with Mesh.GetTopology, and set it as a parameter of Mesh.SetIndices.

For more information on supported mesh topologies, see the documentation for the MeshTopology enum.

**Note:** You must convert any meshes that use other modelling techniques (such as NURBS or NURMS/Subdivision Surfaces modelling) into supported formats in your modelling software before you can use them in Unity.

## Index data

The index array contains integers that refer to elements in the vertex positions array. These integers are called indices. 

Unity uses the indices to connect the vertex positions into faces. The number of indices that make up each face depends on the topology of the mesh.

In the `Mesh` class, you can get this data with Mesh.GetIndices, and set it with Mesh.SetIndices. Unity also stores this data in Mesh.triangles, but this older property is less efficient and user-friendly.

**Note:** The Points topology doesn’t create faces; instead, Unity renders a single point at each position. All other mesh topologies use more than one index to create either faces or edges.

For example, for a mesh that has an index array that contains the following values:

0,1,2,3,4,5

If the mesh has a triangular topology, then the first three elements (0,1,2) identify one triangle, and the following three elements (3, 4, 5) identify another triangle. There is no limit to the number of faces that a vertex can contribute to. This means that the same vertex can appear in the index array multiple times. For example, an index array could contain these values:

0,1,2,1,2,3

If the mesh has a triangular topology, then the first three elements (0,1,2) identify one triangle, and the following three elements (1,2,3) identify another triangle that shares vertices with the first.

### Winding order

The order of the vertices in each group in the index array is called the **winding order**. Unity uses winding order to determine whether a face is front-facing or back-facing, and in turn whether it should render a face or cull it (exclude it from rendering). By default, Unity renders front-facing polygons and culls back-facing polygons. Unity uses a clockwise winding order, which means that Unity considers any face where the indices connect in a clockwise direction is front facing.

Unity’s winding order visualized on a prism

The above diagram demonstrates how Unity uses winding order. The order of the vertices in each face determines the direction of the normal for that face and Unity compares this to the forward direction of the current **camera** perspective. If the normal points away from the current camera’s forward direction, it is back-facing. The closer triangle is ordered (1, 2, 3), which is a clockwise direction in relation to the current perspective, so the triangle is front-facing. The further triangle is ordered (4, 5, 6), which from this perspective is an anti-clockwise direction, so the triangle is back-facing.

## Blend shapes

Blend shapes describe versions of the mesh that are deformed into different shapes. Unity interpolates between these shapes. You use blend shapes for morph target animation, which is a common technique for facial animation.

Blend shape data is stored as blend shape vertices. Blend shape data is “sparse”. This means that there isn’t a blend shape vertex for every mesh vertex; there is only a corresponding blend shape vertex if the mesh vertex deforms.

A blend shape vertex contains deltas for position, normal, and tangent, and an index value. The meaning of the index value depends on how you request the data.

In the `Mesh` class, you can access blend shape vertex data with Mesh.GetBlendShapeBuffer. This returns a GraphicsBuffer that provides access to the blend shape vertex data on the GPU. This method allows you to choose between two different buffers; one that orders the data by blend shape, and one that orders the data by mesh vertex. The choice of buffer determines the meaning of the index value and the layout of the data in the buffer. For more information on buffer layouts, see BlendShapeBufferLayout.

For information on using blend shapes with animations, see Working with blend shapes.

This data is optional.

## Bind poses

In a skinned mesh, the **bind pose** of a bone describes its position when the skeleton is in its default position (also called its bind pose or rest pose).

In the `Mesh` class, you can get and set this data with Mesh.bindposes. Each element contains data for the bone with the same index.

This data is required for skinned meshes.