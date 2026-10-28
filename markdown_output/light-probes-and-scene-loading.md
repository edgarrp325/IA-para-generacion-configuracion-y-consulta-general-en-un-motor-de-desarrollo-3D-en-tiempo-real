---
title: "Light Probes and Scene loading"
category: "General"
source_file: "light-probes-and-scene-loading.html"
doc_type: "manual"
---

# Light Probes and Scene loading

Unity updates its **Light Probe** data differently depending on how you load or unload **Scenes** data differently depending on how you load or unload **Scenes**.

Unity uses a LightProbes C# object to store Light Probe data for all currently loaded Scenes. The `LightProbes` object contains an internal data structure called a tetrahedral tessellation. Unity uses the tetrahedral tessellation in its calculations to determine how Light Probes light **GameObjects**

When you load or unload a Scene, Unity automatically updates the `LightProbes` object to contain the positions and coefficients of all Light Probes in all currently loaded Scenes. However, whether Unity updates the tetrahedral tessellation depends on how you load or unload the Scene.

When you load a Scene with LoadSceneMode.Single, Unity updates the tetrahedral tessellation automatically as part of the load process, because the new light probe data completely replaces the previous light probe data.

When you load a Scene with LoadSceneMode.Additive, or unload a Scene with UnloadSceneAsync, Unity does not automatically update the tetrahedral tessellation, because the new or removed light probe data needs to be recalculated - which is a computationally expensive operation, and there may be subsequent scenes to be loaded or unloaded after this operation.

Therefore Unity provides you with the needsRetetrahedralization event to allow you to decide when to retetrahedralize the new light probe data. For example, if you are additively loading five new scenes, you would not want to retetrahedralize the data five times, once after each scene loads. Instead, you would only want to retetrahedralize the data after all five scenes have loaded and all the new light probe data is ready.

If Unity performs calculations using an out-of-date tetrahedral tessellation, the results do not take into account any newly loaded or unloaded Light Probes. This means that Light Probes might not light GameObjects as expected, and calls to LightProbes.CalculateInterpolatedLightAndOcclusionProbes() or LightProbes.GetInterpolatedProbe() might return unexpected results.

To force Unity to update the tetrahedral tessellation, you can call LightProbes.Tetrahedralize or LightProbes.TetrahedralizeAsync(). These functions cause Unity to update the tetrahedral tessellation with data from all Light Probes for all currently loaded Scenes.

Updating the tetrahedral tessellation is CPU-intensive, and the CPU impact increases with the number of Light Probes. If you are loading and unloading multiple Scenes, and you experience a performance impact from updating the tetrahedral tessellation, then it might be beneficial to delay the update until you have loaded or unloaded a certain amount of content, or until a time when the CPU impact is not likely to affect the performance of your application.