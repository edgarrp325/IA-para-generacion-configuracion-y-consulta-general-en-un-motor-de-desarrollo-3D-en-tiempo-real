---
title: "Create, modify, and apply Material Variants"
category: "General"
source_file: "materialvariant-tasks.html"
doc_type: "manual"
---

# Create, modify, and apply Material Variants

These instructions explain how to work with Material Variants. Programmers should consult the Material and MaterialEditor API documentation for information about how to work with Material Variants in **scripts** and MaterialEditor API documentation for information about how to work with Material Variants in **scripts**.

## Differences between Prefab Variants and Material Variants

The Material Variant workflow is mostly the same as the Prefab Variant workflow. There are two key differences:

  * You can lock one or more Properties of a Material Variant so that no one can edit these Properties in its children
  * It is possible to change the parent of a Material Variant

## Create a Material Variant

There are two ways to create a Material Variant.

### Right-click on a Material in the Project window

  1. Select a Material in the **Project window**.
  2. Right-click on that Material.
  3. Select **Create** > **Material Variant**.

### Select in the Material Hierarchy

  1. Open the Material Hierarchy dialog.
  2. Select the material type dropdown.
  3. Select **Material Variant**.
  4. Assign a material to the parent field

The dropdown to create a Material Variant from the Material Hierarchy

### Identify the new Material Variant

When you create a new Material Variant, it has the name [Material Name] **Variant (Material Variant)** in the Material **Inspector**. When Unity begins to load a new Material Variant, the Material Variant has a striped icon in the Project window. After Unity finishes loading the new Material Variant, the normal Material preview replaces the striped icon in the Project window.

## Add an Override on a Material Variant

  1. Select a Material Variant.
  2. Modify one of its Properties in the Material Inspector.

The thick line to the left of a Property (circled in red in this screenshot) indicates an Override.

## Revert one or more Overrides on a Material Variant

  1. Right-click on an Override.
  2. Select **Revert** to revert this specific Override, or select **Revert all Overrides** to revert every Override on this variant. If this Override originated from a child, reverting also applies to that child.

For a detailed explanation of how inheritance determines the effect of reverting changes, see Material Variant inheritance or Revert an Override applied upward.

## Apply an Override upward in the hierarchy

You can apply an Override upward to any ancestor in the hierarchy.

This dropdown makes it possible for you to Revert Overrides, apply them upward, or lock them.

### Apply the Override to the parent

To apply an Override to a parent, right-click on an Override and select **Apply to** [name of parent] in the dropdown.

### Apply the Override to an ancestor

To apply an Override to an ancestor, right-click on an Override and select **Apply to** [name of ancestor] in the dropdown.

### Revert one or more Overrides applied upward

Once an Override is applied upward, you can no longer revert it on the child that originated it. Instead, you must revert it on the recipient parent or ancestor; see the instructions in Revert one or more Overrides on a Material Variant.

## Delete a Material Variant

  1. Select the Material Variant in the Project window.
  2. Press the **Delete** key. The next step depends on whether the Material Variant has children. 
     * If the Material Variant has no children, click **Delete** in the warning dialog to delete the variant.
     * If the Material Variant has one or more children, a warning dialog appears that says **One or more of these Material(s) has one or more children. Would you like you reparent all of these children to their closest remaining ancestor?**
       * The warning dialog provides three options: 
         * **Delete and reparent children** : This option causes Unity to automatically assign this parent’s children to their closest ancestor; this new parent can be either a Material Variant or a Material, or no parent if the Material to be deleted is the root of the hierarchy.
         * **Delete only** Note: A Material with a missing parent is in an invalid state and will not load correctly at runtime.
         * **Cancel** See Inheritance error messages for information about orphan Material Variants.

## Reparent a Material Variant

There are two ways to reparent a Material Variant.

### In the Material Inspector

  1. Select the variant you want to reparent in the Project window.
  2. Select the bullseye next to the **Parent** Property and choose a new parent in the **Select Material** dialog.

Select a new parent

### In the Project window

Drag the new parent Material or Material Variant onto the target child.

## Lock a Property

  1. Right-click on a Property.
  2. Select **Lock in children** in the dropdown.
  3. A padlock icon appears next to the locked Property.

To unlock the property, click **Lock in children** again.

The lock menu

## Convert a Material Variant to a Material

There are two ways to convert a Material Variant to a Material.

### From the Hierarchy View

  1. Select the Material Variant in the Project window.
  2. Expand the Hierarchy dialog in the Material Inspector.
  3. Select **Material** in the Material type dropdown.

Convert to a Material from the Hierarchy view

### From the Settings dropdown

  1. Click the Settings dropdown in the Material Inspector.
  2. Select **Flatten Material Variant** in the dropdown.

The Flatten Material Variant option.

## Additional resources

  * Materials introduction
  * Material Inspector Reference
  * Prefabs
  * Prefab Variants
  * Shader Graph
  * HDRP Lit shader