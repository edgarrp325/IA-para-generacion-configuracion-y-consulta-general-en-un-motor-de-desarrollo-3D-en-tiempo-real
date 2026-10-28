---
title: "Trees"
category: "General"
source_file: "terrain-Trees.html"
doc_type: "manual"
---

# Trees

You can paint Trees onto a **Terrain** in a way that is similar to painting **heightmaps** and Textures. However, Trees are solid **3D objects** in a way that is similar to painting **heightmaps** and Textures. However, Trees are solid **3D objects** that grow from the surface. Unity uses optimizations like billboarding for distant Trees to maintain good rendering performance. This means that you can have dense forests with thousands of Trees, and still keep an acceptable frame rate.

Terrain with Trees

## Painting Trees

The **Paint Trees** button on the **toolbar** enables Tree painting:

The Paint Trees button

Initially, the Terrain has no tree prototypes available. To start painting onto the Terrain, you need to add a tree prototype. Click the **Edit Trees** button, and select **Add Tree**. From here, you can select a Tree Asset from your Project, and add it as a **Tree Prefab** for use with the Brush:

The Add Tree window

To help prototyping, SpeedTree provides six SpeedTree models in the free Unity Terrain - HDRP Demo Scene on the **Asset Store**

If the Tree **Prefab** that you are importing supports **Bend Factor** , the **Add Tree** window displays a **Bend Factor** property for adjusting wind responsiveness. Trees created with the SpeedTree Modeler don’t have a **Bend Factor** ; only those created with Tree Editor do. See the section on **Making Trees bend in the wind** , below.

When you have configured your **Settings** (described below), you can paint Trees onto the Terrain in the same way you paint textures or heightmaps. To remove Trees from an area, hold the Shift key while you paint. To remove just the currently selected Tree type, hold down the Control key while you paint.

## Settings

After you select which Tree to place, adjust its settings to customize Tree placement and characteristics.

Settings for Trees **Property** | **Function**  
---|---  
**Mass Place Trees** | Create an overall covering of Trees without painting over the whole landscape. After mass placement, you can still use painting to add or remove Trees to create denser or sparser areas.  
**Brush Size** | Controls the size of the area that you can add Trees to.  
**Tree Density** |  **Tree Density** controls the average number of Trees painted onto the area defined by **Brush Size**.  
**Tree Height** | Control the Tree’s minimal height and maximal height using a slider. Drag the slider to the left for short Trees, and right for tall Trees. If you uncheck **Random** , you can specify the exact scale for the height of all newly painted Trees within the range of 0.01 to 2.  
**Lock Width to Height** | By default, a Tree’s width is locked to its height so that Trees are always scaled uniformly. However, you can disable the **Lock Width to Height** option, and specify the width separately.  
**Tree Width** | If the Tree’s width is not locked to its height, you can control the Tree’s minimal width and maximal width using a slider. Drag the slider to the left for thin Trees, and right for wide Trees. If you uncheck **Random** , you can specify the exact scale for the width of all newly painted Trees within the range of 0.01 to 2.  
**Random Tree Rotation** | If you configure the Tree with an LOD Group, use the **Random Tree Rotation** setting to help create the impression of a random, natural-looking forest rather than an artificial plantation of identical Trees. Uncheck this option if you want to place Trees with fixed, identical rotations.  
**Color Variation** | The amount of random shading applied to Trees. This only works if your **shader** reads the `_TreeInstanceColor` property. For example, shaders for all trees you create with Tree Editor read the `_TreeInstanceColor` property.  
**Tree Contribute Global Illumination** | Enable this check box to indicate to Unity that the Tree influences **Global Illumination** computations.  
  
## Creating Trees

There are two ways to create new Tree models. Use the SpeedTree Modeler from IDV, Inc. to create Trees with advanced visual effects, such as smooth LOD transition, fast billboarding, and natural wind animation. For more detailed information, refer to the SpeedTree Modeler documentation. Alternatively, use the Tree Editor to create Tree Models.

