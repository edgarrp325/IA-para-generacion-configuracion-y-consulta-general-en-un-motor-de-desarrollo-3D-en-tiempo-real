---
title: "AssetBundle workflow"
category: "General"
source_file: "AssetBundles-Workflow.html"
doc_type: "manual"
---

# AssetBundle workflow

To get started with AssetBundles, follow these steps. More detailed information about each piece of the workflow can be found in the other pages in this section of documentation.

**Note** : This section describes the creation of AssetBundles using the built-in BuildPipeline.BuildAssetBundles() API. A recommended, and more user friendly, alternative is to use the Addressables package.

## Assigning Assets to AssetBundles

To assign a given Asset to an AssetBundle, follow these steps:

  1. Select the Asset you want to assign to a bundle from your Project View.
  2. Examine the object in the **Inspector**.
  3. At the bottom of the Inspector, there is a section to assign AssetBundles and Variants. Use the left-hand drop down to assign the AssetBundle, and the right-hand drop down to assign the variant.
  4. Click **None** on the left-hand drop to reveal the currently registered AssetBundle names.
  5. Click **New** to create a new AssetBundle
  6. Type in the desired AssetBundle name. **Note:** AssetBundle names support a type of folder structure depending on what you type. To add sub-folders, separate folder names by a `/`. For example, use the AssetBundle name `environment/forest` to create a bundle named `forest` under an `environment` sub-folder
  7. Once you’ve selected or created an AssetBundle name, you can repeat this process for the right hand drop down to assign or create a Variant name, if you desire. Variant names are not required to build the AssetBundles

**Note:** In the Inspector you can assign an AssetBundle to a folder in your Project. By default, all Assets in that folder are assigned to the same AssetBundle as the folder. The AssetBundle assignments for individual Assets takes precedence, however.

To read more information on AssetBundle assignments and accompanying strategies, see documentation on Preparing Assets for AssetBundles.

## Build the AssetBundles

Create a folder called Editor in the Assets folders, and place a script with the following contents in the folder:
    
    
    using UnityEditor;
    using System.IO;
    
    public class CreateAssetBundles
    {
        [MenuItem("Assets/Build AssetBundles")]
        static void BuildAllAssetBundles()
        {
            string assetBundleDirectory = "Assets/AssetBundles";
            if(!Directory.Exists(assetBundleDirectory))
            {
                Directory.CreateDirectory(assetBundleDirectory);
            }
            BuildPipeline.BuildAssetBundles(assetBundleDirectory, 
                                            BuildAssetBundleOptions.None, 
                                            BuildTarget.StandaloneWindows);
        }
    }
    

This script creates a menu item at the bottom of the Assets menu called **Build AssetBundles** that executes the code in the function associated with that tag. When you click **Build AssetBundles** a progress bar appears with a build dialog. This takes all the Assets you labeled with an AssetBundle name and places them in a folder at the path `assetBundleDirectory` defines.

**Note:** You can also define the content of AssetBundles programmatically instead of using the Inspector-based method described above. This is available by using a signature of BuildPipeline.BuildAssetBundles that accepts an array of AssetBundleBuild structures. In that case the list of desired Assets for each bundle are passed in, and any assignment to AssetBundles made in the Inspector is ignored.

For more details about this, see documentation on Building AssetBundles.

## Loading AssetBundles and Assets

If you want to load from local storage, use the `AssetBundles.LoadFromFile` API, which looks like this:
    
    
    public class LoadFromFileExample : MonoBehaviour {
        void Start() {
            var myLoadedAssetBundle 
                = AssetBundle.LoadFromFile(Path.Combine(Application.streamingAssetsPath, "myassetBundle"));
            if (myLoadedAssetBundle == null) {
                Debug.Log("Failed to load AssetBundle!");
                return;
            }
            var prefab = myLoadedAssetBundle.LoadAsset<GameObject>("MyObject");
            Instantiate(prefab);
        }
    }
    

`LoadFromFile` takes the path of the bundle file.

If your AssetBundles are hosted online, or you are running on a platform that does not support direct file system access, then use the `UnityWebRequestAssetBundle` API. Here’s an example:
    
    
    IEnumerator InstantiateObject()
    {
        string url = "file:///" + Application.dataPath + "/AssetBundles/" + assetBundleName;        
        var request 
            = UnityEngine.Networking.UnityWebRequestAssetBundle.GetAssetBundle(url, 0);
        yield return request.Send();
        AssetBundle bundle = UnityEngine.Networking.DownloadHandlerAssetBundle.GetContent(request);
        GameObject cube = bundle.LoadAsset<GameObject>("Cube");
        GameObject sprite = bundle.LoadAsset<GameObject>("Sprite");
        Instantiate(cube);
        Instantiate(sprite);
    }
    

`GetAssetBundle(string, int)` takes the URL of the location of the AssetBundle and the version of the bundle you want to download. This example points to a local file, but `string url` could point to any URL you have your AssetBundles hosted at.

The UnityWebRequestAssetBundle class has a specific handle for dealing with AssetBundles, `DownloadHandlerAssetBundle`, which gets the AssetBundle from the request.

Regardless of the method you use, you now have access to the AssetBundle object. From that object you need to use `LoadAsset<T>(string)` which takes the type, `T`, of the asset you’re attempting to load and the name of the object as a string that’s inside the bundle. This returns whatever object you’re loading from the AssetBundle. You can use these returned objects just like any object inside of Unity. For example, if you want to create a GameObject in the scene, you just need to call `Instantiate(gameObjectFromAssetBundle)`. 

For more information on APIs that load AssetBundles, see documentation on Using AssetBundles Natively.