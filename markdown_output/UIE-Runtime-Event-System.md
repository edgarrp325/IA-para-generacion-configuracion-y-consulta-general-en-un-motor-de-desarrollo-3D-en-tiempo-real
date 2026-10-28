---
title: "Runtime UI event system"
category: "General"
source_file: "UIE-Runtime-Event-System.html"
doc_type: "manual"
---

# Runtime UI event system

UI Toolkit uses an **event system** to handle input and send events to all active panels.

The **UI** Toolkit’s event system can receive events from IMGUI and the legacy **Input Manager** Toolkit’s event system can receive events from IMGUI and the legacy **Input Manager**. Navigation events are created from axes defined in the legacy Input Manager. Other events come from the IMGUI event queue.

Except in specific instances, you don’t need to add a component to the **scene** to use the event system.

## Event system with multiple Panel Settings assets

If the Scene uses more than one Panel Settings asset, the event system sends pointer events to their panels according to their **Sort Order**. A pointer event propagates through the panels until a panel reacts to it.

The first panel that uses an event to affect the focused element becomes the focused panel for the event system. That panel continues to receive keyboard events until another event causes a different panel to become the focused panel.

**Note** : Stopping an event’s propagation and giving an element focus are two separate things. For example, when you click a button, it stops the propagation and allows only the button to react to being pressed, but it doesn’t prevent the other default actions for the click, such as giving focus to the button or, in general, any focusable element that is clicked.

## Use uGUI with UI Toolkit

You can use UI Toolkit UI Documents and uGUI components at the same time. 

When you add your first uGUI element in the Scene, an **Event System** and a **Standalone Input Module** are automatically added to the Scene:

  * The **Event System** allows uGUI objects to respond to events.
  * The **Standalone Input Module** dispatches events to UI Toolkit elements.

The Event System reads the scene and executes events, whereas the Standalone Input Module interprets the input and requests event execution. You can replace the Standalone Input Module with other input modules. Other input modules change what input is consumed, but all events still go through the Event System to execute.

UI Toolkit uses the sorting order of the Panel and compares it with the sorting order of uGUI canvases and other valid raycast targets, to decide whether pointer events should be sent to a UI Toolkit element or to a uGUI object, or to something else in the scene. Similarly, UI Toolkit sets the Event System’s `currentSelectedGameObject` to make sure that when a UI Toolkit panel wants to get focus, it removes the focus from other uGUI objects, and when a uGUI object becomes selected, UI Toolkit panels automatically lose their focus.

To add the event system manually, select **GameObject** > **UI** > **Event System**.

## Use the event system and the input system with UI Toolkit

When you use UI Toolkit (and uGUI) with different input systems, you need to choose different input module and event system.

The following table describes the required components and settings for each input system usage:

**Usage** | **Required components** | **Active Input Handling**  
---|---|---  
**UI Toolkit elements with legacy Input Manager** | Uses the default event system. No scene component is required. |  **Input Manager (Old)**.  
**UI Toolkit elements with Input System package** | An **Input System UI Input Module** and an **Event System** components. | **Input System Package (New)**  
**UI Toolkit elements and uGUI components with legacy Input Manager** | A **Standalone Input Module** and an **Event System** components. |  **Input Manager (Old)** or **Both**.  
**UI Toolkit elements and uGUI components with Input System package** | An **Input System UI Input Module** and an **Event System** components. |  **Input System Package (New)** or **Both**  
  
_You can find the**Active Input Handling** setting in **Edit** > **Project Settings** > **Player** > **Active Input Handling**._

## Use Input System package

You can use UI Toolkit with the **Input System** package:

  1. Use the **Package Manager** to install the **Input System** package.
  2. Select **Edit** > **Project Settings** > **Player**.
  3. Set **Active Input Handling** to **Input System Package (New)**.
  4. Select **GameObject** > **UI** > **Event System**. This adds an **Event System** **GameObject** that includes a **Standalone Input Module** in the Scene. The module shows an error message along with a button in the **Inspector** that includes a **Standalone Input Module** in the Scene. The module shows an error message along with a button in the **Inspector** window.
  5. Select **Replace with InputSystemUIInputModule** to replace the **Standalone Input Module** with the **Input System UI Input Module**. The **Input System UI Input Module** and its accompanying **Event System** allows the events of both UI Toolkit and uGUI elements to be dispatched correctly.

## Additional resources

  * Input System
  * uGUI
  * Get started with runtime UI
  * Render UI in the Game view
  * Panel Settings properties
  * FAQ for input and event systems with UI Toolkit