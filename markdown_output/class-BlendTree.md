---
title: "Blend Trees"
category: "General"
source_file: "class-BlendTree.html"
doc_type: "manual"
---

# Blend Trees

A common task in game animation is to blend between two or more similar motions. Perhaps the best known example is the blending of walking and running animations according to the character’s speed. Another example is a character leaning to the left or right as it turns during a run.

It is important to distinguish between Transitions and Blend Trees. While both are used for creating smooth animation, they are used for different kinds of situations.

  * **Transitions** are used for transitioning smoothly from one Animation State to another over a given amount of time. Transitions are specified as part of an Animation State Machine are used for transitioning smoothly from one Animation State to another over a given amount of time. Transitions are specified as part of an Animation State Machine. A transition from one motion to a completely different motion is usually fine if the transition is quick.

  * **Blend Trees** are used for allowing multiple animations to be blended smoothly by incorporating parts of them all to varying degrees. The amount that each of the motions contributes to the final effect is controlled using a _blending parameter_ , which is just one of the numeric animation parameters associated with the **Animator Controller** associated with the **Animator Controller**. In order for the blended motion to make sense, the motions that are blended must be of similar nature and timing. Blend Trees are a special type of state in an Animation **State Machine**. In order for the blended motion to make sense, the motions that are blended must be of similar nature and timing. Blend Trees are a special type of state in an Animation **State Machine**.

Examples of similar motions could be various walk and run animations. In order for the blend to work well, the movements in the clips must take place at the same points in normalized time. For example, walking and running animations can be aligned so that the moments of contact of foot to the floor take place at the same points in normalized time (e.g. the left foot hits at 0.0 and the right foot at 0.5). Since normalized time is used, it doesn’t matter if the clips are of different length.

## Using Blend Trees

To start working with a new Blend Tree, you need to:

  1. Right-click on empty space on the Animator Controller Window.
  2. Select **Create State > From New Blend Tree** from the context menu that appears.
  3. Double-click on the Blend Tree to enter the Blend Tree Graph.

The **Animator Window** now shows a graph of the entire Blend Tree while the **Inspector** now shows a graph of the entire Blend Tree while the **Inspector** shows the currently selected node and its immediate children.

The Animator Window shows a graph of the entire Blend Tree. To the left is a Blend Tree with only the root Blend Node (no child nodes have been added yet). To the right is a Blend Tree with a root Blend Node and three Animation Clips as child nodes.

To add **animation clips** to the blend tree you can select the blend tree, then click the plus icon in the motion field in the inspector.

A Blend Node shown in the inspector before any motions have been added. The plus icon is used to add animation clips or child blend trees.

Alternatively, you can add animation clips or child **blend nodes** by right-clicking on the blend tree and selecting from the context menu:

The context menu when right-clicking on a blend tree node.

When the blendtree is set up with Animation clips and input parameters, the inspector window gives a graphical visualization of how the animations are combined as the parameter value changes (as you drag the slider, the arrows from the tree root change their shading to show the dominant animation clip).

A 2D Blendtree set up with five animation clips, being previewed in the inspector

You can select any of the nodes in the Blend Tree graph to inspect it in the Inspector. If the selected node is an Animation Clip the Inspector for that Animation Clip will be shown. The settings will be read-only if the animation is imported from a model. If the node is a Blend Node, the Inspector for Blend Nodes will be shown.

You can choose either 1D or 2D blending from the _Blend Type_ menu; the differences between the two types are described on their own pages in this section.

BlendTree