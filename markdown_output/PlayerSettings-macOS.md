---
title: "macOS player settings"
category: "General"
source_file: "PlayerSettings-macOS.html"
doc_type: "manual"
---

# macOS player settings

This page details the **Player** settings specific to macOS. For a description of the general **Player** settings, refer to Player Settings.

You can find documentation for the properties in the following sections:

  * Icon
  * Resolution and Presentation
  * Splash Image
  * Other Settings

## Icon

Activate the **Override for Windows, Mac, Linux** setting to assign a custom icon for your desktop game. You can upload different sizes of the icon to fit each of the squares provided.

## Resolution and presentation

Use the **Resolution and Presentation** section to customize aspects of the screen’s appearance.

### Resolution

This section allows you to customize the screen mode and default size.

**Property** | **Description**  
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

Use this section to specify the settings to customize the screen. For example, you can set options for users to resize the screen and specify the number of instances that can run concurrently.

**Property** | **Description**  
---|---  
**Use Player Log** | Activate this option to write a log file with debugging information.  
**Warning:** If you plan to submit your application to the Mac App Store, leave this option deactivated. For more information, refer to Publishing to the Mac App Store.  
**Resizable Window** | Activate this option to allow resizing of the desktop player window.  
**Note:** If you deactivate this option, your application can’t use the _Windowed_ Fullscreen Mode.  
**Visible in Background** | Activate this option to display the application in the background when using _Windowed_ Fullscreen Mode. This option isn’t supported on macOS.  
**Allow Fullscreen Switch** | Activate this option to allow default OS full-screen key presses to toggle between full-screen and windowed modes.  
**Force Single Instance** | Activate this option to restrict desktop players to a single concurrent running instance.  
**Use DXGI flip model swap chain for D3D11** | Using the flip model ensures the best performance. This setting affects the D3D11 graphics API. Deactivate this option to fall back to the Windows 7-style BitBlt model. For more information, refer to PlayerSettings.useFlipModelSwapchain.  
  
## Splash Image

Use the **Virtual Reality Splash Image** setting to select a custom splash image for Virtual Reality displays. For information on common Splash Screen settings, refer to Splash Screen.

## Other Settings

  * Rendering
  * Vulkan Settings
  * Mac App Store Options
  * Configuration
  * Mac Configuration
  * Shader Settings
  * Shader Variant Loading Settings
  * Script Compilation
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
**Auto Graphics API for Windows** | Enable this option to use the best Graphics API on the Windows machine the game is running on. Disable it to add and remove supported Graphics APIs.   
**Auto Graphics API for Mac** | Enable this option to use the best Graphics API on the Mac the game is running on. Disable it to add and remove supported Graphics APIs.   
**Auto Graphics API for Linux** | Enable this option to use the best Graphics API on the Linux machine it runs on. Disable it to add and remove supported Graphics APIs.   
**Color Gamut for Mac** | You can add or remove color gamuts for the Mac platform to use for rendering. Click the plus (+) icon to display a list of available gamuts. A color gamut defines a possible range of colors available for a given device (such as a monitor or screen). The sRGB gamut is the default (and required) gamut.   
**Metal API Validation** | Enable this option to use in-Editor tool to debug Shader issues. On a draw call, the tool checks a shaders expected textures and buffers against the attached and confirms its compatibility. The results of the checks are available in the console.   
  
**Metal API Validation** doesn’t enable Apple’s Metal API validation, but you can enable it by setting **Run in Xcode as** to **Debug** in the Build Settings window for macOS and iOS.  
  
**Note** : This setting only appears when running the Editor on macOS.  
**Metal Write-Only Backbuffer** |  Allow improved performance in non-default device orientation. This sets the `frameBufferOnly` flag on the back buffer, which prevents readback from the back buffer and enables some driver optimization.   
**Force hard shadows on Metal** | Enable point sampling for shadows on Metal. This reduces shadow quality and improves performance.  
**Memoryless Depth** |  Choose when to use memoryless render textures. Memoryless render textures are temporarily stored in the on-tile memory when rendered, not in CPU or GPU memory. This reduces memory usage of your app but you can’t read or write to these render textures.  
  
