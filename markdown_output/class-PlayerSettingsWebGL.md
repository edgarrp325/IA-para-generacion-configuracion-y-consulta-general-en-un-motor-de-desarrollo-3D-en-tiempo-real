---
title: "WebGL Player settings"
category: "General"
source_file: "class-PlayerSettingsWebGL.html"
doc_type: "manual"
---

# WebGL Player settings

Use **Player** settings to know how Unity builds and displays your final **WebGL** and displays your final **WebGL** application. For a description of the general **Player** settings, refer to Player settings.

To access the WebGL **Player settings** :

  * From the Unity main menu, go to **Edit** > **Project Settings** > **Player**. The **Player** settings window appears.
  * Select the **WebGL** tab to view the WebGL Player settings.

WebGL Player settings

You can find documentation for the properties in the following sections:

  * Resolution and Presentation
  * Splash Image
  * Other Settings
  * Publishing Settings

**Note:** Although the **Icon** panel appears on the WebGL **Player** settings, there are no icon settings available because WebGL games don’t use icons. 

For more information about WebGL **Publishing Settings** , see WebGL Building and Running.

## Resolution and Presentation

Use the **Resolution and Presentation** section to customize the aspects of the screen’s appearance in the Resolution section.

Resolution section for the WebGL Player platform

### Resolution

**Setting** | **Function**  
---|---  
**Default Canvas Width** | Set the width of the WebGL canvas element.  
**Default Canvas Height** | Set the height of the WebGL canvas element.  
**Run In Background** | Enable this option to allow your content to continue to run when the canvas or the browser window loses focus.  
  
### WebGL Template

Select a template to use for your WebGL Project:

  * The **Default** page is a simple white page with a loading bar on a grey canvas.
  * The **Minimal** page has only the necessary boilerplate code to run the WebGL content.
  * The **PWA** page has a **Progressive Web App** including a web manifest file and service worker code.

You can specify your own template so that you can run your game in a similar environment to the finished game. Follow the instructions in Using WebGL Templates.

## Splash Image

Use the **Virtual Reality Splash Image** setting to select a custom splash image for XR displays. For information on common Splash Screen settings, see Splash Screen.

Splash screen settings for virtual reality.

## Other Settings

This section allows you to customize a range of options organized into the following groups:

  * Rendering
  * Configuration
  * Shader Variant Loading
  * Optimization
  * Stack Trace
  * Legacy

### Rendering

Use these settings to customize how Unity renders your game for the WebGL platform.

**Property** | **Description**  
---|---  
**Color Space** | Choose what color space to use for rendering: **Gamma** or **Linear**.   
Refer to Linear rendering overview for an explanation of the difference between the two.  
**MSAA Fallback** | Select the multi sample **antialiasing** fallback strategy to upgrade or downgrade the sample count if the sample count requested by the user isn’t supported by the device.  
| **Upgrade** | The sample count reduces to the nearest supported lower sample count.  
| **Downgrade** | The sample count increases to the next higher sample count. If that sample count is not supported, then it reduces to the nearest supported lower sample count.  
**Auto Graphics API** | Disable this option to manually pick and reorder the graphics APIs. By default this option is enabled, and Unity includes WebGL2.0, with WebGL1.0 as a fallback for devices where WebGL2.0 isn’t supported.  
**Static Batching** | Enable this option to use Static batching.  
**Dynamic Batching** | Enable this option to use Dynamic Batching on your build (enabled by default).  
**Graphics Jobs** | Enable this option to instruct Unity to offload graphics tasks (render loops) to worker threads running on other CPU cores. Use it to reduce the time spent in `Camera.Render` on the main thread, which is often a bottleneck.   
**Note:** This feature is experimental. It might not deliver a performance improvement for your project, and might introduce new crashes. |   
**Texture**compression** format** | Choose **DXT** , **ETC2** , or **ASTC** to set the **texture compression** format for WebGL. For information on how to pick the right format, refer to Texture compression format overview and to learn how to create builds for desktop and mobile browsers from a script, refer to Texture Compression in WebGL.  
****Lightmap** Encoding** | Choose **Low Quality** , **Normal Quality** , or **High Quality** to set the lightmap encoding. This setting affects the encoding scheme and compression format of the lightmaps. For more information, refer to Lightmaps: Technical information.  
****HDR** **Cubemap** **Cubemap** Encoding** | Choose **Low Quality** , **Normal Quality** , or **High Quality** to set the HDR Cubemap encoding. This setting affects the encoding scheme and compression format of the HDR Cubemaps.  
**Lightmap Streaming Enabled** | Whether to use Mipmap Streaming for lightmaps. Unity applies this setting to all lightmaps when it generates them.  
**Note:** To use this setting, you must enable the Texture Streaming Quality setting.  
**Streaming Priority** | Set the priority for all lightmaps in the Mipmap Streaming system. Unity applies this setting to all lightmaps when it generates them.  
Positive numbers give higher priority. Valid values range from —128 to 127.  
**Frame Timing Stats** | Enable this option to gather CPU/GPU frame timing statistics.  
**Virtual Texturing (Experimental)** | Indicates whether to enable Virtual Texturing.  
**Note** : The Unity Editor requires a restart for this setting to take effect.  
**360 Stereo Capture** | Indicates whether Unity can capture stereoscopic 360 images and videos. When enabled, Unity compiles additional **shader** variants to support 360 capture (currently only on Windows/OSX). When enabled, the `enable_360_capture_` keyword is added during the Stereo RenderCubemap call. Note that this keyword is not triggered outside the `Stereo RenderCubemap` function.  
**Load/Store Action Debug Mode** | Highlights undefined **pixels** that might cause rendering problems in your built application. The highlighting appears only in the Game view, and your built application if you select ****Development Build** that might cause rendering problems in your built application. The highlighting appears only in the Game view, and your built application if you select ****Development Build**** in Build Settings. Refer to LoadStoreActionDebugModeSettings.**  
**Editor Only** | Highlights undefined pixels in the Game view in the Editor, but not your built application.   
  
