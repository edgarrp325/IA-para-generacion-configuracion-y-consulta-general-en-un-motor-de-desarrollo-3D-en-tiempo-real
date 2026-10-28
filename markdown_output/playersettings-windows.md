---
title: "Windows Player settings"
category: "General"
source_file: "playersettings-windows.html"
doc_type: "manual"
---

# Windows Player settings

This page details the **Player** settings specific to Windows. For a description of the general **Player** settings, refer to Player settings.

Windows Player settings

You can find documentation for the properties in the following sections:

  * Icon
  * Resolution and Presentation
  * Splash Image
  * Other Settings

## Icon

Enable the **Override for Windows, Mac, Linux** setting to assign a custom icon for your desktop game. You can upload different sizes of the icon to fit each of the squares provided.

Icon settings

## Resolution and Presentation

Use the **Resolution and Presentation** section to customize aspects of the screen’s appearance.

### Resolution

This section allows you to customize the screen mode and default size.

Resolution **Property** | **Description**  
---|---  
**Fullscreen Mode** | Choose the full-screen mode. This defines the default window mode at startup.  
| **Fullscreen Window** | Set your app window to the full-screen native display resolution, covering the whole screen. This mode is also known as borderless full-screen. Unity renders the app content at the resolution set by a script, or the native display resolution if none is set and scales it to fill the window. When scaling, Unity adds black bars to the rendered output to match the display **aspect ratio** to prevent content stretching. This process is called letterboxing. The OS overlay **UI** to prevent content stretching. This process is called letterboxing. The OS overlay **UI** displays on top of the full-screen window (such as IME input windows). All platforms support this mode.  
| **Exclusive Fullscreen (Windows only)** | Set your app to maintain sole full-screen use of a display. Unlike **Fullscreen Window** , this mode changes the OS resolution of the display to match the app’s chosen resolution. This option is only supported on Windows.  
| **Maximized Window (Mac only)** | Set the app window to the operating system’s definition of **maximized** , which is typically a full-screen window with a hidden menu bar and dock on macOS. This option is only supported on macOS. **Fullscreen Window** is the default setting for other platforms.  
| **Windowed** | Set your app to a standard, non-full-screen movable window, the size of which is dependent on the app resolution. In this mode, the window is resizable by default. Use the Resizable Window setting to disable this. All desktop platforms support this full-screen mode.  
**Default Is Native Resolution** | Enable this option to make the game use the default resolution used on the target machine. This option isn’t available if the **Fullscreen Mode** is set to **Windowed**.  
**Default Screen Width** | Set the default width of the game screen in **pixels**. This option is only available if the **Fullscreen Mode** is set to **Windowed**.  
**Default Screen Height** | Set the default height of the game screen in pixels. This option is only available if the **Fullscreen Mode** is set to **Windowed**.  
**Mac Retina Support** | Enable this option to enable support for high DPI (Retina) screens on a Mac. Unity enables this by default. This enhances Projects on a Retina display, but it’s somewhat resource-intensive when active.  
**Run In background** | Enable this option to have the game running in the background instead of pausing if the app loses focus.  
  
### Standalone Player Options

This section allows you to specify how the user can customize the screen. For example, you can determine whether the user can resize the screen and how many instances can run concurrently.

Standalone Player Options **Property** | **Description**  
---|---  
**Use Player Log** | Enable this option to write a log file with debugging information. This option is enabled by default.  
**Resizable Window** | Enable this option to allow resizing of the desktop player window.  
**Visible in Background** | Enable this option to display the application in the background if **Windowed** Fullscreen Mode is used. **Note:** This prevents keyboard shortcuts that minimize the app window from functioning. For example, `Alt+Tab` and `Windows+M`. For more information, refer to PlayerSettings.visibleInBackground.  
**Allow Fullscreen Switch** | Enable this option to allow default OS full-screen key presses to toggle between full-screen and windowed modes.  
**Force Single Instance** | Enable this option to restrict desktop players to a single concurrent running instance.  
**Use DXGI flip model swap chain for D3D11** | Using the flip model ensures the best performance. This setting affects the D3D11 graphics API. Disable this option to fall back to the Windows 7-style BitBlt model. For more information, refer to PlayerSettings.useFlipModelSwapchain.  
  
