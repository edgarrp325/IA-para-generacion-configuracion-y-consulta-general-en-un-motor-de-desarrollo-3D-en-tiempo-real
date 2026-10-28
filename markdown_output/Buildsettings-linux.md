---
title: "Linux Build settings"
category: "General"
source_file: "Buildsettings-linux.html"
doc_type: "manual"
---

# Linux Build settings

To create a build for Linux, go to **File > Build Settings** from Unity’s main menu. In the Platform list, select **Linux** and then click **Switch Platform**.

When you have configured the Build Settings, choose from the following two options:

  * **Build** builds your application into a Player
  * **Build and Run** builds your application in a Player, and opens that Player on your target platform.

Linux build settings in Unity

## Scenes in Build

The Scenes In Build pane displays a list of the Scenes from your Project that Unity includes in the build. If you can’t see any Scenes in this pane, select **Add Open Scenes** to add all the currently open Scenes to the build. You can also drag Scene Assets from your **Project window** into this window.

To exclude a Scene in the list from the build, clear the checkbox next to that scene. This removes the Scene from the build, but not from the list. To remove a Scene from the list, select it and press the Delete key on your keyboard.

When you select **Build** or **Build and Run** , Unity creates a build that includes all **Scenes in the Scenes** in Build list. Unity uses the list of Scenes to determine the order that it loads the Scenes in. To adjust the order of the Scenes, drag them up or down the list.

## Platform list

The Platform pane lists all platforms available in your Unity Editor. The list displays the Unity icon next to the name of the platform currently selected as the target platform.

Unity determines the platforms available to you depending on the platform modules you have installed.

To install further platform modules to your Project, do the following:

  * Go to the Unity Hub and select the version of Unity you want to add the module to.
  * Click the vertical ellipses and select **Add Modules**.

To change the target platform, select the platform you want to switch to, then select **Switch Platforms**. This might take some time, because Unity might need to re-import your Assets in formats that match your target platform.

When you select a platform, Unity displays a list of options that you can adjust for the build. Each platform has unique settings that are listed on each platform-specific manual page. Select the Windows, Mac, Linux build target to build standalone applications for most desktop platforms.

### Build settings

Use these settings to configure how Unity builds your application.

**Setting** | **Description**  
---|---  
**Target platform** | Select **Linux** to build your app for the Linux platform.  
****Development Build**** | Enable this setting to include scripting debug symbols and the **Profiler** in your build. When you enable this, Unity sets the `DEVELOPMENT_BUILD#define` for testing purposes. When you select **Development Build** , Autoconnect Profiler, Deep Profiling Support, Script Debugging, and Wait for Managed Debugger settings also become available.  
**Autoconnect Profiler** | Enable this setting to automatically connect the Unity Profiler to your build.  
**Deep Profiling Support** | Enable this setting to switch Deep Profiling in the Profiler. This makes the Profiler instrument every function call in your application and returns more detailed profiling data. When you enable Deep Profiling Support, it might slow down script execution.  
**Script debugging** | Enable this setting to allow your script code to be debugged. Not available on **WebGL**.  
**Wait for Managed Debugger** | Enable this setting to be prompted to attach a debugger before Unity executes any script code.  
****Compression** Method** (Not available on the WebGL platform) | Compress the data in your Project when you build the Player. This includes Assets, Scenes, Scenes, Player settings, and GI data. Choose between the following methods:  
| **Default** | On Windows, Mac, Linux, and iOS, there is no compression by default. On Android, the default compression is ZIP, which provides better compression results than LZ4HC; however, data is slower to decompress.  
| **LZ4** | A fast compression format that’s useful for development builds. For more information, see BuildOptions.CompressWithLz4.  
| **LZ4HC** | A high compression variant of LZ4 that’s slower to build but produces better results for release builds. For more information, refer to BuildOptions.CompressWithLz4HC.  
  
## Asset import overrides 

The Asset Import Overrides section allows you to locally override all texture import settings to speed up import and platform switch time. You must avoid shipping your final build with any import overrides, but during development they can be useful to speed up iteration time, especially, if assets such as textures resulting in lower resolution is not of any concern.

**Setting** | **Description**  
---|---  
**Max Texture Size** | Override the maximum imported texture size. Unity imports textures in the lower of two values: this value, or the Max Size value specified in Texture import settings.   
  
The time it takes to import a texture is roughly proportional to the amount of pixels it contains; therefore, reducing maximum allowed texture size can speed up the import times. However, as this setting might result in lower resolution textures, use it only for development.  
**Texture Compression** | Override the texture compression options set in Texture import settings.   
  
This only affects textures imported into one of the compressed texture formats.  
| **Force Fast Compressor** | Use a faster yet lower quality texture compression mode for formats where this is applicable (BC7, BC6H, ASTC, ETC, ETC2). Typically, this results in more compression artifacts, but for many formats the compression itself is many times faster (2 to 20 times faster).   
  
This setting also disables the **Crunch** texture compression format on any textures that have it.   
  
The effect is the same as if all textures had their **Compressor Quality** set to **Fast** setting in their platform’s Texture import settings.  
| **Force Uncompressed** | Don’t compress the textures; use uncompressed formats instead. Note that while this is faster to import because it skips the whole texture compression process, the resulting textures take up more memory, game data size, and can impact rendering performance. Texture import settings.   
  
This option has the same effect as all textures that have their **Compression** set to **None** in their platforms’ Texture Import settings.  
  
You can also set Asset import override settings using `-overrideMaxTextureSize` and `-overrideTextureCompression` Editor Command line arguments to change any initial project import.

## Additional resources:

  * Linux IL2CPP cross-compiler
  * Incremental build pipeline
  * Linux Player settings
  * Build a Linux application
  * BuildOptions API reference