**Note** : This option is visible only when **Load/Store Action Debug Mode** is active.  
  
### Configuration

Configuration settings for the WebGL platform **Property** | **Description**  
---|---  
**Scripting Backend** |  Choose the scripting backend you want to use. The scripting backend determines how Unity compiles and executes C# code in your Project.  
**Mono** | Compiles C# code into .NET Common Intermediate Language (CIL) and executes that CIL using a Common Language Runtime. For more information, refer to Mono.  
**IL2CPP** | Compiles C# code into CIL, converts the CIL to C++ and then compiles that C++ into native machine code, which executes directly at runtime. For more information, refer to IL2CPP.  
**API Compatibility Level** | Choose which .NET APIs you can use in your project. This setting can affect compatibility with third-party libraries. However, it has no effect on Editor-specific code (code in an Editor directory, or within an Editor-specific Assembly Definition).  
  
**Tip:** If you are having problems with a third-party assembly, you can try the suggestion in the API Compatibility Level section below.  
**.Net Framework** | Compatible with the .NET Framework 4 (which includes everything in the .NET Standard 2.0 profile plus additional APIs). Choose this option when using libraries that access APIs not included in .NET Standard 2.0. Produces larger builds and any additional APIs available aren’t necessarily supported on all platforms. Refer to Referencing additional class library assemblies for more information.  
**.Net Standard 2.1** | Produces smaller builds and has full cross-platform support.  
**IL2CPP Code Generation** | Defines how Unity manages IL2CPP code generation.  
**Faster runtime** | Generates code optimized for runtime performance. This setting is enabled by default.  
**Faster (smaller) builds** | Generates code optimized for build size and iteration. This setting generates less code and produces a smaller build, but may reduce runtime performance, especially for generic code. Use this option when faster build times are important, such as when iterating on changes.  
**C++ Compiler Configuration** | Chooses the C++ compiler configuration used when compiling IL2CPP generated code.  
  
**Note:** This property is disabled for the Universal Windows Platform because it’s chosen in the generated Visual Studio project.  
**Use incremental GC** | Uses the incremental garbage collector, which spreads garbage collection over several frames to reduce garbage collection-related spikes in frame duration. For more information, refer to Automatic Memory Management.  
**Allow downloads over HTTP** | Indicates whether to allow downloading content over HTTP. The default option is **Not allowed** due to the recommended protocol being HTTPS, which is more secure.  
**Not Allowed** | Never allow downloads over HTTP.  
**Allowed in Development Builds** | Only allow downloads over HTTP in development builds.  
**Always Allowed** | Allow downloads over HTTP in development and release builds.  
**Active Input Handling** | Choose how to handle input from users.  
**Input Manager (Old)** | Uses the traditional Input settings.  
**Input System Package (New)** | Uses the Input system. This option requires you to install the InputSystem package.  
**Both** | Use both systems.  
  
#### Shader Variant Loading

Use these settings to control how much memory shaders use at runtime.

**Property** | **Description**  
---|---  
**Default chunk size (MB)** | Sets the maximum size of compressed shader variant data chunks Unity stores in your built application for all platforms. The default is `16`. For more information, refer to Shader loading.  
**Default chunk count** | Sets the default limit on how many decompressed chunks Unity keeps in memory on all platforms. The default is `0`, which means there’s no limit.  
**Override** | Enables overriding **Default chunk size** and **Default chunk count** for this build target.  
**Chunk size (MB)** | Overrides the value of **Default chunk size (MB)** on this build target.  
**Chunk count** | Overrides the value of **Default chunk count** on this build target.  
  
