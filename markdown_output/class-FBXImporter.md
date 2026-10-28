---
title: "Model Import Settings window"
category: "General"
source_file: "class-FBXImporter.html"
doc_type: "manual"
---

# Model Import Settings window

The FBX Model Import Settings window

**Note:** These settings are for importing Models and animations created in most 3D modeling applications. However, Models created in SketchUp and SpeedTree use specialized settings. For more information, see SketchUp Settings, and SpeedTree Import Settings. 

When you put **Model files** in the Assets folder under your Unity Project, Unity automatically imports and stores them as Unity Assets. To view the import settings in the **Inspector** in the Assets folder under your Unity Project, Unity automatically imports and stores them as Unity Assets. To view the import settings in the **Inspector** window, click on the file in the **Project** window, click on the file in the **Project** window. You can customize how Unity imports the selected file by setting the properties on four tabs on this window:

  
A 3D Model can represent a character, a building, or a piece of furniture. In these cases, Unity creates multiple Assets from a single model file. In the Project window, the main imported object is a model **Prefab**. Usually there are also several **Mesh**. Usually there are also several **Mesh** objects that the model Prefab references.

  
A Rig (sometimes called a _skeleton_) comprises a set of deformers arranged in a hierarchy that animate a Mesh (sometimes called _skin_) on one or more models created in a 3D modeling application such as as Autodesk® 3ds Max® or Autodesk® Maya®. For **Humanoid** and **Generic** (non-humanoid) Models, Unity creates an **Avatar** to reconcile the imported Rig with the Unity **GameObject** to reconcile the imported Rig with the Unity **GameObject**.

  
You can define any series of different poses occurring over a set of frames, such as walking, running, or even idling (shifting from one foot to the other) as an Animation Clip. You can reuse clips for any Model that has an identical Rig. Often a single file contains several different actions, each of which you can define as a specific **Animation Clip**

  
You can extract Materials and Textures or leave them embedded within the model. You can also adjust how Material is mapped in the Model.

### See also

  * Model import workflows: Overview of importing Model files
  * Model file formats: Which file formats (both proprietary and generic) that Unity supports, as well as issues specific to various 3D modeling software applications

FBXImporter