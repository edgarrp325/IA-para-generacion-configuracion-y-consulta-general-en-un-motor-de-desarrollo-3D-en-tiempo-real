---
title: "Unity Editor command line arguments"
category: "General"
source_file: "EditorCommandLineArguments.html"
doc_type: "manual"
---

# Unity Editor command line arguments

You can launch the Unity Editor from the command line and pass in arguments to change how the Editor launches. You can also use the command line to execute specific methods from your project’s C# **scripts** at launch (see Example script for executing methods at launch).

**Note** : To use the information on this page, you need to know how to use your operating system’s command-line interface to launch applications and run command-line arguments.

When launching the Unity Editor, the delimiter for a command-line argument value is a single space. For example, to set the window mode to borderless, use `-window-mode borderless`.

## Launching Unity

On macOS, type the following into the Terminal to launch Unity:

`/Applications/Unity/Hub/Editor/<version>/Unity.app/Contents/MacOS/Unity -projectPath <project path>`

On Linux, type the following into the Terminal to launch Unity:

`/Applications/Unity/Hub/Editor/<version>/Unity.app/Contents/Linux/Unity -projectPath <project path>`

On Windows, type the following into the Command Prompt to launch Unity:

`"C:\Program Files\Unity\Hub\Editor\<version>\Editor\Unity.exe" -projectPath "<project path>"`

When you launch Unity like this, it receives commands and information on startup, which can be useful for test suites, automated builds and other production tasks.

**Notes** :

  * The above instructions assume the relevant Unity Editor is installed in the default location through the Unity Hub. Adjust the path in the command if you use Unity Editor installed in a different location. For more information about how to find your Editor’s location path, refer to Install and uninstall Editor versions.

  * When passing arguments on the Windows platform, make sure the directory path doesn’t end with a single backslash to prevent syntax errors. Use either double backslashes (`\\`) or no backslash. For example,

    * `"C:\Program Files\Unity\Hub\Editor\<version>\Editor\Unity.exe" -projectPath "C:\MyUnityProjects\MyProject"`
    * `"C:\Program Files\Unity\Hub\Editor\<version>\Editor\Unity.exe" -createProject "C:\MyUnityProjects\MyProject\\"`

## Configuration arguments

You can run the Unity Editor and build Unity applications with additional commands and information on startup. This page lists the command line arguments you can use to launch and configure Unity Editor and Unity Player instances.

**Command** | **Details:**  
---|---  
`-createProject <pathname>` | Create an empty project at the given path.  
`-disable-assembly-updater <assembly1 assembly2>` | Specify a space-separated list of assembly names as parameters for Unity to ignore on automatic updates.  
  
The space-separated list of assembly names is optional: pass the command line options without any assembly names to ignore all assemblies, as in example 1.  
  
**Example 1**  
`unity.exe -disable-assembly-updater`  
  
**Example 2**  
`unity.exe -disable-assembly-updater A1.dll subfolder/A2.dll`  
  
Example 2 has two assembly names, one with a pathname. Example 2 ignores `A1.dll`, no matter what folder it is stored in, and ignores `A2.dll` only if it is stored under `subfolder` folder:  
  
If you list an assembly in the `-disable-assembly-updater` command line parameter (or if you don’t specify assemblies), Unity logs the following message to Editor.log:  
  
`[Assembly Updater] warning: Ignoring assembly [assembly_path] as requested by command line parameter.”).`  
  
Use this to avoid unnecessary API Updater overhead when you import assemblies.  
  
This argument is useful if you want to import assemblies that access a Unity API which doesn’t need updating. It’s also useful when you import assemblies which don’t access any Unity APIs (for example, if you have built some or all of your source code outside of Unity, and you want to import the resulting assemblies into your Unity project).  
  
**Note** : If you disable the update of any assembly that needs updating, you might get errors at compile time, run time, or both, that are hard to track.  
`-disable-gpu-skinning` | Disable Graphics Processing Unit (GPU) **skinning** at startup.  
`-executeMethod <ClassName.MethodName>` or `-executeMethod <NamespaceName.ClassName.MethodName>` | Execute the static method as soon as Unity opens the project, and after the optional Asset server update is complete. You can use this for tasks such as continuous integration, performing Unit Tests, making builds or preparing data.  
  
