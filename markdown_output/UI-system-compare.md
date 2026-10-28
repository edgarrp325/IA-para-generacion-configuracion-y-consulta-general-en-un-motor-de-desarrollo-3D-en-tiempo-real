---
title: "Comparison of UI systems in Unity"
category: "General"
source_file: "UI-system-compare.html"
doc_type: "manual"
---

# Comparison of UI systems in Unity

UI Toolkit is intended to become the recommended **UI** system for your new UI development projects. However, in the current release, UI Toolkit does not have some features that Unity UI (uGUI) and Immediate Mode GUI (IMGUI) support. uGUI and IMGUI are more appropriate for certain use cases, and are required to support legacy projects.

This page provides a high-level feature comparison of UI Toolkit, uGUI, and IMGUI, and their respective approaches to UI design. 

## General consideration

The following table lists the recommended and alternative system for runtime and Editor:

**2022** | **Recommendation** | **Alternative**  
---|---|---  
**Runtime** | Unity UI | UI Toolkit  
**Editor** | UI Toolkit | IMGUI  
  
## Roles and skill sets

Your team’s skill set and comfort level with different technologies is also an important consideration.

The following table lists the recommended system for different roles:

**Roles** | **UI Toolkit** | **Unity UI  
(uGUI)** | **IMGUI** | **Skill sets**  
---|---|---|---|---  
**Programmer** | Yes | Yes | Yes | Programmers can use any game development tool or API.  
**Technical Artist** | Partial | Yes | No | Technical artists who are familiar with Unity’s GameObject-based tools and workflows are likely to be comfortable working with GameObjects, Components, and the Scene view.   
  
They might not be comfortable with UI Toolkit’s web-like approach or IMGUI’s pure C# approach.  
**UI Designer** | Yes | Partial | No | UI designers who are familiar with UI creation tools are likely to be comfortable with UI Toolkit’s document-based approach and can use the UI Builder to visually edit their UI.  
  
If they are not familiar with GameObject-based workflows, they might require help from programmers or level designers.  
  
## Innovation and development

UI Toolkit is in active development and releases new features frequently. uGUI and IMGUI are established and production-proven UI systems that are updated infrequently.

uGUI and IMGUI might be better choices if you need features that are not yet available in UI Toolkit, or you need to support or reuse older UI content.

## Runtime

uGUI is the recommended solution for the following:

  * UI positioned and lit in a 3D world
  * VFX with custom **shaders** and materials
  * Easy referencing from `MonoBehaviours`

UI Toolkit is an alternative to uGUI if you create a screen overlay UI that runs on a wide variety of screen resolutions. Consider UI Toolkit to do the following:

  * Produce work with a significant amount of user interfaces
  * Require familiar authoring workflows for artists and designers
  * Seek textureless UI rendering capabilities

### Use Cases

The following table lists the recommended system for major runtime use cases:

**2022** | **Recommendation**  
---|---  
**Multi-resolution menus and HUD in intensive UI projects** | UI Toolkit  
**World space UI and**VR**** | Unity UI  
**UI that requires customized shaders and materials** | Unity UI  
  
### In details

The following table lists the recommended system for detailed runtime features:

**2022** | **UI Toolkit** | **Unity UI**  
---|---|---  
****WYSIWYG** authoring** | Yes | Yes  
**Nesting reusable components** | Yes | Yes  
**Global style management** | Yes | No  
**Layout and Styling Debugger** | Yes | Yes  
****Scene** integration** | Yes | Yes  
**Rich text tags** | Yes | Yes*  
**Scalable text** | Yes | Yes*  
**Font fallbacks** | Yes | Yes*  
**Adaptive layout** | Yes | Yes  
**Input system support** | Yes | Yes  
**Serialized events** | No | Yes  
**Visual Scripting support** | No | Yes  
**Rendering pipelines support** | Yes | Yes  
**Screen-space (2D) rendering** | Yes | Yes  
**World-space (3D) rendering** | No | Yes  
**Custom materials and shaders** | No | Yes  
**Sprites / Sprite atlas / Sprite atlas support** | Yes | Yes  
**Dynamic texture atlas** | Yes | No  
**Textureless elements** | Yes | No  
**UI anti-aliasing** | Yes | No  
**Rectangle clipping** | Yes | Yes  
**Mask clipping** | No | Yes  
**Nested masking** | Yes | Yes  
**UI transition animations** | Yes | No  
**Integration with**Animation Clips** and Timeline** | No | Yes  
  
*_Requiresthe TextMesh Pro package_

## Editor

UI Toolkit is recommended if you create complex editor tools. UI Toolkit is also recommended for the following reasons: 

  * Better reusability and decoupling
  * Visual tools for authoring UI
  * Better scalability for code maintenance and performance

IMGUI is an alternative to UI Toolkit for the following:

  * Unrestricted access to editor extensible capabilities
  * Light API to quickly render UI on screen

### Use Cases

The following table lists the recommended system for major Editor use cases:

**2022** | **Recommendation**  
---|---  
**Complex editor tool** | UI Toolkit  
****Property drawers**** | UI Toolkit  
**Collaboration with designers** | UI Toolkit  
  
### In details

The following table lists the recommended system for detailed Editor features:

**2022** | **UI Toolkit** | **IMGUI**  
---|---|---  
**WYSIWYG authoring** | Yes | No  
**Nesting reusable components** | Yes | No  
**Global style management** | Yes | Yes  
**Layout and Styling Debugger** | Yes | No  
**Rich text tags** | Yes | Yes  
**Scalable text** | Yes | No  
**Font fallbacks** | Yes | Yes  
**Adaptive layout** | Yes | Yes  
**Default**Inspectors**** | Yes | Yes  
**Inspector: Edit custom object types** | Yes | Yes  
**Inspector: Edit custom property types** | Yes | Yes  
**Inspector: Mixed values (multi-editing) support** | Yes | Yes  
**Array and list-view control** | Yes | Yes  
**Data binding: Serialized properties** | Yes | Yes  
  
## Additional resources

  * Migrate from Unity UI (UGUI) to UI Toolkit
  * Migrate from Immediate Mode GUI (IMGUI) to UI Toolkit