---
title: "Unity’s Package Manager"
category: "General"
source_file: "Packages.html"
doc_type: "manual"
---

# Unity’s Package Manager

A _package_ is a container that stores various types of features or assets, such as:

  * Editor tools and libraries, such as a text editor, an animation viewer, or test frameworks.
  * Runtime tools and libraries, such as the Physics API or a Graphics pipeline.
  * Asset collections, such as Textures or animations.
  * Project templates to share common project types with others.

Packages deliver a wide range of enhancements to Unity through the Package Manager. To help find and use these packages, the Package Manager window provides collections of packages that you can use together, called _feature sets_.

In the Editor, you can access the Package Manager window through this menu: **Window** > **Package Manager**.

The Package Manager also supports management of packages you download or import from the Unity **Asset Store**. 

Unity provides three Package Manager interfaces: Package Manager window, Scripting API, and manifest files. The following table contains introductions to each interface, and more.

**Topic** | **Description**  
---|---  
**How Unity works with packages** | Get an overview of Unity’s Package Manager.  
**Concepts** | Learn the principles and features of the Package Manager, including concepts like versions, manifests, registries, states, sources, the package lifecycle, and dependency and resolution.  
**Package Manager window** | Find packages and manage them in your project, and resolve conflicts in package dependencies. The Package Manager provides a user interface that makes changes to the Project manifest directly.  
**Scripting API for packages** | Use the Scripting API to interact with the Package Manager using C# **scripts**. View samples to see how to query the package registry, install, embed, and remove packages, and list packages using a variety of criteria.  
**Project manifest** | Learn about the file that the Unity Package Manager reads so it can compute a list of packages to retrieve and load. See also Package manifest.  
**Inspecting packages** | Use a dedicated **Inspector** window to view any package manifest. Use this window to directly edit package manifests for embedded or local packages.  
**Scoped Registries** | Learn how to set up or access a custom registry server. Use this registry server to host and distribute (or consume) custom packages, in addition to the registry that Unity provides.  
**Configuration** | Learn how configure scoped registry authentication, solve network issues, customize cache locations, and more.  
**Resolution and conflict** | Learn how the Package Manager determines the direct and **indirect dependencies** of a project and evaluates all the requested package versions before retrieving the best version from the registry.  
**Troubleshooting** | Match a symptom to a possible solution if any of your project’s packages, including the Package Manager window itself, fails to load.  
  
## Additional resources

  * Asset Store packages
  * Embedded packages
  * Local packages
  * Package manifest