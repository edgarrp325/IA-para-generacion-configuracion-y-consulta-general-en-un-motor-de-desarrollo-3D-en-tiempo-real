---
title: "Using AssetBundles Natively"
category: "General"
source_file: "AssetBundles-Native.html"
doc_type: "manual"
---

# Using AssetBundles Natively

There are four different APIs that you can use to load AssetBundles. Their behavior varies based on the platform the bundle is being loaded and the **compression** method used when the AssetBundles were built (uncompressed, LZMA, LZ4). 

The four APIs we have to work with are:

  * AssetBundle.LoadFromMemoryAsync
  * AssetBundle.LoadFromFile
  * WWW.LoadfromCacheOrDownload
  * UnityWebRequestAssetBundle’s DownloadHandlerAssetBundle (Unity 5.3 or newer)

## AssetBundle.LoadFromMemoryAsync

AssetBundle.LoadFromMemoryAsync

This function takes an array of bytes that contains AssetBundle data. Optionally you can also pass in a CRC value if you desire. If the bundle is LZMA compressed it will decompress the AssetBundle while it’s loading. LZ4 compressed bundles are loaded in their compressed state.

Here’s one example of how to use this method:
    
    
    using UnityEngine;
    using System.Collections;
    using System.IO;
    
    public class Example : MonoBehaviour
    {
        IEnumerator LoadFromMemoryAsync(string path)
        {
            AssetBundleCreateRequest createRequest = AssetBundle.LoadFromMemoryAsync(File.ReadAllBytes(path));
            yield return createRequest;
            AssetBundle bundle = createRequest.assetBundle;
            var prefab = bundle.LoadAsset<GameObject>("MyObject");
            Instantiate(prefab);
        }
    }
    

However, this is not the only strategy that makes using LoadFromMemoryAsync possible. File.ReadAllBytes(path) could be replaced with any desired procedure of obtaining a byte array.

## AssetBundle.LoadFromFile

AssetBundle.LoadFromFile

This API is highly-efficient when loading uncompressed bundles from local storage. LoadFromFile will load the bundle directly from disk if the bundle is uncompressed or chunk (LZ4) compressed. Loading a fully compressed (LZMA) bundle with this method will first decompress the bundle before loading it into memory.

One example of how to use `LoadFromFile`:
    
    
    using System.IO;
    using UnityEngine;
    
    public class LoadFromFileExample : MonoBehaviour
    {
        void Start()
        {
            var myLoadedAssetBundle = AssetBundle.LoadFromFile(Path.Combine(Application.streamingAssetsPath, "myassetBundle"));
    
            if (myLoadedAssetBundle == null)
            {
                Debug.Log("Failed to load AssetBundle!");
                return;
            }
            var prefab = myLoadedAssetBundle.LoadAsset<GameObject>("MyObject");
            Instantiate(prefab);
        }
    }
    

Note: On Android devices with Unity 5.3 or older, this API will fail when trying to load AssetBundles from the Streaming Assets path. This is because the contents of that path will reside inside a compressed .jar file. Unity 5.4 and newer can use this API call with Streaming Assets just fine.

## UnityWebRequestAssetBundle

UnityWebRequestAssetBundle

The UnityWebRequestAssetBundle has a specific API call to deal with AssetBundles. To begin, you’ll need to create your web request using `UnityWebRequestAssetBundle.GetAssetBundle`. After returning the request, pass the request object into `DownloadHandlerAssetBundle.GetContent(UnityWebRequestAssetBundle)`. This `GetContent` call will return your AssetBundle object.

You can also use the `assetBundle` property on the DownloadHandlerAssetBundle class after downloading the bundle to load the AssetBundle with the efficiency of `AssetBundle.LoadFromFile`.

Here’s an example of how to load an AssetBundle that contains two **GameObjects** and Instantiate them. To begin this process, we’d just need to call `StartCoroutine(InstantiateObject())`;
    
    
    IEnumerator InstantiateObject()
    {
        string uri = "file:///" + Application.dataPath + "/AssetBundles/" + assetBundleName; 
        UnityEngine.Networking.UnityWebRequestAssetBundle request 
            = UnityEngine.Networking.UnityWebRequestAssetBundle.GetAssetBundle(uri, 0);
        yield return request.SendWebRequest();
        AssetBundle bundle = DownloadHandlerAssetBundle.GetContent(request);
        GameObject cube = bundle.LoadAsset<GameObject>("Cube");
        GameObject sprite = bundle.LoadAsset<GameObject>("Sprite");
        Instantiate(cube);
        Instantiate(sprite);
    }
    

#### Loading Assets from AssetBundles

Now that you’ve successfully downloaded your AssetBundle, it’s time to finally load in some Assets.

Generic code snippet:
    
    
    T objectFromBundle = bundleObject.LoadAsset<T>(assetName);
    

T is the type of the Asset you’re attempting to load. 

There are a couple options when deciding how to load Assets. We have `LoadAsset`, `LoadAllAssets`, and their Async counterparts `LoadAssetAsync` and `LoadAllAssetsAsync` respectively.

This is how to load an asset from an AssetBundles synchronously:

To load a single GameObject:
    
    
    GameObject gameObject = loadedAssetBundle.LoadAsset<GameObject>(assetName);
    

