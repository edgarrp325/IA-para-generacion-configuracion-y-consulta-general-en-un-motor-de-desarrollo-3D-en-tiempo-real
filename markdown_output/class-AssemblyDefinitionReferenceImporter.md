---
title: "Assembly Definition Reference properties"
category: "General"
source_file: "class-AssemblyDefinitionReferenceImporter.html"
doc_type: "manual"
---

# Assembly Definition Reference properties

An Assembly Definition Reference is an asset that defines a reference to an Assembly Definition. Create an Assembly Definition Reference asset in a folder to include the **scripts** in that folder in the referenced Assembly Definition (rather than creating a new assembly). Scripts in child folders are also included, unless they have their own Assembly Definition or Assembly Definition Reference asset.

Property | Description  
---|---  
Use GUID | This setting controls how Unity serializes the reference to the Assembly Definition asset. When you enable this property, Unity saves the reference as the asset’s GUID, instead of the Assembly Definition name. It’s good practice to use the GUID instead of the name, because it means you can make changes to the name of an Assembly Definition asset without having to update other Assembly Definitions and References that reference it.  
Assembly Definition | The referenced Assembly Definition asset.  
  
See Creating an Assembly Definition Reference asset

AssemblyDefinitionReferenceImporter