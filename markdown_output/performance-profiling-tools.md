---
title: "Profiling tools"
category: "General"
source_file: "performance-profiling-tools.html"
doc_type: "manual"
---

# Profiling tools

Profiling your application is the best way to measure its performance. You can use a variety of profiling tools to understand where there might be any issues with elements of your application including memory usage, CPU performance, GPU performance, and your custom **scripts**

## Unity’s profiling tools

Unity has several profiling tools that you can use to measure the performance of your application:

  * Unity Profiler: Measure the performance of the Unity Editor, your application in Play mode, or connect to a device running your application in development mode.
  * Profiling Core package: Provides APIs that you can use to add contextual information to Unity **Profiler**
  * Memory Profiler: A tool that provides in-depth memory performance analysis
  * Profile Analyzer: Compare two profiling datasets together to analyze how your changes affect your application’s performance.
  * Frame Debugger: A tool that provides a way to measure the graphical performance of your application.

### Third party profiling tools

Alongside the Unity Profiler, use platform-specific profilers to ensure that your application runs as expected. The following list provides some examples of available profiling tools. You can also use Unity’s low level native plug-in Profiler API to export profiling data to third-party profiling tools.

  * **Android:**
    * General Android GPU profiling: Google’s Android GPU Inspector, if you have a device that supports it.
    * Arm CPU: Streamline from Arm Mobile Studio.
    * Arm Mali GPU: Use the tools from Arm Mobile Studio for GPU and system profiling.
    * Imagination PowerVR GPU: PVRTune for GPU profiling.
    * Qualcomm chips: Snapdragon Profiler for GPU and system profiling.
  * **macOS and iOS** : 
    * Xcode
    * Xcode GPU Frame Capture
  * **PC:**
    * AMD uProf
    * Intel GPA
    * NVIDIA Nsight Graphics
    * PIX on Windows
    * Superluminal
    * VTune
    * Windows Performance Analysis Toolkit
    * Visual Studio graphics debugger
    * RenderDoc
    * Radeon Developer Tool Suite
    * GPU Driver Instruments

These tools have the most utility on platforms that can use IL2CPP to produce a C++ version of the project. These native-code versions provide transparent call stacks and high-resolution method timings that are unavailable when running under Mono.