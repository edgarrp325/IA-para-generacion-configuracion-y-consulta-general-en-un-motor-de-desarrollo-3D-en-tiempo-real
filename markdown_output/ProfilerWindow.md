---
title: "The Profiler window"
category: "General"
source_file: "ProfilerWindow.html"
doc_type: "manual"
---

# The Profiler window

To access the Unity Profiler, go to **Window > Analysis > Profiler** or use the keyboard shortcut **Ctrl+7** (**Command+7** on macOS).

The **Profiler** records multiple areas of your application’s performance, and displays that information to you. You can use this information to make informed decisions about what you might need to optimize in your application, and to confirm that your optimizations produce the results you expect.

By default, the Profiler records and keeps the last 300 frames of your game, and shows you detailed information about every frame. You can increase the number of frames it records in the Preferences window up to 2,000 frames. **Note:** If you increase this setting to a large number of frames, the Profiler’s overhead and memory usage might become more performance intensive.

You can inspect script code, and how your application uses certain Assets and resources that might be slowing it down. You can also compare how your application performs on different devices. The Profiler has several different Profiler modules that you can add to your profiling session to get more information on areas such as rendering, memory, and audio. 

This page covers the following topics:

  * Profiler window layout
  * Profiler Preferences
  * Profiler controls
    * Deep Profiling
  * Profiler modules
    * Profiler module overhead
    * Profiler frame charts
  * Standalone Profiler
  * Command line arguments

## Profiler window layout

The Profiler window is laid out as follows:

The Profiler window, with the CPU Usage Profiler module selected

  * **A:** Profiler modules. This is a list of all the modules you can profile in your application. Use the drop-down menu at the top of this area to add and remove modules from the window.
  * **B:** Profiler controls. Use these controls to set which device to profile from and what kind of profiling Unity should perform, navigate between frames, and start recording data.
  * **C:** **Frame charts**. This area contains charts of each module the Profiler profiles. This area is blank when you open the Profiler for the first time, and fills with information when you start profiling your application.
  * **D:** **Module details panel**. The information in this area of the window changes based on the module you have selected. For instance, when you select the CPU Usage Profiler module, it contains a detailed timeline and the option to switch to a Hierarchy view. When you select the Rendering Profiler module, this area displays a list of debugging information. This area is blank when you open the Profiler for the first time, and fills with information when you start profiling your application.

## Profiler Preferences

The Preferences window contains additional Profiler window settings as follows:

**Preference** | **Description**  
---|---  
**Frame count** | Set the maximum number of frames for the Profiler to capture. You can set this number between 300 and 2,000.  
**Show stats for ‘current frame’** | By default, when you select the **Current Frame** button and enter Current Frame mode, the frame indicator line does not have annotations with the stats for the current frame. This is because the stats annotations might make it difficult to view data in real-time. To display the annotations, enable this setting.  
**Default recording state** | Select which recording state the Profiler should open in. Choose from **Enabled** , **Disabled** , or **Remember**. Enabled keeps the **Record** button enabled between sessions, while **Disbled** disables it, regardless of whether you turn it on or off during your profiling session. The **Remember** state remembers whether you have enabled or disabled the **Record** button during your session and keeps it at its last state next time you open the Profiler window.  
**Default editor target mode** | Select what mode the **Attach to Player** dropdown should target by default. Choose from either **Playmode** or **Editor**.  
  
## Profiler controls

The Profiler controls are in the **toolbar** at the top of the Profiler window. Use these to start or stop recording profiler data, and to navigate through profiled frames.

**Control** | **Function**  
---|---  
**Attach to Player** | Select which target to profile your application on. By default, this is set to **Playmode**. You can also select **Editor** to profile the Unity Editor and display the resources that the Editor is currently using.  
  
