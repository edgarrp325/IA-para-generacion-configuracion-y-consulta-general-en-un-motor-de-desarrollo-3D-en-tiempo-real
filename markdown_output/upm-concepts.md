---
title: "Concepts"
category: "General"
source_file: "upm-concepts.html"
doc_type: "manual"
---

# Concepts

This section explains many of the concepts surrounding the Unity Package Manager functionality:

  * Versions
  * Manifests
  * Registry
  * Package Management
  * Package sources
  * Package types
  * Package states and lifecycle
  * Dependency and resolution
  * Global cache

## Versions

Multiple versions of each package are available, marking changes to that package along its lifecycle. Every time a developer updates the package, they give it a new version number. A change in package version tells you whether it contains a breaking change (major), new backward-compatible functionality (minor), or bug fixes only (patch). These indicators follow Semantic Versioning rules.

To view the list of versions available for a specific package, refer to Finding a specific version.

## Manifests

There are two types of manifest files:

  * Project manifests (`manifest.json`) store information that the Package Manager needs to locate and load the right packages, including a list of packages and versions declared as dependencies.
  * Package manifests (`package.json`) store information about a specific package, and a list of packages and versions that the package requires.

Both files use JSON (JavaScript Object Notation) syntax.

## Registry

In the domain of Unity’s Package Manager, a package registry is a server that stores package contents and information (metadata) on each package version. Unity maintains a central registry of official packages that are available for distribution. By default, all projects use the official Unity package registry. But you can add additional registries to store and distribute private packages or stage custom packages while you are developing them.

## Package management

The Unity Package Manager is a tool that manages the entire package system. Its primary tasks include the following:

  * It communicates with the Unity package registry server and any additional registries you specify.
  * It reads your project manifest and fetches package contents and metadata.
  * It installs, updates, and removes **UPM packages** , whether they’re dependencies of the project or one of the installed packages.
  * It downloads and imports asset packages that you previously acquired from the **Asset Store**
  * It enables and disables Unity’s built-in packages.
  * It displays information about every version of every package.
  * It resolves conflicts when the project and its packages require more than one package version.

The Unity Package Manager installs samples, tools, and assets on a per-project basis, rather than installing them across all projects for a specific machine or device. It uses a global cache to store downloaded package metadata and contents. Once installed in a project, Unity treats package assets similarly to other assets in the project. The only difference is that these assets are stored inside the package folder and are **immutable**. You can permanently change content only from Local and Embedded package sources.

## Package sources

Sources describe where the package came from:

**Source** | **Description**  
---|---  
**Registry** | The Unity Package Manager downloads most packages from a package registry server into a global cache on your computer as you request them. These packages are immutable, so you can use them in your project, but you can’t modify them or change their package manifests.  
**Built-in** | These packages allow you to enable or disable Unity features (for example, Terrain Physics, Animation, etc.). Built-in packages are immutable. For more information, refer to Built-in packages.  
**Embedded** | An embedded package is any package stored inside your project folder. This source corresponds with the Custom state because you typically put all the scripts, libraries, samples, and other assets your new package needs in a folder under your project folder when you begin development on a custom package.  
**Local** | You can install a package from any folder on your computer (for example, if you have cloned a development repository locally).  
**Tarball (local)** | You can install a package from a tarball file on your computer. The Package Manager extracts the package from the tarball and stores it in the cache. However, these packages are immutable, unlike installations from a local folder.  
**Git** | The Package Manager installs **Git** -based packages directly from a Git repository instead of from the package registry server.  
  
To edit the package manifest for a package, refer to Inspecting packages.

The Package Manager window displays a label that corresponds to some of these sources. For more information, refer to Labels.

**Note** : The Package Manager stores packages that you download from the Asset Store in different caches, depending on the package type. 

  * For information about **asset packages** , refer to Asset Store packages.
  * For information about UPM packages, refer to Global cache.