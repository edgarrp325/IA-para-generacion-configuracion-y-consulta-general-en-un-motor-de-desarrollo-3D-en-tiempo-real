---
title: "Presets"
category: "General"
source_file: "Presets.html"
doc_type: "manual"
---

# Presets

Presets are assets that you can use to save and apply identical property settings across multiple components, assets, or Project Settings windows. You can also use Presets to specify default settings for new components and default import settings for assets in the Preset Manager The Preset Manager supports any importers, components, or scriptable objects you add to the Unity Editor.

You can only apply Presets in the Editor. Presets have no effect at runtime. You can use scripting to support presets in your own Monobehaviour, ScriptableObject or ScriptedImporter classes.

## Saving and applying Presets

Presets allow you to save the property configuration of a component, asset, or Project Settings window as a Preset asset. You can then use this Preset asset to apply the same settings to a different component, asset, or Project Settings window.

For example, you could edit the properties of a **Rigidbody** component, save these settings to a Preset asset, then apply that Preset asset to Rigidbody components in other **GameObjects** component, save these settings to a Preset asset, then apply that Preset asset to Rigidbody components in other **GameObjects**. The other components in the GameObjects are not affected; the Preset only applies its settings to the Rigidbody component.

You can store Presets in the `Assets` folder of your project. Use the Project window to view and select Presets to edit in the **Inspector**

Example of Preset assets in the **Project** window, organized in a _Presets_ sub-folder

## Saving property settings to a Preset

To save property settings to a Preset asset, follow the instructions below. You can save property settings while in Edit mode or in Play mode.

  1. Select the GameObject, Asset import settings, or Project Settings window from which you want to reuse settings. When you select it, it appears in the **Inspector** window.

  2. In the **Inspector** window, configure the properties as you want to save them.

  3. Click the Preset selector (the slider icon) at the top-right of the **Inspector** window.   

  4. In the Select Preset window, click **Create new Preset**.   
  
A File Save dialog appears.

  5. Choose the location of your new Preset, enter its name, and click **Save**.

## Applying settings from a Preset

There are two ways to apply a Preset: the **Select Preset** window, or for component Presets, you can also drag and drop a Preset from the **Project** window onto the GameObject that contains that component.

**Note:** Applying a Preset copies properties from the Preset to the item. It doesn’t link the Preset to the item. Changes you make to the Preset do not affect the items you have previously applied the Preset to.

To apply a Preset via the **Select Preset** window:

  1. For GameObjects or assets you want to apply a Preset to, select them so that they appear in the **Inspector** window. For Project Settings that you want to apply a Preset to, open them in the **Project Settings** window.

  2. In the **Inspector** , click the Preset selector (the slider icon).

  3. In the **Select Preset** window, search for and select the Preset to apply.

Unity applies this Preset to the component, asset, or Project Settings window.

  4. Close the **Select Preset** window.

If you apply a component Preset via drag-and-drop, Unity’s behavior depends on the state of your GameObject:

  * If you drop the Preset on an existing GameObject in the Hierarchy window, Unity adds a new component and copies properties from the Preset.
  * If you drop the Preset on an empty area in the Hierarchy window, Unity creates a new, empty GameObject and adds a component with properties copied from the Preset.
  * If you drop the Preset on the Inspector window onto the title of an existing component, Unity copies properties from the Preset.
  * If you drop the Preset on an empty area in the Inspector window, Unity adds a new component and copies properties from the Preset.

### Applying partial Presets

You can choose to only apply some properties from a Preset and exclude others. To do this:

  1. Select your Preset in the **Project** window.

  2. In the **Inspector** , right-click a property and choose **Exclude Property**. The window displays a red horizontal line next to excluded properties.  

  3. Apply the Preset to the target component, asset, or Project settings.

**Note:** To select all or clear all checkboxes in a Preset, select the **More items** menu (**⋮**) or right-click the Preset name, and select **Include all properties** or **Exclude all properties**. You can still adjust individual properties if you need to.

You can also use the Exclude option for Presets that you then set as the default configuration for components and asset importers. See Preset Manager for more details on how to do this.

## Editing a Preset

To edit a Preset asset, select it from the **Project** window and view it in the **Inspector** window.

**Note:** When you change the properties in a Preset, your changes do not affect items you have already applied the Preset to. For example, if you apply a Preset for a Rigidbody component to a GameObject, and then edit the Preset, the settings in the Rigidbody component do not change.

Editing a Preset in the Inspector window

## Importing Assets using Presets by folder

You can use a script to apply a Preset to an Asset based on the location of the Asset in the _Project_ window.

## Exporting Preset Assets

Use Presets to streamline your team’s workflows. You can even use Presets to specify settings for Project Settings windows, including the **Preset** settings themselves. Use this feature to configure a project then export it as a custom **asset package**

  1. In the **Project window** , select the Presets you want to export .
  2. In the Unity menu, go to **Assets > Export Package**, or right-click inside the Project window and choose **Export Package**.  
The **Exporting package** window displays the items to export.
  3. If your Presets contain references to assets you want to include in the package, enable **Include dependencies**. This option includes **scripts** that are **direct dependencies** that are **direct dependencies** of the selected assets.
  4. If your Presets contain references to scripts that might depend on other scripts, enable **Include all scripts**. This option reduces the likelihood of compilation errors when using the exported package in another project.
  5. Click **Export**.
  6. Choose where you want to store the package, enter a file name, and click **Save**. Unity saves the package as a .unitypackage file.

## Using Presets for transitions of Animation State nodes

You can save and apply Presets for Animation State nodes. However, the transitions in the Preset are shared among Presets and the nodes that you apply the Preset to. For example, you apply a Preset to two different nodes in the Animator window. In the Inspector window, you edit the settings for one of the transitions in the first node. Your change also appears in the other node and in the Preset.