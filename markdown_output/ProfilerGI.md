---
title: "Global Illumination Profiler module"
category: "General"
source_file: "ProfilerGI.html"
doc_type: "manual"
---

# Global Illumination Profiler module

The **Global Illumination** **Profiler** **Profiler** module displays statistics about how much CPU time the Enlighten Realtime Global Illumination subsystem uses across all worker threads. There is an option to control the number of **Enlighten** module displays statistics about how much CPU time the Enlighten Realtime Global Illumination subsystem uses across all worker threads. There is an option to control the number of **Enlighten** worker threads included in Command Line Arguments.

Global Illumination Profiler module

## Chart categories

The Global Illumination Profiler module’s chart tracks the time the global illumination subsystem spent on all worker threads. The timings are divided into 10 categories. To change the order of the categories in the chart, you can drag and drop them in the chart’s legend. You can also click a category’s colored legend to toggle its display.

**Chart** | **Description**  
---|---  
**Light Probe** | The time spent updating Light Probes.  
**Setup** | The time spent in the Setup stage.  
**Environment** | The time spent processing Environment lighting.  
**Input Lighting** | The time spent processing input lighting.  
**Systems** | The time spent updating Systems.  
**Solve Tasks** | The time spent running radiosity solver tasks.  
**Dynamic Objects** | Time spent updating Dynamic **GameObjects**.  
**Other Commands** | Time spent updating other commands.  
**Block Command Write** | Time spent in a blocked state, waiting for the command buffer.  
  
## Module details pane

When you select the Global Illumination module, the details pane below it displays a breakdown of where the application spent time in the selected frame. The data available is as follows:

**Data** | **Description**  
---|---  
**Total CPU Time** | Total Enlighten Global Illumination CPU time across all threads in ms.  
**Probe Update Time** | Time spent updating Light Probes in ms.  
**Setup Time** | Time spent in the Setup stage in ms.  
**Environment Time** | Time spent processing Environment lighting in ms.  
**Input Lighting Time** | Time spent processing input lighting in ms.  
**Systems Time** | Time spent updating Systems in ms.  
**Solve Tasks Time** | Time spent running radiosity solver tasks in ms.  
**Dynamic Objects Time** | Time spent updating Dynamic GameObjects in ms.  
**Time Between Updates** | Time between Global Illumination updates in ms.  
**Other Commands Time** | Time spent processing other commands in ms.  
**Blocked Command Write Time** | Time spent in blocked state, waiting for command buffer in ms.  
**Blocked Buffer Writes** | Number of writes to the command buffer that were blocking.  
**Total Light Probes** | Total number of Light Probes in the **Scene**.  
**Solved Light Probes** | Number of solved Light Probes since the last update.  
**Probe Sets** | Number of Light Probe sets in the Scene.  
**Systems** | Number of Enlighten Global Illumination Systems in the Scene.  
**Pending Material GPU Renders** | Number of Albedo/Emission renders queued for rendering on the GPU.  
**Pending Material Updates** | Number of Material updates waiting to get processed.