## Splash Image

Use the **Virtual Reality Splash Image** setting to select a custom splash image for Virtual Reality displays. For information on common Splash Screen settings, refer to Splash Screen.

Splash Image

## Other Settings

This section allows you to customize a range of options organized into the following groups:

  * Rendering
  * Vulkan Settings
  * Configuration
  * Shader Settings
  * Shader Variant Loading Settings
  * Optimization
  * Stack Trace
  * Legacy

### Rendering

Use these settings to customize how Unity renders your game for desktop platforms.

**Property** | **Description**  
---|---  
**Color Space** | Choose which color space to use for rendering. For more information, refer to Linear rendering overview.  
**Gamma** | Gamma color space is typically used for calculating lighting on older hardware restricted to 8 bits per channel for the framebuffer format. Even though monitors today are digital, they might still take a gamma-encoded signal as input.  
**Linear** | Linear color space rendering gives more precise results. When you select to work in linear color space, the Editor defaults to using sRGB sampling. If your Textures are in linear color space, you need to work in linear color space and deactivate sRGB sampling for each Texture.  
**MSAA Fallback** | Select the multi sample antialiasing fallback strategy to upgrade or downgrade the sample count if the sample count requested by the user isn’t supported by the device.  
**Upgrade** | The sample count reduces to the nearest supported lower sample count.  
**Downgrade** | The sample count increases to the next higher sample count. If that sample count is not supported, then it reduces to the nearest supported lower sample count.  
**Auto Graphics API for Windows** | Enable this option to use the recommended Graphics API on the Windows machine the game is running on. Disable it to add and remove supported Graphics APIs.   
**Auto Graphics API for Mac** | This setting doesn’t apply to the Windows platform.  
**Auto Graphics API for Linux** | Enable this option to use the best Graphics API for the Linux machine the application runs on. Disable it to add and remove supported Graphics APIs.  
**Color Gamut for Mac** | This setting doesn’t apply to the Windows platform.   
**Static Batching** | Enable this option to use static batching.  
**Dynamic Batching** | Use Dynamic Batching on your build (enabled by default)..  
  
**Note:** Dynamic batching has no effect when a Scriptable Render Pipeline is active. This setting is visible only when the **Scriptable Render Pipeline Asset** Graphics setting is blank.  
**Sprite Batching Threshold** | Controls the maximum vertex threshold used when batching.  
**GPU Compute Skinning** | Enable the use of shaders to calculate mesh skinning and blend shapes on the GPU.  
**Graphics Jobs** | Offload graphics tasks (render loops) to worker threads running on other CPU cores. This option reduces the time spent in `Camera.Render` on the main thread, which can be a bottleneck.  
**Lightmap Encoding** | Defines the encoding scheme and compression format of the lightmaps.   
You can choose from **Low Quality** , **Normal Quality** , or **High Quality**  
**HDR Cubemap Encoding** | Defines the encoding scheme and compression format of the HDR Cubemaps.   
You can choose from **Low Quality** , **Normal Quality** , or **High Quality**. For more information, refer to Lightmaps: Technical information.  
**Lightmap Streaming** | Enable this option to use Mipmap Streaming for lightmaps. Unity applies this setting to all lightmaps when it generates them.  
  
**Note:** To use this setting, you must enable the Texture Streaming Quality setting.  
**Streaming Priority** | Set the priority for all lightmaps in the Mipmap Streaming system. Unity applies this setting to all lightmaps when it generates them.  
Positive numbers give higher priority. Valid values range from `-128` to `127`.  
**Frame Timing Stats** | Enable this property to gather CPU and GPU frame timing data using the FrameTimingManager API. If you disable this property, the Dynamic Resolution  
**OpenGL: Profiler GPU Recorders** | Enable GPU recorder support and disable the GPU profiler. The OpenGL API doesn’t allow both the recorder and profiler to work simultaneously.  
**Allow HDR Display Output** | Enable HDR mode output when the application runs. If the display doesn’t support HDR mode, the game runs in standard mode.  
**Use HDR Display Output** | Checks if the main display supports HDR, and if it does, swaps to HDR output when the application launches.  
  
