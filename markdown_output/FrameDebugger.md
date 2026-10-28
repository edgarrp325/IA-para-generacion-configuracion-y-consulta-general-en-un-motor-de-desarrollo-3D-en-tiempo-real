---
title: "Debug frames in Unity"
category: "General"
source_file: "FrameDebugger.html"
doc_type: "manual"
---

# Debug frames in Unity

Debug frames to help identify rendering artefacts and other issues. Unity includes a dedicated Frame Debugger that can pause the application on a particular frame and display the list of rendering events that constitute the frame. The Frame Debugger can step through each event and display the graphical state of the **scene**

## Render Pipeline compatibility

**Feature** | **Built-in**Render Pipeline**** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)**  
---|---|---|---|---  
**Frame Debugger** | Yes | Yes | Yes | Yes  
  
## 3rd-party frame debugging software

If you need information about a frame that Unity’s Frame Debugger doesn’t provide, there are 3rd-party frame debugging programs that support Unity. The Unity Editor supports native launching and frame capturing for RenderDoc. You can also build a standalone Player and attach a supported frame debugger. For information about supported frame debugging software, see Profiling tools.