To return an error from the command line process, either throw an exception which causes Unity to exit with return code 1, or call EditorApplication.Exit with a non-zero return code.  
  
To pass parameters, add them to the command line and retrieve them inside the function using `System.Environment.GetCommandLineArgs`. To use `-executeMethod`, you need to place the enclosing script in an Editor folder. The method you execute must be defined as static.  
`-exportPackage <exportAssetPath1 exportAssetPath2 ExportAssetPath3 exportFileName>` | Export a package, given a path (or set of given paths). In this example, `exportAssetPath` is a folder (relative to the Unity project root) to export from the Unity project, and `exportFileName` is the package name. This option only exports whole folders at a time. You normally need to use this command with the `-projectPath` argument.  
`-importPackage <pathname>` | Import the given asset package. Unity doesn’t display any import dialog.  
`-job-worker-count <N>` | Specify the maximum thread count for the Unity JobQueue Job Worker Count.  
`-gc-helper-count <N>` | Specify the number of asset garbage collector helper threads. The default value is the number of cores available.  
`-logFile <pathname>` | Specify where Unity writes the Editor or Windows/Linux/macOS standalone log file. To output to the console, specify - for the path name. On Windows, use `-logfile - <pathname>` to direct the output to `stdout`, which by default is not the console.  
`-noUpm` | Disables the Unity Package Manager.  
`-openfile <path>` | Open the project from a path to a scene or package file. Alternatively, you can use the `-projectPath` argument  
`-password <password>` | Enter a password into the log-in form during the activation of the Unity Editor.  
`-projectPath <pathname>` | Open the project at the given path. If the pathname contains spaces, enclose it in quotes.  
`-quit` | Quit the Unity Editor after other commands have finished executing. This can cause error messages to be hidden (but they still appear in the `Editor.log` file).  
`-releaseCodeOptimization` | Enables release code optimization mode, overriding the current default code optimization mode for the session.  
`-setDefaultPlatformTextureFormat` (Android only) | Set the default texture ****compression**** to the desired format before you import a texture or build the project. This is so you don’t have to import the texture again with the format you want. The available formats are dxt, pvrtc, atc, etc, etc2, and astc.  
`-silent-crashes` | Prevent Unity from displaying the dialog that appears when a Standalone Player crashes. This argument is useful when you want to run the Player in automated builds or tests, where you don’t want a dialog prompt to obstruct automation.  
`-username <username>` | Enter a username into the log-in form during the activation of the Unity Editor.  
`-vcsMode <mode>` | Set the version control mode. Available modes are `"Visible Meta Files"`, `"Hidden Meta Files"`, `Perforce`, and `PlasticSCM`. You can use additional flags to fill out the configuration fields for the given version control mode. These flags are based on the Provider.GetActiveConfigFields method. For example, you can use the `-vcPerforceUsername`, `-vcPerforcePassword`, `-vcPerforceWorkspace` and `-vcPerforceServer` to set the Perforce username, workspace and server fields.  
  
**Note** : `<mode>` arguments that contain spaces must be wrapped in double quotes (“).| |`-vcsModeSession <mode>`|Set the version control mode for this session. Available modes are `"Visible Meta Files"`, `"Hidden Meta Files"`, `Perforce`, and `PlasticSCM`. You can use additional flags to fill out the configuration fields for the given version control mode. These flags are based on the Provider.GetActiveConfigFields method. For example, you can use the `-vcPerforceUsername`, `-vcPerforcePassword`, `-vcPerforceWorkspace` and `-vcPerforceServer` to set the Perforce username, workspace and server fields.  
  
**Note** : `<mode>` arguments that contain spaces must be wrapped in double quotes (”).  
`-version` | Print the version number of the Unity Editor in the command line, without launching the Editor.  
`-timestamps` | Prefixes every Editor.log message with the current timestamp and thread ID.  
  
## Batch mode arguments

Use the following arguments to configure Unity’s batch mode. Batch mode enables Unity to run predefined tasks without additional input, which makes batch mode useful for automated tasks like testing. For more information, see Batch mode and built-in coroutine compatibility.

