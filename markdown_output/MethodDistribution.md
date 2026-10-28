---
title: "Methods of distribution"
category: "General"
source_file: "MethodDistribution.html"
doc_type: "manual"
---

# Methods of distribution

After you prepare the Sprite Atlases for distribution, there are several methods to distribute the Atlases. Each method is more suitable for different Project needs or characteristics, such as the size of the Atlas Assets or the target platform of the Project.

The following are the two main methods to consider when you distribute **Sprite** Atlases:

  1. Place the Sprite Atlases into the build’s _Resources_ folder.
  2. Distribute them as downloadable AssetBundles.

## Method A: Resources folder

Unity can distribute Sprite Atlases in the final build, as long as it is within the size limits of their chosen target platform. To distribute Sprite Atlases together with the final build, place them in the Project’s `Resource` folder, which includes Sprite Atlases in the exported build when users download the application. Unity then loads these Atlases from the `Resource` folder via script). Refer to documentation on the Resources API for more information.

## Method B: Downloadable AssetBundles

Sprite Atlases that are large in size can cause inconvenience for the application user if Unity includes them with the exported build’s download, because they require a lot of bandwidth and device storage. To avoid problems, distribute large Sprite Atlases in **AssetBundles** , so that the player can download each AssetBundle individually at their discretion. Unity then loads the Sprite Atlases during run time via script. Refer to the AssetBundle Workflow for more information.