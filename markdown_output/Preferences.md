---
title: "Preferences"
category: "General"
source_file: "Preferences.html"
doc_type: "manual"
---

# Preferences

Use preferences to customize the behavior of the Unity Editor.

To open the **Preferences** window, go to **Edit > Preferences** (macOS: **Unity > Settings**) in the main menu. 

To navigate the **Preferences** window, use the search box to filter the list of settings categories and highlight keywords in the details pane on the right of the **Preferences** window.

The following preference categories are available:

  * General
  * 2D
  * Analysis
  * Asset Pipeline
  * Colors
  * Editor Diagnostics
  * External Tools
  * Jobs
  * GI Cache
  * Package Manager
  * Scene view
  * Search
  * Custom package preferences

## General

**General** preferences let you customize the overall behavior for working in Unity.

**Property** | **Function**  
---|---  
**Load Previous Project on Startup** | Always load the previous project at startup.  
**Disable Editor Analytics** (Pro only) | Stop the Editor automatically sending information back to Unity.  
**Script Changes While Playing** | Choose Unity’s behavior when **scripts** change while your game is running in the Editor.  
| _Recompile And Continue Playing_ | Recompile your scripts and keep running the Scene. This is the default behavior, but you might want to change it if your scripts rely on any non-serializable data.  
| _Recompile After Finished Playing_ | Defer recompilation until you manually stop your Scene, avoiding any interruption.  
| _Stop Playing And Recompile_ | Immediately stops your Scene for recompilation, allowing you to quickly restart testing.  
**Code Optimization On Startup** | Choose whether to set code optimization mode to **Debug** or **Release** when the Unity Editor starts. **Debug** mode allows you to attach external debugger software, but gives slower C# performance when you run your Project in Play mode in the Editor. **Release** mode gives faster C# performance when you run your Project in Play mode in the Editor, but you can’t attach any external debuggers. For more information, see Code Optimization Mode.  
**Editor Theme** | Choose the background to use in the Unity Editor.  
| _Light_ | Applies the light grey background with black text.  
| _Dark_ | Applies the dark theme with white text.  
**Editor Font** | Select which font to display in the Unity Editor. The default font is Inter.  
**Enable Alpha Numeric Sorting** | Display a button in the top-right corner of the Hierarchy window, which toggles between Transform sort (the default) and Alphanumeric sort.  
**Interaction Mode** | Specifies how long the Editor can idle before it updates. After one frame finishes, the Editor waits up to the specified amount of time before the next frame begins.  
  
This allows you to throttle Editor performance, and reduce consumption of CPU resources and power.  
  
For example, if you want to test the Editor’s performance, set this property to **No Throttling**. If you want to conserve power (for example, to prolong battery life on a laptop computer), set this property to one of the throttled modes.  
  
In throttled modes, the Editor stops idling if you interact with it (for example, by panning in the Scene view).  
  
**Note:** In Play mode, Unity ignores any throttling that you apply using this preference. The editor updates as fast as possible unless you enable the VSync option in the Game view, or set `Application.targetFrameRate` to a value other than –1.  
| _Default_ | The Editor idles up to 4 ms each tick. If a frame takes 5 ms or more, the Editor doesn’t idle at all, and the next frame starts automatically.  
| _No Throttling_ | Each time a frame finishes, the next frame begins immediately. The Editor never waits, and updates as fast as possible.  
  
This mode consumes a lot of CPU resources. If you are using a laptop computer, it can cause the battery to drain quickly.  
| _Monitor Refresh Rate_ | The Editor idles up to the monitor’s update rate in milliseconds. For most monitors, this is 16 ms.  
| _Custom_ | You specify the maximum amount of time application can be idle.  
  