**Command** | **Details:**  
---|---  
`-accept-apiupdate` | Use this command line option to specify that APIUpdater should run when Unity is launched in batch mode.  
  
Example:  
  
`unity.exe -accept-apiupdate -batchmode [other params]`  
  
The APIUpdater doesn’t run if you omit this command line argument when you launch Unity in batch mode. This might lead to compiler errors.  
`-batchmode` | Run Unity in batch mode. In batch mode, Unity runs command line arguments without the need for human interaction. It also suppresses pop-up windows that require human interaction (such as the Save Scene window). You should always run Unity in batch mode when using command line arguments, because it allows automation to run without interruption.  
  
When an exception occurs during execution of the script code, the Asset server updates fail, or other operations fail, Unity immediately exits with return code **1**.  
  
In batch mode, Unity sends a minimal version of its log output to the console. However, the Log Files still contain the full log information. You can’t open a project in batch mode while the Editor has the same project open; only a single instance of Unity can run at a time.  
  
To check whether the Editor or Standalone Player is running in batch mode, use the Application.isBatchMode operator.  
  
If the project has not yet been imported when using `-batchmode`, the target platform is the default one. To force a different platform, use the `-buildTarget` option.  
`‑ignorecompilererrors` | When you use this argument, Unity continues to start your application even if there are compilation errors.  
`-nographics` | When you run this in batch mode, Unity doesn’t initialize the graphics device. You can then run automated workflows on machines that don’t have a GPU. Automated workflows only work when you have a window in focus, otherwise you can’t send simulated input commands. `-nographics` does not allow you to bake GI, because Enlighten requires a GPU for Meta Pass rendering. See the Meta Pass section of the Lightmapping and Shaders page for more information.   
**Note** : Output logs are turned off in this mode. To enable the creation of output logs, specify a file location using the command `-logFile`.  
  
## Build Arguments

Use the following arguments to build players for various platforms from the command line. For more information about building players with command line arguments, see Unity Standalone Player command line arguments.

**Command** | **Details:**  
---|---  
`-buildLinux64Player <pathname>` | Build a 64-bit standalone Linux player (for example, `-buildLinux64Player path/to/your/build`).  
`-buildOSXUniversalPlayer <pathname>` | Build a 64-bit standalone Mac OSX player (for example, `-buildOSXUniversalPlayer path/to/your/build.app`).  
`-buildTarget <name>` | Select an active build target to launch the Editor in. The options available to you depend on which build targets you have enabled in the Editor. These options correspond to the options available to you via the API enumeration `BuildTarget`. Possible options include:  
  
• `win64`  
• `win`  
• `osxuniversal`  
• `linux64`  
• `android`  
• `ios`  
• `webgl`  
• `tvos`  
• `windowsstoreapps`  
• `cloudrendering`  
• `embeddedlinux`  
• `qnx`  
• `visionos`  
• `stadia`  
  
If you are a developer with access to Closed platforms, you might have other `-buildTarget` options available. For details, see the documentation for your target platform.  
`-standaloneBuildSubtarget <name>` | Select an active build sub-target for the Standalone platforms before loading a project. Possible options are:   
  
• Player  
• Server  
`-buildWindowsPlayer <pathname>` | Build a 32-bit standalone Windows player (for example, -buildWindowsPlayer path/to/your/build.exe).  
`-buildWindows64Player <pathname>` | Build a 64-bit standalone Windows player (for example, -buildWindows64Player path/to/your/build.exe).  
  
## Cache server arguments

Use the following arguments to configure Unity’s use of the cache server. For more information, see Cache Server.

**Command** | **Details:**  
---|---  
`-EnableCacheServer` | Tells Unity to use the newer Accelerator Cache Server. You must also use `-cacheServerEndpoint` to specify the address.  
`-cacheServerEndpoint` | Specifies the endpoint address if you are using the newer **Accelerator** Cache Server.  
  
Example: `-cacheServerEndpoint 127.0.0.1:10080`. This overrides any configuration stored in the Editor Preferences. Use this to connect multiple instances of Unity to different Cache Servers.  
`-cacheServerNamespacePrefix` | Set the namespace prefix for the newer **Accelerator** Cache Server. Used to group data together on the Cache Server.  
  
