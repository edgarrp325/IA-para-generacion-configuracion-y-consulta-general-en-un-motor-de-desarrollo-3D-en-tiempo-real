---
title: "Materials tab"
category: "General"
source_file: "FBXImporter-Materials.html"
doc_type: "manual"
---

# Materials tab

You can use this tab to change how Unity deals with Materials and Textures when importing your model.

When Unity imports a Model without any Material assigned, it uses the Unity diffuse Material. If the Model has Materials, Unity imports them as sub-Assets.

The Materials tab defines how Unity imports Materials and Textures

If your Model has Textures, you can also extract them into your Project using the Extract Textures button.

**Property** | **Function**  
---|---  
**Material Creation Mode** | Define how you want Unity to generate or import the Materials for your Model. When you choose **None** from this drop-down menu, the **Inspector** hides the rest of the settings on this tab.  
| **None** | Do not use any Materials embedded within this Model. Use Unity’s default diffuse Material instead.  
| **Standard** | On import, Unity applies a set of default rules to generate Materials. If you want to customize how Unity generates Material via scripting, choose the **Import via MaterialDescription (Experimental)** mode instead.  
| **Import via MaterialDescription (Experimental)** | On import, Unity uses the Material description embedded within the FBX file to generate the Materials. This method provides more accurate results than previous import methods, and supports a wider range of Material types, such as Arnold and Physical from Autodesk, as well as Unity’s HDRP Materials. For more information, see the Material description section below.  
**sRGB Albedo Colors** | Enable this option to use Albedo colors in gamma space. This is enabled by default for legacy import methods.   
  
Disable this for Projects using linear color space.  
  
This property is not available if you choose **Import via MaterialDescription (Experimental)** from the **Material Creation Mode** drop-down menu.  
**Location** | Define how to access the Materials and Textures. Different properties are available depending on which of these options you choose.  
| **Use Embedded Materials** |  Keep the imported Materials inside the imported Asset. This is the default option from Unity 2017.2 onwards.  
| **Use External Materials (Legacy)** |  Extract imported Materials as external Assets. This is a Legacy way of handling Materials, and is intended for Projects created with 2017.1 or previous versions of Unity.  
  
## Use Embedded Materials

When you choose **Use Embedded Materials** for the **Location** option, the following import options appear:

Import settings for Materials

**(A)** Click the **Extract Materials** and **Extract Textures** buttons to extract all Materials and Textures that are embedded in your imported Asset. These are greyed out if there are no sub-Assets to extract. Below these buttons, Unity displays any messages about the import process.

**(B)** The On Demand Remap section provides the Naming and Search properties which allow you to customize how Unity maps imported Materials to the Model. Click the **Search and Remap** button to remap your imported Materials to existing Material Assets. Nothing changes if Unity can’t find any Materials with the correct name.

**(C)** Unity displays all imported Materials found in the Asset in the Remapped Materials list. If Unity can’t automatically match each Material to an existing Material Asset in your Project, you can set references to the Materials yourself in this list.

### Remapped Materials

New imports or changes to the original Asset do not affect extracted Materials. If you want to re-import the Materials from the source Asset, you need to remove the references to the extracted Materials in the **Remapped Materials** list. To remove an item from the list, select it and press the Backspace key on your keyboard.

### Naming

Define a naming strategy for the Materials.

**Property** | **Function**  
---|---  
**By Base Texture Name** | Use the name of the diffuse Texture of the imported Material to name the Material. When you don’t assign a diffuse Texture to the Material, Unity uses the name of the imported Material.  
**From Model’s Material** | Use the name of the imported Material to name the Material.  
**Model Name + Model’s Material** | Use the name of the **Model file** in combination with the name of the imported Material to name the Material.  
  
### Search

Define where Unity tries to locate existing Materials when it uses the name defined by the **Naming** option.

**Property** | **Function**  
---|---  
**Local Materials Folder** | Find existing Materials in the local _Materials_ subfolder, which is in the same folder as the Model file).  
**Recursive-Up** | Find existing Materials in all Materials subfolders in all parent folders up to the _Assets_ folder.  
**Project-Wide** | Find existing Materials in all Unity Project folders.  
  
### Material description

Starting with version 2019.3, Unity introduced the ability to modify the Material mapping during import via scripting. Users can modify how Unity maps the imported Material properties from the data embedded in an FBX file to Unity Material properties. The Material description defines a name and several sets of values that describe the Material and any Textures it references. For more information about the structure of this description, see the MaterialDescription class reference page.

When in ImportViaMaterialDescription mode, the Model importer delegates the creation of Materials to the AssetPostProcessor.OnPreprocessMaterialDescription callback.

Unity provides default implementations of this Post Processor that handle the following Materials:

  * FBX Standard Material, Arnold Standard, Autodesk Interactive and 3Ds Physical Material from FBX files
  * Sketchup, Collada and 3DS Materials

These default implementations handle importing Materials differently from the ImportStandard mode, including the following improvements:

  * It supports more Material types, such as Autodesk’s Arnold and Interactive, or Physical, as well as Unity’s HDRP Materials.

  * It supports Emissive Materials.

  * If a diffuse Texture is set, it ignores the diffuse color (this matches how it works in Autodesk® Maya® and Autodesk® 3ds Max®).

  * It takes the bump factor, the emissive color, and emissive factor into account.

  * It imports emissive color animation when defined in the FBX file.

**Note** : 3ds Max does not export emissive color animation, so Unity cannot import it.

  * It imports transparent Materials as fully transparent. The legacy system imports them as fully opaque.

In addition, it imports all Autodesk Interactive Material property animations and no longer ignores the opacity when importing Materials from 3DS files.

## Use External Materials (Legacy)

When you choose **Use External Materials (Legacy)** for the **Location** option, the following import options appear:

Import settings for Use External Materials (Legacy)

This option extracts Materials and saves them externally instead of saving them inside your Model Asset. The Naming and Search properties help Unity find imported Materials to map to the Model.

Before Unity version 2017.2, this was the default way of handling Materials.

* * *

  * Materials tab added in 2017.2 NewIn20172
  * Use Embedded Materials added in 2017.3 NewIn20173
  * Import via Material Description added in 2019.3 NewIn20193