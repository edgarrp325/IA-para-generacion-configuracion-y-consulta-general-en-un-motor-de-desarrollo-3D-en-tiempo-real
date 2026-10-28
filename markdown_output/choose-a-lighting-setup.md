---
title: "Choose a lighting setup"
category: "General"
source_file: "choose-a-lighting-setup.html"
doc_type: "manual"
---

# Choose a lighting setup

The following flowchart provides a high-level perspective of the entire lighting pipeline in Unity, from the point of view of a content creator.

You start by selecting a render pipeline. Then you decide how the indirect lighting is generated and pick a **Global Illumination** system accordingly. After you’ve made sure all the global lighting settings are tuned appropriately for your project, you can continue adding Lights, Emissive Surfaces, Reflection Probes, Light Probes, and Light Probe Proxy Volumes (LPPVs). Detailing the usage and features of all these lighting objects is beyond the scope of this article, therefore I encourage you to read the Lighting section of the manual to learn how to utilize them correctly in your projects.

## Global Illumination systems

The Global Illumination systems available in Unity are:

  1. Realtime Global Illumination: This system builds upon **Enlighten** , a third-party middleware solution. It enables you to adjust your lighting in real-time if you do a precompute and do not modify **GameObjects** in your **scene** in your **scene** with the **ContributeGI** setting enabled. 

  2. Baked Global Illumination: When you select this system, Unity uses the Progressive **Lightmapper** (CPU or GPU) to bake lighting data into Light Probes, textures called **lightmaps** (CPU or GPU) to bake lighting data into Light Probes, textures called **lightmaps** , and Reflection Probes. 

The Progressive Lightmapper calculates indirect lighting values using path tracing. It can prioritize precomputing lighting that affects objects visible to the **scene view** **camera** **camera**. Although only updating lighting for parts of lightmaps increases the overall bake time, it also enables you to more quickly iterate on your lighting design.

See the Render Pipeline Feature Comparison for compatibility information specific to scriptable render pipelines. Unless the comparison matrix specifies otherwise, the Built-In **Render Pipeline**

### Static versus Dynamic

No matter which Global Illumination system you use, Unity will only consider objects that are marked as “Contribute GI” during the baking/precomputing of the lighting. Dynamic (i.e. non-static) objects have to rely on the Light Probes you placed throughout the scene to receive indirect lighting.

Because the baking/precomputing of the lighting is a relatively slow process, only large and complex assets with distinct lighting variations, such as concavity and self-shadowing, should be tagged as “Contribute GI”. Smaller and convex meshes that receive homogeneous lighting should not be marked as such, and they should, therefore, receive indirect lighting from the Light Probes which store a simpler approximation of the lighting. Larger dynamic objects can rely on LPPVs, in order to receive better localized indirect lighting. Limiting the number of objects tagged as “Contribute GI” in your scene is absolutely crucial to minimize baking times while maintaining an adequate lighting quality. You can learn more about this optimization process and the importance of Probe lighting in this tutorial.

### Warning

The Unity Editor and Player allow you to use both Enlighten Realtime Global Illumination and baked lighting at the same time.

However, simultaneously enabling these features greatly increases baking time and memory usage at runtime, because they do not use the same data sets. You can expect visual differences between indirect light you have baked and indirect light provided by Enlighten Realtime Global Illumination, regardless of the lightmapper you use for baking. This is because Enlighten Realtime Global Illumination often operates at a significantly different resolution than Unity’s baking backends, and relies on different techniques to simulate indirect lighting.

If you wish to use both Enlighten Realtime Global Illumination and baked lighting at the same time, limit your simultaneous use of both global illumination systems to high-end platforms and/or to projects that have tightly controlled scenes with predictable costs. Only expert users who have a very good understanding of all lighting settings can effectively use this approach. Consequently, picking one of the two global illumination systems is usually a safer strategy for most projects. Using both systems is rarely recommended.

### Light Modes

The Mode property of a Light component is a common source of confusion.

There are three Light Modes available in the Light Inspector:

  1. Baked: The direct and indirect lighting from these lights is baked into lightmaps, which can be a time-consuming process. There is no runtime cost to process these lights, however applying the resulting lightmaps to the scene does have a minor cost.
  2. Realtime: The direct lighting and shadows from these lights are real-time and therefore not baked into lightmaps. Their runtime cost can be high, depending on the complexity of the scene, the number of shadow casting lights, the number of overlapping lights, etc. Furthermore, if you enable Enlighten Realtime Global Illumination, further performance costs will be incurred to update the indirect lighting at runtime.
  3. Mixed: This is a hybrid mode that offers a mix of baked and real-time features, such as baked indirect lighting and real-time direct lighting. The behavior of all Mixed lights in your Scene and their performance impact depends on the Lighting Mode for that Scene.

