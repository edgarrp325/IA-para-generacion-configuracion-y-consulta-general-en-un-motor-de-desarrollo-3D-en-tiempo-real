---
title: "Memory Profiler module"
category: "General"
source_file: "ProfilerMemory.html"
doc_type: "manual"
---

# Memory Profiler module

There are two ways of analyzing memory usage in your application in Unity:

  * **Memory** **Profiler** **module** : A built-in Profiler module that gives you basic information on where your application uses memory.
  * **Memory Profiler package** : A Unity package that you can add to your project. It adds an additional Memory Profiler window to the Unity Editor, which you can then use to analyze memory usage in your application in even more detail. You can store and compare snapshots to find memory leaks, or see the memory layout to find memory fragmentation issues.

This page covers information on the built-in Memory Profiler module. For more information on the Memory profiler package, see the Memory Profiler documentation.

The Memory Profiler module visualizes counters that represent the total allocated memory in your application. You can use the memory module to see information like the number of loaded objects, and the memory that they take in total per category. You can also see the number of GC allocations per Profiler frame.

## Memory profiling in the Editor

When you profile your application in the Editor, the Memory Profiler module reports higher data use than a similar profile of the application built on a target device would. This is because the Unity Editor uses specific objects that take up memory, and the Editor window itself uses extra memory.

Part of the extra memory use is because Unity treats objects like textures as read/write enabled in the Editor and keeps an extra copy of each texture on the CPU. This effectively doubles the reported memory use of textures in the Editor; for a more accurate idea of memory use by textures, profile a built version of your application running on the target platform.

Also, because Unity can’t cleanly separate the memory that the Profiler itself takes up from the Play mode’s memory, memory that the Profiler uses is displayed in the Profiler window. To remind you of this, a warning displays at the top of the Memory Profiler module details pane whenever you have the Profiler target set to **Play Mode** or **Editor**. For more precise numbers and memory usage for your application, you should profile your application on the target device and operating system you intend it to run on. For more information, see the documentation on Profiling your application. 

## Chart categories

The Memory Profiler module is divided into categories that display detailed information on where your application spends memory. You can also click a category’s colored legend to toggle its display.

**Category** | **Description**  
---|---  
**Total Allocated** | The total memory your application has used.  
**Texture Memory** | How much memory the Textures in your application have used.  
****Mesh** Memory** | How much memory the Meshes in your application have used.  
**Material Count** | The number of Material instances in your application.  
**Object Count** | The number of native object instances in your application.  
**GC Used Memory** | The amount of memory the GC heap has used.  
**GC Allocated in Frame** | The amount of memory allocated per frame on the GC heap.  
  
## Module details pane

There are two views available in the module details pane, located at the bottom of the Profiler window: 

  * **Simple:** Displays a high level overview of the memory statistics per frame
  * **Detailed:** This view is deprecated. Use the Memory Profiler package to get a detailed memory analysis of your application.

### Simple view

The Simple view displays an overview of how Unity uses memory in real-time on a per-frame basis. It breaks down the total memory that your application uses into a few major categories. The **Total** value is based on the System Used Memory Profiler counter, which indicates how much memory the operating system (OS) reports as being in use by your application.

The Simple view with some Profiler data loaded

Unity sets some memory pools aside for allocations to avoid asking the operating system for memory too often. The Profiler module displays how much memory Unity reserves, and how much memory Unity used at the time of the Profiler capture. 

The Simple view displays the data collected within the **System Used Memory** Profiler counter. This indicates how much memory the operating system (OS) reports as being in use by the app and corresponds to the **Total** value of the **Total Committed Memory** bar and the **Total Memory Breakdown** bar. 

On platforms that support getting the total memory size of the application from the operating system, the **System Memory Usage** is over 0 and is the same size in a task manager. 

The following reference table describes the statistics available in the Simple view, plus its corresponding profiler counter, and availability in Release builds. This information is also available via the ProfilerRecorder API and in the Profiler Module Editor so you can add them to a custom Profiler module.

**Property** | **Description** | **Corresponding Profiler counter** | **Available in Release Players?**  
---|---|---|---  
**Normalized** | Enable this setting to scale the **Total Committed Memory** and **Total Memory Breakdown** charts to the memory usage of the selected frame. If you disable this setting, the charts scale to the total used memory within the frame range. This setting can help you see how the total or relative amounts of memory change from frame to frame | N/A | N/A  
**Total Committed Memory** | The length of the Total Committed Memory bar indicates the total amount of memory that Unity’s Memory Manager system tracked, how much of that it used, and how much memory isn’t tracked through this system. | System Used Memory | Yes  
Tracked Memory (in use / Reserved) | Indicates the total amount of memory that Unity uses and tracks (**in use**), and the amount of memory that Unity reserves for tracking purposes and pool allocations (**Reserved**). | Total Used Memory   
  
Total Reserved Memory | Yes  
Untracked Memory | Indicates the total amount of memory that Unity used but isn’t aware of. Some examples of untracked memory are:   
  
\- Memory allocated through native plug-ins or some drivers   
\- Mono or IL2CPP type metadata   
\- Memory that executable code and DLLs use   
  