Unity also automatically detects any devices that are running on your network or connected via USB, and displays them in the drop-down. Click **Enter IP** in the drop-down to manually enter the IP address of the device you want to profile your application on. For more information, see Profiling your application.  
**Record** | Enable this setting to record profiling information for the active modules when you run your application. If you don’t have this button enabled, the Profiler doesn’t collect any data when you run your application.  
**Back arrow** | Navigate one frame back.  
**Forward arrow** | Navigate one frame forward.  
**Current Frame** | When you click the **Current Frame** button, the frame indicator line jumps to the last recorded frame, and the Profiler enters Current Frame mode. While the Profiler collects data in this mode, it stays on the current frame and displays the data it collects in real-time. Click the button again to exit Current Frame mode.  
**Frame number** | Indicates the frame number you are currently looking at in the Profiler. The number on the left is the current frame selected, and the number on the right is the total number of frames combined that the Profiler collected during your entire Profiling session.  
**Clear** | Erase all data from the Profiler window.  
**Clear on Play** | Enable this setting to erase all data from the Profiler window next time you click Play in the Player window, or when you connect to a new target device.  
**Deep Profile** | Enable this setting to profile all C# methods. When you enable this setting, Unity adds instrumentation to all mono calls, which then allows for a more detailed investigation of your **scripts**. See Deep Profiling.  
**Call Stacks** | To record call stacks for scripting memory allocations, click this toggle. Frames that the Profiler records when you enable this option have information about the selected samples on the full call stack that lead to a managed scripting allocation, even when **Deep Profile** is not active. By default, the Profiler records the full call stack information for GC.Alloc samples when you enable this setting, but you can change this to a different sample from the dropdown menu (**UnsafeUtility.Malloc** , **JobHandle.Complete** , or **Native Allocations**). For more information, see the Allocation call stacks section of the CPU Usage Profiler module page.  
**Load** | Load saved Profiler data into the Profiler window. You can also load binary profile data that the Player has written out to file via the Profiler.logFile API.  
  
Hold down the Shift button and click the **Load** button to append the file contents to the current profile frames.  
**Save** | Save the Profiler data into a .data file in your Project folder.  
**Context menu**  
| Color Blind Mode | Enable this setting to make the Profiler use higher contrast colors in its graphs. This enhances visibility for users with red-green color blindness (such as deuteranopia, protanopia, or tritanopia).  
| Show stats for “current” frame | By default, when you select the **Current Frame** button and enter Current Frame mode, the frame indicator line does not have annotations with the stats for the current frame. This is because the stats annotations might make it difficult to view data in real-time. To display the annotations, enable this setting.  
| Preferences | Open the **Preferences** menu to adjust Profiler-specific properties.  
  
To maintain a low overhead, Unity only redraws every fifth frame of the Editor UI. This results in a slightly stuttered update.

### Deep Profiling

Usually the Profiler only profiles code timings that are explicitly wrapped in ProfilerMarkers. This includes the first call stack depth of invocations from the engine’s native code into your scripting code, such as a `MonoBehaviour`’s `Start`, `Update`, or similar methods. 

Without adding more explicit `ProfilerMarker` instrumentation to your own code, the only other samples you can see as child samples of your scripting code are those that call back into Unity’s API, if that API has been instrumented. Most API calls that carry a performance overhead are instrumented. For example, accessing the main **Camera** through the `Camera.main` API is registered as a “`FindMainCamera`” sample.

When you enable the **Deep Profile** setting, the Profiler profiles every part of your script code and records all function calls, including at least the first call stack depth into any Unity API. This is useful information to help you work out where your code impacts on your application’s performance, but it comes with a large overhead.

When you deep profile your application, Unity injects profiler instrumentation into all of your script methods to record all function calls. This is useful to understand where your application code spends the most time. 

Deep Profiling is resource-intensive and uses a lot of memory. As a result, your application runs significantly slower while it is profiling. Deep Profiling is better suited for small games with simple scripting. If you are using complex script code, your application might not be able to use Deep Profiling at all, and for many larger applications, Deep Profiling might make Unity run out of memory. 

If you run into issues where there are too many samples for the Profiler to store in the ring buffer it uses to stream them to the Profiler, then Unity displays an error message. To increase the size of the ring buffer, you can adjust the Profiler.maxUsedMemory property for the Player you’re profiling.