When you select this option the **Frame Throttling (milliseconds)** property appears.  
**Frame Throttling (milliseconds)** | When **Interaction Mode** is set to **Custom** , this property specifies how long the Editor can idle between frames. The value can be between 0 and 33 ms. 0 is equivalent to setting **Interaction Mode** to **No Throttling**.  
**Package Manager Log Level** | Choose the **level of detail** you want the Package Manager logs to report. The options are:  
| _Error_ | Unexpected errors and failures only.  
| _Warn_ | Unusual situations that can cause issues.  
| _Info_ | High-level informational-only messages.  
| _Verbose_ | Detailed informational messages.  
| _Debug_ | High-level debugging messages.  
| _Silly_ | Detailed debugging messages.  
**Enable extended Dynamic hints** | Enable extended dynamic hints, which displays more information when a property, object, or tool is hovered for enough time, or when a dynamic hint appears.  
**Perform**Bump Map** Check** | Enable bump map checks upon material imports, which helps check that textures used in a **normal map** material slot are actually defined as normal maps.  
  
## 2D

The **2D** preference settings allow you to define the settings of 2D-related features and packages. When you install 2D related packages (such as the Tilemap Editor package) into your Project, their preference settings will appear in this section.

### Physics

Use the **Physics** preferences to configure the 2D physics settings, such as the colors used in the **UI**.

**Property** | **Function** |   
---|---|---  
****Colliders**** | The colors for the following UI elements.  
| **Awake Color (Outline)** | The color of the Collider 2D **Gizmo** ’s outline when the **Rigidbody** ’s outline when the **Rigidbody** 2D it’s attached to is **Awake**.  
| **Awake Color (Filled)** | The color of the Collider 2D Gizmo’s interior fill when the Rigidbody 2D it’s attached to is **Awake**.  
| **Asleep Color (Outline)** | The color of the Collider 2D Gizmo’s outline when the Rigidbody 2D it’s attached to is **Asleep**.  
| **Asleep Color (Filled)** | The color of the Collider 2D Gizmo’s interior fill when the Rigidbody 2D it’s attached to is **Asleep**.  
| **Bounds Color** | The color of the bounds for all PhysicsShape2D that a Collider 2D creates.  
**Contacts** | The colors used for the following UI elements.  
| **Contact Color** | The color of the Collider 2D Gizmo’s contacts which are displayed as a directional arrow starting at the contact point in the direction of the contact normal.  
| **Contact Arrow Scale** | The scale of the Collider 2D contacts arrow. Larger values draw the arrow larger.  
  
## Analysis

The **Analysis** preferences let you define settings for the Profiler.

**Property** | **Function**  
---|---  
**Frame count** | The maximum number of frames for the Profiler to capture. You can set this number between 300 and 2,000.  
**Show stats for ‘current frame’** | By default, when you select the **Current Frame** button and enter Current Frame mode, the frame indicator line doesn’t have annotations with the stats for the current frame. This is because the stats annotations might make it difficult to view data in real-time. To display the annotations, enable this setting.  
**Default recording state** | which recording state the Profiler should open in. Choose from **Enabled** , **Disabled** , or **Remember**. Enabled keeps the **Record** button enabled between sessions, while **Disbled** disables it, regardless of whether you turn it on or off during your profiling session. The **Remember** state remembers whether you have enabled or disabled the **Record** button during your session and keeps it at its last state next time you open the Profiler window.  
**Default editor target mode** | Which mode the **Attach to Player** dropdown should target by default. Choose from either **Playmode** or **Editor**.  
**Custom connection ID** | The connection name that you want to use for the device that’s running your application in the **Attach to Player** drop down in the Profiler Window or Console Window  
  
## Asset Pipeline

**Property** | **Function**  
---|---  
**Auto Refresh** | Import Assets automatically as they change.  
**Import Worker Count %** | Enter your **Desired Import Worker Count** for new projects in percentage of available logical CPU cores. For example, if your system has 16 logical cores and this preference is set to 25%, the **Desired Import Worker Count** for new projects is set to 4. If you set this value too high, your import worker processes need to compete over other processes and system resources such as reading and writing files. The default value of 25% is suitable for most situations.  
**Directory Monitoring (available only on Windows)** | Monitor directories instead of scanning all project files to detect asset changes.  
**Compress Textures on Import** | Disable this setting to skip texture **compression** during import. Textures are typically imported into uncompressed formats.  
**Verify Saving Assets** | Verify which Assets to save individually. A dialog is shown any time Unity saves any assets.  
**Unity Accelerator (Cache Server)**  
**Default Mode** | The default setting for the Cache Server, whether to enable or disable it by default. You can override this per Project in the Unity Editor settings. For more information, see Unity Accelerator.  
**Default IP address** | The default IP address for the Cache Server to use. You can override this per Project in the Unity Editor settings.  
**Check Connection** | Attempt to connect to the remote Cache Server.  
  
