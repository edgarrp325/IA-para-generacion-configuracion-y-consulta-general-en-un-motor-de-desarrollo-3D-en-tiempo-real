---
title: "Windows Build Settings"
category: "General"
source_file: "WindowsStandaloneBinaries.html"
doc_type: "manual"
---

# Windows Build Settings

To create a build for Windows, go to **Build Settings** (menu: **File** > **Build Settings**). In the **Platform** list, select **Windows** , then select **Switch Platform**.

Windows build settings in Unity

Use these settings to configure how Unity builds your application.

**Setting** | **Description**  
---|---  
**Target platform** | Select **Windows** to build your app for the Windows platform.  
| **Architecture** | Select the CPU to build for (only applies to Build And Run).  
| **Intel 64-bit** | Intel/AMD 64-bit CPU architecture.  
| **Intel 32-bit** | Intel 32-bit CPU architecture.  
**Copy PDB files** | Enable this setting to include Microsoft program database (PDB) files in the built Windows Player. PDB files contain debugging information for your application, but might increase the size of your Player. For more information, refer to Windows debugging.  
**Create Visual Studio Solution** | Enable this setting to generate Visual Studio solution files for the project such that you can build the project from Microsoft Visual Studio directly.  
****Development Build**** | Enable this setting to include scripting debug symbols and the **Profiler** in your build. When you enable this, Unity sets the `DEVELOPMENT_BUILD#define` for testing purposes. When you select **Development Build** , Autoconnect Profiler, Deep Profiling Support, Script Debugging, and Wait for Managed Debugger settings also become available.  
**Autoconnect Profiler** | Enable this setting to automatically connect the Unity Profiler to your build.  
**Deep Profiling Support** | Enable this setting to select Deep Profiling in the Profiler. This makes the Profiler instrument every function call in your application and returns more detailed profiling data. When you enable Deep Profiling Support, it might slow down script execution.  
**Script debugging** | Enable this setting to allow your script code to be debugged. Not available on **WebGL**.  
**Wait for Managed Debugger** | Enable this setting to be prompted to attach a debugger before Unity executes any script code.  
****Compression** Method (Not available on the WebGL platform)** | Compress the data in your application when you build your application. This includes Assets, Scenes, Scenes, Player settings, and GI data. Choose from the following methods:  
| **Default** | On Windows, Mac, Linux, and iOS, there is no compression by default. On Android, the default compression is ZIP, which provides better compression results than LZ4HC; however, data is slower to decompress.  
| **LZ4** | A fast compression format that’s useful for development builds. For more information, see BuildOptions.CompressWithLz4.  
| **LZ4HC** | A high compression variant of LZ4 that’s slower to build but produces better results for release builds. For more information, see BuildOptions.CompressWithLz4HC.  
  
## Asset Import Overrides 

Use Asset Import Overrides to locally override all texture import settings to speed up import and platform switch time. You must avoid shipping your final build with any import overrides, but you can use this setting during development to speed up iteration time, especially if assets such as low resolution textures are not of any concern.

**Setting** | **Description**  
---|---  
**Max Texture Size** | Override the maximum imported texture size. Unity imports textures in the lower of two values: this value, or the Max Size value specified in Texture import settings.   
  
The time it takes to import a texture is roughly proportional to the amount of pixels it contains; therefore, reducing maximum allowed texture size can speed up the import times. As this setting might result in lower resolution textures, use it only for development purposes.  
**Texture Compression** | Override the texture compression options set in Texture import settings.   
  
This only affects textures imported into one of the compressed texture formats.  
| **Force Fast Compressor** | Use a faster yet lower quality texture compression mode for formats where this is applicable (BC7, BC6H, ASTC, ETC, ETC2). Typically, this results in more compression artifacts, but for many formats the compression itself is many times faster (2 to 20 times faster).   
  
This setting also disables the **Crunch** texture compression format on any textures that have it.   
  
The effect is the same as if all textures had their **Compressor Quality** set to **Fast** setting in their platform’s Texture import settings.  
| **Force Uncompressed** | Don’t compress the textures; use uncompressed formats instead. Note that while this is faster to import because it skips the whole texture compression process, the resulting textures take up more memory, game data size, and can impact rendering performance. Texture import settings.   
  
This option has the same effect as all textures that have their **Compression** set to **None** in their platforms’ Texture Import settings.  
  
You can also set Asset import override settings using `-overrideMaxTextureSize` and `-overrideTextureCompression` Editor Command line arguments to change any initial application import.

## Building your Windows application

To build your application, select from one of the following options:

  * **Build** : Compile your application. The default build is incremental, except for the first build, which is always a full non-incremental (clean) build. To force a clean build instead of an incremental build, select **Clean Build** from the dropdown menu.

  * **Build and run** : Compile your application and open it in your native platform. This option always uses the incremental build.

## Windows Player build binaries

When you build a Unity title on the Windows platform, Unity produces the following files, where `ProjectName` is the name of your application:

  * `ProjectName.exe` \- The project executable file, that’s your project application. This contains the program entry point which calls into the Unity engine when launched. The path to the source code for `ProjectName.exe` is in the `WindowsPlayer` folder: `Editor\Data\PlaybackEngines\WindowsStandaloneSupport\Source\WindowsPlayer`.
  * `UnityPlayer.dll` \- The DLL file that contains all the native Unity engine code. It’s signed with the Unity Technologies certificate, which lets you verify that no malicious entities have tampered with your engine.
  * `*.pdb files` \- Symbol files for debugging. Unity copies these to the build directory if you enable **Copy PDB files** in the Build Settings window.
  * `WinPixEventRuntime.dll` \- This DLL enables Introducing PIX on Windows (beta) support. Unity only creates this file if you enable the **Development Build** option in the Build Settings window.
  * `ProjectName_Data folder` \- This folder contains all the data needed to run your application.

## Modify and rebuild your application

To modify your application or distribute the built code (for example, if you want to sign it or modify the built executable metadata), you must rebuild your project and place the output in your built game directory.

Modifying the built executable metadata, such as the publisher or company name is necessary to ensure that your application is correctly identified by the system. For example, various operating system tools and dialogs, such as Windows firewall use the executable metadata to display your application’s information, such as the publisher or company name. The Unity Player executable included with the Unity installation is pre-built and might not reflect details specific your application. In this case, you can modify the executable metadata to include your application’s information.

To modify the metadata, follow these steps:

  1. Enable the **Create Visual Studio Solution** setting to generate Visual Studio Solution files for your project and build your project in the Unity Editor.
  2. Open the build folder and locate a subfolder with the same name as your project. In the subfolder, find the `WindowsPlayerVersion.rc` file and open it with a text editor.
  3. Remove the lines of code that include conditional compilation directive `#if defined(BUILDING_UNITY_PLAYER_DLL)` and the corresponding `#endif`.
  4. Modify any metadata, such as `CompanyName`, `FileVersion`, `FileDescription`, or `ProductName` as required. For more information on these fields, refer to the documentation on StringFileInfo BLOCK Statement.
  5. Open the Visual Studio Solution from the build folder using Visual Studio and rebuild your project.

**Note** : To build your application outside of Unity, you need Visual Studio 2019 or 2022 with Desktop development with C++ workload installed.

## Additional resources

  * Visual Studio project generation for Windows
  * BuildOptions API reference