Example: `-cacheServerNamespacePrefix` MyProject  
`-cacheServerEnableDownload` | Enable downloading from the newer **Accelerator** Cache Server.  
  
Example:`-cacheServerEnableDownload true`  
`-cacheServerEnableUpload` | Enable uploading to the newer **Accelerator** Cache Server.  
  
Example:`-cacheServerEnableUpload false`  
  
## Debugging arguments

**Command** | **Details:**  
---|---  
`-disableManagedDebugger` | Disables the debugger listen socket.  
`-diag-debug-shader-compiler` | Unity launches only one instance of the ****Shader**** Compiler, and forces its timeout to be one hour. Useful for debugging Shader Compiler issues.  
`-debugCodeOptimization` | Enables debug code optimization mode, overriding the current default code optimization mode for the session.  
`-enableCodeCoverage` | Enables code coverage and allows access to the Coverage API.  
`-force-d3d12-debug` | Enables the DX12 validation layer. This is useful for working on **XR** plugins or native plugins.  
`-force-d3d12-debug-gbv` | Enables the DX12 GPU-based validation. This is useful for working on XR plugins or native plugins.  
`-force-vulkan-layers` | Enables the Vulkan validation layer. This is useful for working on XR plugins or native plugins.  
`-stackTraceLogType` | Allow detailed debugging. All settings allow **None** , **Script Only** and **Full** to be selected (for example, `-stackTraceLogType Full`).  
  
## Graphics API arguments

Use the following arguments to force the Unity Editor to use a specific graphics API.

**Command** | **Details:**  
---|---  
`-force-d3d11` (Windows only) | Make the Editor use Direct3D 11 for rendering. Normally the graphics API depends on ****Player Settings**** (typically defaults to D3D11).  
`-force-d3d12` (Windows only) | Make the Editor use Direct3D 12 for rendering. Normally the graphics API depends on **Player Settings**.  
`-force-opengl` | Make the Editor use the legacy OpenGL back end.  
`-force-glcore` | Make the Editor use OpenGL 3/4 core profile for rendering. The Editor tries to use the best OpenGL version available and all OpenGL extensions exposed by the OpenGL drivers. If the platform isn’t supported, the editor uses Direct3D.  
`-force-glcoreXY` | Similar to`-force-glcore`, but requests a specific OpenGL context version. Accepted values for XY: 32, 33, 40, 41, 42, 43, 44, or 45. If the platform doesn’t support a specific version of OpenGL, Unity will fallback to a supported version.  
`-force-gles` (Windows only) | Make the Editor use OpenGL for Embedded Systems for rendering. The Editor tries to use the best OpenGL ES version available, and all OpenGL ES extensions exposed by the OpenGL drivers.  
`-force-glesXY` (Windows only) | Similar to `-force-gles`, but requests a specific OpenGL ES context version. Accepted values for XY: 30, 31, 31aep, or 32. If the platform doesn’t support a specific version of OpenGL ES, Unity will fallback to a supported version. If the platform doesn’t support OpenGL ES, Unity will fallback to another graphics API.  
`-force-vulkan` | Make the Editor use Vulkan for rendering. Normally the graphics API depends on **Player Settings**.  
`-force-clamped` | Use this with `-force-glcoreXY` to prevent Unity from checking for additional OpenGL extensions, allowing it to run between platforms with the same code paths. This approach helps to determine if an issue is platform-specific. For example, a driver bug.  
  
## License arguments

Use the following arguments to process a Unity license or run the Unity Editor with different license options.

**Command** | **Details:**  
---|---  
`-createManualActivationFile` | Step one of a three-step process to manually activate a Unity license. For more information, see Generate a license activation file (.alf) from the command line.  
`-manualLicenseFile <yourulffile>` | Step three of a three-step process to manually activate a Unity license. For more information, see Generate a license activation file (.alf) from the command line.  
`-returnlicense` | Return the currently active serial-based license. Do not use `-returnlicense` to return a floating license. For more information, see Returning your license.  
`-serial <serial>` | Activate your Unity license with the specified serial key. For more information, see Activate a license from the command line.  
  
