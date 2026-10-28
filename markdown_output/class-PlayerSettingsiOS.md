---
title: "iOS Player settings"
category: "General"
source_file: "class-PlayerSettingsiOS.html"
doc_type: "manual"
---

# iOS Player settings

This page details the **Player** settings specific to iOS. For a description of general **Player** settings that apply to all platforms, see Player - General settings.

Standalone iOS Player settings

You can find documentation for the properties in the following sections:

  * Icon
  * Resolution and Presentation
  * Splash Image
  * Debugging and crash reporting
  * Other Settings

## Icon

Icon settings for iOS.

Use the **Icon** settings to customize the branding for your application on the Apple Store.

You can upload and assign the following types of custom icons for each iOS device:

**Property** | **Description**  
---|---  
**Application icons** | The main device icons for your application.  
**Spotlight icons** | Icons that appears in spotlight search results.  
**Settings icons** | Icons that appears in the device’s main settings page.  
**Notification icons** | Icons that display in notifications sent from your application.  
**Marketing icons** | Icons to use in the Apple App Store.  
  
Icon files can be any image file supported by Unity, in the form of a Texture2D asset. If an icon Texture is missing, Unity scales the icon Texture with the nearest size, with a preference towards using larger Textures.

## Resolution and presentation

Use the **Resolution and Presentation** section to customize aspects of the screen’s appearance.

These settings are split into the following categories:

  * Resolution Scaling
  * Orientation
  * Allowed Orientations for Auto Rotation
  * Multitasking Support
  * Status Bar

Resolution Scaling player settings for the iOS platform

### Resolution Scaling

**Property** | **Description**  
---|---  
**Resolution Scaling Mode** | Use the **Resolution Scaling Mode** setting to set the scaling to be equal to or below the native screen resolution.  
| **Disabled** | Scaling doesn’t apply and the application renders to its native screen resolution.  
| **FixedDPI** | When you select this value, the **Target DPI** property appears.  
  
Use the **Target DPI** property to set the target DPI of the game screen. Unity downscales the game screen to match this setting if the device’s native screen DPI is higher than this value. This helps you optimize performance and battery life. You can also use it to target a specific DPI setting.  
  
Unity calculates the scale as **min(Target DPI * Factor / Screen DPI, 1)**. The Factor uses the **Resolution Scaling Fixed DPI Factor** value you enter in the Quality settings.  
**Reset resolution on window resize** | Set the screen resolution to the new window size when the window size changes. If you set **Resolution Scaling Mode** to **Fixed DPI** , the resolution recalculates based on the **Fixed DPI** property.  
  
### Orientation

**Property** | **Description**  
---|---  
**Default Orientation** | Specify the orientation of the application window within the device’s screen.  
  
**Note** : Unity shares the value you set for this setting between Android, iOS, and UWP.  
**Portrait** | Portrait orientation where the bottom of the application aligns with the bottom of the screen.  
**Portrait Upside Down** | Portrait orientation where the bottom of the application aligns with the top of the screen.  
**Landscape Right** | Landscape orientation where the right side of the application aligns with the top of the screen.  
**Landscape Left** | Landscape orientation where the left side of the application aligns with the top of the screen.  
**Auto Rotation** | The screen can rotate to any of the orientations you specify in the Allowed Orientations for Auto Rotation section.  
**Use Animated Autorotation** | Enable an animated transition when the user rotates the device. Otherwise, screen rotation changes instantly.   
**Notes** :   
• This property is visible only when you set the **Default Orientation** to **Auto Rotation**.  
• On iOS 16 and later versions, this property has no effect as autorotation is always animated.  
  
### Allowed Orientations for Auto Rotation

Use the **Allowed Orientations for Auto Rotation** section to specify which orientations the application supports when you set **Default Orientation** to **Auto Rotation**. This is useful, for example, to lock the application to landscape orientation but allow the user to change between landscape left and landscape right.

