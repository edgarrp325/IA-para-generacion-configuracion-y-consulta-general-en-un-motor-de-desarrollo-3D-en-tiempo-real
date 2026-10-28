---
title: "Additional Search filters"
category: "General"
source_file: "search-additional-searchfilters.html"
doc_type: "manual"
---

# Additional Search filters

## Prefab Filters

Prefab filters can be used with **Scene** and Object Search Providers.

Filter | Search token | Description  
---|---|---  
**Root prefab** | `prefab:root` |  `prefab:root`  
  
Searches all GameObjects that are a Prefab root.  
**Top prefab** | `prefab:top` |  `prefab:top`   
  
Searches all GameObjects that are part of a Prefab instance.  
**Non asset prefab** | `prefab:nonasset` |  `prefab:nonasset`   
  
Searches all GameObjects that are part of a Prefab that is not inside a Prefab asset.  
**Asset prefab** | `prefab:asset` |  `prefab:asset`   
  
Searches all GameObjects that are part of a Prefab asset.  
**Any prefab** | `prefab:any` |  `prefab:any`   
  
Searches all GameObjects that are part of a Prefab.  
**Model prefab** | `prefab:model` |  `prefab:model`   
  
Searches all GameObjects that are part of a model Prefab.  
**Regular prefab** | `prefab:regular` |  `prefab:regular`   
  
Searches all GameObjects that are part of a regular Prefab instance or Asset.  
**Variant prefab** | `prefab:variant` |  `prefab:variant`   
  
Searches all GameObjects that are part of a Prefab variant.  
**Modified prefab** | `prefab:modified` |  `prefab:modified`   
  
Searches all GameObjects that are a Prefab instance with overrides.  
**Altered prefab** | `prefab:altered` |  `prefab:altered`   
  
Searches all GameObjects that are a Prefab instance with overrides even on default overrides.  
  
## File Filters

File filters can be used with Asset and Object Search Providers.

Filter | Search token | Description  
---|---|---  
**Default Search** | `<search term>` | Searches `term` attempting to match the asset name, type, or path.  
  
`texture`  
  
Searches all Assets that have the word texture in their name, path, or type.  
**Name** | `name:` |  `name:laser`  
  
Searches all Assets that contain the word laser.  
  
`name=laserbeam`  
  
Searches all Assets where the name is exactly laserbeam.  
**Directory** | `dir:<directory exact name>` |  `dir:Scripts`  
  
Searches all Assets contained in a directory with the exact name `Scripts`.  
**Packages** | `a:packages` |  `a:packages texture`  
  
Searches all textures in any package.  
**Project** | `a:assets` |  `a:assets texture`  
  
Searches all textures in the current project’s Assets folder.  
**Index file** | `a:<index name>` |  `a:psd_textures texture`  
  
Assuming there is an index file named `psd_textures.index` in the project, searches all textures in that index.  
**Size** | `size:<number of bytes>` |  `size:4000 texture`  
  
Searches all textures over 4000 bytes (4KB).  
**Extension** | `ext:<file extension without period>` |  `ext:png texture`  
  
Searches all textures with the png extension.  
**Age** | `age:<number of days since last modification>` |  `age<3 texture`  
  
Searches all textures that were modified in the last 3 days.  
  
## Type Filters

These filters are available if the index uses the Types Indexing option (See Index Manager).

Filter | Search token | Description  
---|---|---  
**Type** | `t:<Asset Type>` |  `t:texture`  
  
Searches all Assets containing texture in their type name (ex: Texture2D, Texture).  
  
`t:prefab`  
  
Searches all prefab assets.  
**Type** | `<Asset Type>` | You can search Assets by type without using the t: filter above.  
  
`texture`  
  
Searches all Assets containing texture in their type name (ex: Texture2D, Texture) or in their name (ex: myTexture.png).  
  
`prefab`  
  
Searches all Prefab Assets or Assets with “prefab” in their name.  
**File** | `t:file` |  `t:file level1`  
  
Searches all file Assets containing the word level1.  
**Folder** | `t:folder` |  `t:folder`  
  
Searches all folder Assets.  
  
## Indexed Property Search

