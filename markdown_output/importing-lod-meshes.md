---
title: "Importing LOD Meshes"
category: "General"
source_file: "importing-lod-meshes.html"
doc_type: "manual"
---

# Importing LOD Meshes

You can create meshes with different levels of detail in an external 3D application for use with Unity’s LOD system. If you name these meshes correctly, Unity automatically creates and configures a **GameObject** with LOD group component for them when it imports the Model.

To import a Model with **LOD** level into Unity, you must do the following:

  1. In your external 3D application, follow the application’s process to create as many LOD meshes as you need.

  2. Name the meshes according to the following naming convention: 
     * ExampleMeshName_LOD0 for the first LOD level (i.e., the most detailed version)
     * ExampleMeshName_LOD1
     * ExampleMeshName_LOD2
  3. Export your Model as an FBX file. Alternatively, if you are using Maya, export the mesh group directly into Unity; to do this, go to **File > Send to Unity > Selection.**

  4. Import the FBX into Unity. Unity recognizes the grouped Meshes and naming convention, and automatically creates an LOD Group component with the appropriate settings. 

## Additional information

To learn more about importing models, see Importing models.

To learn more about creating and exporting LOD Meshes in Maya, follow the Unity tutorial Creating LODs in Maya.