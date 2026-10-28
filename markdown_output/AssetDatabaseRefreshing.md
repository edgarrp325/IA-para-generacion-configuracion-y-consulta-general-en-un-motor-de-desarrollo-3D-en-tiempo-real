---
title: "Refreshing the Asset Database"
category: "General"
source_file: "AssetDatabaseRefreshing.html"
doc_type: "manual"
---

# Refreshing the Asset Database

Unity refreshes the Asset Database in the following situations:

  * When the Unity Editor regains focus (if you have enabled Auto-Refresh in the Preferences window)
  * When you select **Assets > Refresh** from the menu
  * When you call AssetDatabase.Refresh from C#

Some other AssetDatabase APIs trigger a Refresh() but only for the Assets you specify. For example CreateAsset() and ImportAsset().

Unity performs the following steps during an Asset Database refresh:

  1. It looks for changes to the Asset files, and then updates the source Asset Database
  2. It imports and compiles code-related files such as .dll, .asmdef, .asmref, .rsp, and .cs files.
  3. It then reloads the domain, if Refresh was not invoked from a script.
  4. It post-processes all of the Assets for the imported code-related files
  5. It then imports non-code-related Assets and post-processes all the remaining imported Assets
  6. It then hot reloads the Assets

## The Asset Database detailed refresh process

Unity performs the steps described in the previous section during the Asset Database refresh. This section describes this process in more detail. These steps happen inside a loop, and some steps might cause the refresh process to restart (for example, if importing an Asset creates other Assets which Unity also needs to import). 

Unity restarts the Asset Database refresh loop under the following conditions:

  * If, after the import, a file that the importer used has changed on disk.
  * If, in OnPostProcessAllAssets, you call any of the following: 
    * ForceReserializeAssets
    * AssetImporter.SaveAndImport
    * Any AssetDatabase API that queues an additional Refresh, such as MoveAsset, CreateAsset and ImportAsset
  * If the timestamp of the file being imported changes while it is being imported, the file is queued for re-import
  * When an importer creates a file in the middle of an import (for example, FBX models can restart a Refresh by extracting their Textures from the model).

### Look for changes on disk

When Unity looks for changes on disk, it scans the `Assets` and `Packages` folders in your Project to check if any files have been added, modified, or deleted since the last scan. It gathers any changes into a list to process in the next step.

### Update source Asset Database

Once Unity gathers the file list, it then gets the file hashes for the files which have either been added or modified. It then updates the Asset Database with the GUIDs for those files, and removes the entries for the files that it detected as deleted.

### Dependency tracking

The Asset Database keeps track of two types of Asset dependencies: **static dependencies** and **dynamic dependencies**. If any dependency of an Asset changes, Unity triggers a reimport of that Asset.

##### Static dependencies

A static dependency is a value, setting or property that an importer depends on. Static dependencies are known before the Asset is imported, and are not affected by the behavior of the importer during the import process. If a static dependency of an Asset changes, Unity re-imports that Asset.

Some common static dependencies are:

  * The name of the Asset
  * ID of the importer associated with the Asset
  * The version of the importer
  * The currently selected build target platform

##### Dynamic dependencies

Unity typically discovers the dynamic dependencies of an asset during the import process. This is because these dependencies are defined by the content of the source asset. For example, a **Shader** might reference another Shader, and a **Prefab** might reference another Shader, and a **Prefab** might depend on other Prefabs. 

The importer might also use a global state conditionally based on the content of the source asset, in which case it also becomes a dynamic dependency. Examples of this are the target platform, the Project’s color space, the graphics API, the scripting runtime version, or the Texture **compression** state.

Unity stores these dynamic dependencies of an asset in an Asset Import Context. 

### Import and compile code-related files

In the list of changed or added files, Unity gathers the ones that relate to code, and sends them to the script compilation pipeline. The compiler generates assemblies from the script files and assembly definition files in your Project. For more information on this step, see documentation on script compilation assembly definition files.