#### API Compatibility Level

You can choose your mono API compatibility level for all targets. Sometimes a third-party .NET library uses functionality that’s outside of your .NET compatibility level. To understand what is going on in such cases, and how to best fix it, try following these suggestions: 

  1. Install ILSpy for Windows.
  2. Drag the .NET assemblies for the API compatibility level that you’re having issues with into ILSpy. You can find the problematic files under `Frameworks/Mono/lib/mono/YOURSUBSET/`.
  3. Drag in your third-party assembly.
  4. Right-click your third-party assembly and select **Analyze**.
  5. In the analysis report, inspect the **Depends on** section. The report highlights anything that the third-party assembly depends on, but that’s not available in the .NET compatibility level of your choice in red.

### Script Compilation

Script compilation settings for the WebGL platform **Property** | **Description**  
---|---  
**Scripting Define Symbols** | Sets custom compilation flags.   
  
For more details, see Platform dependent compilation.  
**Additional Compiler Arguments** | Adds entries to this list to pass additional arguments to the Roslyn compiler. Use one new entry for each additional argument.  
To create a new entry, click **Add** (**+**). To remove an entry, click **Remove** (**-**).  
  
When you have added all desired arguments, click **Apply** to include your additional arguments in future compilations. Click **Revert** to reset this list to the most recent applied state.  
**Suppress Common Warnings** | Indicates whether to display the C# warnings CS0169 and CS0649.  
**Allow ‘unsafe’ Code** | Enables support for compiling ‘unsafe’ C# code in a pre-defined assembly (for example, `Assembly-CSharp.dll`).   
For Assembly Definition Files (`.asmdef`), click on one of your `.asmdef` files and enable the option in the Inspector window that appears.  
**Use Deterministic Compilation** | Indicates whether to prevent compilation with the -deterministic C# flag. With this setting enabled, compiled assemblies are byte-for-byte identical each time they are compiled.  
  
For more information, see Microsoft’s deterministic compiler option.  
  
### Optimization

Optimization settings for the WebGL platform **Property** | **Description**  
---|---  
**Prebake Collision Meshes** | Adds collision data to Meshes at build time.   
**Keep Loaded Shaders Alive** | Indicates whether to prevent shaders from being unloaded.   
  
For more information, see Shader Loading.   
**Preloaded Assets** | Sets an array of Assets for the player to load on startup.   
To add new Assets, increase the value of the **Size** property and then set a reference to the Asset to load in the new **Element** box that appears.  
**Strip Engine Code** | Enable this option if you want the Unity Linker tool to remove code for Unity Engine features that your Project doesn’t use. This setting is only available with the IL2CPP scripting backend. Most apps do not use every available DLL. This option strips out DLLs that your app doesn’t use to reduce the size of the built Player. If your app is using one or more classes that would normally be stripped out under your current settings, Unity displays a debug message when you try to build the app.  
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

Select the logging settings for the WebGL platform.

Logging settings for the WebGL platform

Select your preferred stack trace method by enabling the option that corresponds to each Log Type (**Error** , **Assert** , **Warning** , **Log** , and **Exception**) based on the type of logging you require. For more information, refer to stack trace logging. 

**Property** | **Description**  
---|---  
**None** | No logs are ever recorded.  
**ScriptOnly** | Logs only when running **scripts**.  
**Full** | Logs all the time.  
  
### Legacy

Enable the **Clamp BlendShapes (Deprecated)** option to clamp the range of blend shape weights in Skinned Mesh Renderers.

Legacy settings for the WebGL platform

## Publishing settings

Use the Publishing Settings to configure how Unity builds your WebGL app. For example, you can choose to enable the browser cache to store its files in your build.