**Note** : This section is visible only when you set **Default Orientation** in the Orientation section to **Auto Rotation**.

**Property** | **Description**  
---|---  
**Portrait** | Allow portrait orientation with the bottom of the application aligned with the bottom of the screen.  
**Portrait Upside Down** | Allow portrait orientation with the bottom of the application aligned with the top of the screen.  
**Landscape Right** | Allow landscape orientation with the right side of the application aligned with the top of the screen.  
**Landscape Left** | Allow landscape orientation with the left side of the application aligned with the top of the screen.  
  
### Multitasking Support

Enable the **Requires Fullscreen** option if your application needs to run in full screen mode.

### Status Bar

Use the **Status Bar** section to specify parameters related to the iOS status bar.

**Property** | **Description**  
---|---  
**Status Bar Hidden** | Enable this option to hide the status bar when your application launches.  
**Status Bar Style** | Define the style of the status bar when the application launches. The options are _Default_ and _Light_.  
**Disable Depth and Stencil** | Enable this option to disable the depth and stencil buffers.  
**Render Over Native UI** | Enable this option to force your app to render on top of the native iOS UI.   
**Show Loading Indicator** | Select how the loading indicator appears. The options are _White Large_ , _White_ , and _Gray_.  
  
## Splash image

Use the **Virtual Reality Splash Image** setting to select a custom splash image for Virtual Reality displays. For information on common Splash Screen settings, refer to Splash Screen.

### Launch screens

Launch Screen settings for iOS.

A **launch screen** is a Storyboard file from which iOS creates a splash screen on the device. It has the following limitations:

  * You can’t display different content based on device orientation for iPads.
  * All iPhones support landscape launch screens, but certain iOS versions display the **Landscape Left** launch screen instead of the **Landscape Right** one due to a bug.
  * Before iOS 13, it wasn’t possible to override the root view controller for a storyboard, so the launch screen supports all orientations and ignores some **UI** settings like status bar behavior. Starting with iOS 13, launch screen is fully compliant with your app’s settings for orientation and status bar appearance.

**Note** : These limitations also apply to custom storyboards.

Select the **Launch screen type** for iPhone and iPad in the **iPhone Launch Screen** and **iPad Launch Screen** sections:

**Property** | **Description**  
---|---  
**Default** | When you select this option, Unity adds a solid blue-black image that’s the same color as the background for Unity’s default splash screen. The image is used for both portrait and landscape orientations, and displays using aspect-fill mode.  
**None (Deprecated)** | Apple no longer supports Launch Images. This option exists for backwards compatibility reasons. If you select it, your project will use Unity’s default splash screen instead.  
**Image and background (relative size)** | Displays an image in the center of the screen and fills the remaining area with a solid color.  
| **Portrait Image** | Select an image for portrait orientation.  
| **Landscape Image** | Select an image for landscape orientation.  
| **Background Color** | Select a background color to fill any screen space that the image doesn’t cover.  
| **Fill percentage** | Specify image size as a percentage of the screen size. Unity calculates image size based on the length or width of the screen, whichever one is smaller (vertical for landscape displays, horizontal for portrait ones).  
**Image and background (constant size)** | Displays an image in the center of the screen and fills the area with a solid color. This has the same options as **Image and background (relative size)** , except that you specify image size in points rather than as a percentage.  
  
**Tip:** Points and pixels aren’t the same. A pixel (px) is a single dot in your image. A point (pt) is a unit of length that measures 1/72 of an inch. Pixel sizes are relative to the screen size and resolution, while point sizes are the size on any screen. For more information, refer to the W3C guidance on size units.  
**Custom Storyboard** | Use a custom Storyboard file as a loading screen. When you choose this option, click the **Custom Storyboard** button to open an explorer window and select a storyboard file.  
  
### Custom storyboards

When you select the **Custom Storyboard** option in the **Launch screen type** dropdown for either iPhone or iPad, the **Custom Storyboard** button appears.

