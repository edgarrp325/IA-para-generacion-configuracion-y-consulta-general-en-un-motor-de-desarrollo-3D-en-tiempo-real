---
title: "AssetBundle Dependencies"
category: "General"
source_file: "AssetBundles-Dependencies.html"
doc_type: "manual"
---

# AssetBundle Dependencies

AssetBundles can become dependent on other AssetBundles if one or more of the `UnityEngine.Objects` contains a reference to a `UnityEngine.Object` located in another bundle. A dependency does not occur if the `UnityEngine.Object` contains a reference to a `UnityEngine.Object` that is not contained in any AssetBundle. In this case, a copy of the object that the bundle would be dependent on is copied into the bundle when you build the AssetBundles. If multiple objects in multiple bundles contain a reference to the same object that isn’t assigned to a bundle, every bundle that would have a dependency on that object will make its own copy of the object and package it into the built AssetBundle.

Should an AssetBundle contain a dependency, it is important that the bundles that contain those dependencies are loaded before the object you’re attempting to instantiate is loaded. Unity will not attempt to automatically load dependencies.

Consider the following example, a Material in **Bundle 1** references a Texture in **Bundle 2** :

In this example, before loading the Material from **Bundle 1** , you would need to load **Bundle 2** into memory. It does not matter which order you load **Bundle 1** and **Bundle 2** , the important takeaway is that **Bundle 2** is loaded before loading the Material from **Bundle 1**. In the next section, we’ll discuss how you can use the `AssetBundleManifest` objects we touched on in the previous section to determine, and load, dependencies at runtime.

## Duplicated information across AssetBundles

By default, Unity doesn’t optimize duplicated information across AssetBundles. This means multiple AssetBundles in your Project might contain the same information, such as a Material which is used by multiple **Prefabs**. Assets which are used in multiple AssetBundles are known as common Assets. These can affect memory resources and loading times. 

This page describes how Unity manages duplicated information across AssetBundles, and how you can apply optimization. 

### Editor setup

By default, Unity doesn’t perform any optimization to reduce or minimize the memory required to store duplicate information. During build creation, Unity builds duplicates of any implicitly referenced Assets inside the AssetBundles. To prevent this duplication, assign common Assets (such as Materials) to their own AssetBundle.

For example: you could have an application with two Prefabs, both of which are assigned to their own AssetBundle. Both Prefabs share the same Material, which is not assigned to an AssetBundle. This Material references a Texture, which is not assigned to an AssetBundle.

If you follow the AssetBundle Workflow and use the example class `CreateAssetBundles` to build AssetBundles, each generated AssetBundle contains the Material (including its Shader and referenced Textures). In the example image below, the Prefab files have a size of 383 KB and 377 KB respectively.

If the project contains a larger number of Prefabs, this behaviour impacts the final installer size, and the runtime memory footprint when both AssetBundles are loaded. Data duplication across AssetBundles also impacts batching, because Unity considers each copy of the same Material as a unique Material.

To avoid data duplication, assign the Material and its referenced Assets to its own `modulesmaterials` AssetBundle. You can also tag the Material only, because the Texture dependency is also included in the AssetBundle automatically during the build process.

Now if you rebuild the AssetBundles, the generated output includes a separate `modulesmaterials` AssetBundle (359 KB), which contains the Material and its associated Texture. This significantly reduces the size of the other AssetBundles for the Prefabs (from roughly 380 KB in the previous iteration down to roughly 20 KB).

The image below illustrates this.

### Runtime loading

When you extract common Assets to a single AssetBundle, be careful about dependencies. In particular, if you only use a Prefab to instantiate a module, the Materials do not load.

A Prefab without a loaded Material

To solve this problem, load the Materials AssetBundle in memory before you load the AssetBundle that belongs to the module. In the following example, this happens in the variable `materialsAB`.
    
    
    using System.IO;
    using UnityEngine;
    
    public class InstantiateAssetBundles : MonoBehaviour
    {
        void Start()
        {
            var materialsAB = AssetBundle.LoadFromFile(Path.Combine(Application.dataPath, Path.Combine("AssetBundles", "modulesmaterials")));
            var moduleAB = AssetBundle.LoadFromFile(Path.Combine(Application.dataPath, Path.Combine("AssetBundles", "example-prefab")));
    
            if (moduleAB == null)
            {
                Debug.Log("Failed to load AssetBundle!");
                return;
            }
            var prefab = moduleAB.LoadAsset<GameObject>("example-prefab");
            Instantiate(prefab);
        }
    }
    
    

A Prefab with a correctly loaded Material

**Note:** When you use LZ4 compressed and uncompressed AssetBundles, AssetBundle.LoadFromFile only loads the catalog of its content in memory, but not the content itself. To check if this is happening, use the Memory Profiler package to inspect memory usage.