---
title: "SpeedTree Import Settings window"
category: "General"
source_file: "class-SpeedTreeImporter.html"
doc_type: "manual"
---

# SpeedTree Import Settings window

Switch to Scripting

When you put SpeedTree files in your Unity project’s Assets folder, Unity automatically imports and stores them as Unity assets. To view the import settings in the **Inspector** , select the file in the **Project** , select the file in the **Project** window. To customize how Unity imports the selected file, use the properties on the **Model** and **Materials** tabs on this window.

**Note:** These settings are for importing models created in SpeedTree. For information on models and animation created in other 3D modeling applications, see the Model Import Settings window. 

The SpeedTree Import Settings window

Unity recognizes and imports SpeedTree model assets in the same way it handles other assets. If you’re using SpeedTree Modeler 7, re-save your `.spm` files using the Unity version of the Modeler. If you’re using SpeedTree Modeler 8, save your `.st` files directly into the Unity project folder. The SpeedTree Importer generates a **prefab** with the LOD Group with the LOD Group component configured. You can instantiate the prefab in a **scene** component configured. You can instantiate the prefab in a **scene** as a common prefab instance or select the prefab as a tree prototype and paint it across the **terrain** as a common prefab instance or select the prefab as a tree prototype and paint it across the **terrain**.

Materials come embedded in the imported SpeedTree model as sub-assets. If you want to make adjustments to the materials, you can extract them to a location of your choice or re-use existing materials with Material Remapping.

**Topic** | **Description**  
---|---  
**Model tab** | Understand the options in the Model tab of the SpeedTree Import Settings window.  
**Materials tab** | Understand the options in the Materials tab of the SpeedTree Import Settings window.  
  
* * *

  * New feature in 2018.3 NewIn20183

SpeedTreeImporter