If Deep Profiling causes the frame rate of your application to drop so much that it is impossible to run, you can manually profile blocks of your script code, which has a smaller overhead than Deep Profiling. Use ProfilerMarkers to manually add the instrumentation you need to mark up script blocks. These appear in the CPU Usage Profiler module.

If you want to find out which call stacks lead to a GC.Alloc sample without Deep Profiling, you can turn on the collection of **Allocation call stacks**. Enable the **Call Stacks** setting in the Profiler controls, and then you can select the GC.Alloc samples in the Timeline view, or use the Show **Related Objects panel** in the Hierarchy view to find the call stacks for these samples. For more information, see the documentation on Allocation call stacks in the CPU Profiler Module page.

## Profiler modules

The top part of the Profiler window is divided into Profiler modules that profile specific areas of your game. When you profile your application, Unity displays the data related to each module in corresponding charts.

The **CPU Usage** module provides the best overview of how much time your application spends on each frame. The other modules collect more specific data and can help you inspect more specific areas or to monitor the vitals of your application, such as memory consumption, rendering, or audio statistics.

Each module has its own chart. When you select a module, a Module Details panel appears in the bottom section of the window, which you can use to inspect the detailed data the module collects.

**Profiler module** | **Function**  
---|---  
**CPU Usage** | Displays an overview of where your application spends the most time, in areas such as physics, scripts, animation, and garbage collection. This module contains broad profiling information about your application, and you can use it to decide which further modules to use to investigate more specific issues in your application. This module is always active, even if you close it. See CPU Usage Profiler module  
**GPU Usage** | Displays information related to graphics processing. By default this module is not active, because it has a high overhead. See GPU Usage Profiler module.  
**Rendering** | Displays information on how Unity renders graphics in your application, including information on static and **dynamic batching** , SetPass and Draw calls, triangles, and vertices. See Rendering Profiler module.  
**Memory** | Displays information on how Unity allocates memory in your application. This is particularly useful for seeing how scripting allocations (GC.Alloc) lead up to garbage collection, or how your application’s Asset memory usage trends over time. See Memory Profiler module.  
**Audio** | Displays information related to the audio in your application, such as when and how many **audio sources** play, how much CPU usage the Audio system requires, and how much memory Unity allocates to it. See Audio Profiler module.  
**Video** | Displays information related to video in your application. See Video Profiler module.  
**Physics** | Displays information about the physics in your application that the **physics engine** has processed. See Physics Profiler module.  
**Physics (2D)** | Similar to the Physics Profiler module, this module displays information about where the physics engine has processed 2D physics in your application. See 2D Physics Profiler module.  
**UI** | Displays information about how Unity handles UI batching for your application, including why and how Unity batches items. See UI and UI Details Profiler module.  
**UI Details** | Similar to the UI Module, this module’s chart adds data about batch and vertices count, as well as markers which include information about user input events that trigger UI changes. See UI and UI Details Profiler module  
**Global Illumination** | Displays information on how much CPU resource Unity spends on the Global Illumination lighting subsystem in your application. See Global Illumination Profiler window.  
**Virtual Texturing** | Displays statistics about Streaming Virtual Texturing in your application. See the Virtual Texturing Profiler module.  
**Asset Loading** | Displays information about how your application loads assets. See the Asset Loading Profiler module.  
**File Access** | Displays information about file accesses in your application. See the File Access Profiler module.  
  
### Profiler module overhead

Some Profiler modules have a large data collection overhead, such as the GPU, UI, and Audio Profiler module. To prevent these modules from affecting your application’s performance, you can deactivate them by unselecting them in the **Profiler Module** dropdown. This removes the module from the window, stops the Profiler from collecting that module’s data, and lowers the Profiler’s overhead. 

This does not apply to the CPU Usage module, which always collects data even when it’s not active, because other modules rely on it.

To add a module, select the **Profiler Module** dropdown and choose the Profiler you want to activate. When you choose a Profiler module from the drop-down, it starts collecting data, but shows no data for the period in which it was not active. 

To avoid the overhead of the GPU Profiler module, it is not active by default. The GPU Profiler module must be active at the start of your application to hook into the graphics driver. If you add it later, it has no effect on most platforms, and the Profiler displays the message “GPU profiling is not supported by the graphics card driver (or it was disabled because of driver bugs)”.