**Note** : This option is available only when **Allow HDR Display Output** is active.  
**Swap Chain Bit Depth** | Select the number of bits in each color channel for swap chain buffers.   
  
This setting is available only when **Use display in HDR Mode** is enabled.  
**Bit Depth 10** | Unity uses the R10G10B10A2 buffer format and Rec2020 primaries with ST2084 PQ encoding.  
**Bit Depth 16** | Unity uses the R16G16B16A16 buffer format and Rec709 primaries with linear color (no encoding).  
**Virtual Texturing (Experimental)** | Enable this option to reduce GPU memory usage and texture loading times if your Scene has many high resolution textures. For more information, refer to Virtual Texturing.   
  
**Note** : The Unity Editor requires a restart for this setting to take effect.   
**360 Stereo Capture** | Indicates whether Unity can capture stereoscopic 360 images and videos.  
**Load/Store Action Debug Mode** | Highlights undefined pixels that might cause rendering problems on mobile platforms. This affects the Unity Editor Game view, and your built application if you select **Development Build** in Build Settings. Refer to LoadStoreActionDebugModeSettings for more information.  
**Editor Only** | Indicates whether the Load/Store Action Debug Mode only runs in the Unity Editor.  
  
**Note** : This option is visible only when **Load/Store Action Debug Mode** is active.  
  
### Vulkan Settings

**Property** | **Description**  
---|---  
**SRGB Write Mode** |  Enable this option to allow `Graphics.SetSRGBWrite()` renderer to toggle the sRGB write mode during runtime. That is, if you want to temporarily turn off Linear-to-sRGB write color conversion, you can use this property to achieve that. Enabling this has a negative impact on performance on mobile tile-based GPUs; therefore, do NOT enable this for mobile.  
**Number of swapchain buffers** |  Set this option to 2 for double-buffering, or 3 for triple-buffering to use with Vulkan renderer. This setting may help with latency on some platforms, but in most cases you should not change this from the default value of 3. Double-buffering might have a negative impact on performance. Do not use this setting on Android.  
**Acquire swapchain image late as possible** |  If enabled, Vulkan delays acquiring the backbuffer until after it renders the frame to an offscreen image. Vulkan uses a staging image to achieve this. Enabling this setting causes an extra blit when presenting the backbuffer. This setting, in combination with double-buffering, can improve performance. However, it also can cause performance issues because the additional blit takes up bandwidth.  
**Recycle command buffers** | Indicates whether to recycle or free CommandBuffers after Unity executes them.  
  
### Configuration

Configuration settings **Property** | **Description**  
---|---  
**Scripting Backend** |  Choose the scripting backend you want to use. The scripting backend determines how Unity compiles and executes C# code in your Project.  
**Mono** | Compiles C# code into .NET Common Intermediate Language (CIL) and executes that CIL using a Common Language Runtime. For more information, refer to Mono.  
**IL2CPP** | Compiles C# code into CIL, converts the CIL to C++ and then compiles that C++ into native machine code, which executes directly at runtime. For more information, refer to IL2CPP.  
**API Compatibility Level** | Choose which .NET APIs you can use in your project. This setting can affect compatibility with third-party libraries. However, it has no effect on Editor-specific code (code in an Editor directory, or within an Editor-specific Assembly Definition).  
  
