---
title: "AssetBundles"
category: "General"
source_file: "AssetBundlesIntro.html"
doc_type: "manual"
---

# AssetBundles

An **AssetBundle** is an archive file that contains platform-specific non-code Assets (such as Models, Textures, Prefabs, Audio clips, and even entire Scenes) that Unity can load at run time. AssetBundles can express dependencies between each other; for example, a Material in one AssetBundle can reference a Texture in another AssetBundle. For efficient delivery over networks, you can compress AssetBundles with a choice of built-in algorithms depending on use case requirements (LZMA and LZ4).

AssetBundles can be useful for downloadable content (DLC), reducing initial install size, loading assets optimized for the end-user’s platform, and reduce runtime memory pressure.

**Note:** An AssetBundle can contain the serialized data of an instance of a code object, such as a ScriptableObject. However, the class definition itself is compiled into one of the Project assemblies. When you load a serialized object in an AssetBundle, Unity finds the matching class definition, creates an instance of it, and sets that instance’s fields using the serialized values. This means that you can introduce new items to your game in an AssetBundle as long as those items do not require any changes to your class definitions. 

## What’s in an AssetBundle?

“AssetBundle” can refer to two different, but related things. 

First is the actual file on disk. This is called the AssetBundle archive. The AssetBundle archive is a container, like a folder, that holds additional files inside it. These additional files consist of two types:

  * A serialized file, which contains your Assets broken out into their individual objects and written out to this single file.
  * Resource files, which are chunks of binary data stored separately for certain Assets (Textures and audio) to allow Unity to efficiently load them from disk on another thread.

“AssetBundle” can also refer to the actual AssetBundle object you interact with via code to load Assets from a specific AssetBundle archive. This object contains a map of all the file paths of the Assets you added to this archive.