---
title: "Supported Asset Types"
category: "General"
source_file: "AssetTypes.html"
doc_type: "manual"
---

# Supported Asset Types

Unity supports many different types of assets and most common image file types, including BMP, TIFF, TGA, JPG, and PSD. 

If you save layered Photoshop (.psd) files in your `Assets` folder, Unity imports them as flattened images. You can find out more about importing images as textures, or importing images as sprites.

For the full list of Unity’s built-in importers, supported file types and supported filename extensions, see Built-in importers.

Listed below are some of the more common types of asset that you might want to use when getting started with Unity, and links to find out more about how to work with them.

## Commonly used asset types

Type | Description  
---|---  
**3D Model Files** | Unity supports the FBX file format, which means that you can import data from any 3D modeling software that supports FBX. Unity also natively supports importing SketchUp files. For a list of 3D modeling software that Unity supports, see Model file formats.  
  
3D Model files can contain many types of asset, such as meshes, animation, materials  
**Image files** | Unity imports image files as textures. Unity supports most common image file types, such as BMP, TIF, TGA, JPG, and PSD. If you save your layered Photoshop (.psd) files in your `Assets` folder, Unity imports them as flattened images. Read more about importing textures.  
**Audio files** | Unity supports many audio file formats. It’s generally best to import uncompressed audio file formats such as `.wav` or `.aiff`, because during import Unity applies the **compression** settings specified in your import settings. Read more about importing audio files.  
**Text, HTML, XML, JSON** | Unity can import arbitrary data from files, allowing you to store and use data from external sources. These are all handled by the Text Asset Importer.  
**Plug-ins and code-related assets** | You can drop managed and native plug-ins into your Unity project as assets (such as `.dll` files) to expand the functionality of your game or app. Unity also supports assembly definitions to help you create and organize your **scripts** into your Unity project as assets (such as `.dll` files) to expand the functionality of your game or app. Unity also supports assembly definitions to help you create and organize your **scripts** into assemblies.  
**Native Assets** | There are a range of asset types that are native to the Unity Editor. You can create assets of these types using Editor features. When you create these, Unity saves the files which represent them as asset files in the Assets folder of your project.  
  
These include animations, curves, gradients, masks  
  
## Assets in the Unity Package Manager

You can install a wide range of assets, including plug-ins, tools, and libraries directly into Unity through the **Unity Package Manager (UPM)**. These are a new type of package, and are available through the Package Manager window. For more information about packages in general, see the Packages

## Reusing assets between projects

As you build your game, Unity stores a lot of metadata about your assets, such as import settings and links to other assets, among other information. If you want to transfer your assets into a different project and preserve all this information, you can export your assets into one of these containers:

  * A custom package, which you can access and manage inside Unity’s Package Manager.
  * An asset package, which you can create directly in the Editor.