**Note** : Memoryless render textures are only supported on iOS, tvOS 10.0+, Metal, and Vulkan. Render textures are read/write protected and stored in CPU or GPU memory on other platforms.   
**Unused** | Never use memoryless framebuffer depth.  
**Forced** | Always use memoryless framebuffer depth.  
**Automatic** | Let Unity decide when to use memoryless framebuffer depth.  
**Multithreaded Rendering** | Enable this option to move graphics API calls from Unity’s main thread to a separate worker thread. This can help to improve performance in applications that have high CPU usage on the main thread.  
**Static Batching** | Enable this option to use static batching.  
**Dynamic Batching** | Use Dynamic Batching on your build (enabled by default)..  
  
**Note:** Dynamic batching has no effect when a Scriptable Render Pipeline is active. This setting is visible only when the **Scriptable Render Pipeline Asset** Graphics setting is blank.  
**Sprite Batching Threshold** | Controls the maximum vertex threshold used when batching.  
**GPU Compute Skinning** | Enable this option to use Metal GPU compute skinning, which frees up CPU resources.  
**Graphics Jobs (Experimental)** | Enable this option to instruct Unity to offload graphics tasks (render loops) to worker threads running on other CPU cores. This is intended to reduce the time spent in `Camera.Render` on the main thread, which is often a bottleneck.   
**Note:** This feature is experimental. It may not deliver a performance improvement for your project, and may introduce new crashes.  
**Lightmap Encoding** | Defines the encoding scheme and compression format of the lightmaps.   
You can choose from **Low Quality** , **Normal Quality** , or **High Quality**  
**HDR Cubemap Encoding** | Defines the encoding scheme and compression format of the HDR Cubemaps.   
You can choose from **Low Quality** , **Normal Quality** , or **High Quality**. For more information, refer to Lightmaps: Technical information.  
**Lightmap Streaming** | Enable this option to use Mipmap Streaming for lightmaps. Unity applies this setting to all lightmaps when it generates them.  
  
**Note:** To use this setting, you must enable the Texture Streaming Quality setting.  
**Streaming Priority** | Set the priority for all lightmaps in the Mipmap Streaming system. Unity applies this setting to all lightmaps when it generates them.  
Positive numbers give higher priority. Valid values range from `-128` to `127`.  
**Frame Timing Stats** | Enable this option to gather CPU/GPU frame timing statistics.  
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
**360 Stereo Capture** | Allows Unity to capture stereoscopic 360 images and videos. When enabled, Unity compiles additional shader variants to support 360 capture (only on Windows). When enabled, the `enable_360_capture` keyword is added during the Stereo RenderCubemap call. This keyword isn’t triggered outside the `Stereo RenderCubemap` function.  
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
  
### Mac App Store Options

**Property** | **Description**  
---|---  
**Override Default Bundle Identifier** | Indicates whether you can manually set the bundle identifier.  
  
**Note:** This setting affects macOS, iOS, tvOS, and Android.  
| **Bundle Identifier** | Enter the Bundle Identifier of your application. This appears as `CFBundleIdentifier` in the associated `info.plist` file. The Bundle Identifier must follow the convention `com.YourCompanyName.YourProductName` and must contain only alphanumeric and hyphen characters. For more information, refer to CFBundleIdentifier.  
  
**Important** : Unity automatically replaces any invalid characters you type with a hyphen.  
**Build** | Enter the build number for this version of your app. This appears as `CFBundleVersion` in the associated _info.plist_ file. For more information, refer to CFBundleVersion.  
**Category** | Enter the string corresponding to the app’s type. The App Store uses this string to select the appropriate categorization for the app. By default, this is `public.app-category.games`. For more information, refer to LSApplicationCategoryType.  
**Mac App Store Validation** | Activate this so that your app only runs when it has a valid receipt from the Mac App Store. This prevents people from running the game on a different device. Only deactivate this setting if you have implemented your own receipt validation.  
  