**Note** : When you use this argument, you must also use the `-batchmode` argument. It’s also good practice to specify the `-quit` argument.  
  
## Metal arguments (macOS only)

Use the following arguments to configure Unity’s use of the Metal graphics API for Apple devices.

**Command** | **Details:**  
---|---  
`-force-device-index` | When using Metal, make the Editor use a particular GPU device by passing it the index of that GPU (macOS only).  
`-force-low-power-device` (macOS only) | If you use Metal, make the Editor use a low power device.  
`-force-metal` | Make the Editor use Metal as the default graphics API (macOS only).  
  
## Profiler arguments

Use the following arguments to configure Unity’s use of the Profiler.

**Command** | **Details:**  
---|---  
`-deepprofiling` | Enable Deep Profiling option for the CPU profiler.  
`-profiler-enable` | Profile the start-up of a Player or the Editor. When you use this argument with a Player, it has the same effect as building the Player with the **Autoconnect Profiler** option enabled in Build Settings.  
  
When you use this argument with the Editor, it starts collecting and displaying Profiler information in the Profiler window on start-up of the Editor.  
`-profiler-log-file <Path/To/Log/File.raw>` | This argument sets up the Unity Profiler to stream the profile data to a .raw file on startup. It works for both Players and the Editor.  
`-profiler-capture-frame-count <NumberOfFrames>` | This argument sets how many frames the Profiler should capture in a profile when streaming to a .raw file on start-up. It only works on Players.  
`-profiler-maxusedmemory` | By default, `maxUsedMemory` for the Unity Profiler is 16MB for Players and 256MB for the Editor. You can use this argument to set the `maxUsedMemory` parameter to a custom size at start-up (for example, `-profiler-maxusedmemory 16777216`). The size is set in bytes.  
  
## Unity Editor special command line arguments

You should only use these under special circumstances, or when directed by Unity Support.

**Command** | **Details:**  
---|---  
`-enableIncompatibleAssetDowngrade` | Use this when you have Assets made by a newer, incompatible version of Unity, that you want to downgrade to work with your current version of Unity. When you enable this, Unity presents you with a dialog asking for confirmation of this downgrade if you attempt to open a project that would require it.  
  
Note: This procedure is unsupported and highly risky, and should only be used as a last resort.  
`-giCustomCacheLocation` | Use this to set a custom location for the Global Illumination (GI) cache folder.  
  
**Note:** When you close the Editor, `giCustomCacheLocation` reverts to the default location for the GI cache, or a custom location you set before.  
  
## Extra Editor arguments from packages

Additional Editor command line arguments are available when these packages are installed.

**Package** | **Details:**  
---|---  
Burst | See Burst package documentation.  
Test Framework | See Unity Test Framework package documentation.  
Code Coverage | See Code Coverage package documentation.  
  
## Example script for executing methods at launch

You can use the command line to execute specific methods from your project’s C# scripts at launch. The following examples demonstrate a C# script, and the command line arguments that execute methods from that script at launch.

An example C# script in the project:
    
    
    using UnityEditor;
    class MyEditorScript
    {
         static void PerformBuild ()
         {
            BuildPlayerOptions buildPlayerOptions = new BuildPlayerOptions();
            buildPlayerOptions.scenes = new[] { "Assets/Scene1.unity", "Assets/Scene2.unity" };
            BuildPipeline.BuildPlayer(buildPlayerOptions);
         }
    }
    

The following command executes Unity in batch mode, executes the `MyEditorScript.PerformBuild` method from the above script, and then quits upon completion.

**Windows:**
    
    
    "C:\Program Files\Unity\Hub\Editor\<version>\Editor\Unity.exe" -quit -batchmode -projectPath "C:\Users\UserName\Documents\MyProject" -executeMethod
    MyEditorScript.PerformBuild
    

**macOS:**
    
    
    /Applications/Unity/Hub/Editor/<version>/Unity.app/Contents/MacOS/Unity -quit -batchmode -projectPath ~/UnityProjects/MyProject -executeMethod
    MyEditorScript.PerformBuild
    

**Note:** In the Editor path, replace `<version>` with the version of Unity you want to launch, or replace the path entirely if your Unity Editor path is not the default.