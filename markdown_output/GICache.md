---
title: "GI cache"
category: "General"
source_file: "GICache.html"
doc_type: "manual"
---

# GI cache

The **GI cache** is an internal data cache that the Unity Editor uses to store intermediate files when precomputing lighting data for Baked **Global Illumination** and **Enlighten** and **Enlighten** Realtime Global Illumination. By storing this data in a cache, Unity can speed up subsequent precomputations.

All Unity projects on the computer share the cache so that projects with similar content and the same lightmapping backend can use the same cached files. You can manage the size, location, and **compression** of the cache using the **GI Cache** preferences. For more information, see the Preferences documentation.

## Using the GI Cache

The Unity Editor uses the GI Cache when it precomputes lighting data. To enable the GI Cache, open the Lighting window (**Window** > **Lighting**) and enable the **Auto** option. This makes lighting data precomputation automatic and stores output data in the GI Cache. If you prefer to store lighting data in a Lighting Data Asset instead, disable the **Auto** option. However, even when you disable **Auto** and store precomputed data in a Lighting Data Asset, the Editor stores intermediate results in the GI Cache. You can also set a custom location for the GI cache folder. For more information, refer to Unity Editor special command line arguments.

In the Lighting window, you can clear the baked data in a **Scene** (disable the **Auto** option and choose **Clear Baked Data** from the **Build** (disable the **Auto** option and choose **Clear Baked Data** from the **Build** button drop-down menu). This only removes the data in the scene, it does not clear the GI Cache, because this would increase bake time afterwards. To clean the GICache, go to Preferences documentation. Cleaning the cache should only be done as a last resort and any issues forcing you do do so, should be reported via the bug reporter built into the Editor.

You can copy the _GiCache_ folder among different machines. This can make your lighting build faster, because the files are fetched from the _GiCache_ folder instead of being recomputed.

If you try to bake with more than one instance of the Editor running on the same computer, the Editor displays the following warning message: "The GI Cache is using increasing amounts of space on your hard drive to support concurrent **lightmap** generation. To prevent failed bakes, close all other instances of the Unity Editor.