---
title: "Late binding"
category: "General"
source_file: "LateBinding.html"
doc_type: "manual"
---

# Late binding

Late binding is the process of loading or swapping in a Sprite Atlas at runtime via the Sprite Atlas API. It’s necessary when the atlas isn’t available during start-up, such as when loading assets from AssetBundles. You can choose to bind different Sprite Atlases based on specific criteria, such as loading a high or low-resolution **Sprite** at runtime via the Sprite Atlas API. It’s necessary when the atlas isn’t available during start-up, such as when loading assets from AssetBundles. You can choose to bind different Sprite Atlases based on specific criteria, such as loading a high or low-resolution **Sprite** Atlas ford different platforms to improve performance and efficiency.

After you pack your sprites into a Sprite Atlas in your project, you can decide whether to include the Sprite Atlas with the published build. To exclude the Sprite Atlas from the build, clear **Include in Build** in the Sprite Atlas’ properties. When not included in a build, the Sprite Atlas isn’t loaded at runtime and sprites that reference textures packed into the atlas will appear blank until you use late binding to load the atlas. Note that this also means that Unity Editor won’t automatically load the Sprite Atlas and that your sprites will appear blank when you enter Play mode.

Additional samples of the different ways and scenarios to use Sprite Atlases and late binding are available for download from the 2D Common package’s **Samples** tab.

## Loading a Sprite Atlas with SpriteAtlasManager.atlasRequested 

`atlasRequested` is a callback that tells you when a sprite, which isn’t included in the build, is requested. You need to manually load the Sprite Atlas with late binding, and send the sprite to the Unity Editor.

The following example demonstrates how to set up the callback to load the Sprite Atlas from an AssetBundle with late binding. Note that this script is for loading and binding a Sprite Atlas to sprites which already exist in the build or project. You can create sprites that don’t exist in the project from a Sprite Atlas by retrieving the sprite atlas’ contents at runtime with `GetSprites`
    
    
    void OnEnable()
    {
        SpriteAtlasManager.atlasRequested += RequestAtlas;
    }
    void OnDisable()
    {
        SpriteAtlasManager.atlasRequested -= RequestAtlas;
    }
    void RequestAtlas(string tag, System.Action callback)
    {
        if (spriteAtlas == null)
        {
            StartCoroutine(LoadFromStreammingAsset(callback));
        }
        else
        {
            callback(spriteAtlas);
        }
    }
    
    IEnumerator LoadFromStreammingAsset(System.Action callback)
    {
        string path = Application.streamingAssetsPath + "/" + bundleName;
        print(path);
        AssetBundleCreateRequest bundleLoadRequest = AssetBundle.LoadFromFileAsync(Application.streamingAssetsPath + "/" + bundleName);
        yield return bundleLoadRequest;
        bundle = bundleLoadRequest.assetBundle;
        if (bundle == null)
        {
            Debug.Log("Failed to load AssetBundle!");
            yield break;
        }
        SpriteAtlas spriteAtlas = bundle.LoadAsset(bundleName);
        callback(spriteAtlas);
    }
    

## Retrieving sprite contents at runtime with GetSprites 

If the sprites packed into a Sprite Atlas don’t exist in the current build or project, use GetSprites to create sprites bound to a Sprite Atlas at runtime with the following steps.

  1. Create a custom component that takes SpriteAtlas as a public variable.
  2. Assign a Sprite Atlas to that property.
  3. Enter the Editor’s Play mode.
  4. Access the variable and call the property GetSprites to retrieve the array of sprites packed in the selected atlas.

## Additional resources

  * Sprite Atlas workflow
  * Methods of distribution
  * Unity Support: Sprite Atlas with late binding and Asset Bundles