### Reload the domain

If Unity detects any script changes, it reloads the C# domain. It does this because new Scripted Importers could have been created, and their logic could potentially impact the import result of Assets in the Refresh queue. This step restarts the Refresh() to ensure any new Scripted Importers take effect.

### Import non-code-related Assets

Once Unity imports all code-related assets and it reloads the domain, it then moves on to the remaining Assets. Each Asset’s importer processes that type of Asset, and identifies the file types that it should import based on the filename extensions. For example, the TextureImporter is responsible for importing .jpg, .png and .psd files, among others.

There are two types of importers: 

  * Native importers: Unity’s built-in importers.
  * Scripted importers: Custom importers that extend Unity’s import capabilities. These are written in C#.

Unity processes all native importers first, and then all scripted importers in a separate phase.

When an importer imports an asset file, Unity generates an **AssetImportContext**. The AssetImportContext reports the Static Dependencies of an asset.

Also, during the import step, there are a number of callbacks which occur.

Preprocess Asset Importer Calls:

  * `OnPreprocessAsset`
  * `OnPreprocessAnimation`
  * `OnPreprocessAudio`
  * `OnPreprocessModel`
  * `OnPreprocessSpeedTree`
  * `OnPreprocessTexture`

Postprocess Asset Importer Calls:

  * `OnAssignMaterialModel`
  * `OnPostprocessAnimation`
  * `OnPostprocessAssetbundleNameChanged`
  * `OnPostprocessAudio`
  * `OnPostprocessCubemap`
  * `OnPostprocessGameObjectWithAnimatedUserProperties`
  * `OnPostprocessGameObjectWithUserProperties`
  * `OnPostprocessMaterial`
  * `OnPostprocessMeshHierarchy`
  * `OnPostprocessModel`
  * `OnPostprocessSpeedTree`
  * `OnPostprocessSprites`
  * `OnPostprocessTexture`

One final post processing callback which is triggered once all importing has completed is `OnPostprocessAllAssets`.

There are a number of things that can happen which will restart the refresh process on the Asset folder, some of them being:

  * If the import of an asset failed

  * If the asset was modified during the import phase of the Refresh. For example, if a file in the list gets modified so its modification date is not what it was in the previous refresh. This can happen if you start pulling files from a **Version Control** system while the Editor has focus.

  * If an Asset created other assets during import. For example: When importing an FBX, textures can get extracted from the FBX and placed into the project, and this means that Unity has to import the textures (and any artifacts they generate).

  * If you force the re-import of a file during one of the pre/post process callbacks or inside OnPostProcessAllAssets, for example, using `AssetDatabase.ForceReserializeAssets` or `AssetImport.SaveAndReimport`. Note, you must be careful not to cause infinite reimport loops if you do this.

  * If an Assembly Reload happens after compiling **scripts**. If you generate a C# file during the refresh process, that new file must then be compiled, so Unity restarts the refresh.

  * If you save an asset as “Text only” but the Asset must be serialized as binary, a restart will happen. (For example, Scenes with Terrains in them must be serialized as Binary, since the terrain data would be unwieldy if viewed as an array of characters in a text file.)

#### Hot reloading

Hot reloading refers to the process where Unity imports and applies any changes to scripts and assets while the Editor is open. This might happen while the Editor is in Play Mode or outside of Play Mode. You do not have to restart your application or the Editor for changes to take effect.

When you change and save a script, Unity hot-reloads all of the project’s script data. It first stores all serializable variable values in all loaded scripts, reloads the scripts, then restores the values. All of the data stored in non-serializable variables is lost during a hot reload.

**Note:** Unity imports assets imported by the (built-in DefaultImporter)[BuiltInImporters] first, and then script assets, so it does not call any script-defined PostProcessAllAssets for default assets.

#### End of Refresh

Once all these steps have completed, the `Refresh()` is complete. The **Artifact Database** is updated with the relevant information, and the necessary import result files are generated on disk.