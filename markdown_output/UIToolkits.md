---
title: "User interface (UI)"
category: "General"
source_file: "UIToolkits.html"
doc_type: "manual"
---

# User interface (UI)

Unity provides three **UI** systems that you can use to create user interfaces (UI) for the Unity Editor and applications made in the Unity Editor:

  * UI Toolkit
  * The Unity UI package (uGUI)
  * IMGUI

This page provides an overview of each.

## UI Toolkit

UI Toolkit is the newest UI system in Unity. It’s designed to optimize performance across platforms, and is based on standard web technologies. You can use UI Toolkit to create extensions for the Unity Editor, and to create runtime UI for games and applications.

UI Toolkit includes:

  * A retained-mode UI system that contains the core features and functionality required to create user interfaces.
  * UI Asset types inspired by standard web formats such as HTML, XML, and CSS. Use them to structure and style UI.
  * Tools and resources for learning to use UI Toolkit, and for creating and debugging your interfaces.

Unity intends for UI Toolkit to become the recommended UI system for new UI development projects, but it is still missing some features found in Unity UI (uGUI) and IMGUI.

## The Unity UI (uGUI) package

The Unity User Interface (Unity UI) package (also called uGUI) is an older, GameObject-based UI system that you can use to develop runtime UI for games and applications. In Unity UI, you use components and the Game view to arrange, position, and style the user interface. It supports advanced rendering and text features.

See the Unity UI package documentation for the manual and API reference.

## IMGUI

Immediate Mode Graphical User Interface (IMGUI) is a code-driven UI Toolkit that uses the `OnGUI` function, and **scripts** that implement it, to draw and manage user interfaces. You can use IMGUI to create custom **Inspectors** for script components, extensions for the Unity Editor, and in-game debugging displays. It is not recommended for building runtime UI.

## Choosing a UI system for your project

Unity intends for UI Toolkit to become the recommended UI system for new UI development projects, but it is still missing some features found in Unity UI (uGUI) and IMGUI. These older systems are better in certain use cases, and are required to support legacy projects.

Your choice of UI system for a given project depends on the kind of UI you plan to develop, and the features you need support for.

For a comparison of the available UI systems, see the Comparison of UI systems in Unity.