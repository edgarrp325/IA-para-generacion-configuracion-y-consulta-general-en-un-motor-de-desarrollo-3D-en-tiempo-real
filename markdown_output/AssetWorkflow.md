---
title: "Asset workflow"
category: "General"
source_file: "AssetWorkflow.html"
doc_type: "manual"
---

# Asset workflow

An asset is any item that you use in your Unity project to create your game or app. Assets can represent visual or audio elements in your project, such as 3D models, textures, **sprites** , sound effects, or music. Assets can also represent more abstract items such as color gradients, animation masks, or arbitrary text or numeric data for any use.

An asset might come from a file created outside of Unity, such as a 3D Model, an audio file, or an image. You can also create some types of asset in the Unity Editor, such as a ProBuilder **Mesh** , an **Animator Controller** , an **Animator Controller** , an Audio Mixer, or a **Render Texture** , an Audio Mixer, or a **Render Texture**.

## Import, Create, Build, Distribute, Load

Asset workflow in Unity

The above diagram shows the typical workflow when you work with assets in Unity. Each column represents a separate step and is described below:

  * **Import** assets into the Unity Editor
  * **Create** content using the Unity Editor with those assets.
  * **Build** your app or game file, and optionally its accompanying content bundles
  * **Distribute** the built files so that your users can access them, via a publisher, or an app store
  * **Load** further updates as necessary at runtime, depending on your user’s behavior, and how you have grouped and bundled your content.

### Import

Importing is the process of bringing your source files into the Unity Editor to work with. When you save or copy a file into your project’s `Assets` folder, Unity imports that file which allows you to work with it in the Editor. 

It’s important to learn some fundamentals of importing assets into Unity, such as where the files are stored in your Project, how to adjust the Import Settings for each kind of asset, what the meta files are for, and how the Asset Database stores imported data. See Importing Assets for more detail about these topics.

You can speed up Unity’s processing of assets when working with teams by using Unity Accelerator.

### Create

Once you have imported some assets into your project, you can start creating your game or app. This typically involves placing assets into one or more Scenes as **GameObjects** as **GameObjects** , and adding scripts, and adding scripts which control how the user interacts with them.

As development on your project grows, you might need to split your assets up into separate groups which allows your game to incrementally download selected extra content at runtime.

During the creation process, you can decide a strategy on how to group your assets into separate **bundles** , and implement the code for choosing when to load them.

Grouping your assets into bundles allows you reduce the size of your initial download and load some assets later at runtime. This can help you optimize the download size and memory usage of your game or app. The recommended way to do this is to use Unity’s Addressables system.

### Build

Building refers to the process of exporting your completed project to binary files which you can then distribute and run on the platform of your choice. For example, when building for Windows, Unity generates an `.EXE` file, along with some accompanying data files which you can then distribute.

If you’re using Addressables or Asset Bundles to group your assets into separate downloadable bundles you also need to build those bundle files for distribution. 

You can build your project on your own computer, or you can use Unity’s Build Automation service which provides automated build generation and continuous integration for your Unity projects.

### Distribute

Once you have built your game or app and its content bundles, your users need a way to access it. Your choice of distribution method depends on the platforms that you’re targeting. 

For example, mobile platforms have their own app stores, you could use a professional publisher, or you could self-host on your own servers.

Unity offers its own Cloud Content Delivery service, allowing you to host and deliver your game or app and its content to your users, and is fully integrated into the Unity development platform. This can save lots of time and is valuable for content-rich, live games or applications that require content updates on a regular basis.

### Load

When users load and use your game or app, the loading process and experience is defined by the rules and programming that you set up, and the way that you grouped and bundled your assets.

Using a combination of the techniques and services described here, you can provide fast initial downloads, and ongoing updates and extra content which you can roll out over the lifetime of your project.

* * *

## Artist workflow benefits

Unity’s asset workflow has tools and features which make it easy to edit and design directly in the Unity Editor:

  * Support for many different file formats
  * Quick roundtripping between Unity and third-party tools
  * Presets to apply custom default settings for types of assets
  * Update live content seamlessly using Addressables and Cloud Content Delivery

## Programmer workflow benefits

  * A tailored content pipeline (for example, you can write scripts to process assets as Unity imports them, or to control which presets Unity automatically applies based on your own rules).
  * Modify source assets through scripting. You can adjust source assets such as materials, meshes or physics through your game code.
  * Save memory using the Addressable assets system, which simplifies content management for complex projects, and provides automatic memory management and profiling tools.
  * Optimize assets for target platforms. When you’re making a multi-platform project, you might have hundreds of different textures, which all need to be packaged at different resolutions for different platforms. Unity packages, resizes and recompresses your assets automatically when you build to each target platform.

## Workflow considerations

When working with assets in Unity there are different strategies you can use. Which one suits your project depends on factors such as the size of your team, the size of your project, your target platforms, the memory availability on those platforms, and whether you want to release updates, patches, and DLC after publishing it.

For example, if you are working in a team, you could use a Cache Server alongside your **version control**

If you are working with a large number of assets that you want to publish as separate bundles, you might find it useful to separate some of those groups of assets out into separate projects, so that members of your team don’t need to load a single huge project to work on those bundles.

## Platform considerations

If you keep all your assets in a single project, Unity automatically builds them in the correct format for the current selected platform when you run a build. However, if you split your assets across multiple projects to build your bundles separately, you must make a build for each platform you support. See the Addressables documentation Building for multiple platforms for more information.

The characteristics of a platform also determine the restrictions and possibilities of how you organize your runtime assets. For example, on the standalone platforms (PC or macOS), virtual memory provides an almost unbounded pool of memory, so using the Resources folder or large asset bundles doesn’t typically pose a memory challenge. Conversely, mobile devices and console platforms typically have limited or nonexistent virtual memory, so apps built for those platforms must manage asset loading and unloading more efficiently. 

User expectations on a platform are also an important consideration. For example, on mobile platforms, a long initial download and install process can lead to players abandoning your app before they ever play it. For this reason, it’s common for mobile apps to include only a minimal set of assets in the initial build and to download the remaining assets from a remote server the first time the user runs your app.