## Colors

The **Colors** preferences let you pick colors for various user interface elements in the Unity Editor.

**Property** | **Function** |   
---|---|---  
**Animation** | Customize color preferences for animated properties. |   
| **Property Animated** | The color to indicate a property that’s currently being animated.  
| **Property Candidate** | The color to indicate the animated property that you modified recently.  
| **Property Recorded** | The color to indicate that an animated property automatically records changes in the **animation clip**.  
**Cloth** | Settings for the Cloth Component’s editing interface. |   
| **Brush Color 2** | The color of the brush you use when you edit Cloth constraints and **collisions**.  
| **Selected Self or Inter Collision Particle Color** | The color of particles currently selected in Select mode.  
| **Self or Inter Collision Particle Color 2** | The color of painted particles.  
| **Unselected Self or Inter Collision Particle Color** | The color of unpainted particles.  
**General** | Customize color preferences for General settings. |   
| **Playmode Tint** | The color to tint the editor to for ease of identifying when you’re in Play mode. Unity tints the whole editor with the color you pick here when you enter Play mode. Some operations in the Editor aren’t available when in Play mode, and you can reset some edited values when exiting the Play mode.  
**Scene** | Customize preferences for a Scene. |   
| **Background** | The color for the scene **camera** to clear to when the Scene FX **skybox** to clear to when the Scene FX **skybox** setting is turned off.  
| **Background for**Prefabs**** | The color for the scene camera to clear to when the Scene FX skybox setting is turned off.  
| **Contribute GI: Off / Receive GI:**Light Probes**** | The color to display when **ContributeGI** is disabled in the **GameObject** ’s Static Editor Flags.  
| **Contribute GI: On / Receive GI: Light Probes** | The color to display when **ContributorGI** is enabled in the GameObject’s Static Editor Flags, and the Renderer’s ReceiveGI property is set to ****Lightmaps****.  
| **Contribute GI: On / Receive GI: Lightmaps** | The color to display when **ContributeGI** is enabled in the GameObject’s Static Editor Flags, and the Renderer’s ReceiveGI property is set to **Light Probes**.  
| **Grid** | The color of the grid in the Scene view.  
| **Guide Line** | The color of the Guide Line in the Scene view.  
| **Material Validator Pure Metal** | The color for the **Validate Albedo/Metal Specular debug render mode** to indicate the material properties.  
| **Material Validator Value Too High** | The color for the **Validate Albedo/Metal Specular debug render mode** to indicate when the material value is too high.  
| **Material Validator Value Too Low** | The color for the **Validate Albedo/Metal Specular debug render mode** to indicate when the material value is too low.  
| **Selected Axis** | The color for the selected handle to show highlighted in, when Move, Rotate, or the Scale tool is engaged.  
| **Selected Children Outline** | The outline color for the children of the selected objects.  
| **Selected Material Highlight** | The outline color that shows when clicking on a **mesh** in the MeshRenderer to ping the submesh in the Scene view.  
| **Selected Outline** | The outline color for the selected GameObjects.  
| **UI Collider Handle** | The color to use for the Unity UI’s padding visualization.  
| **Volume Gizmo** | The color to indicate the **audio source** in Gizmo.  
| **Wireframe** | The color of the wireframe when the wireframe render mode is active.  
| **Wireframe Overlay** | The color of the wireframe when the textured wireframe render mode is active.  
| **Wireframe Selected** | If you’ve enabled **Selection Wire** in the Gizmo options, then the selected wireframes appear in the color that you set here.  
| **X Axis** | The color that you set here is indicated for any built-in transform tool handle affecting x-axis.  
| **Y Axis** | The color that you set here is indicated for any built-in transform tool handle affecting y-axis.  
| **Z Axis** | The color that you set here is indicated for any built-in transform tool handle affecting z-axis.  
****Trail Renderer**** | Settings for the visualizations of the Trail Renderer component. |   
| **Bounds** | The color of the bounding lines of the Trail Renderer in the Scene view.  
| **Shape Gizmos** | The trail’s path color in the Scene view.  
  