Click the **Custom Storyboard** button to select a storyboard to display when your game starts up on the device. For your storyboard to appear here, you must first create the storyboard in Xcode and copy it to your Project. For more information, refer to storyboards, scenes, and connections.

If you don’t use custom storyboards, you can use Unity’s built-in launch screens to implement splash images.

## Debugging and crash reporting

Use the debugging and crash reporting settings to gather data about your app’s performance and troubleshoot crashes.

### Debugging

**Property** | **Description**  
---|---  
**Enable Internal Profiler (Deprecated)** | This feature is deprecated and will be removed in a future version of Unity. Use the Profiler window instead.  
  
The Profiler collects application performance data and prints a report to the console. The report has the number of milliseconds each Unity subsystem takes to execute on each frame, averaged across 30 frames.  
  
### Crash Reporting

**Property** | **Description**  
---|---  
**On .Net UnhandledException** | Select the action Unity takes when a .NET unhandled exception occurs.  
| **Crash** | Generates a crash report if the application crashes, which users can submit to iTunes and developers can use to troubleshoot the crash.  
| **Silent Exit** | The application exits with no errors and doesn’t generate a crash report.  
**Log Obj-C Uncaught Exceptions** | Print Objective-C Uncaught Exception information to the console.  
**Enable Crash Report API** | Enable a custom crash reporter to capture crashes. You can use **scripts** to access crash logs via the CrashReport API.  
  
## Other settings

You can configure a range of **Player settings** in the **Other Settings** section. These options are organized into the following groups:

  * Rendering
  * Identification
  * Configuration
  * Shader Settings
  * Shader Variant Loading
  * Script Compilation
  * Optimization
  * Stack Trace
  * Legacy

### Rendering

Use these settings to customize how Unity renders your application for the iOS platform.

**Property** | **Description**  
---|---  
**Color Space** | Choose which color space to use for rendering. For more information, refer to Linear rendering overview.  
**Gamma** | Gamma color space is typically used for calculating lighting on older hardware restricted to 8 bits per channel for the framebuffer format. Even though monitors today are digital, they might still take a gamma-encoded signal as input.  
**Linear** | Linear color space rendering gives more precise results. When you select to work in linear color space, the Editor defaults to using sRGB sampling. If your Textures are in linear color space, you need to work in linear color space and deactivate sRGB sampling for each Texture.  
**MSAA Fallback** | Select the multi sample antialiasing fallback strategy to upgrade or downgrade the sample count if the sample count requested by the user isn’t supported by the device.  
**Upgrade** | The sample count reduces to the nearest supported lower sample count.  
**Downgrade** | The sample count increases to the next higher sample count. If that sample count is not supported, then it reduces to the nearest supported lower sample count.  
**Color Gamut** | You can add or remove color gamuts to use for rendering. Click the plus (+) icon to see a list of available gamuts. A color gamut defines a possible range of colors available for a given device (such as a monitor or screen). The sRGB gamut is the default (and required) gamut.  
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
**Texture compression format** |  Choose between ASTC and PVRTC as the default texture compression format for iOS. Check the texture compression format overview for more information.   
**Normal Map Encoding** | Choose **XYZ** or **DXT5nm-style** to set the normal map encoding. This setting affects the encoding scheme and compression format used for normal maps. **DXT5nm-style** normal maps are of higher quality, but more expensive to decode in shaders.  
**Lightmap Encoding** | Defines the encoding scheme and compression format of the lightmaps.   
You can choose from **Low Quality** , **Normal Quality** , or **High Quality**  
**HDR Cubemap Encoding** | Defines the encoding scheme and compression format of the HDR Cubemaps.   
You can choose from **Low Quality** , **Normal Quality** , or **High Quality**. For more information, refer to Lightmaps: Technical information.  
**Lightmap Streaming** | Enable this option to use Mipmap Streaming for lightmaps. Unity applies this setting to all lightmaps when it generates them.  
  
