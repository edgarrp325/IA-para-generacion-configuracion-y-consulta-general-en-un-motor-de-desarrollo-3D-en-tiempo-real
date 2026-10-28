---
title: "Material Variant benefits and limitations"
category: "General"
source_file: "materialvariant-concept.html"
doc_type: "manual"
---

# Material Variant benefits and limitations

## How Material Variants help artists

Many of the materials in a game may be variations on a source—outfits with a variety of color schemes, damaged and undamaged versions of scenery, shiny and weathered instances of props. To help you manage and maintain these materials, Material Variants address specific shortcomings of copied materials, as illustrated in this table.

**Copied material** | **Material Variant**  
---|---  
Does not automatically change if its source material changes. | Automatically changes if its parent changes.  
To replicate a change to a copy in its source material, you must manually adjust the source material. | You can copy changes from a child material to its parent with two mouse clicks.  
You can’t limit changes to the Properties of copies. | You can lock one or more Properties on a Material or Material Variant to prevent modifications to those Properties in its children.  
You can’t associate a copy with a different source. | You can reparent Material Variants.  
  
### Create, convert, or reparent Material Variants

You can create Material Variants from both Materials and other Material Variants. It is also possible to convert Material Variants into Materials. To use the Override(s) in a variant with a variety of different Materials, you can change the parent of that variant.   
  
See Create, modify, and apply Material Variants for information about how to create and convert Material Variants.   
  
See Material Variant inheritance for an explanation of the Material Variant hierarchy.

### Variant sources

It is possible to create a Material Variant from any Material, including one you make with Shader Graph or download from the Asset Store. See Create, modify, and apply Material Variants for detailed information about how to create Material Variants from **shaders**.

### Identify and revert changes

An Override is a change you make to a Material Variant’s Properties. You can revert one Override at a time or all Overrides at once. Unity does not handle reverts through the Undo stack, which means that you can revert an Override without undoing any other changes.   
  
See Create, modify, and apply Material Variants for detailed information about how to identify and revert Overrides.

### Unity prevents inheritance issues

Unity protects against ancestor deletion and circular dependencies. If you attempt to delete the parent of a Material Variant, Unity warns you to select a new parent for the child or reparent it.   
  
See Material Variant inheritance for detailed information about Material Variant hierarchies and inheritance error messages.

### Scripts

You can use the Material Variant API to access Material Variant functionality for complex or large operations.   
  
See the Material and MaterialEditor API documentation for information about how to work with Material Variants in **scripts** and MaterialEditor API documentation for information about how to work with Material Variants in **scripts**.

## Similarities to Prefab Variants

Prefab Variants and Material Variants have much the same functionality, foundational concepts, and workflow. There are two key differences between them:

  * You can reparent a Material Variant.
  * You can lock Material Variant Properties.

## Prerequisites and limitations

Material Variants are not designed to address optimization and scalability concerns. In addition, it is not possible to use Material Variants to alter Materials at runtime in the Player.

## Additional resources

  * Materials introduction
  * Material Inspector Reference
  * Prefabs
  * Prefab Variants