## Editor Diagnostics

When you report a problem to Unity, the Unity Support Team might need you to enable diagnostic switches to help identify the cause. Running diagnostics on an application, whether in the Editor or a player, impacts performance and user experience. You should only run diagnostics when the Unity Support Team requires them.

If diagnostic switches are active in your application, Unity shows a warning in the console. To reset switches, in the **Editor Diagnostics** tab, click **Reset all**.

If an active diagnostic switch prevents the Unity Editor from opening, use the `--reset-diagnostic-switches` parameter to reset all switches from the command line. For more information on using command line arguments at launch, see Command line arguments.

## External Tools

Use the **External Tools** preferences to set up external applications for scripting, working with images, and source control.

**Property** | **Function**  
---|---  
**External Script Editor** | Choose which application Unity should use to open script files. Unity automatically passes the correct arguments to script editors it has built-in support for. Unity has built-in support for Visual Studio Community, Visual Studio Code (VSCode) and JetBrains Rider. The **Open by file extension** option uses your device’s default application for the relevant file type when you open a file. If no default application is available, your device opens a window that prompts you to choose an application to use to open the file.  
**External Script Editor Args** | Controls parameters that Unity can send to your code editor when you open a file. The `$(File)`, `$(Line)` and `$(Column)` arguments pass the filename, line number and column number to your external code editor. Your code editor uses these arguments to open the correct file with the cursor at the correct position. For example, if you double click an error message in the Unity Console, Unity passes these arguments from that error message to the external editor, which then opens the right file at the position where that error occurred.  
  
You can manually edit this field to customize the arguments Unity sends to your external code editor. Click the **Reset argument** button to reset this field to its default setting.  
**Generate all .csproj files** | Generate all .csproj files. Code editors use .sln and .csproj files to access data about your Project. .csproj files store descriptive data or metadata in an XML format. This data might include versioning information, platform requirements, build files, or database settings.  
  
When these files are present, code editors can use the data they contain to provide useful features like highlighting potential compilation errors. Enable this setting to instruct Unity to create .csproj files wherever possible in your Project.  
**Extensions handled**  
 _(Only available if you select either Rider or Visual Studio Code as your External Script Editor)_ | Determines which file types the **External Script Editor** opens. The field is pre-populated with a list of files that the script editor opens by default. To add other file types to this list, type in the file extension and separate each extension with a semicolon.  
**Image application** | Choose which application you want Unity to use to open image files.  
**Revision Control Diff/Merge** | Choose which application you want Unity to use to resolve file differences in your source control repository. Unity detects these tools in their default installation locations. On Windows, Unity checks registry keys for TortoiseMerge, WinMerge, PlasticSCM Merge, and Beyond Compare 4.  
  
For more information, see the Revision Control Diff/Merge section below.  
  
### Revision Control Diff/Merge

Unity currently supports these tools:

  * SourceGear DiffMerge
  * TkDiff
  * P4Merge
  * TortoiseMerge
  * WinMerge
  * PlasticSCM Merge
  * Beyond Compare 4

**Note:** As these are third-party tools that Unity doesn’t include by default, you might want to download and install them separately.

To set up a custom revision tool, follow these steps:

  1. From the **Revision Control Diff/Merge** dropdown list, select **Custom Tool**.
  2. Enter the path to the custom tool’s installation folder. On Mac, this should point to the _Contents / MacOS_ folder in the tool’s installation folder.
  3. Enter the arguments for two-way diffs, three-way diffs, and merges.

To specify file layout in the revision tool, use these arguments:

