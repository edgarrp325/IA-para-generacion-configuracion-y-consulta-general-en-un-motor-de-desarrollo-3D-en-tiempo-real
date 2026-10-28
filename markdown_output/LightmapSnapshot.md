---
title: "Lighting Data Asset"
category: "General"
source_file: "LightmapSnapshot.html"
doc_type: "manual"
---

# Lighting Data Asset

A Lighting Data Asset stores precomputed lighting data for a Scene in the Unity Editor. Lighting Data Assets exist as separate files in your Project for workflow reasons; storing precomputed lighting data in a separate file means that changes to the precomputed lighting data do not result in changes to the Scene file. Lighting Data Assets are not intended for users to edit.

Unity stores precomputed lighting data in a Lighting Data Asset when you manually invoke a lighting precompute, either by using the **Generate Lighting** button in the Lighting window, or by using the Lightmapping.Bake or Lightmapping.BakeAsync APIs.

The Lighting Data Asset contains **global illumination** data and all the supporting files needed to recreate the lighting for a **scene** data and all the supporting files needed to recreate the lighting for a **scene**. This asset references the renderers, the real-time **lightmaps**. This asset references the renderers, the real-time **lightmaps** , the baked lightmaps, **light probes** , the baked lightmaps, **light probes** , **reflection probes** , **reflection probes** and a data structure which stores the relationships between these elements. It also includes all the precomputed **Enlighten** and a data structure which stores the relationships between these elements. It also includes all the precomputed **Enlighten** Realtime Global Illumination data needed to update how real-time global illumination looks in the Player.

When you change the scene, for instance by breaking a **prefab** connection on a **GameObject** connection on a **GameObject** that is marked as **Contribute GI** , the asset data will get out of date and has to be rebuilt.

The intermediate files that are generated during the lighting build process, but is not needed for generating a Player build is not part of the asset, they are stored in the GI Cache instead.

The build time for the Lighting Data Asset can vary. If your GI Cache is fully populated i.e. you have done a bake on the machine before (with the scene in its current state) it will be fast. If you are pulling the scene to a machine with a blank cache or the cache data needed has been removed due to the cache size limit, the cache will have to be populated with the intermediate files first which requires the precompute and bake processes to run. These steps can take some time.