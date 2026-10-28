---
title: "iOS Build Settings reference"
category: "General"
source_file: "BuildSettingsiOS.html"
doc_type: "manual"
---

# iOS Build Settings reference

Use the iOS Build settings to configure and build your application for iOS devices. The iOS Build settings are part of the Build Settings window. 

To view the iOS Build settings, use the following steps:

  1. Select **File** > **Build Settings**.
  2. From the list of platforms in the **Platform** pane, select **iOS**. If **iOS** is unavailable, follow the steps on iOS environment setup.
  3. Select **Switch Platform** if the **Build** options aren’t available.

You can configure the following settings for your build:

**Property** | **Description** |   
---|---|---  
**Run in Xcode** | Select the Xcode version to open your project with. You can choose the **Latest version** or select a specific version from the drop-down list.  
  
If you have a specific Xcode version installed on your machine that doesn’t appear in this list, select **Other** to find the version in the **Applications** window that appears. If Unity can’t find an Xcode installation on your computer, select the **Browse** button that you can select to locate the Xcode installation directory on your computer, if it exists.   
  
**Note** : This option is visible only when you run Unity on macOS.  
**Run in Xcode as** | Selects whether Xcode runs your Project as a **Release** or **Debug** build.  
| **Release** | Builds an optimized version of your app.  
| **Debug** | Builds a testing version of your app that contains additional code that helps with debugging.  
**Symlink Sources** | References Unity libraries instead of copying them into the Xcode project. This option reduces the Xcode project size and makes iteration times faster.   
  
**Note** : This option is visible only when you run Unity on macOS.  
****Development Build**** | Indicates whether to include scripting debug symbols and the Profiler in your build. Use this setting when you want to test your application. When you select this option, Unity sets the `DEVELOPMENT_BUILD` scripting define. Your build then includes preprocessor directives that set `DEVELOPMENT_BUILD` as a condition. For more information, refer to Platform dependent compilation.  
**Autoconnect Profiler** | Automatically connects the Profiler to the build. For more information, refer to Profiler.  
  
**Note** : This property is visible only when **Development Build** is enabled.  
**Deep Profiling** | Allow the Profiler to process all your script code and record every function call, returning detailed profiling data. For more information, refer to Deep Profiling This option might slow down script execution.  
  
**Note** : This property is visible only when **Development Build** is enabled.  
**Script Debugging** | Attach script debuggers to the Player remotely.   
  
**Note** : This property is visible only when **Development Build** is enabled.  
**Wait For Managed Debugger** | Force the Player to wait for a debugger to be attached before it executes any script code.  
  
**Note** : This property is visible only when **Script Debugging** is enabled.  
****Compression** Method** | Specifies the method Unity uses to compress the data in your Project when it builds the Player. This includes Assets, Scenes, Scenes, Player settings, Player settings, and GI data.  
| **Default** | The default compression is None.  
| **LZ4** | A fast compression format that’s useful for development builds. LZ4 compression can significantly improve the loading time of your application. For more information, refer to BuildOptions.CompressWithLz4.  
| **LZ4HC** | A high compression variant of LZ4 that’s slower to build but produces better results for release builds. LZ4HC compression can significantly improve the loading time of your application. For more information, refer to BuildOptions.CompressWithLz4HC.  
  
## Additional resources

  * Build an iOS application
  * BuildOptions API reference