---
title: "Create and apply a custom Physic Material"
category: "General"
source_file: "create-apply-physics-material.html"
doc_type: "manual"
---

# Create and apply a custom Physic Material

You can create as many custom **Physic Material** assets as you need, and apply them to **colliders** assets as you need, and apply them to **colliders** in your **scene** in your **scene**.

Several colliders can have the same Physic Material asset assigned to them, and you can set a project-wide default to apply new default settings to all colliders in the project. 

## Create a custom Physic Material asset

To create a Physic Material asset, go to **Assets** > **Create** > **Physic Material**. By default, Unity places new Physic Material assets in your `Assets` directory.

You can create as many custom Physic Material assets as you need. Physic Material assets have the file extension `.physicMaterial`.

## Apply a custom Physic Material asset to a collider

To apply a Physic Material asset to a collider: 

  1. Navigate to the target collider’s **Material** property.
  2. In the **Material** property field, select the picker icon.
  3. Select the Physic Material asset you want to use.

Alternatively, you can click and drag the Physic Material asset file directly from the **Project window** onto the target collider’s **Material** field.

Each collider can only have one assigned Physic Material asset at a time. You can assign the same Physic Material asset to multiple colliders.

## Set a custom Physic Material asset as the project default

You can use a custom Physic Material asset to replace the project-wide default settings. Unity applies the project-wide default settings to any collider that does not have an assigned Physic Material asset.

To change the default Physic Material values: 1\. Create a Physic Material asset and configure it to the default settings you want for the project. 2\. Go to the Physics Settings (**Edit** > **Project Settings** > **Physics**). 3\. In the **Default Material** property field, select the picker icon. 4\. Select the Physic Material you want to use.