Searching properties is available if the index has been specified with the Properties Indexing option (see Index Manager). To view the list of all indexed properties check the Index Manager Keywords tab. All property values are converted to a string or number. The name of the property has to be complete and not partial (case does not matter though). Unity indexes properties at the top level object of a **Prefab** Asset. If you want all Prefab hierarchies to be indexed, create a Prefab Index (see Index Manager). For .unity files Unity indexes the properties of the SceneAsset and not the Scene content. If you want all Scene contents to be indexed, create a Scene Index (see Index Manager).

Filter | Search token | Description  
---|---|---  
**Type** | `t:<type>` | When using the indexed Property, you can use `t:` to search for a component type for an Asset type.  
  
`t:collider`  
  
Searches all Prefabs containing a component with the word `collider`.  
  
`t:texture`  
  
Searches all Assets with a type containing the word `texture` (ex: Texture or Texture2D).  
**Has Component** | `t:<component type>` |  `t:collider`  
  
Searches all Prefabs containing a component with the word collider.  
  
`t=BoxCollider`  
  
Searches all Prefabs containing a component called BoxCollider.  
**Label** | `l:<label name>` |  `l:archi`  
  
Searches all Assets with a label containing the word `archi` (e.g.: Architecture).  
  
`l=Wall`  
  
Searches all Assets with a label that is exactly `Wall`.  
  
All properties of an Asset (Prefab or other types) are indexed and searchable. Here are a few examples of Property query:

Filter | Search token | Description  
---|---|---  
**Number** | `property:value` |  `bounciness>0.1`  
  
Searches all assets with a property named `bounciness` (e.g.: a PhysicsMaterial2D) higher than 0.1.  
  
`health=2`  
  
Searches all Assets with a property named `health` (e.g.: HealthSystem Component of a Prefab) with of a value of exactly 2.  
  
`t:texture filtermode!=0`  
  
Searches all textures with a `filtermode` property different than 0 (i.e different than Point).  
**Boolean** | `property:value` |  `t:Dungeon generatePath=true`  
  
Searches all Dungeon ScriptableObjects where the property `generatePath` is true.  
  
`isStunned=false`  
  
Searches all GameObjects containing a property `isStunned` that is false.  
**String** | `property:string value` |  `t:Character trait:indestru`  
  
Searches all Prefab with a Character component whose trait property contains the word `indestru` (ex: indestructible).  
  
`t:Character trait="tough but fair"`  
  
Searches all Prefab with a Character component whose trait property is exactly `tough but fair`.  
**Enum** | `property:<enum value>` |  `characterclass:rog`  
  
Searches all GameObjects with with a property named `characterclass` whose value contains the word rog (e.g.: value is rogue).  
  
`characterclass=FighterMage`  
  
Searches all GameObjects with a property named `characterclass` with an exact value of `FighterMage`.  
**Color** | `property:<html color value>` |  `color:ADA`  
  
Searches all GameObjects with a property named `color` where the color value starts with ADA (like ADADAD00).  
  
`color=ADADAD00`  
  
Searches all GameObjects with a property named `color` where the color value is exactly ADADAD00.  
  
`color=ADADAD`<br/>  
Searches all GameObjects with a property named color where the color value is exactly ADADAD and alpha value is 1.  
**Vector** | `property.[xyzw]:value` |  `bounds.x>1`  
  
Searches all GameObjects with a property named `bounds` where the x value is larger than 1.  
  
`acceleration.z=2`  
  
Searches all GameObjects with a property named acceleration where the z value is equal to 2  
**Object** | `sprite:<object exact name>` |  `sprite:CharacterBody`  
  
Searches all Assets with a `sprite` property (e.g.: Image Component of a Prefab) that references a GameObject named CharacterBody.  
  
## Dependency filters

If you are using the Dependencies Indexing option (See Index Manager) Unity indexes **direct dependencies**

Filter | Search   
token | Description  
---|---|---  
**Reference Path** | `ref:<asset full path>` |  `ref:assets/images/particles/p_smoke.png`  
Searches all Assets that have direct dependencies on the **exact** Asset path: `assets/images/particles/p_smoke.png` .  
**Reference Name** | `ref:<asset name>` |  `ref:p_smo`  
Searches all Assets that have direct dependencies on an Asset whose name contains the word `p_smo`.   
  
`ref:p_smoke.png`  
Searches all Assets that have direct dependencies on an Asset named `p_smoke.png`.