If you instruct the Profiler to collect and send data to disk through the Profiler.logFile API instead of through the Profiler window, you can turn off Profiler modules through Profiler.SetAreaEnabled().

Some settings that debug your scripts through an external IDE might also create overhead. To avoid this overhead and get more accurate measurements, disable the **Editor Attaching** setting (menu: **Preferences > External Tools**). Similarly, when you profile build Players, open **Build Settings** and disable **Script Debugging** to avoid that overhead.

### Profiler frame charts

The upper part of the Profiler window displays performance data over time on a frame-by-frame basis. When you run your application, the Profiler records data for each frame. By default, the Profiler window displays the history of the last 300 frames it profiles. You can increase the number of frames the Profiler profiles in the **Preferences** window, up to a maximum of 2,000.

When you click in the Profiler frame chart area of the Profiler window, a white line appears, which highlights one frame of your application. To navigate between frames, use the transport controls in the toolbar of the Profiler window.

Unity manages the vertical scale of the charts automatically, and the charts attempt to fill the vertical space of the window. To see more detail in a chart, you can remove other Profiler modules, or you can drag the splitter between the charts and the detailed statistics area to increase the screen area of the charts.

To toggle hiding and displaying a metric in a chart, click the colored square next to its label in its module. This can be useful to identify the causes of spikes. In stacked charts such as the CPU Usage Profiler’s chart, you can reorder the metric labels to affect the stacking order, which helps make more prominent metrics more visible.

Each Profiler module collects different performance data metrics and displays them in separate charts. When you click on a frame, Unity displays more details about the frame in the Module Details pane in the bottom half of the Profiler window. The type of detail in this window changes depending on which Profile module you select. For more information about the specific details that each module displays in this area, see the individual documentation for the Profiler modules.

## Standalone Profiler

To use the Standalone Profiler, go to **Window > Analysis > Profiler (Standalone process)**. When you select the Standalone Profiler, Unity launches the Profiler outside of the Unity Editor’s process, and instead launches the Profiler in a new, separate process.

Launching the Profiler in its own dedicated process ensures cleaner Profiler data when you target the Editor or Play mode. It also reduces overhead, because the Profiler isn’t profiling itself or sharing a process with your application or the Editor. The functionality and controls of the Profiler remain the same as when you run the Profiler in the same process as the Editor.

Menu selection for the Standalone Profiler

When you start a separate process for the Profiler window, it takes longer to start up than opening it in the same process as the Editor. You cannot dock any Editor windows that are connected to the separate process to the main process’s windows. Additionally, when you restart the Editor, Unity does not re-open the windows in the out-of-process Profiler.

## Command line arguments

If you start your built Player or the Unity Editor from the command line (such as the Command Prompt on Windows, Terminal on macOS, Linux shell, or adb for Android), you can pass command line arguments to configure some Profiler settings.

**Command line argument** | **Description**  
---|---  
`-deepprofiling` | Enable Deep Profiling in a built Player.  
`-profiler-enable` | Profile the start-up of a Player or the Editor. When you use this argument with a Player, it has the same effect as building the Player with the **Autoconnect Profiler** option enabled in Build Settings.   
  
When you use this argument with the Editor, it starts collecting and displaying Profiler information in the Profiler window on start-up of the Editor.  
`-profiler-log-file <Path/To/Log/File.raw>` | This argument sets the Profiler up to stream the profile data to a .raw file on startup. It works for both Players and the Editor.  
`-profiler-capture-frame-count <NumberOfFrames>` | This argument sets how many frames to capture in a profile when streaming to a .raw file on start-up. It only works on Players.  
`-profiler-maxusedmemory` | By default, `maxUsedMemory` is 16MB for Players and 256MB for the Editor. You can use this argument to set the `maxUsedMemory` parameter to a custom size at start-up (for example, `-profiler-maxusedmemory 16777216`). The size is set in bytes.  
  
* * *

  * Added Out-of-process Profiler in 2020.1 NewIn20201