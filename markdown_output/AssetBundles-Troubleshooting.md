---
title: "Troubleshooting"
category: "General"
source_file: "AssetBundles-Troubleshooting.html"
doc_type: "manual"
---

# Troubleshooting

This section describes several problems that commonly appear in projects using AssetBundles.

## Asset Duplication

Unity’s AssetBundle system will discover all dependencies of an Object when the Object is built into an AssetBundle. This is done using the Asset Database. This dependency information is used to determine the set of Objects that will be included in an AssetBundle.

Assignment to AssetBundles happens at the Asset level. The Objects inside an Asset that is explicitly assigned to an AssetBundle will only be built into that single AssetBundle. Depending which signature of BuildPipeline.BuildAssetBundles is called, an Asset is “explicitly assigned” either by setting the Asset’s AssetImporter.assetBundleName property to a non-empty string, or by listing it in AssetBundleBuild.assetNames.

Any Object that is part of an Asset that is not explicitly assigned in an AssetBundle will be included in each AssetBundle that contains any Objects that reference it.

In other words, if two different Objects are assigned to two different AssetBundles, but both have references to a common dependency Object, then that dependency Object will be copied into both AssetBundles. The duplicated dependency will also be instanced, meaning that the two copies of the dependency Object will be considered different Objects with a different identifiers. This will increase the total size of the application’s AssetBundles. This will also cause two different copies of the Object to be loaded into memory if the application loads both of its parents.

There are several ways to address this problem:

  1. Ensure that Objects built into different AssetBundles do not share dependencies. Any Objects which do share dependencies can be placed into the same AssetBundle without duplicating their dependencies.

     * This method usually is not viable for projects with many shared dependencies. It can produce monolithic AssetBundles that must be rebuilt and re-downloaded too frequently to be convenient or efficient.
  2. Segment AssetBundles so that no two AssetBundles that share a dependency will be loaded at the same time.

     * This method may work for certain types of projects, such as level-based games. However there is still a trade-off, because duplicated objects will increase the build time and sizes of the project’s AssetBundles, and could impact loading times.
  3. Ensure that all dependency assets are built into their own AssetBundles. This entirely eliminates the risk of duplicated assets, but also introduces complexity. The application must track dependencies between AssetBundles, and ensure that the right AssetBundles are loaded before calling any AssetBundle.LoadAsset APIs.

Object dependencies are tracked via the AssetDatabase API, located in the UnityEditor namespace. As the namespace implies, this API is only available in the Unity Editor and not at runtime. AssetDatabase.GetDependencies can be used to locate all of the immediate dependencies of a specific Object or Asset. Note that these dependencies may have their own dependencies so this can be a recursive calculation. The assignment of Assets to AssetBundles will either be defined explicitly by passing arrays of AssetBundleBuild structures when calling BuildPipeline.BuildAssetBundles, or can be queried using the AssetImporter API. It is possible to write an Editor script that ensures that all of an AssetBundle’s direct or **indirect dependencies**

**Note** : When building AssetBundles with the Addressables package, the `Addressables Analyze` window can be used to discover duplicated assets.

## Sprite Atlas Duplication

The following sections describe a quirk of asset dependency calculation code when used in conjunction with automatically-generated **sprite** atlases.

Any automatically-generated **sprite atlas** will be assigned to the AssetBundle containing the Sprite Objects from which the sprite atlas was generated. If the sprite Objects are assigned to multiple AssetBundles, then the sprite atlas will not be assigned to an AssetBundle and will be duplicated. If the Sprite Objects are not assigned to an AssetBundle, then the sprite atlas will also not be assigned to an AssetBundle.

To ensure that sprite atlases are not duplicated, check that all sprites tagged into the same sprite atlas are assigned to the same AssetBundle.

## Android Textures

Due to heavy device fragmentation in the Android ecosystem, it is often necessary to compress textures into several different formats. While all Android devices support ETC1, ETC1 does not support textures with alpha channels. Should an application not require OpenGL ES 2 support, the cleanest way to solve the problem is to use ETC2, which is supported by all Android OpenGL ES 3 devices.

Most applications need to ship on older devices where ETC2 support is unavailable. One way to solve this problem is with AssetBundle Variants. (Please see Unity’s Android optimization guide for details on other options.)

To use AssetBundle Variants, all textures that cannot be cleanly compressed using ETC1 must be isolated into texture-only AssetBundles. Next, create sufficient variants of these AssetBundles to support the non-ETC2-capable slices of the Android ecosystem, using vendor-specific texture **compression** formats such as DXT5, PVRTC and ATITC. For each AssetBundle Variant, change the included textures’ TextureImporter settings to the compression format appropriate to the Variant.

At runtime, support for the different **texture compression** formats can be detected using the SystemInfo.SupportsTextureFormat API. This information should be used to select and load the AssetBundle Variant containing textures compressed in a supported format.

More information on Android texture compression formats can be found here.

## Interactions between Shaders and AssetBundles

When you build an AssetBundle, Unity uses information in that bundle to select which **shader** variants to compile. This includes information about the **scenes** variants to compile. This includes information about the **scenes** , materials, Graphics Settings, and ShaderVariantCollections in the AssetBundle.

Separate build pipelines compile their own shaders independently of other pipelines. If both a Player build and an Addressables build reference a shader, Unity compiles two separate copies of the shader, one for each pipeline.

This process doesn’t account for any runtime information such as keywords, textures, or changes due to code execution. If you want to include specific shaders in your build, either include a ShaderVariantCollection with the desired shaders, or include the shader in your build manually by adding it to the Always Included Shaders list in your graphics settings.