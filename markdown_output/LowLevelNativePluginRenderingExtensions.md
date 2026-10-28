---
title: "Low-level native plug-in rendering extensions"
category: "General"
source_file: "LowLevelNativePluginRenderingExtensions.html"
doc_type: "manual"
---

# Low-level native plug-in rendering extensions

On top of the low-level native plug-in interface, Unity also supports low level rendering extensions that can receive callbacks when certain events happen. This is mostly used to implement and control low-level rendering in your **plug-in**

Due to the low-level nature of this extension the plug-in might need to be preloaded before the devices get created. Currently the convention is name-based; the plug-in name must begin _GfxPlugin_ (for example: _GfxPluginMyNativePlugin_).

The rendering extension definition exposed by Unity is in the file _IUnityRenderingExtensions.h_ , provided with the Editor (see file path _Unity\Editor\Data\PluginAPI_).

All platforms supporting **native plug-ins** support these extensions.

## Rendering extensions API

To take advantage of the rendering extension, a plug-in should export _UnityRenderingExtEvent_ and optionally _UnityRenderingExtQuery_. There is a lot of documentation provided inside the include file.

## plug-in callbacks on the rendering thread

A plug-in gets called via _UnityRenderingExtEvent_ whenever Unity triggers one of the built-in events. The callbacks can also be added to CommandBuffers via CommandBuffer.IssuePluginEventAndData or CommandBuffer.IssuePluginCustomBlit from **scripts**

* * *

  * New feature in Unity 2017.1 NewIn20171

  * 2017–07–04 Page published