**Note:** To use this setting, you must enable the Texture Streaming Quality setting.  
**Streaming Priority** | Set the priority for all lightmaps in the Mipmap Streaming system. Unity applies this setting to all lightmaps when it generates them.  
Positive numbers give higher priority. Valid values range from `-128` to `127`.  
**Frame Timing Stats** |  Enable this option to gather CPU/GPU frame timing statistics.  
**Virtual Texturing (Experimental)** | Enable this option to reduce GPU memory usage and texture loading times if your Scene has many high resolution textures. For more information, refer to Virtual Texturing.   
  
**Note** : The Unity Editor requires a restart for this setting to take effect.   
**360 Stereo Capture** | Indicates whether Unity can capture stereoscopic 360 images and videos.  
**Load/Store Action Debug Mode** | Highlights undefined pixels that might cause rendering problems on mobile platforms. This affects the Unity Editor Game view, and your built application if you select **Development Build** in Build Settings. Refer to LoadStoreActionDebugModeSettings for more information.  
**Editor Only** | Indicates whether the Load/Store Action Debug Mode only runs in the Unity Editor.  
  
**Note** : This option is visible only when **Load/Store Action Debug Mode** is active.  
  
### Identification

Enter identifying information for your app.

Identification settings for iOS platforms **Property** | **Description**  
---|---  
**Override Default Bundle Identifier** | Indicates whether you can manually set the bundle identifier.  
**Note:** This setting affects macOS, iOS, tvOS, and Android.  
**Bundle Identifier** | Enter the provisioning profile of the application you are building. The basic structure of the identifier is **com.CompanyName.ProductName**. This structure might vary based on which country you live in, so always default to the string Apple provides to you for your Developer Account. Your **ProductName** is set up in your provisioning certificates.  
The Bundle Identifier must follow the convention `com.YourCompanyName.YourProductName` and must contain only alphanumeric and hyphen characters. For more information, refer to CFBundleIdentifier.  
**Important** : Unity automatically replaces any invalid characters you type with a hyphen.  
  
To set this property, enable **Override Default Bundle Identifier**.  
**Version** | Enter the release-version-number string for the bundle (for example, 4.3.6).  
  
This value appears as `CFBundleShortVersionString` in the associated _info.plist_ file. For more information, refer to Apple developer documentation on CFBundleShortVersionString.  
**Build** | Enter the build number for this version of your app.  
  
This value appears as `CFBundleVersion` in the associated **info.plist** file. For more information, refer to Apple developer documentation on CFBundleVersion.  
**Signing Team ID** | Enter your Apple Developer Team ID. You can find this on the Apple Developer website under Xcode Help. This sets the Team ID for the generated Xcode project, allowing you to use **Build and Run** functionality. You must enter an Apple Developer Team ID for automatic signing of your app.  
  
