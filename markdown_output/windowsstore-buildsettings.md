---
title: "UWP build settings"
category: "General"
source_file: "windowsstore-buildsettings.html"
doc_type: "manual"
---

# UWP build settings

Use the Universal Windows Platform (UWP) Build Settings to configure and build your application for UWP. The UWP Build Settings are part of the Build Settings window. 

To build your application for UWP:

  1. Select **File** > **Build Settings**.
  2. From the list of platforms in the **Platform** pane, select UWP.  
**Note** : Universal Windows Platform only shows in the Platform list if you’re using Unity on a Windows computer.  
If UWP appears dimmed, refer to UWP environment setup.
  3. If the **Build** button isn’t visible and **Build And Run** appears dimmed, select **Switch Platform**. The UWP Build Settings now have an effect on the build.
  4. Click either **Build** or **Build and Run**.  
**Build** builds your application into a Player. **Build and Run** builds your application in a Player, and opens that Player on your target platform.
  5. Select the destination for Unity to place the application.  
If you selected **Build and Run** , Unity also installs the application on the run device.
  6. Click **Save**. This starts the build.

You can configure the following settings for your build:

**Property** | **Description**  
---|---  
**Architecture** | Select from the following CPU architectures to build (only applies to **Build And Run**) for UWP.  
| **Intel 64-bit** | 64-bit Intel CPU.  
| **Intel 32-bit** | 32-bit Intel CPU.  
| **ARM 64-bit** | 64-bit ARM CPU.  
| **ARM 32-bit** | 32-bit ARM CPU.  
**Build Type** | Select the Visual Studio project or build type to generate.  
| **XAML Project** | Integrates Unity within a full XAML environment. This results in some performance loss, but lets you use XAML elements in your application.  
| **D3D Project** | Integrates Unity in a basic app window. This results in the best performance.  
| **Executable Only** | Hosts the project in a pre-built executable for rapid iteration. This setting has the quickest iteration speed because it doesn’t require you to build the generated project in Visual Studio. It offers the same performance as D3D Project builds.  
**Target SDK Version** | Select the Windows 10 SDK installed on the local PC to build the application against. This setting is relevant only when calling Windows 10 APIs directly from scripts.  
  
**Note:** Unity requires the base Windows 10 SDK version 10.0.10240.0 or higher for building UWP apps, and doesn’t support Windows 8/8.1 SDKs.  
**Minimum Platform Version** | Select the minimum Windows 10 release version required to run the app.   
  
**Note:** This setting is only relevant if you’re using Windows features or APIs that aren’t available in the base Windows 10 version (10.0.10240).  
**Visual Studio Version** | Specify the Visual Studio version if you have multiple versions installed.  
**Build and Run on** | Select the target device or transport to deploy and launch the app during **Build And Run**.  
| **Local Machine** | Deploys and launches the app on the local PC.  
| **Remote Device (via Device Portal)** | Deploys and launches the app to a connected device over the Device Portal transport. For more information, refer to Windows Device Portal deployment.  
**Build Configuration** | Select the build configuration (only applies to **Build And Run**).  
  
**Note:** These build configurations are the same as those available in the Visual Studio project that Unity generates.  
| **Debug** | Produces a build that contains additional code you can use for debugging, and enables the Profiler for your build.  
| **Release** | Produces a build that has debug code stripped out, and enables the Profiler for your build.  
| **Master** | Produces a build that’s fully optimized for release.  
**Copy References** | Disable this setting to allow the generated solution to reference Unity files from Unity’s installation folder instead of copying them to the build folder. This can save up to 10 GB of disk space, but you can’t copy the build folder to another PC. Unity also builds your application faster when you disable this setting.  
**Copy PDB files** | Enable this setting to include Microsoft program database (PDB) files in the built Player. PDB files contain debugging information for your application, but might increase the size of your Player. For more information, refer to Windows debugging.  
**Development Build** | A development build includes scripting debug symbols. When you select this option, Unity sets the DEVELOPMENT_BUILD scripting define. Your build then includes preprocessor directives that set DEVELOPMENT_BUILD as a condition.   
  
For more information, refer to Platform dependent compilation.  
**Autoconnect Profiler** | Indicates whether to automatically connect the Profiler to the built application when it runs.  
  
This property is visible only when **Development Build** is enabled.  
**Deep Profiling** | Indicates whether to enable Deep Profiling in the Profiler. This makes the Profiler instrument every function call in your application so it returns more detailed profiling data. This option might slow down script execution.  
  
This property is visible only when **Development Build** is enabled.  
**Script Debugging** | Indicates whether to allow debugging for the application’s script code.  
  
This property is visible only when **Development Build** is enabled.  
****Compression** Method** | Specifies the method Unity uses to compress the data in your Project when it builds the Player. This includes Assets, Scenes, Scenes, Player settings, Player settings, and GI data.  
| **Default** | The Default compression is set to None.  
| **LZ4** | LZ4 is a fast compression format that’s useful for **development builds**. This compression can improve loading time of applications built with Unity. For more information, see BuildOptions.CompressWithLz4.  
| **LZ4HC** | LZ4HC is a high compression variant of LZ4 that’s slower to build but produces better results for release builds. This compression can improve loading time of applications built with Unity. For more information, see BuildOptions.CompressWithLz4HC.  
  
## Additional resources

  * Integrate Unity into UWP applications
  * BuildOptions API reference