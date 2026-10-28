---
title: "Unity"
category: "General"
source_file: "scriptmultiplescenes.html"
doc_type: "manual"
---

## Use scripts to edit multiple scenes

You can edit multiple **scenes** using **scripts** using **scripts** within the Editor or at runtime.

## Use scripts within the Editor

When using (or running) scripts within the Editor, use:

  * Scene struct: Available both in the Editor and at runtime, Scene struct contains read-only properties that relate to the scene itself, such as name and asset path.
  * EditorSceneManager API: This class is only available only in the Editor and has several functions to implement all the Multi-Scene editing features described in the pages Setup multiple scenes and Bake data in multiple scenes.
  * SceneSetup utility class: A utility class that you can use to store information about a scene that is in the Hierarchy window.

## Use runtime scripts

When using scripts at runtime to edit multiple scenes, use the functions in the SceneManager class such as `LoadScene` and `UnloadScene`.

**Tips** :

  * To instantiate a prefab in a scene, use PrefabUtility.InstantiatePrefab.
  * To move objects to the root of a scene, use Undo.MoveGameObjectToScene.
  * To avoid having to setup your Hierarchy window every time you restart the Editor, or to store different setups, use EditorSceneManager.GetSceneManagerSetup, which also gets a list of SceneSetup objects that describes the current setup. You can serialize the objects into a `ScriptableObject` along with any other information you want to store about your scene setup. To restore your Hierarchy window, recreate the list of `SceneSetups` and use EditorSceneManager.RestoreSceneManagerSetup.
  * To get a list of your loaded scenes at runtime, get the `sceneCount` and iterate over the scenes with `GetSceneAt`.