**Tip:** If you are having problems with a third-party assembly, you can try the suggestion in the API Compatibility Level section below.  
**.Net Framework** | Compatible with the .NET Framework 4 (which includes everything in the .NET Standard 2.0 profile plus additional APIs). Choose this option when using libraries that access APIs not included in .NET Standard 2.0. Produces larger builds and any additional APIs available aren’t necessarily supported on all platforms. Refer to Referencing additional class library assemblies for more information.  
**.Net Standard 2.1** | Produces smaller builds and has full cross-platform support.  
**IL2CPP Code Generation** | Defines how Unity manages IL2CPP code generation. This option is only available if you use the IL2CPP scripting backend.  
**Faster runtime** | Generates code optimized for runtime performance. This setting is enabled by default.  
**Faster (smaller) builds** | Generates code optimized for build size and iteration. This setting generates less code and produces a smaller build, but can reduce runtime performance for generic code. Use this option when faster build times are important, such as when iterating on changes.  
**C++ Compiler Configuration** | Choose the C++ compiler configuration used when compiling IL2CPP generated code.  
**Debug** | Debug configuration turns off all optimizations, which makes the code quicker to build but slower to run.  
**Release** | Release configuration enables optimizations, so the compiled code runs faster and the binary size is smaller but it takes longer to compile.  
**Master** | Master configuration enables all possible optimizations, squeezing every bit of performance possible. For instance, on platforms that use the MSVC++ compiler, this option enables link-time code generation. Compiling code using this configuration can take significantly longer than it does using the Release configuration. Unity recommends building the shipping version of your game using the Master configuration if the increase in build time is acceptable.  
**Use incremental GC** | Uses the incremental garbage collector, which spreads garbage collection over several frames to reduce garbage collection-related spikes in frame duration. For more information, refer to Automatic Memory Management.  
**Allow downloads over HTTP** | Indicates whether to allow downloading content over HTTP. The default option is **Not allowed** due to the recommended protocol being HTTPS, which is more secure.  
**Not Allowed** | Never allow downloads over HTTP.  
**Allowed in Development Builds** | Only allow downloads over HTTP in development builds.  
**Always Allowed** | Allow downloads over HTTP in development and release builds.  
**Active Input Handling** | Choose how to handle input from users.  
**Input Manager (Old)** | Uses the traditional Input settings.  
**Input System Package (New)** | Uses the Input system. This option requires you to install the InputSystem package.  
**Both** | Use both systems.  
  
#### API Compatibility Level

You can choose your mono API compatibility level for all targets. Sometimes a third-party .NET library uses functionality that is outside of your .NET compatibility level. In order to understand what is going on in such cases, and how to best fix it, try following these suggestions: 

  1. Install ILSpy for Windows.
  2. Drag the .NET assemblies for the API compatibility level that you are having issues with into ILSpy. You can find these under `Frameworks/Mono/lib/mono/YOURSUBSET/`.
  3. Drag in your third-party assembly.
  4. Right-click your third-party assembly and select **Analyze**.
  5. In the analysis report, inspect the **Depends on** section. The report highlights anything that the third-party assembly depends on, but that is not available in the .NET compatibility level of your choice in red.

### Shader Settings

**Property** | **Description**  
---|---  
**Shader Precision Model** | Select the default precision shaders use. For more information, refer to Use 16-bit precision in shaders.  
**Platform default** | Use lower precision on mobile platforms, and full precision on other platforms.  
**Unified** | Use lower precision if the platform supports it.  
**Strict shader variant matching** | Enable this option to use the error shader for rendering if a shader variant is missing in the Player build and display an error in the console. The error specifies the shader, subshader index, pass, and keywords used for shader variant search  
**Keep Loaded Shaders Alive** | Keep all loaded shaders alive and prevent unloading. For more information, refer to shader loading.  
  
### Shader Variant Loading Settings

Use these settings to control how much memory **shaders** use at runtime.

**Property** | **Description**  
---|---  
**Default chunk size (MB)** | Sets the maximum size of compressed shader variant data chunks Unity stores in your built application for all platforms. The default is `16`. For more information, refer to Shader loading.  
**Default chunk count** | Sets the default limit on how many decompressed chunks Unity keeps in memory on all platforms. The default is `0`, which means there’s no limit.  
**Override** | Enables overriding **Default chunk size** and **Default chunk count** for this build target.  
**Chunk size (MB)** | Overrides the value of **Default chunk size (MB)** on this build target.  
**Chunk count** | Overrides the value of **Default chunk count** on this build target.  
  
### Script Compilation

Script Compilation settings **Property** | **Description**  
---|---  
**Scripting Define Symbols** | Set custom compilation flags. For more details, refer to Platform dependent compilation.  
**Additional Compiler Arguments** | Add entries to this list to pass additional arguments to the Roslyn compiler. Use one new entry for each additional argument.  
  
