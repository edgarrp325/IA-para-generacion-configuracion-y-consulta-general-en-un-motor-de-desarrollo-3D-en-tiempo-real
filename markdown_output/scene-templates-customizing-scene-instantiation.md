---
title: "Customizing new scene creation"
category: "General"
source_file: "scene-templates-customizing-scene-instantiation.html"
doc_type: "manual"
---

# Customizing new scene creation

To run custom code when Unity instantiates a new **scene** from a template, create a Scene Template Pipeline script and connect it to the template. Each time you create a new scene from the template, Unity creates a new instance of the pipeline script as well.

To connect the script to a template:

  1. Inspect the template to edit its properties.
  2. Set the **Scene Template Pipeline** property to point to your Scene Template Pipeline script.

You can also use the `SceneTemplateAsset.templatePipeline` method to connect the script to the template via C#.

A Scene Template Pipeline script must derive from the [`ISceneTemplatePipeline`] interface or [`SceneTemplatePipelineAdapter`]. It should implement the events you want to react to; for example, `BeforeTemplateInstantiation` or `AfterTemplateInstantiation` in the code below.

**Example:**
    
    
    using UnityEditor.SceneTemplate;
    using UnityEngine;
    using UnityEngine.SceneManagement;
    public class DummySceneTemplatePipeline : ISceneTemplatePipeline
    {
        public void BeforeTemplateInstantiation(SceneTemplateAsset sceneTemplateAsset, bool isAdditive, string sceneName)
        {
            if (sceneTemplateAsset)
            {
                Debug.Log($"Before Template Pipeline {sceneTemplateAsset.name} isAdditive: {isAdditive} sceneName: {sceneName}");
            }
        }
    
        public void AfterTemplateInstantiation(SceneTemplateAsset sceneTemplateAsset, Scene scene, bool isAdditive, string sceneName)
        {
            if (sceneTemplateAsset)
            {
                Debug.Log($"After Template Pipeline {sceneTemplateAsset.name} scene: {scene} isAdditive: {isAdditive} sceneName: {sceneName}");
            }
        }
    }
    

## Scene Template instantiation sequence

When you create a new scene from a template with cloneable dependencies, Unity performs several file operations. Most of these operations trigger Unity events that you can listen for, and react to, in **scripts**.

The instantiation sequence is as follows:

  1. You click **Create** in the New Scene dialog. Unity calls the: 
     * Scene template asset.
     * Template Scene. This is the Unity Scene associated with the template.
     * New Scene. This is a new instance of the template Scene.
  2. Unity triggers the `ISceneTemplatePipeline.BeforeTemplateInstantiation` event for the template asset, and binds the asset to a `ISceneTemplatePipeline` script that it triggers.

  3. Unity triggers the `SceneTemplate.NewTemplateInstantiating` event.

  4. Unity creates a new scene that is a copy of the template scene.

  5. Unity creates a folder with the same name as the new scene, and copies all cloneable dependencies into that folder.

  6. Unity opens the new scene in memory, and triggers the following events: 
     * `EditorSceneManager.sceneOpening`
     * `MonoBehavior.OnValidate` (on all GameObjects that implement it)
     * `EditorSceneManager.sceneOpened`
  7. Unity remaps references to all cloneable assets, so the new scene points to the clones.

  8. Unity saves the new scene, and triggers the following events: 
     * `EditorSceneManager.sceneSaving`
     * `EditorSceneManager.sceneSaved`
  9. Unity triggers the `ISceneTemplatePipeline.AfterTemplateInstantiation` for the template asset, and binds the asset to a `ISceneTemplatePipeline` script that it triggers.

  10. Unity triggers the `SceneTemplate.NewTemplateInstantiated` event.

* * *