---
title: "Rig tab"
category: "General"
source_file: "FBXImporter-Rig.html"
doc_type: "manual"
---

# Rig tab

The settings on the **Rig** tab define how Unity maps the deformers to the **Mesh** in the imported Model so that you can animate it. For Humanoid characters, this means assigning or creating an Avatar. For non-Humanoid (_Generic_) characters, this means identifying a Root bone in the skeleton.

By default, when you select a Model in the **Project** view, Unity determines which **Animation Type** best matches the selected Model and displays it in the **Rig** tab. If Unity has never imported the file, the Animation Type is set to **None** :

No rig mapping **Property:** | **Function:**  
---|---  
**Animation Type** | Specfiy the type of animation.  
| **None** | No animation present  
| **Legacy** | Use the Legacy Animation System. Import and use animations as with Unity version 3.x and earlier.  
| **Generic** | Use the Generic Animation System if your rig is _non-humanoid_ (quadruped or any entity to be animated). Unity picks a root node but you can identify another bone to use as the **Root node**  
| **Humanoid** | Use the Humanoid Animation System if your rig is _humanoid_ (it has two legs, two arms and a head). Unity usually detects the skeleton and maps it to the Avatar correctly. In some cases, you may need to set a change the **Avatar Definition** and **Configure** the mapping manually.  
  
## Generic animation types

Your rig is _non-humanoid_ (quadruped or any entity to be animated)

Generic Animations do not use Avatars like **Humanoid animations** do. Since the skeleton can be arbitrary, you must specify which bone is the **Root node**. The Root node allows Unity to establish consistency between **Animation clips** for a generic model, and blend properly between Animations that have not been authored “in place” (that is, where the whole model moves its world position while animating).

Specifying the root node helps Unity determine between movement of the bones relative to each other, and motion of the Root node in the world (controlled from OnAnimatorMove).

**Property:** | **Function:**  
---|---  
**Avatar Definition** | Choose where to get the Avatar definition.  
| **Create from this model** | Create an Avatar based on this model  
| **Copy from Other Avatar** | Point to an Avatar set up on another model.  
**Root node** | Select the bone to use as a root node for this Avatar.   
  
This setting is only available if you set the **Avatar Definition** to **Create From This Model**.  
**Source** | Copy another Avatar with an identical rig to import its animation clips.   
  
This setting is only available if you set the **Avatar Definition** to **Copy from Other Avatar**.  
**Skin Weights** | Set the maximum number of bones that can influence a single vertex.  
  
  
| **Standard (4 Bones)** | Use a maximum influence of four bones. This is the default, and is recommended for performance.  
| **Custom** | Set your own maximum number of bones.   
  
When you select this option, the **Max Bones/Vertex** and **Max Bone Weight** properties appear.  
**Max Bones/Vertex** | Set the maximum number of bones per vertex to influence a given vertex. You can set between 1 and 32 bones per vertex, but the higher the number of bones you use to influence a vertex, the greater the performance cost.  
  
This setting is only available you set the **Skin Weights** property to **Custom**.  
**Max Bone Weight** | Set the bottom threshold for considering bone weights. The weighting calculation ignores anything smaller than this value, and Unity scales up the bone weights higher than this value to a total of 1.0.  
  
This setting is only available if the **Skin Weights** property is set to **Custom**.  
**Optimize Game Object** | Remove and store the GameObject Transform hierarchy of the imported character in the Avatar and Animator component. If enabled, the SkinnedMeshRenderers of the character use the Unity animation system’s internal skeleton, which improves the performance of the animated characters.   
  
Only available if the **Avatar Definition** is set to **Create From This Model**.  
**Extra Transforms to Expose** | Specify which Transform paths you want Unity to ignore when **Optimize Game Object** is enabled. For more information, see Including extra Transforms.  
  
This section only appears when **Optimize Game Object** is enabled.  
  
## Humanoid animation types

Your rig is _humanoid_ (it has two legs, two arms and a head)

With rare exceptions, humanoid models have the same basic structure. This structure represents the major articulated parts of the body: the head and limbs. The first step to using Unity’s Humanoid animation features is to set up and configure an **Avatar**

**Property:** | **Function:**  
---|---  
**Avatar Definition** | Choose where to get the Avatar definition.  
| **Create from this model** | Create an Avatar based on this model  
| **Copy from Other Avatar** | Point to an Avatar set up on another model.  
**Source** | Copy another Avatar with an identical rig to import its animation clips.   
  
Only available if the **Avatar Definition** is set to **Copy from Other Avatar**.  
**Configure…** | Open the Avatar configuration.   
  
Only available if the **Avatar Definition** is set to **Create From This Model**.  
**Skin Weights** | This property is identical for both Humanoid and Generic Models. See the documentation on Skin Weights above for information about it.  
**Optimize Game Object** | Remove and store the GameObject Transform hierarchy of the imported character in the Avatar and Animator component. If enabled, the SkinnedMeshRenderers of the character use the Unity animation system’s internal skeleton, which improves the performance of the animated characters.   
  
Only available if the **Avatar Definition** is set to **Create From This Model**.  
**Extra Transforms to Expose** | Specify which Transform paths you want Unity to ignore when **Optimize Game Object** is enabled. For more information, see Including extra Transforms.  
  
This section only appears when **Optimize Game Object** is enabled.  
  
## Including extra Transforms

When you enable the **Optimize Game Object** property, Unity ignores any Transform which is part of the hierarchy but is not mapped in the Avatar, in order to improve CPU performance. However, you can mark specific nodes in the **GameObject** hierarchy to include in calculations using the **Extra Transforms to Expose** section:

The Extra Transforms to Expose property appears when Optimize Game Objects is enabled

**(A)** Enter the full or partial name in the search box to filter the list of Transforms. This makes it easier to navigate through characters with a large number of bones.

**(B)** Enable each Transform (bones of a skeleton) you want Unity to include in calculations.

**(C)** Use the buttons to help select specific Transforms. For example, the **Toggle All** button selects or deselects everything at once (regardless of the current selection, including filtered items).

**(D)** Use the **Revert** button to undo your selections or the **Apply** button to apply the exceptions to the Model.

**Note** : In optimized mode, skinned Mesh matrix extraction is multi-threaded.

## Legacy animation types

Your rig uses the Legacy Animation System **Property:** | **Function:**  
---|---  
**Generation** | Select the animation import method.  
| **Don’t Import** | Do not import animation  
| **Store in Original Roots (Deprecated)** | Deprecated. Do not use.  
| **Store in Nodes (Deprecated)** | Deprecated. Do not use.  
| **Store in Root (Deprecated)** | Deprecated. Do not use.  
| **Store in Root (New)** | Import the animation and store it in the Model’s root node. This is the default setting.  
**Skin Weights** | See the documentation on Skin Weights above for information about this property.  
  
For more information about legacy animation, see the documentation for Legacy Animation System.

* * *

  * **Skin Weights** added in 2019.1 NewIn20191
  * **Materials** tab added in 2017.2 NewIn20172