**Property** | **Function**  
---|---  
`#LTITLE` | Left title  
`#RTITLE` | Right title  
`#ATITLE` | Ancestor title  
`#LEFT` | Left file  
`#RIGHT` | Right file  
`#ANCESTOR` | Ancestor file  
`#OUTPUT` | Output file  
`#ABSLEFT` | Absolute path to the left file  
`#ABSRIGHT` | Absolute path to the right file  
`#ABSANCESTOR` | Absolute path to the ancestor file  
`#ABSOUTPUT` | Absolute path to the output file  
  
Examples:

SourceGear DiffMerge P4Merge

## GI Cache

The Global Illumination (GI) system uses a cache on each computer to store intermediate files used to pre-compute real-time Global Illumination. All projects on the computer share the cache.

**Property** | **Function**  
---|---  
**Maximum Cache Size (GB)** | The maximum GI cache folder size. Unity keeps the GI cache folder size below this number whenever possible. Unity periodically deletes unused files to create more space (deleting the oldest files first). This is an automatic process, and doesn’t require you to do anything.   
**Note:** If the current Scene is using all the files in the GI cache, increase your cache size. Otherwise, resource-intensive recomputation occurs when baking. This can happen when the Scene is large or the cache size is too small.  
**Custom cache location** | Allow a custom location for the GI cache folder. By default, the GI cache is stored in the _Caches_ folder. All Projects share the cache folder.  
**Tip:** Storing the GI Cache on an SSD drive can speed up baking in cases where the baking process is I/O bound.  
**Cache Folder Location** | Click the **Browse** button to specify a location for the cache.  
**Cache compression** | Compress datafiles in the GI cache to use less hard drive space. The datafiles are LZ4-compressed by default, and the naming scheme is a hash and a file extension. Unity computes the hashes based on the inputs to the lighting system, so changing any of the following settings, properties or assets can lead to lighting recomputation:  
\- Materials (Textures, Albedo, Emission)  
\- Lights  
\- Geometry  
\- Static flags  
\- Light Probe groups  
\- Reflection probes  
\- Lightmap Parameters  
**Tip:** If you need to access the raw Enlighten Realtime Global Illumination data, disable Cache Compression and clear the cache.  
**Clean Cache** | Clear the cache directory.   
It’s not safe to delete the GI Cache directory manually while the Editor is running. This is because the Editor creates the _GiCache_ folder when it starts and maintains a set of references to those files. The **Clean Cache** button ensures that the Editor releases all references to the files on disk before they’re deleted.  
**Cache size is** | Displays the current size of the cache.  
**Cache Folder Location** | Displays the current cache folder location.  
  
## Jobs

Use the job system to write simple and safe multithreaded code so that your application can use all its available CPU cores to execute code. The job system can improve the performance of your application.

**Property** | **Function** |   
---|---|---  
**Use Job Threads** | Disable **Use Job Threads** to run all jobs on the main thread. If you’re debugging and want to simplify the problem space and remove all parallelism, you can disable **Use Job Threads** to run all jobs immediately on the main thread when they are scheduled. Disabling **Use Job Threads** has the same effect as if you set JobsUtility.JobWorkerCount to 0.   
  
**Use Job Threads** is enabled by default when the Editor restarts.  
**Enable Jobs Debugger** | Disable **Enable Jobs Debugger** to remove the job system safety system checks which detect potential race conditions and prevent the bugs they can cause. Disable **Enable Jobs Debugger** if you want to monitor performance without the overhead of job system safety checks.   
  
**Enable Jobs Debugger** is enabled by default when the Editor restarts.  
**Leak Detection Level** | Select a mode for leak detection. Leak detection checks if allocations that are made with MallocTracked are freed with FreeTracked. If you do not free unmanaged memory, you will cause memory leaks which have a negative effect on memory usage and reduce performance. Memory leaks persist across domain reloads in the Editor.  
  