### Publishing to the Mac App Store

The Use Player Log property creates a log file with debugging information, helping to investigate any problems with your game. Deactivate this when publishing games for Apple’s Mac App Store, as Apple can reject your submission if activated. For more information, refer to Log Files.

The **Use Mac App Store Validation** property activates receipt validation for the Mac App Store. If activated, your game only runs when it has a valid receipt from the Mac App Store. Use this when submitting games to Apple for publishing on the App Store. This prevents people from running the game on a different computer.

**Note** : This feature doesn’t implement any strong copy protection. In particular, any potential crack for one Unity game can work for any other Unity content. For this reason, it’s recommended that you implement your own receipt validation code on top of this, using Unity’s **plug-in** feature. Because Apple requires plug-in validation to initially happen before showing the screen setup dialog, it’s recommended to activate this property to avoid Apple rejecting your submission.

### Configuration

**Property** | **Description**  
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
**C++ Compiler Configuration** | Chooses the C++ compiler configuration used when compiling IL2CPP generated code.  
  
**Note:** This property is disabled for the Universal Windows Platform because it’s chosen in the generated Visual Studio project.  
**Use incremental GC** | Uses the incremental garbage collector, which spreads garbage collection over several frames to reduce garbage collection-related spikes in frame duration. For more information, refer to Automatic Memory Management.  
**Allow downloads over HTTP** |  Indicates whether to allow downloading content over HTTP. The options are **Not allowed** , **Allowed in Development builds only** , and **Always allowed**. The default option is **Not allowed** due to the recommended protocol being HTTPS, which is more secure.   
**Target minimum macOS Version** | Enter the minimum version of macOS that the application will run on.  
**Active Input Handling** |  Choose how to handle input from users.   
  
#### API compatibility level

You can choose your mono API compatibility level for all targets. Sometimes a third-party .NET library uses functionality that’s outside of your .NET compatibility level. To understand what’s going on in such cases, and how to best fix it, try following these suggestions:

  1. Install ILSpy for Windows.
  2. Drag the .NET assemblies for the API compatibility level that you are having issues with into ILSpy. You can find these under `Frameworks/Mono/lib/mono/YOURSUBSET/`.
  3. Drag in your third-party assembly.
  4. Right-click your third-party assembly and select **Analyze**.
  5. In the analysis report, inspect the **Depends on** section. The report highlights anything that the third-party assembly depends on, but that’s not available in the .NET compatibility level of your choice in red.

### Mac Configuration

**Property** | **Description**  
---|---  
**Camera Usage Description** | Enter the reason for accessing the camera on the device.  
**Microphone Usage Description** | Enter the reason for accessing the microphone on the device.  
**Bluetooth Usage Description** | Enter the reason for accessing the device’s Bluetooth connection.   
**Supported URL schemes** | A list of supported URL schemes. To add new schemes, increase the value of the **Size** property, then set a reference to the Asset to load in the new **Element** box that appears.  
  
### Shader Settings

**Property** | **Description**  
---|---  
**Shader Precision Model** | Select the default precision shaders use. For more information, refer to Use 16-bit precision in shaders.  
**Platform default** | Use lower precision on mobile platforms, and full precision on other platforms.  
**Unified** | Use lower precision if the platform supports it.  
**Strict shader variant matching** | Use the error shader if a shader variant is missing and display an error in the console.  
**Keep Loaded Shaders Alive** | Keep all loaded shaders alive and prevent unloading.  
  
### Shader Variant Loading Settings

Use these settings to control how much memory **shaders** use at runtime.