The Memory Profiler package and native platform providers might have more information on some of these untracked memory amounts. | N/A | N/A  
**Total Memory Breakdown** | Displays the same total amount as the **Total Committed Memory** bar but breaks it into some high level categories, based on which subsystems Unity allocated the memory for.   
  
Not all memory systems use pools or differentiate between used and reserved memory. Those that do display two numbers, the used and the reserved amount of memory. If the used amount doesn’t share the same unit (B, MB, GB) as the reserved amount, Unity displays the unit, otherwise it’s omitted. | System Used Memory | Yes  
Managed Heap (in use / Reserved) | The used heap size and total heap size that managed code uses. This memory is garbage collected. | GC Used Memory   
  
GC Reserved Memory | Yes  
Graphics & Graphics Driver | The estimated amount of memory the driver uses on Textures, render targets, Shaders, and Mesh data. | Gfx Used Memory  
  
Gfx Reserved Memory | No  
Audio | The Audio system’s estimated memory usage. | Audio Used Memory  
  
Audio Reserved Memory | Yes  
Video | The Video system’s estimated memory usage. | Video Used Memory  
  
Video Reserved Memory | Yes  
Other | Displays native memory that Unity tracks, but isn’t reported under a specific counter.   
  
To get more information on the makeup of this or the other categories, use the Memory Profiler package. | N/A | N/A  
Profiler | The memory that the Profiler functionality uses and reserves from the system. | Profiler Used Memory  
  
Profiler Reserved Memory | Yes  
**Objects stats** | Displays the amount of object instances of the types of Assets that commonly take up a high percentage of the memory (Textures, Meshes, Materials, Animation Clips), together with their accumulated sizes in memory (Assets, GameObjects, Scene Objects).   
  
**Note:** Texture and Mesh memory doesn’t map directly to the **Graphics & Graphics** Driver stat in the **Total Memory Breakdown** view. This is because some of that memory might also fall into the **Other** category of the Total Memory Breakdown bar. | Object Count | No  
Textures | The total count of loaded textures and memory they use. | Texture Count  
  
Texture Memory | No  
Meshes | The total count of loaded meshes and memory they use. | Mesh Count  
  
Mesh Memory | No  
Materials | The total count of loaded materials and memory they use. | Material Count  
  
Material Memory | No  
Animation Clips | The total count of loaded AnimationClips and memory they use. | AnimationClip Count  
  
AnimationClip Memory | No  
Assets | The total number of loaded assets. | Asset Count | No  
Game Objects | The total number of GameObject instances in the **scene** instances in the **scene**. | GameObject Count | No  
Scene Objects | The total number of dynamic `UnityEngine.Objects`. This number includes the GameObject Count, plus the total number of components, and everything which isn’t an asset in the scene. | Scene Object Count | No  
GC allocated in frame | Displays the amount of managed allocations in the selected frame, and their total size in bytes. | GC Allocation In Frame Count  
  
GC Allocated In Frame | No  
  
### Availability in Players

You can use the ProfilerRecorder API to access the Memory Profiler module’s counters in Players. The following example contains a simple script that collects **Total Reserved Memory** , **GC Reserved Memory** and **System Used Memory** metrics, and displays those as a GUI.TextArea. The Memory Profiler module information belongs to the ProfilerCategory.Memory **Profiler category**.
    
    
    using System.Text;
    using Unity.Profiling;
    using UnityEngine;
    
    public class MemoryStatsScript : MonoBehaviour
    {
        string statsText;
        ProfilerRecorder totalReservedMemoryRecorder;
        ProfilerRecorder gcReservedMemoryRecorder;
        ProfilerRecorder systemUsedMemoryRecorder;
    
        void OnEnable()
        {
            totalReservedMemoryRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Memory, "Total Reserved Memory");
            gcReservedMemoryRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Memory, "GC Reserved Memory");
            systemUsedMemoryRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Memory, "System Used Memory");
        }
    
        void OnDisable()
        {
            totalReservedMemoryRecorder.Dispose();
            gcReservedMemoryRecorder.Dispose();
            systemUsedMemoryRecorder.Dispose();
        }
    
        void Update()
        {
            var sb = new StringBuilder(500);
            if (totalReservedMemoryRecorder.Valid)
                sb.AppendLine($"Total Reserved Memory: {totalReservedMemoryRecorder.LastValue}");
            if (gcReservedMemoryRecorder.Valid)
                sb.AppendLine($"GC Reserved Memory: {gcReservedMemoryRecorder.LastValue}");
            if (systemUsedMemoryRecorder.Valid)
                sb.AppendLine($"System Used Memory: {systemUsedMemoryRecorder.LastValue}");
            statsText = sb.ToString();
        }
    
        void OnGUI()
        {
            GUI.TextArea(new Rect(10, 30, 250, 50), statsText);
        }
    }
    

The following screenshot shows the result of adding the script to the Tanks! tutorial project.

Tanks! tutorial with the overlaid memory information

This information is available in Release Players, as are the other high level counters in the table above. If you want to see the selected memory counters in a custom module in the Profiler window, use the Module Editor to configure the chart.