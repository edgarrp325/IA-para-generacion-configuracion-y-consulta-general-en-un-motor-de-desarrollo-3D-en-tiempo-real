---
title: "Static GameObjects"
category: "General"
source_file: "StaticObjects.html"
doc_type: "manual"
---

# Static GameObjects

If a **GameObject** does not move at runtime, it is known as a **static GameObject**. If a GameObject moves at runtime, it is known as a **dynamic GameObject**.

Many systems in Unity can precompute information about static GameObjects in the Editor. Because the GameObjects do not move, the results of these calculations are still valid at runtime. This means that Unity can save on runtime calculations, and potentially improve performance.

## The Static Editor Flags property

The Static Editor Flags checkbox and drop-down menu, as seen when viewing a GameObject in the Inspector

The **Static Editor Flags** property lists a number of Unity systems which can include a static GameObject in their precomputations. Use the drop-down to define which systems include the GameObject in their precomputations. Setting Static Editor Flags at runtime has no effect on these systems.

Only include a GameObject in the precomputations for systems that need to know about that GameObject. Including a GameObject in the precomputations for a system that does not need to know about that GameObject can result in wasted calculations, unnecessarily large data files, or unexpected behavior.

The **Static Editor Flags** property is located in the **Inspector** for a GameObject, in the extreme top-right. It includes a checkbox, which sets the value to **Everything** or **Nothing** , and a drop-down menu that lets you choose which values to include.

To set the Static Editor Flags property in code, use the GameObjectUtility.SetStaticEditorFlags API and the GameObject.isStatic. To get the status of the Static Editor Flags property in code, use the GameObjectUtility.GetStaticEditorFlags API.

The following values are available:

**Property:** | **Description**  
---|---  
**Nothing** | Do not include the GameObject in precomputations for any systems.  
**Everything** | Include the GameObject in precomputations for all systems below.  
**Contribute GI** | When you enable this property, Unity includes the target Mesh Renderer in **global illumination** calculations. These calculations take place while precomputing lighting data at bake time. The ContributeGI property exposes the ReceiveGI property. The ContributeGI property only takes effect if you enable a global illumination setting such as Baked Global Illumination or Enlighten Realtime Global Illumination for the target **Scene** in **global illumination** calculations. These calculations take place while precomputing lighting data at bake time. The ContributeGI property exposes the ReceiveGI property. The ContributeGI property only takes effect if you enable a global illumination setting such as Baked Global Illumination or Enlighten Realtime Global Illumination for the target **Scene**. For additional context, refer to this tutorial for setting up the Built-in Render Pipeline and lighting in Unity.  
**Occluder Static** | Mark the GameObject as a Static Occluder in the occlusion culling system. For more information, refer to the Occlusion Culling system.  
**Occludee Static** | Mark the GameObject as a Static Occludee in the occlusion culling system. For more information, refer to the Occlusion Culling system.  
**Batching Static** | Combine the GameObject’s **Mesh** with other eligible Meshes, to potentially reduce runtime rendering costs. For more information, refer to the documentation on Static Batching with other eligible Meshes, to potentially reduce runtime rendering costs. For more information, refer to the documentation on Static Batching.  
**Navigation Static** | Include the GameObject when precomputing navigation data. This workflow is deprecated and you cannot set **Navigation Static** here. However, you can still set this option in the **Navigation (Obsolete)** window > **Object** tab, or in code with `StaticEditorFlags.NavigationStatic`.   
Instead of **Navigation Static** flags, the preferred workflow is to use the **NavMesh Modifier** component and **NavMesh Surfaces**.  
**Off Mesh Link Generation** | Attempt to generate an OffMesh link that starts from this GameObject when precomputing navigation data. This workflow is deprecated and you cannot set **Off Mesh Link Generation** from this menu. However, you can still set this option in the **Navigation (Obsolete)** window > **Object** tab, or in code with `StaticEditorFlags.OffMeshLinkGeneration`.   
Instead of **Off Mesh Link Generation** flags, the preferred workflow is to use the **NavMesh Modifier** component and **NavMesh Surfaces**.  
**Reflection Probe** | Include this GameObject when precomputing data for **Reflection Probes** whose **Type** property is set to **Baked**. For more information, refer to the documentation on Reflection Probes.  
  
## Additional resources

  * GameObjectUtility.SetStaticEditorFlags
  * GameObjectUtility.GetStaticEditorFlags
  * StaticEditorFlags.NavigationStatic
  * StaticEditorFlags.OffMeshLinkGeneration
  * StaticEditorFlags
  * Draw call batching
  * Occlusion Culling
  * NavMesh Modifier component
  * NavMesh Surface component
  * Reflection Probes