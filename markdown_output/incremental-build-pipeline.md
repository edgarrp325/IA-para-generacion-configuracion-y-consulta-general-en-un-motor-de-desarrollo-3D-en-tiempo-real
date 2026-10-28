---
title: "Incremental build pipeline"
category: "General"
source_file: "incremental-build-pipeline.html"
doc_type: "manual"
---

# Incremental build pipeline

For faster iteration during development, Unity uses an incremental build pipeline that only rebuilds parts of the application if they have changed since the previous build (stored in the project’s `Library/Bee` directory), including build steps such as asset serialization, code compilation, data **compression** , and signing.

This setup has a local cache that reuses some specific parts of builds (such as non-embedded packages and libIL2CPP artifacts) across different projects. The location of this cache is set using the `BEE_CACHE_DIRECTORY` environment variable, and defaults to a different location depending on your operating system:

  * On Windows, `BEE_CACHE_DIRECTORY` defaults to `%USERPROFILE%\AppData\Local\Unity\Caches\bee`
  * On Mac, `BEE_CACHE_DIRECTORY` defaults to `$HOME/Library/Unity/cache/bee`
  * On Linux, `BEE_CACHE_DIRECTORY` defaults to `$XDG_CONFIG_HOME/.cache/unity3d/bee` (if `$XDG_CONFIG_HOME` is set) or `$HOME/.cache/unity3d/bee`

The incremental build pipeline also automates the Scripts Only Build feature. ****Scripts****

The incremental build pipeline works for both the Mono and **IL2CPP** scripting backend scripting backend, although the output file structure changes depending on which scripting backend your project uses.

By default, Unity uses the incremental build pipeline for both release and **development builds**. See the Creating non-incremental builds section below for details on how to make a clean build, which may be useful if the cache has been corrupted somehow.

## Platform compatibility

Unity supports the incremental build pipeline for the following platforms:

  * Standalone (Windows, Mac and Linux)
  * WebGL
  * Xbox One
  * Xbox Series X and Xbox Series S
  * Android
  * iOS
  * tvOS

## Creating non-incremental builds

In some scenarios, it can be useful or necessary to create builds that don’t use the incremental build pipeline.

To create a clean, non-incremental, build:

  1. Open the Build Settings window.
  2. Next to the **Build** button, select the drop-down.
  3. Select **Clean Build**.

In general, if expected changes are not present after an incremental build and you think there is a problem with the incremental build pipeline, create a clean build. The most common reason for this is when you implement or make changes to build process callbacks that affect assets.

Since the build process can’t know how a callback you’ve implemented affects an asset, it can’t determine how to rebuild the asset. Unity only regenerates files if the file’s dependencies change. This means if the callback modifies a file that Unity generates, and the file’s dependencies don’t change, the callback can apply modifications to an already modified file. For example, if the callback adds new entries to an Android App Manifest, and the dependencies for the Android App Manifest don’t change, the callback still adds the new entries, which results in an invalid file.

If you change a callback or its input data and you want Unity to rebuild assets that the callback affects, create a clean build. Examples of callbacks include:

  * PostProcessSceneAttribute
  * IPreprocessShaders.OnProcessShader
  * IPreprocessComputeShaders.OnProcessComputeShader

**Note** : If you make changes to an asset, Unity rebuilds that asset when it builds the application. This also includes processing any callback that affects it which means you don’t need to create a clean build if you make changes to an asset, only if you make changes to a build process callback.