For more information, refer to the Apple developer documentation on Creating Your Team Provisioning Profile.  
**Automatically Sign** | Enable this option to instruct Xcode to automatically sign your build.  
  
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
**C++ Compiler Configuration** | Choose the C++ compiler configuration used when compiling IL2CPP generated code.  
**Debug** | Debug configuration turns off all optimizations, which makes the code quicker to build but slower to run.  
**Release** | Release configuration enables optimizations, so the compiled code runs faster and the binary size is smaller but it takes longer to compile.  
**Master** | Master configuration enables all possible optimizations, squeezing every bit of performance possible. For instance, on platforms that use the MSVC++ compiler, this option enables link-time code generation. Compiling code using this configuration can take significantly longer than it does using the Release configuration. Unity recommends building the shipping version of your game using the Master configuration if the increase in build time is acceptable.  
**Use incremental GC** | Uses the incremental garbage collector, which spreads garbage collection over several frames to reduce garbage collection-related spikes in frame duration. For more information, refer to Automatic Memory Management.  
**Allow downloads over HTTP** | Indicates whether to allow downloading content over HTTP. The default option is **Not allowed** due to the recommended protocol being HTTPS, which is more secure.  
**Not Allowed** | Never allow downloads over HTTP.  
**Allowed in Development Builds** | Only allow downloads over HTTP in development builds.  
**Always Allowed** | Allow downloads over HTTP in development and release builds.  
**Camera Usage Description** | Enter the reason for accessing the camera on the device.  
**Microphone Usage Description** | Enter the reason for accessing the microphone on the device.  
**Location Usage Description** | Enter the reason for accessing the location of the device.  
**Use On-Demand Resources** | Use on-demand resources and enable **Variant map for app slicing**.  
**Accelerometer Frequency** | Choose how often to sample the accelerometer. Use a lower frequency for better performance. If your app doesn’t use the accelerometer, select **Disabled**.  
**Mute Other Audio Sources** | Indicates whether your Unity application should stop audio from applications running in the background. Otherwise, Audio from background applications continues to play alongside your Unity application.  
**Prepare iOS for Recording** | Initializes the microphone recording APIs. This lowers recording latency, but it also re-routes iPhone audio output via earphones.  
**Force iOS Speakers when Recording** | Send the phone’s audio output through the internal speakers, even when headphones are plugged in and recording.  
**Requires Persistent WiFi** | Enable this option to require a Wi-Fi connection. This maintains the active Wi-Fi connection while the app is running.  
**Supported URL schemes** | A list of supported URL schemes.  
  
To add new schemes, increase the value of the **Size** property, then set a reference to the URL to open in the new **Element** box that appears.  
**Target Device** | Select which devices the app targets.  
**Target SDK** | Select which SDK the app targets.  
  
**Note:** Be sure to select the correct SDK. For example, if you select the Device SDK in Unity and target the Simulator in Xcode, your build will fail.  
**Target minimum iOS Version** | Select the minimum version of iOS that the app works on.  
**Enable ProMotion Support** | Use high frequency refresh rates (120 Hz) on ProMotion displays. This might cause your app to use more battery power.  
**Requires ARKit support** | Restrict the app to iPhone 6s/iOS 11 and later devices when you publish it to the App Store.  
**Automatically add capabilities** | Generate an `entitlements.plist` file and add capabilities for Game Center if detected in your project. Disable this setting if you intend to sign your app with an enterprise certificate or use a wildcard bundle identifier.  
**Defer system gestures on edges** | Select one or more edges that users must swipe twice to enact system gestures.  
**Hide home button on iPhone X** | Hide the home button on iPhone X devices when the app is running.  
**Render Extra Frame on Pause** | Issue an additional frame after the frame when the app pauses. This lets your app display graphics that display the paused state when the app goes into the background.  
**Enable Custom Background Behaviors** | Choose what the app can do when the user sends the app to the background. For an example, refer to the BackgroundFetch GitHub project.  
**Variant map for app slicing** | Expand the Variant map for app slicing section to find the list of variant names configured in scripting. For more information on variants, refer to App slicing.  
  
**Note** : Enable **Use on-demand resources** to view this property.  
**Architecture** | Choose which architecture to target. Only **ARM64** is available for iOS.  
**Simulator Architecture** | Choose the architecture to build for the Simulator. This property is visible only when you set the **Target SDK** to **Simulator SDK**.   
**ARM64** | Supports 64-bit ARM architecture.  
**X86_64** | Supports 64-bit Intel/AMD architecture.  
**Universal** | Supports all architectures including 64-bit ARM and Intel/AMD.  
**Active Input Handling** | Choose how to handle input from users.  
**Input Manager (Old)** | Uses the traditional Input settings.  
**Input System Package (New)** | Uses the Input system. This option requires you to install the InputSystem package.  
**Both** | Use both systems.  
  
#### API Compatibility Level