Internally, the Terrain Engine distinguishes between the two types of models by determining whether an LOD Group is present on the Tree Prefab’s root **GameObject** is present on the Tree Prefab’s root **GameObject**. A SpeedTree Prefab has an _LODGroup_ component, but a Tree Editor Prefab does not.

When creating Trees, position the anchor point at the base of the Tree where it emerges from the ground. Performance depends on the polygon count of your Tree model, so be sure to test on your platform, and create simpler Trees if necessary. Also, for Tree Editor Trees, each **Mesh** always has exactly two materials: one for the Tree body and the other for the leaves.

Trees you create using Tree Editor must use the **Nature/Soft Occlusion Leaves** and **Nature/Soft Occlusion Bark** shader. To use those shaders, you have to place Trees in a specific folder named _Ambient-Occlusion_ , otherwise the Trees don’t render correctly. When you place a model in this folder and re-import it, Unity calculates soft **ambient occlusion** in a way that is specifically designed for Trees.

If you change an imported Tree Asset in a separate 3D modelling application, you need to click the **Refresh** button in the Editor to see the updated Trees on your Terrain:

Refresh buton location

**Note:** When you import and alter a SpeedTree model in a 3D modeling program, then re-export it (as an `.fbx` or `.obj`), you might lose the natural wind animation functionality that comes with SpeedTree models.

## Using Colliders with Trees

You can add a Capsule Collider to a Tree Asset. First, click **>** next to the Tree Asset to open the Prefab.

Then, select **Add Component > Physics > Capsule Collider** to add the collider. To return to the Scene, click **<** next to the Prefab name.

You must also check **Enable Tree Colliders** in the **Terrain Collider** component.

## Make Trees bend in the wind

Wind Zones can bend Trees to simulate the direct effect of wind. This feature is only available for Trees that you place through the Terrain menu. To do this, select the Terrain, click the **Paint Trees** button in the Inspector, then select **Edit Trees > Add Tree** and select your Tree Prefab. If you did not create the Tree in Unity, set the **Bend Factor** to 1. Click on the Terrain to place the selected Tree.

Terrain-based Trees that have a **Bend Factor** react to Wind Zones by bending and swaying, according to the values of the Wind Zone’s **Turbulence** and **Main** properties. The **Turbulence** setting controls the fluttering of leaves. Reducing this value smooths the fluttering effect. The **Main** value controls the main force of the wind. To create a Wind Zone, select **GameObject > 3D Object > Wind Zone**.

If the Wind Zone’s **Mode** is **Directional** , then its position relative to the Tree does not matter. The Trees will sway in the direction of the Wind Zone. However, if your Wind Zone’s **Mode** is **Spherical** , then its **Radius** has to overlap the Tree’s radius. This results in multi-directional gusts of wind, with a falloff from the center towards the edge.

With the default settings, Trees such as the Broadleaf Prefab (which is provided in the Standard Assets Environment pack) sway in a smooth and realistic way. However, if you’re using your own Tree Prefab, you might need to adjust the Wind Zone property values. If your Tree Prefab trunk is bent all the way to one side, try reducing the **Main** value. Alternatively, if the branches of your Tree Prefab bend or stretch excessively, reduce the **Turbulence** value.

## Tree Level of Detail (LOD) transition zone

For Tree Editor Trees, Unity’s LOD system uses a 2D to 3D transition zone to seamlessly blend 2D billboards with 3D Tree models. This prevents any sudden popping of 2D and 3D Trees, which is vital in **VR**. Note that **billboard**. Note that **billboard** Trees don’t receive local lighting such as Point Lights and Spot Lights. They work with directional lights, but lighting on the billboards only updates when you rotate the **Camera** Trees don’t receive local lighting such as Point Lights and Spot Lights. They work with directional lights, but lighting on the billboards only updates when you rotate the **Camera**.

For SpeedTree Trees, see the LOD and LOD Group documentation for more information about configuring LOD components.

* * *

  * 2020–02–19 Page amended 

  * Added billboard limitations for Tree Editor Trees.