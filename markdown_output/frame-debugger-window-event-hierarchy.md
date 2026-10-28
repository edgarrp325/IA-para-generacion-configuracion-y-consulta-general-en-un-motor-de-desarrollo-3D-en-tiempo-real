---
title: "Frame Debugger Event Hierarchy"
category: "General"
source_file: "frame-debugger-window-event-hierarchy.html"
doc_type: "manual"
---

# Frame Debugger Event Hierarchy

The Event Hierarchy panel in the Frame Debugger window displays the sequence of rendering events that constitute the frame. The panel organizes the events into a hierarchy so you can see where each event originates from.

The Event Hierarchy for the URP template scene.

To view information about an event, select the event in the Event Hierarchy. When you select an event:

  * The Frame Debugger displays information about the event in the event information panel.
  * Unity processes events up to and including the selected event and displays the result in the Game view.
  * If there is a single **GameObject** associated with the event, you can double click or CTRL + click the event to highlight the GameObject in the Hierarchy. If the event represents a batch that contains multiple GameObjects, Unity doesn’t highlight the GameObjects.

For more information, see Frame Debugger.

## Hierarchy search bar

The search bar at the top of the Event Hierarchy can filter events by name. Use it to quickly find specific events by name.

Event hierarchy search bar