---
title: "Play Asset Delivery"
category: "General"
source_file: "play-asset-delivery.html"
doc_type: "manual"
---

# Play Asset Delivery

Play Asset Delivery (PAD) is the asset splitting solution for the Android App Bundle (AAB) publishing format. PAD uses asset packs to store additional assets such as textures, sounds, and meshes. Google hosts and serves asset packs on Google Play, which means you don’t need to create a content delivery network to send application resources to users. For more information about PAD, see Android’s Play Asset Delivery documentation.

PAD is only available for Google Play and enables applications to be larger than the Google Play application size limit of 200MB.

**Important** : If you have a large application and want to publish it to digital distribution services that don’t support the AAB publishing format, you must use the **APK**

**Topic** | **Description**  
---|---  
Asset packs in Unity | Learn how asset packs work in Unity.  
Set up Play Asset Delivery | Configure your Unity project to produce an AAB that contains asset packs.  
Create a custom asset pack | Create a custom asset pack to store additional assets for an application.  
Manage asset packs at runtime | Download and access asset packs at runtime.  
  
**Notes:**

  * All versions of Unity from 2021.3 support Play Asset Delivery. Support was also added for previous Unity versions in the following patch releases:

    * 2019.4.29f1
    * 2020.3.15f2
    * 2021.1.16f1
    * 2021.2.0f1
  * Unity doesn’t support Play Feature Delivery.

## Additional resources

  * Android application publishing format