**Property** | **Description**  
---|---  
**Default chunk size (MB)** | Sets the maximum size of compressed shader variant data chunks Unity stores in your built application for all platforms. The default is `16`. For more information, refer to Shader loading.  
**Default chunk count** | Sets the default limit on how many decompressed chunks Unity keeps in memory on all platforms. The default is `0`, which means there’s no limit.  
**Override** | Enables overriding **Default chunk size** and **Default chunk count** for this build target.  
**Chunk size (MB)** | Overrides the value of **Default chunk size (MB)** on this build target.  
**Chunk count** | Overrides the value of **Default chunk count** on this build target.  
  
### Script compilation

**Property** | **Description**  
---|---  
**Scripting Define Symbols** | Sets custom compilation flags.   
  
For more information, refer to Platform dependent compilation.  
**Additional Compiler Arguments** | Adds entries to this list to pass additional arguments to the Roslyn compiler. Use one new entry for each additional argument.  
To create a new entry, click **Add** (**+**). To remove an entry, click **Remove** (**-**).  
  
When you have added all desired arguments, click **Apply** to include your additional arguments in future compilations. Click **Revert** to reset this list to the most recent applied state.  
**Suppress Common Warnings** | Indicates whether to display the C# warnings CS0169 and CS0649.  
**Allow ‘unsafe’ Code** | Activate support for compiling ‘unsafe’ C# code in a pre-defined assembly (for example, `Assembly-CSharp.dll`).   
For Assembly Definition Files (`.asmdef`), click on one of your `.asmdef` files and activate the option in the Inspector window that appears.  
**Use Deterministic Compilation** | Indicates whether to prevent compilation with the -deterministic C# flag. With this setting active, compiled assemblies are byte-for-byte the same each time they’re compiled.  
  
For more information, refer to Microsoft’s deterministic compiler option.  
  
### Optimization

**Property** | **Description**  
---|---  
**Prebake Collision Meshes** | Adds collision data to Meshes at build time.   
**Preloaded Assets** | Sets an array of Assets for the player to load on startup.   
To add new Assets, increase the value of the **Size** property and then set a reference to the Asset to load in the new **Element** box that appears.  
**Managed Stripping Level** | Chooses how aggressively Unity strips unused managed (C#) code. The options are **Minimal** , **Low** , **Medium** , and **High**.   
When Unity builds your app, the Unity Linker process can strip unused code from the managed DLLs your Project uses. Stripping code can make the resulting executable significantly smaller, but can sometimes accidentally remove code that’s in use.   
  
For more information about these options and bytecode stripping with IL2CPP, refer to ManagedStrippingLevel.  
**Vertex Compression** | Sets vertex compression per channel. This affects all the meshes in your project.   
Typically, Vertex Compression is used to reduce the size of mesh data in memory, reduce file size, and improve GPU performance.   
  
For more information on how to configure vertex compression and limitations of this setting, refe to Compressing mesh data.   
**Optimize Mesh Data** | Enable this option to strip unused vertex attributes from the mesh used in a build. This option reduces the amount of data in the mesh, which can help reduce build size, loading times, and runtime memory usage.   
  
**Warning:** If you have this setting enabled, you should remember to not change material or shader settings at runtime.   
  
For more information, refer to PlayerSettings.stripUnusedMeshComponents.  
**Texture MipMap Stripping** | Enables mipmap stripping for all platforms. This strips unused mipmaps from Textures at build time. Unity determines unused mipmaps by comparing the value of the mipmap against the **Quality Settings** for the current platform. If a mipmap value is excluded from every **Quality Setting** for the current platform, then Unity strips those mipmaps from the build at build time. If QualitySettings.masterTextureLimit is set to a mipmap value that has been stripped, Unity will set the value to the closest mipmap value that has not been stripped.  
  
### Stack Trace

Select your preferred logging type by enabling the option that corresponds to each Log Type.

**Property** | **Description**  
---|---  
**None** | No logs are ever recorded.  
**ScriptOnly** | Logs only when running **scripts**.  
**Full** | Logs all the time.  
  
For more information, refer to stack trace logging.

### Legacy

**Property** | **Description**  
---|---  
**Clamp BlendShapes (Deprecated)** | Activate the option to clamp the range of blend shape weights in SkinnedMeshRenderers.