To create a new entry, press the ‘+’ button. To remove an entry, press the ‘-’ button. When you have added all desired arguments, click the **Apply** button to include your additional arguments in future compilations. The **Revert** button resets this list to the most recent applied state.  
**Suppress Common Warnings** | Disable this setting to display the C# warnings CS0169 and CS0649.  
**Allow ‘unsafe’ Code** | Enable support for compiling ‘unsafe’ C# code in a pre-defined assembly (for example, `Assembly-CSharp.dll`).   
For Assembly Definition Files (`.asmdef`), click on one of your `.asmdef` files and enable the option in the Inspector window that appears.  
**Use Deterministic Compilation** | Disable this setting to prevent compilation with the -deterministic C# flag. With this setting enabled, compiled assemblies are byte-for-byte identical each time they’re compiled.  
For more information, refer to Microsoft’s deterministic compiler option documentation.  
  
### Optimization

Optimization settings **Property** | **Description**  
---|---  
**Prebake Collision Meshes** | Adds collision data to Meshes at build time.  
**Preloaded Assets** | Sets an array of Assets for the player to load on startup.   
To add new Assets, increase the value of the **Size** property and then set a reference to the Asset to load in the new **Element** box that appears.  
**Managed Stripping Level** | Chooses how aggressively Unity strips unused managed (C#) code. When Unity builds your app, the Unity Linker process can strip unused code from the managed DLLs your Project uses. Stripping code can make the resulting executable smaller, but can sometimes remove code that’s in use.   
  
For more information about these options and bytecode stripping with IL2CPP, refer to ManagedStrippingLevel.  
**Minimal** | Use this to strip class libraries, UnityEngine, Windows Runtime assemblies, and copy all other assemblies.  
**Low** | Remove unreachable managed code to reduce build size and Mono/IL2CPP build times.  
**Medium** | Run UnityLinker to reduce code size beyond what **Low** can achieve. You might need to support a custom link.xml file, and some reflection code paths might not behave the same.  
**High** | UnityLinker will strip as much code as possible. This will further reduce code size beyond what Medium can achieve but managed code debugging of some methods might no longer work. You might need to support a custom link.xml file, and some reflection code paths might not behave the same.  
**Vertex Compression** | Sets vertex compression per channel. This affects all the meshes in your project.   
Typically, Vertex Compression is used to reduce the size of mesh data in memory, reduce file size, and improve GPU performance.   
  
For more information on how to configure vertex compression and limitations of this setting, refer to Compressing mesh data.  
**Optimize Mesh Data** | Enable this option to strip unused vertex attributes from the mesh used in a build. This option reduces the amount of data in the mesh, which can help reduce build size, loading times, and runtime memory usage.   
  
**Warning:** If you have this setting enabled, don’t change material or shader settings at runtime.   
  
For more information, refer to PlayerSettings.stripUnusedMeshComponents.  
**Texture MipMap Stripping** | Enables mipmap stripping for all platforms. It strips unused mipmaps from Textures at build time.   
Unity determines unused mipmaps by comparing the value of the mipmap against the quality settings for the current platform. If a mipmap value is excluded from every quality setting for the current platform, then Unity strips those mipmaps from the build at build time. If `QualitySettings.masterTextureLimit` is set to a mipmap value that has been stripped, Unity will set the value to the closest mipmap value that hasn’t been stripped.  
  
### Stack Trace

Stack Trace settings

Select your preferred stack trace method by enabling the option that corresponds to each Log Type (**Error** , **Assert** , **Warning** , **Log** , and **Exception**) based on the type of logging you require. For more information, refer to stack trace logging. 

**Property** | **Description**  
---|---  
**None** | No logs are ever recorded.  
**ScriptOnly** | Logs only when running **scripts**.  
**Full** | Logs all the time.  
  
### Legacy

Legacy settings **Property** | **Description**  
---|---  
**Clamp BlendShapes (Deprecated)** | Enable the option to clamp the range of blend shape weights in SkinnedMeshRenderers.