It is important to note that the mode of a light is only relevant if the Baked Global Illumination system is enabled. If you do not use any global illumination system or only use Enlighten Realtime Global Illumination system, then all Baked and Mixed lights will behave as though their Mode property was set to Realtime.

The following diagram combines a decision flowchart with a comparison table; it can help you decide which light mode is appropriate every time a new light is added into the scene.

### Lighting Modes

As you can see in the previous diagram, all Mixed Lights in a Scene have specific baked and real-time capabilities, depending on the Lighting Mode that you picked in the Lighting window.

There are three modes to choose from:

  1. Subtractive
  2. Baked Indirect
  3. Shadowmask

Shadowmask Lighting Mode has two quality settings:

  1. Shadowmask
  2. Distance Shadowmask

When using HDRP’s Shadowmask Lighting Mode, the **Shadowmask**

## Lighting scenarios

Now that we have introduced the render pipelines and the main lighting features, let’s have a look at a few examples of projects and see which settings could be used to light them. Since every project is unique, you might use slightly different options based on your requirements.

### 1\. Prototype or quick previsualization

If you rely heavily on the **Asset Store** to build your prototype, the Built-In Render Pipeline could be the only suitable render pipeline, as most assets found on the Store are not fully compatible with HDRP and URP; nonetheless, asset compatibility will improve over time. If you are building all the assets from the ground up and already have a clear idea of your project’s requirements, then you could pick one of the two SRPs (i.e. URP or HDRP) or even create a custom one.

When you are in the early stage of (pre-)production and need a quick turnaround and maximum flexibility for the lighting, you might prefer a full real-time approach that does not require any precomputation, therefore you might want to turn off both Baked Global Illumination and Enlighten Realtime Global Illumination. To alleviate the lack of proper indirect lighting, you can enable Screen Space **Ambient Occlusion** : it can help ground the object in the scene by offering cheap real-time contact shadows.

### 2\. 3D Mobile strategy game

If you are targeting mobile devices, URP could be a great candidate to ensure solid performance for your game. It is in many cases possible to customise URP to suit your game’s specific needs, with help from a graphics programmer.

The Built-In Render Pipeline and URP both support Shadowmask Lighting Mode which makes it possible for you to bake shadows for static objects while still enabling dynamic objects to cast real-time shadows. If Shadowmasks are too expensive for your project, you can fall back to the cheapest Subtractive mode. Finally, the forward **rendering path** is probably the best option if you have a very small number of lights in your level(s), and if you’re targeting older hardware.

### 3\. AAA corridor shooter (fixed time of day)

If you are aiming for AAA-quality visuals on PC and consoles for your linear first-person shooter, HDRP should be the preferred render pipeline. Again, with the help of graphics programmers, a custom SRP could also be developed.

If your levels contain many real-time shadow casting lights (e.g. destructible light props and moving lights), then using the Baked Global Illumination system with the Baked Indirect mode should ensure you get great looking indirect lighting from the Mixed directional light and the **Baked lights** in static light props. If your levels consist of a larger proportion of fixed shadow casting lights, then an approach with Shadowmasks could be recommended because HDRP offers a great hybrid Shadowmask mode which gives you more control over the blend between real-time and baked shadows.

If you also plan to support the Nintendo Switch, then using URP would be recommended, so that you can support most gaming platforms on the market and not having to go through the potentially tedious process of porting your project from HDRP to URP, or vice versa.

### 4\. Battle Royale (day-night cycle)

If you plan to release a battle royale game for PC and consoles, that features large-scale environments and fully dynamic lighting, you should select HDRP, or extend it to tailor the rendering pipeline to your project. You could consider URP if you are not aiming for AAA visual fidelity and are targeting mobile devices or systems with lower specifications.

For this particular scenario, if you are using the Built-in Render Pipeline, activating both the Enlighten Realtime Global Illumination and a Baked Global Illumination system is not recommended, because the resulting overhead in terms of performance and scene management for an immense level could be problematic. Another argument against the use of both global illumination systems is the unpredictable nature of such large-scale multiplayer games: performance estimations are for instance more difficult than in a highly-scripted linear level.

## Final words

The rendering landscape has changed radically in Unity over the past few years, thanks to the introduction of the Scriptable Render Pipelines. Therefore, keeping up with all these changes and their implications for the lighting pipeline can be exhausting.

Hopefully, this guide and its many illustrations have given you a better understanding of the capabilities of each Render Pipeline so that you can confidently start your projects in Unity with the appropriate rendering and lighting settings!

You can learn more about the lighting in Unity and the rendering pipelines with the following pages:

  * URP documentation & HDRP documentation

  * Use the Unity Hub to get started with HDRP, URP or Built-In RP

  * Introduction to Lighting and Rendering tutorial

  * Creating Believable Visuals tutorial (Built-In RP)

  * Set up HDRP for high-end visualizations

  * Create high-quality light fixtures in Unity