In the Editor and development builds, **Enabled** is selected by default. In non-development builds, **Disabled** is the default mode for **Leak Detection Level**.  
| **Disabled** | Do not detect unmanaged memory leaks.  
| **Enabled** | Perform a lightweight count of all memory leaks for each leak category. This option only prints the number of leaks as part of the domain unload process. Use the **Enabled With Stack Trace** leak detection mode to find detected leaks.  
| **Enabled With Stack Trace** | Leak Detection reports the callstack of any MallocTracked allocation that is not deallocated with FreeTracked. **Enabled With Stack Trace** can add a performance cost to allocations. Only use **Enabled With Stack Trace** to intentionally track native memory leaks. **Enabled With Stack Trace** , like **Enabled** , reports leaks as part of the domain unload process.   
You can only select **Enabled With Stack Trace** in the Editor and in development builds.  
  
## Package Manager

Use the Package Manager preferences to change the default cache location for the following packages:

  * Packages installed from the Unity Registry
  * Packages downloaded from the Asset Store

**Property** | **Function**  
---|---  
**Packages** | Set the cache location that determines where packages installed from the Unity Registry are stored. For more information, see Customizing the global cache location.  
**My Assets** | Set the cache location that determines where packages downloaded from the **Asset Store** are stored. For more information, see Customize the Asset Store cache location.  
  
## Scene View

Use the Scene View preferences to customize object placement and visibility while editing.

**Property** | **Function**  
---|---  
**Create Objects at Origin** | Create new objects at origin (as opposed to the Scene pivot). Disabled by default.  
**Create Objects with Constrained Proportions** | Define the default behavior for Scale in the Transform component.  
If enabled, when you adjust the value of a scale axis, the other values adjust proportionately.  
**Line Thickness** | The line thickness of your transform tools.  
**Enable filtering while searching** | Gray out any non-matching items in the Scene view. Enabled by default.  
**Enable filtering while editing**LOD groups**** | Gray out other objects in the scene while editing level of detail (LOD) groups. Enabled by default.  
  
## Search

Use the Search preferences to set your search preferences for the Editor.

> **Tip:** You can also access the Search preferences in one of the following ways:
> 
>   * Enter **?** (question mark) in the search field and select **Open Search Preferences** from the results.
> 
>   * From **More Options (** :**)** in the top-left of the **Search** window, select **Preferences**.
> 
> 

  
_Search Preferences_

**Setting** | **Function**  
---|---  
**Track the current selection in the search** |  | Execute the `SearchProvider.trackSelection` callback each time the Search selection changes.  
  
The callback _pings_ Assets in the Project window or Hierarchy window, which can slow Search navigation in large Projects.  
**Generate an asset preview thumbnail for found items** |  | Display thumbnails for items that are currently visible in the results pane of the Search window.  
  
When you disable this setting, Search displays a generic icon. This is useful in large Projects, where generating icons can slow Search navigation.  
**Select the typing debounce threshold (ms)** |  | The debouncing threshold is the time the system waits for the user to finish typing before executing the search.  
**Provider Settings** |  |   
|  **A** _[Provider Toggles]_ | Enable and disable providers. When you disable a provider, Search ignores it when executing searches.  
|  **B** _[Provider Order]_ | Modify the order in which search items are shown on the screen. All items of a given provider priority appear before any lower priority items.  
|  **C** _[Default Actions]_ | Choose the default actions to execute when you select (for example, double-click) an item in the search results.  
**Reset Priorities** |  | Resets all providers to their default on/off state and priority.  
**Search Engines** |  | Set the search fields in the Object Selector, Project, and Scene to one of the available search engines.   
  
**Classic** \- The original search functionality.   
**Advanced** \- The latest version of Search for Unity (formerly QuickSearch).  
  
### Indexing

Set the Custom index pages by selecting them or deselecting them from the **Custom Indexers** dropdown list.

## Custom package preferences

Some Asset Store or Unity packages add their own custom preferences to the **Preferences** window. Typically, these use the package name as the preferences category. In this example, you can see the Cinemachine package preferences:

Package-specific preferences appear in the scope list

For information about a specific package’s preferences, see the documentation for that package. This section contains documentation for standard Unity preferences only.