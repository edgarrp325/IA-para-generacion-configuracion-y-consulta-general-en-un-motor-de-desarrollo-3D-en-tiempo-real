---
title: "Meshes introduction"
category: "General"
source_file: "mesh-introduction.html"
doc_type: "manual"
---

# Meshes introduction

A mesh is a collection of data that describes a shape. In Unity, you use meshes in the following ways:

  * In graphics, you use meshes together with materials; meshes describe the shape of an object that the GPU renders, and materials describe the appearance of its surface.
  * In physics, you can use a mesh to determine the shape of a **collider**.

## Deformable meshes

In addition to regular meshes, Unity also supports deformable meshes.

Deformable meshes fall into the following categories:

  * Skinned meshes: These meshes work with additional data called bones. Bones form a structure called a skeleton (also called a rig, or joint hierarchy), and the skinned mesh contains data that allows it to deform in a realistic way when the skeleton moves. You usually use skinned meshes for skeletal animation with Unity’s Animation features, but you can also use them with Rigidbody components to create “ragdoll” effects.
  * Meshes with blend shapes: These meshes contain data called blend shapes. Blend shapes describe versions of the mesh that are deformed into different shapes, which Unity interpolates between. You use blend shapes for morph target animation, which is a common technique for facial animation.
  * Meshes that work with a Cloth component component for realistic fabric simulation.

## Creating meshes

You can add meshes to a Unity project in the following ways:

  * Create a mesh as part of a model in a 3D modeling program, then import it. Unity creates a mesh asset as a part of the model hierarchy when you import a model. For more information, see Importing Models.
  * Create a mesh directly with in-Editor tools. Unity has built-in primitive shapes such as spheres and capsules that you can place directly into a **Scene**. You can also use a package like ProBuilder to model a custom mesh in the Editor.
  * Create meshes with code, either at runtime or in the Editor.

## Working with meshes

Unity stores meshes in your project as mesh assets, and represents them in C# code with the Mesh

Depending on how you use meshes, they work with different components:

  * In graphics, Unity renders regular meshes with Mesh Renderer components, and deformable meshes with Skinned Mesh Renderer components.
  * In physics, Unity uses the Mesh Collider component to determine the shape of a collider.

For detailed information about the data that a mesh contains and how Unity represents that data, see Mesh data.