---
title: "File Access Profiler module"
category: "General"
source_file: "profiler-file-access-module.html"
doc_type: "manual"
---

# File Access Profiler module

The File Access **Profiler** module displays information about the file activity in your application, such as the number of read or write operations Unity performs or the number of file handles open, either for a specific frame or across all frames in a capture. You can use this information to help determine how efficiently your application performs file operations. This module can capture information about file operations on any file within your built application’s folder structure, or within your Unity project folder if you run the Profiler in the Unity Editor. This module is not enabled by default. To enable the File Access Profiler module, open the Profiler window, select the **Profiler Modules** dropdown menu, and toggle the **File Access** checkbox.

The File Access Profiler module

## Chart categories

The File Access Profiler module’s chart is divided into five categories. To change the order of the categories in the chart, drag and drop them in the chart’s legend. You can also click a category’s colored legend to toggle its display on or off. For more information on how to use the Profiler window, see Getting started with the Profiler window. This module doesn’t collect information about unsuccessful file operations. If a file operation attempt is unsuccessful, Unity displays an error.

**Chart** | **Description**  
---|---  
**Files Opened** | The total number of files successfully opened in the local file system this frame.  
**Files Closed** | The total number of files successfully closed in the local file system this frame.  
**File Seeks** | The number of file seek operations performed in the local file system this frame. A file seek operation involves a search through the contents of a file.  
**Reads in Flight** | The total number of read operations that were in progress during this frame.  
**File Handles Open** | The total number of file handles held open at any time during this frame. This includes files that Unity opens and closes within the same frame.  
  
## Module details pane

When you select a frame in the File Access Profiler module, the module details pane displays detailed information about files that Unity accessed during the capture. The File Access Profiler module has two views:

  * The File Summary view provides a summary of all file activity for each file Unity accesses during the selected frame setting.
  * The Accesses view displays each file access operation in the data set in the order that they occurred.

Use the dropdown menu at the top-left of the details pane to toggle which view is active. By default, the **File Summary** view is active.

Both views can display information for either a single selected frame, or for all frames in the capture. Use the second dropdown menu at the top-left of the details pane to choose between a single frame or all frames. This module doesn’t populate the details pane automatically. Instead, you need to select the **Analyze Markers** button at the top of the details pane to populate the view with data.

### File Summary view

The **File Summary** view displays a summary of all file access operations that happened to each file during the capture. One entry in the table represents the full summary for a single file.

The table below describes all possible columns that the **File Summary** view table can display. Not all columns are enabled by default; to enable or disable a column, right-click anywhere in the row that contains the column headers to open a menu. Use this menu to toggle any column on or off.

**Detail** | **Description** | **Enabled by default**  
---|---|---  
**Filename** | The name of the file that was accessed. | Yes  
**Total Bytes Read** | The total number of bytes of information Unity read from this file during the selected frames. | Yes  
**Read Access Time (ms)** | The total time Unity spent performing reads from this file during the selected frames. | Yes  
**Access Count** | The total number of accesses of any type to this file during the selected frames. | Yes  
**First Frame** | The first frame that Unity accessed this file on. | Yes  
**Number of Frames** | The total number of frames that Unity accessed this file on. | Yes  
**ID** | An index that represents the order of execution of the file access markers. | No  
**Read Bandwidth (MBps)** | The average bandwidth of read operations on this file over the selected frames, in megabytes per second. | No  
**Open Count** | Total number of opening operations on this file during the selected frames. | No  
**Close Count** | Total number of closing operations on this file during the selected frames. | No  
**Read Count** | Total number of read operations on this file during the selected frames. | No  
**Write Count** | Total number of write operations on this file during the selected frames. | No  
**Seek Count** | Total number of file seek operations on this file during the selected frames. | No  
**Total Bytes Written** | The total number of bytes Unity wrote to this file during the selected frames. | No  
**Write Bandwidth (MBps)** | The average bandwidth of write operations on this file over the selected frames, in megabytes per second. | No  
**Open Access Time (ms)** | The total time Unity spent performing opening operations on this file during the selected frames, in milliseconds. | No  
**Close Access Time (ms)** | The total time Unity spent performing close operations on this file during the selected frames, in milliseconds. | No  
**Write Access Time (ms)** | The total time Unity spent performing write operations to this file during the selected frames, in milliseconds. | No  
**Total Access Time (ms)** | The total time Unity spent accessing this file during the selected frames, in milliseconds. | No  
  
### Accesses view

The **Accesses** view provides detailed information about every file access operation in the capture. Each entry in the table in the details pane of the Profiler represents a single file access operation to a single file. The below table describes all possible columns that the Accesses view can display.

**Detail** | **Description** | **Enabled by default**  
---|---|---  
**Index** | An ID number that represents the order in which Unity performed the access operations. | Yes  
**Filename** | The name of the accessed file during this operation. To see the file path in full, hover your cursor over the filename entry. | Yes  
**Type** | The type of access operation performed. This can be either **Open** , **Close** , **Seek** , **Read** , or **Write**. | Yes  
**Access Size** | The number of bytes transferred during the access, where the access was a read or write. Where the access was a file seek, the size is the destination offset. | Yes  
**Offset** | The (starting) offset of the file access. | Yes  
**Duration (ms)** | The time taken to perform this access, in milliseconds. | Yes  
**Average Bandwidth (MBps)** | The average bandwidth for this access, where the access type was a read. | Yes  
**First Frame Index** | The ID of the frame this access began on. | Yes  
**Frames** | The total number of frames this access occurred for. | Yes  
**Thread** | The thread the access occurred on. | Yes  
**Timestamp (ms)** | The time this access started, relative to the start of the profiler capture. | No  
  
You can right-click on any of the file access markers to open a sub-menu with additional options to explore the data. The available options are as follows:

**Property** | **Function**  
---|---  
**Show marker in timeline view** | Opens this marker in the CPU Usage Profiler module.  
**Go to the first frame of this marker** | Selects the frame in which the marker first appears in the chart. This option is disabled if the marker only appears on one frame.  
**Go to the last frame of this marker** | Selects the frame in which this marker last appears in the chart. This option is disabled if the marker only appears on one frame.  
**Filter the view to this file path** | Populates the search bar with the contents of the **Filename** column to filter the results.