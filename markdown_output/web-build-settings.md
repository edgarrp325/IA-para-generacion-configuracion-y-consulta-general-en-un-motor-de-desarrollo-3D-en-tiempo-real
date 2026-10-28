---
title: "WebGL Build Settings"
category: "General"
source_file: "web-build-settings.html"
doc_type: "manual"
---

# WebGL Build Settings

Use the **WebGL** **Build Settings** to configure how Unity builds your application for the WebGL platform.

## Access the Build Settings for WebGL

To access the **Build Settings** for WebGL: 

  1. Go to **File** > **Build Settings**. 

  2. Select **WebGL**. 

## WebGL Build Settings reference

The following table gives an overview of the WebGL **Build Settings**. 

**Setting** | **Function**  
---|---  
**Texture**Compression**** | The **texture compression** format to use for the build. For more information, refer to WebGL texture compression. The available options are:  
| **Use Player Settings** | This is the default selection. It uses the texture compression format you set in the Player settings window.  
| **ETC2** | Uses ETC2 format, which is widely supported on mobile devices.  
| **ASTC** | Uses ASTC format, which is widely supported on mobile devices.  
| **DXT** | Uses DXT format, which is widely supported on desktop devices.  
****Development Build**** | Enable this setting to include scripting debug symbols and the Profiler in your build. When you enable this, Unity sets the `DEVELOPMENT_BUILD` scripting define. Use this setting only when you want to test your application because development builds don’t minify content, they’re large to distribute.  
**Code Optimization** | Select the optimization mode to use for compiling the WebGL code.  
| **Shorter Build Time** | This is the default setting. Select this option to generate WebGL code that takes the least amount of time to build.  
| **Runtime Speed** | Select this option to generate WebGL code that’s optimized for runtime performance, at the expense of taking a longer time to build.  
| **Runtime Speed with LTO** | This is the same as Runtime Speed, but with an additional Link Time Optimizations (LTO) stage (sometimes called Whole Program Optimization). Enable LTO when compiling Master shipping builds for deployment to end users.  
| **Disk Size** | Select this option to favor optimizations that minimize build size, at the expense of taking a longer time to build. The recommended best practice is to select this option when targeting mobile web browsers, that may have limits on the size of WebAssembly files that can be loaded. Smaller disk sizes generally result in shorter page startup times.  
| **Disk Size with LTO** | This is the same as Disk Size, but enables additional Link Time Optimizations (LTO) stage (sometimes called Whole Program Optimization). Select this option when compiling Master shipping builds for deployment to end users.  
**Autoconnect Profiler** | Typically, when enabled, this setting allows you to automatically connect the Unity Profiler to your build. However for WebGL, as you can’t connect the Profiler to a running build, use this option to connect the content to the Unity Editor instead. This is because the Profiler connection is handled using WebSockets on WebGL, but a web browser only allows outgoing connections from the content. For this setting to be available, you must enable the **Development Build** option.  
**Deep Profiling** | Enable this setting to activate Deep Profiling in the Profiler. This makes the Profiler instrument every function call in your application and returns more detailed profiling data. When you enable Deep Profiling Support, it might slow down script execution. This option is only available if you enable the **Development Build** option.  
**Build** | Use it to build your application.  
**Build And Run** | Use it to view the WebGL Player locally. Unity uses a local web server to host your build, and opens it from a localhost URL. Alternatively, you can use a custom local web server with properly configured response headers. For more information, see Compressed builds and server configuration.  
  
For changing the settings for **Asset Import Overrides** , refer to Build Settings.

## Additional Resources

  * Build and distribute a WebGL application
  * Build your WebGL application
  * Deploy a WebGL application
  * BuildOptions API reference