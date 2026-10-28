---
title: "The Resources folder"
category: "General"
source_file: "UnderstandingPerformanceResourcesFolder.html"
doc_type: "manual"
---

# The Resources folder

The _Resources_ folder is a common source of many problems in Unity projects. Improper use of the _Resources_ folder can bloat the size of a project’s build, lead to uncontrollable excessive memory utilization, and significantly increase application startup times.

While the problems that this folder make it less suitable for production applications, it can still be useful for fast prototyping. For full production of new projects, you should usually use the Addressables package for asset organization.

If you have an existing project that uses the Resources folder, or you want to use the folder for a prototype, you can use the AssetBundles and Resources series of articles to understand more about organizing your assets in this folder. Use the Resources article from this series to learn more about the problems with the Resources folder and how to use it properly if you need to.

Although you can still use the Resources folder, the tutorial resources are deprecated. They might contain outdated information and you should only use them as a reference for working with the Resources folder.