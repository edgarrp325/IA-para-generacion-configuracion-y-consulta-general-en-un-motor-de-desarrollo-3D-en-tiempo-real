---
title: "XR graphics"
category: "General"
source_file: "xr-graphics.html"
doc_type: "manual"
---

# XR graphics

Graphics and rendering in an **XR** app follow the same principles as they do in any Unity application, with some differences arising from the need for stereo rendering and increased efficiency.

XR apps generally require very high and consistent frame rates for user comfort. At the same time, rendering in stereo means that every visible object must be drawn twice from different perspectives. Techniques like single-pass rendering can improve rendering efficiency by reducing the duplication of effort, but also require changes to **shader** code.

Topic | Description  
---|---  
Universal Render Pipeline compatibility in XR | Understand which Universal **Render Pipeline** features are compatible with XR platforms.  
Stereo rendering | Understand stereo rendering for XR platforms.  
Foveated rendering | Learn about foveated rendering for XR.  
VR frame timing | Learn about **VR** frame timing.