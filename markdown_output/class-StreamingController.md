---
title: "Streaming Controller component"
category: "General"
source_file: "class-StreamingController.html"
doc_type: "manual"
---

# Streaming Controller component

Switch to Scripting

The Streaming Controller component is part of the Mipmap Streaming system.

Use the **Streaming Controller** component to enable Mipmap Streaming for a Camera in your scene when the the **Add All Cameras** setting in Quality settings (**Edit** > **Project Settings** > **Quality**) is disabled. You can also use it to change the mipmap bias setting per-Camera.

This component takes the location and **Camera** settings (such as **Field of View**) directly from the Camera component.

If the Camera is disabled, Unity does not calculate Mipmap Streaming for it, unless the Streaming Controller is enabled and in the preloading state. When the Streaming Controller and associated Camera are enabled, or if the Streaming Controller is in a preloading state, then Unity calculates Mipmap Streaming for this Camera. If the Streaming Controller is disabled, then Unity does not calculate Mipmap Streaming for this Camera.

The Mipmap Streaming Controller component **Property** | **Description**  
---|---  
**Mip Map Bias** | Use this setting to force Unity to load a smaller or larger mipmap level than the one that the Mipmap Streaming system has automatically chosen. Enter a value in this field to set the offset that Unity applies to this mipmap level. Unity adds this offset to all the mipmaps assigned to Textures that are in the Camera’s view.   
  
For example, if Unity loads a texture at mipmap level 1 and the **Mip Map Bias** is set to 1, this means it will load mipmap level 2 instead.  
  
To control this setting using the API, use StreamingController.streamingMipmapBias.  
  
StreamingController