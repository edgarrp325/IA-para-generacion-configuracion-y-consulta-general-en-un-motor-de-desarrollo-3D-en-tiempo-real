---
title: "Importing a model"
category: "General"
source_file: "ImportingModelFiles.html"
doc_type: "manual"
---

# Importing a model

Model files can contain a variety of data, such as meshes, animation rigs and clips, materials and textures. Your file might not contain all of these elements, but you can follow any portion of the workflow that you need to:

  1. Select the file in the Project view to see the Import Settings window
  2. Set any Model-specific or general importer options
  3. Set up options for importing Rigs and Animation (not available for SpeedTree Models)
  4. Dealing with Materials and Textures
  5. Drag the file into Unity

For guidelines on how to export _Humanoid_ animation from your 3D modeling software, see Preparing Humanoid Models for export.

**Note:** Unity’s primary support for **Model files** is the FBX format. However, you can save your 3D files from most common 3D modeling software in their native format (for example, .max, .blend, .mb, .ma). When Unity finds these file types in your `Assets` folder, it calls your 3D modeling software’s FBX export **plug-in** is the FBX format. However, you can save your 3D files from most common 3D modeling software in their native format (for example, .max, .blend, .mb, .ma). When Unity finds these file types in your `Assets` folder, it calls your 3D modeling software’s FBX export **plug-in** , and imports the file. The 3D modeling software must be installed on the same computer as Unity, so in most cases it’s best practice to directly export as FBX from your application into your `Assets` folder.

## Accessing the Import Settings window

No matter what kind of data you want to extract from the Model file, you always start the same way:

  1. Open the **Project** window and the **Inspector** window and the **Inspector** so that you can see both at once.

  2. Select the **Model** file you want to import from the **Asset** file you want to import from the **Asset** folder in the **Project** window. 

The **Import Settings** window opens in the **Inspector** showing the **Model tab** by default.

## Setting Model-specific and general importer options

The options that are available for SpeedTree Models vs. other Models are very different. For example, the SpeedTree Model tab provides options mostly for setting up transitions between **LOD**

Character and animated Models provide more diverse options on their Model tab, which allow you to:

  * Use the **Scale Factor** and **Convert Units** properties to adjust how Unity interprets units. For example, 3ds Max uses 1 unit to represent 10 centimeters, whereas Unity uses 1 unit to represent 1 meter.
  * Use the **Mesh Compression** , **Read/Write Enabled** , **Optimize Mesh** , **Keep Quads** , **Index Format** , or **Weld Vertices** properties to reduce resources and save memory.
  * You can enable the **Import BlendShapes** option if the Model file came from Maya or 3ds Max, or any other 3d modeling application that supports morph target animation.
  * You can enable the **Generate Colliders** option for environment geometry.
  * You can enable specific FBX settings, such as **Import Visibility** , or **Import Cameras** and **Import Lights**.
  * For Model files that contain only Animation, you can enable the **Preserve Hierarchy** option to prevent hierarchy mismatch in your skeleton.
  * You can set the **Swap UVs** and **Generate Lightmap UVs** if you are using a **Lightmap**.
  * You can exercise control over how Unity handles the Normals and Tangents in your Model with the **Normals** , **Normals Mode** , **Tangents** , or **Smoothing Angle** options.

## Setting options for importing Rigs and Animation

If your file contains Animation data, you can follow the guidelines for setting up the Rig using the Rig tab and then extracting or defining **Animation Clips** using the Animation tab. The workflow differs between Humanoid and Generic (non-Humanoid) animation types because Unity needs the Humanoid’s bone structure to be very specific, but only needs to know which bone is the **root node** for the Generic type:

  * Humanoid-type workflow
  * Generic-type workflow

> **Note:** SpeedTree Models have neither a **Rig** nor an **Animation** tab.

## Dealing with Materials and Textures

If your file contains materials and textures, you can define how you want to deal with them:

  1. Click the Materials tab in the **Import Settings** window.
  2. From the Material Creation Mode drop-down menu, choose how you want to import the Materials from the FBX file. Unless you chose **None** , several options appear in the **Materials**
  3. Choose the **Use Embedded Materials** option to keep the Materials inside the imported Asset.
  4. When you have finished setting the options, click the **Apply** button at the bottom of the **Import Settings** window to save them or click the **Revert** button to cancel.

### Finding textures

Unity follows a specific search plan to automatically look for textures on import. First, the importer looks for a sub-folder called Textures within the same folder as the **mesh** , or in any parent folder. If this fails, Unity performs an exhaustive search of all textures in the project. Although slightly slower, the main disadvantage of the exhaustive search is that there could be two or more textures in the project with the same name. In this case, it is not guaranteed that Unity can find the right one.

Place your textures in a **Textures** folder at or above the asset’s level

**(A)** Possible places to find Textures

**(B)** Mesh being imported

### Normal maps

If you have a character with a **normal map** that was generated from a high-polygon version of the Model, you should import the game-quality version with a Smoothing Angle of 180 degrees. This prevents odd-looking seams in lighting due to tangent splitting. If the seams are still present with these settings, choose Calculate Legacy With Split Tangents from the **Tangents** drop-down menu. If you are converting a greyscale image into a normal map, you don’t need to worry about this.

## Drag the file into Unity

Finally, you can import the file into your scene:

  * If it contains a Mesh, drag the file into the **Scene** view to instantiate it as a **Prefab** view to instantiate it as a **Prefab** for a **GameObject** for a **GameObject**.
  * If it contains Animation Clips, you can drag the file into the Animator window to use in the State Machine. You can also drag the Animation take directly onto an instantiated Prefab in the **Scene view**