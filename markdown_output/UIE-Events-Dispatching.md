---
title: "Dispatch events"
category: "General"
source_file: "UIE-Events-Dispatching.html"
doc_type: "manual"
---

# Dispatch events

The **UI** Toolkit **event system** Toolkit **event system** listens to events, coming from the operating system or **scripts** listens to events, coming from the operating system or **scripts** , and dispatches these events to **visual elements** , and dispatches these events to **visual elements** using the EventDispatcher. The event dispatcher determines an appropriate dispatching strategy for each event it sends. Once determined, the dispatcher executes the strategy.

Visual elements implement default behaviors for several events. This can involve the creation and execution of additional events. For example, a `MouseMoveEvent` could generate an additional `MouseEnterEvent` and a `MouseLeaveEvent`. These events enter a queue and process after the current event. For example, the `MouseMoveEvent` finishes processing before the `MouseEnterEvent` and `MouseLeaveEvent` events.

## Dispatch behavior of event types

Each event type has its own dispatch behavior. The behavior of each event type breaks down into three stages:

  * **Trickles down** : Events sent to elements during the trickle down phase.
  * **Bubbles up** : Events sent to elements during the bubble-up phase.
  * **Cancellable** : Events that can have their default action execution cancelled, stopped, or prevented.

For a list of dispatch behavior for each event type, see the Event reference page.

## Event propagation

After the event dispatcher selects the event target, it computes the propagation path of the event. The propagation path is an ordered list of visual elements that receive the event. The propagation path occurs in the following order:

  1. The path starts at the root of the visual element tree and descends towards the target. This is the **trickle-down phase**.
  2. The event target receives the event.
  3. The event then ascends the tree towards the root. This is the **bubble-up phase**.

Propagation path

Most event types are sent to all elements along the propagation path. Some event types skip the bubble-up phase, and some event types are sent to the event target only.

If you hide or disable an element, it won’t receive events. Events still propagate to the ancestors and descendants of a hidden or disabled element.

As an event travels along the propagation path, `Event.currentTarget` updates to the element handling the event. Within an event callback function, there are two properties that log the dispatch behavior:

  * `Event.currentTarget` is the visual element on which the callback was registered.
  * `Event.target` is the element where the event occurs, for example the element directly under the mouse.

## Event target

The target of an event depends on the event type. For mouse events, the target is most commonly the topmost pickable element, directly under the mouse. For keyboard events, the target is the element that has focus.

UI Toolkit events have a `target` property, containing a reference to the element where the event occurred. For most events that originate from the operating system, the dispatch process finds the event target automatically.

The target element is stored in `EventBase.target` and doesn’t change during the dispatch process. The property `Event.currentTarget` updates to the visual element currently handling the event.

### Picking mode and custom shapes

Most mouse events use the picking mode to determine their target. The `VisualElement` class has a `pickingMode` property which supports the following values:

  * `PickingMode.Position` (default): performs picking based on the position rectangle.
  * `PickingMode.Ignore`: prevents picking as the result of a mouse event.

You can override the `VisualElement.ContainsPoint()` method to perform custom intersection logic.

### Capture the mouse

After a `MouseDownEvent`, some elements must capture the pointer position to ensure it receives all subsequent mouse events, even when the cursor is no longer hovering over the element. For example, when you click on a button, slider, or a scroll bar.

To capture the mouse, call `element.CaptureMouse()` or `MouseCaptureController.CaptureMouse()`.

To release the mouse, call `MouseCaptureController.ReleaseMouse()`. If another element is already capturing the mouse when you call `CaptureMouse()`, the element receives a `MouseCaptureOutEvent` and loses the capture.

Only one element in the application can have the capture at any moment. While an element has the capture, it’s the target of all subsequent mouse events except mouse wheel events. This only applies to mouse events that don’t already have a set target and rely on the dispatch process to determine the target.

For more information, see Capture events.

### Focus ring and the tab order

Each UI Toolkit panel has a focus ring that defines the focus order of elements. By default, a depth-first search (DFS) on the visual element tree determines the focus order of elements. For example, the focus order for the tree depicted below would be F, B, A, D, C, E, G, I, H.

Focus order

Some events use the focus order to determine which element holds the focus. For example, the target for a keyboard event is the element in focus.

Use the `focusable` property to control whether a visual element is focusable. By default, `VisualElements` aren’t focusable, but some subclasses, such as `TextField`, might be focusable by default.

Use the `tabIndex` property to control the focus order as follows (`tabIndex` default value of 0) :

  * If the `tabIndex` is negative, you can’t use tab on the element.
  * If the `tabIndex` is zero, the element keeps its default tab order, as determined by the focus ring algorithm.
  * If the `tabIndex` is positive, the element is placed in front of other elements that either have a zero `tabIndex` (`tabIndex = 0`) or a `tabIndex` value smaller than its own.

## Additional resources

  * Handle events
  * Synthesize and send events
  * Events reference