You can choose your mono API compatibility level for all targets. Sometimes a third-party .NET library uses functionality that is outside of your .NET compatibility level. If you’re on Windows, you can use the third-party software ILSpy to understand what’s happening and how to fix it. Follow these steps:

  1. Install ILSpy for Windows.
  2. Drag the .NET assemblies for the API compatibility level that you are having issues with into ILSpy. You can find these under _Frameworks/Mono/lib/mono/YOURSUBSET/_.
  3. Drag in your third-party assembly.
  4. Right-click your third-party assembly and select **Analyze**.
  5. In the analysis report, inspect the **Depends on** section. Anything that the third-party assembly depends on, but that’s not available in the .NET compatibility level of your choice, is highlighted in red.

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
  
#### Script Compilation

Script compilation settings for the iOS platform **Property** | **Description**  
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

Optimization settings for iOS platforms **Property** | **Description**  
---|---  
**Prebake Collision Meshes** | Adds collision data to Meshes at build time.  
**Preloaded Assets** | Sets an array of Assets for the player to load on startup.   
To add new Assets, increase the value of the **Size** property and then set a reference to the Asset to load in the new **Element** box that appears.  
**AOT Compilation Options** | Additional options for ahead-of-time (AOT) compilation. This helps optimize the size of the built iOS player.  
**Strip Engine Code** | Enable this option if you want the Unity Linker tool to remove code for Unity Engine features that your Project doesn’t use. This setting is only available with the IL2CPP scripting backend. Most apps do not use every available DLL. This option strips out DLLs that your app doesn’t use to reduce the size of the built Player. If your app is using one or more classes that would normally be stripped out under your current settings, Unity displays a debug message when you try to build the app.  
**Managed Stripping Level** | Chooses how aggressively Unity strips unused managed (C#) code. The options are **Minimal** , **Low** , **Medium** , and **High**.   
When Unity builds your app, the Unity Linker process can strip unused code from the managed DLLs your Project uses. Stripping code can make the resulting executable significantly smaller, but can sometimes accidentally remove code that’s in use.   
  
For more information about these options and bytecode stripping with IL2CPP, refer to ManagedStrippingLevel.  
**Script Call Optimization** | Choose how to disable exception handling for a speed boost at runtime. For more information, refer to iOS Optimization.  
**Vertex Compression** | Sets vertex compression per channel. This affects all the meshes in your project.   
Typically, Vertex Compression is used to reduce the size of mesh data in memory, reduce file size, and improve GPU performance.   
  
For more information on how to configure vertex compression and limitations of this setting, refer to Compressing mesh data.  
**Optimize Mesh Data** | Enable this option to strip unused vertex attributes from the mesh used in a build. This option reduces the amount of data in the mesh, which can help reduce build size, loading times, and runtime memory usage.   
  
**Warning:** If you have this setting enabled, don’t change material or shader settings at runtime.   
  
For more information, refer to PlayerSettings.stripUnusedMeshComponents.  
**Texture MipMap Stripping** | Enables mipmap stripping for all platforms. It strips unused mipmaps from Textures at build time.   
Unity determines unused mipmaps by comparing the value of the mipmap against the quality settings for the current platform. If a mipmap value is excluded from every quality setting for the current platform, then Unity strips those mipmaps from the build at build time. If `QualitySettings.masterTextureLimit` is set to a mipmap value that has been stripped, Unity will set the value to the closest mipmap value that hasn’t been stripped.  
  
### Stack Trace

Select what type of logging to allow in specific contexts.

Logging settings for iOS platforms

Select your preferred stack trace method by enabling the option that corresponds to each Log Type (**Error** , **Assert** , **Warning** , **Log** , and **Exception**) based on the type of logging you require. For more information, refer to stack trace logging. 

**Property** | **Description**  
---|---  
**None** | No logs are ever recorded.  
**ScriptOnly** | Logs only when running scripts.  
**Full** | Logs all the time.  
  
### Legacy

**Property** | **Description**  
---|---  
**Clamp BlendShapes (Deprecated)** | Enable this option to clamp the range of blend shape weights in SkinnedMeshRenderers.  
  
PlayerSettingsiOS