To load all Assets:
    
    
    Unity.Object[] objectArray = loadedAssetBundle.LoadAllAssets();
    

Now, where as the previously shown methods return either the type of object you’re loading or an array of objects, the asynchronous methods return an AssetBundleRequest. You’ll need to wait for this operation to complete before accessing the asset. To load an asset:
    
    
    AssetBundleRequest request = loadedAssetBundleObject.LoadAssetAsync<GameObject>(assetName);
    yield return request;
    var loadedAsset = request.asset;
    

And
    
    
    AssetBundleRequest request = loadedAssetBundle.LoadAllAssetsAsync();
    yield return request;
    var loadedAssets = request.allAssets;
    

Once you have loaded your Assets you’re good to go! You’re able to use the loaded objects as you would any Object in Unity.

#### Loading AssetBundle Manifests

Loading AssetBundle manifests can be incredibly useful. Especially when dealing with AssetBundle dependencies.

To get a useable AssetBundleManifest object, you’ll need to load that additional AssetBundle (the one that’s named the same thing as the folder it’s in) and load an object of type AssetBundleManifest from it.

Loading the manifest itself is done exactly the same as any other Asset from an AssetBundle:
    
    
    AssetBundle assetBundle = AssetBundle.LoadFromFile(manifestFilePath);
    AssetBundleManifest manifest = assetBundle.LoadAsset<AssetBundleManifest>("AssetBundleManifest");
    

Now you have access to the `AssetBundleManifest` API calls through the manifest object from the above example. From here you can use the manifest to get information about the AssetBundles you built. This information includes dependency data, hash data, and variant data for the AssetBundles.

Remember in the earlier section when we discussed AssetBundle Dependencies and how, if a bundle had a dependency on another bundle, those bundles would need to be loaded in before loading any Assets from the original bundle? The manifest object makes dynamically finding a loading dependencies possible. Let’s say we want to load all the dependencies for an AssetBundle named “assetBundle”. 
    
    
    AssetBundle assetBundle = AssetBundle.LoadFromFile(manifestFilePath);
    AssetBundleManifest manifest = assetBundle.LoadAsset<AssetBundleManifest>("AssetBundleManifest");
    string[] dependencies = manifest.GetAllDependencies("assetBundle"); //Pass the name of the bundle you want the dependencies for.
    foreach(string dependency in dependencies)
    {
        AssetBundle.LoadFromFile(Path.Combine(assetBundlePath, dependency));
    }
    

Now that you’re loading AssetBundles, AssetBundle dependencies, and Assets, it’s time to talk about managing all of these loaded AssetBundles.

## Managing Loaded AssetBundles

**Note:** The Addressable Assets package provides a ready-made system to manage loading Asset Bundles, dependencies, and Assets. Unity recommends using Addressables rather than managing AssetBundles yourself.

See also: Unity Learn tutorial on Managing Loaded AssetBundles

Unity does not automatically unload Objects when they are removed from the active **scene**. Asset cleanup is triggered at specific times, and it can also be triggered manually.

It is important to know when to load and unload an AssetBundle. Improperly unloading an AssetBundle can lead to duplicating objects in memory or other undesirable circumstances, such as missing textures.

The biggest things to understand about AssetBundle management is when to call AssetBundle.Unload(bool) – or AssetBundle.UnloadAsync(bool) – and if you should pass true or false into the function call. Unload is a non-static function that will unload your AssetBundle. This API unloads the header information of the AssetBundle being called. The argument indicates whether to also unload all Objects instantiated from this AssetBundle.

`AssetBundle.Unload(true)` unloads all GameObjects (and their dependencies) that were loaded from the AssetBundle. This does not include copied GameObjects (such as Instantiated GameObjects), because they no longer belong to the AssetBundle. When this happens, Textures that are loaded from that AssetBundle (and still belong to it) disappear from GameObjects in the Scene, and Unity treats them as missing Textures.

Let’s assume Material M is loaded from AssetBundle AB as shown below and used in **Prefab** P.

If AB.Unload(true) is called. Any instance of M in the active scene will also be unload and destroyed. 

If you were instead to call AB.Unload(false) it would break the chain of the current instances of M and AB.

If AB is loaded again later and AB.LoadAsset() is called, Unity will not re-link the existing copies of M to the newly loaded Material. 

If you create another instance of Prefab P, it will not use the existing copy of M. Instead two copies of M are loaded.

Generally, using `AssetBundle.Unload(false)` does not lead to an ideal situation. Most projects should use `AssetBundle.Unload(true)` and adopt a method to ensure that Objects are not duplicated. Two common methods are:

  * Having well-defined points during the application’s lifetime at which transient AssetBundles are unloaded, such as between levels or during a loading screen. 

  * Maintaining reference-counts for individual Objects and unload AssetBundles only when all of their constituent Objects are unused. This permits an application to unload & reload individual Objects without duplicating memory.

If an application must use `AssetBundle.Unload(false)`, then individual Objects can only be unloaded in two ways:

  * Eliminate all references to an unwanted Object, both in the scene and in code. After this is done, call Resources.UnloadUnusedAssets.

  * Load a scene non-additively. This will destroy all Objects in the current scene and invoke Resources.UnloadUnusedAssets automatically.