Publishing settings for the WebGL platform **Setting** | **Function**  
---|---  
**Enable Exceptions** | Choose how to handle unexpected code behavior (generally considered errors) at run time. The options are: _None_ , _Explicitly Thrown Exceptions Only_ , _Full Without Stacktrace_ , and _Full With Stacktrace_. See the Building and running a WebGL project page for details.  
**Compression Format** | Choose the compression format to use for release build files. The options are: _Gzip_ , _Brotli_ , or _Disabled_ (none). Note that this option doesn’t affect development builds.  
**Name Files As Hashes** | Enable this option to use an MD5 hash of the uncompressed file contents as a filename for each file in the build.  
**Data caching** | Enable this option to automatically cache your contents Asset data on the user’s machine so it doesn’t have to be re-downloaded on subsequent runs (unless the contents have changed).   
Caching is implemented using the IndexedDB API provided by the browser. Some browsers might implement restrictions around this, such as asking the user for permission to cache data over a specific size.  
**Debug Symbols** | Select from the available options to specify how debug symbols are added in your build.  
| **Off** | Select this option if you don’t want any debug symbols to be added in your build.  
| **External** | Select this option to store the debug symbols to in a separate file that you can download from the server when an error occurs. It’s recommended to choose this option for release builds.  
| **Embedded** | Select this option to embed the debug symbols in a WASM file. This option helps preserve debug symbols and perform demangling (displaying the original function names) of the stack trace when an error occurs. By default, demangling support is available for this option.  
**Show Diagnostic Overlay** | Enable this option to display an overlay of diagnostics information in Web platform builds when users click the Diagnostics icon on the WebGL canvas. It’s available for both Development and Release builds.  
**Decompression Fallback** | Include decompression fallback code for build files in the loader. Use this option if you are unable to configure server response headers according to the selected compression method.  
**Initial Memory Size** | The initial size of the WASM heap memory in megabytes (MB). By default, this is set to 32 MB. If **Memory Growth Mode** is set to **None** , then this is also the maximum size of WASM heap memory.  
**Memory Growth Mode** | Choose the growth mode for the WASM heap memory from the following options. The recommended option is **Geometric**.  
| **None** | The WASM heap memory has a fixed size configured in **Initial Memory Size**.  
| **Linear** | The WASM heap memory increases by a fixed amount configured by **Linear Memory Growth Step**.  
| **Geometric** | The WASM heap memory increases relative to the current heap size depending on the factor configured in **Geometric Memory Growth Step** and **Geometric Memory Growth Cap**.  
**Power Preference** | Set a preference for which GPU to use when rendering on a multi-GPU device. Note that the browser might ignore this preference.  
| **Default** | Let the browser choose the GPU configuration.  
| **Low Performance** | Request that the browser use the integrated GPU to prioritize power savings.  
| **High Performance** | Request that the browser use the external GPU to prioritize rendering performance.  
**Maximum Memory Size** | The maximum size of the WASM heap memory in MB. By default, this is set to 2048 MB. This option is only available for the **Memory Growth Mode** **Linear** or **Geometric**.  
**Linear Memory Growth Step** | Advanced tuning option to control the WASM heap growth step in MB. By default, this is set to 16 MB. A growth step of 16 MB indicates that the heap is increased by 16 MB each time it needs to grow. Only available if **Memory Growth Mode** is set to **Linear**.  
**Geometric Memory Growth Step** | Advanced tuning option to control the WASM heap growth factor relative to the current heap size. By default, this is set to 0.2. A growth factor of 0.2 means that the size of the heap is increased by 0.2 * currentHeapSize each time the heap needs to grow. Only available if **Memory Growth Mode** is set to **Geometric**.  
**Geometric Memory Growth Cap** | Advanced tuning option to control the upper limit for a heap growth step in MB. By default, this is set to 96 MB. A growth cap of 96 MB means that the size of the heap is increased by at most 96 MB. Only available if **Memory Growth Mode** is set to **Geometric**.  
  
### Show Diagnostic Overlay setting

To help optimize WebGL builds and diagnose potential problems, you can view diagnostics information (currently limited to memory usage) by enabling this setting. Once enabled, an icon appears on the build that displays an overlay with useful data about the build. It’s available for both Development and Release builds.

  1. To view the diagnostics information, enable the **Show Diagnostics Overlay** option in the Player settings window (**File > Build Settings > Player Settings > Publishing Settings**). 

On desktop, the Diagnostics icon appears on the footer of the WebGL canvas:

Diagnostics button on the footer of the canvas

On a mobile device, the Diagnostics icon appears on the bottom-right of the screen:

An Android phone displaying the diagnostics button
  2. Click the **Diagnostics** icon. An overlay appears showing the JavaScript memory, which is further broken down to display WASM heap memory usage:

The Diagnostics overlay shows the JavaScript memory distribution and the WASM heap memory usage

The following diagnostics appear on the overlay screen:

**Property** | **Function**  
---|---  
**Total JS Memory** | The current size of the JavaScript (JS) heap, including unused memory not allocated to any JS objects in megabytes.  
| **Used JS Memory** | Memory in use by JS objects in megabytes.  
**Total WASM heap memory** | Linear memory representing the entire heap of the C/C++ Unity engine that’s compiled with Emscripten, including unallocated memory in megabytes.  
| **Used WASM heap** | The space of the WASM heap that’s allocated in megabytes.  
  
### Important note about JS Memory

The JS Memory information is obtained using the performance.memory API, which is currently only supported on Chrome or Edge. There are no other APIs available that return this information for Safari or Firefox.

**Note:** The `performance.memory` API isn’t supported on iOS devices.

On browsers where this API isn’t supported, a message showing N/A appears.

A N/A message appears on browsers that don’t support performance.memory API

## Additional resources:

  * Texture Compression in WebGL
  * Using WebGL Templates
  * Splash Screen
  * Texture compression format overview
  * Texture compression format override

PlayerSettingsWebGL