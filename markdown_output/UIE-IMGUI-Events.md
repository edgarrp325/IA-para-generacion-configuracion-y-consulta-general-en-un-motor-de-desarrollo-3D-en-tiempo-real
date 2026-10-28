---
title: "IMGUI events"
category: "General"
source_file: "UIE-IMGUI-Events.html"
doc_type: "manual"
---

# IMGUI events

The IMGUI event family refers to IMGUI events that directly affect the Unity Editor, and are Editor-only events.

UI Toolkit receives its events from the IMGUI events in the Editor. If there are IMGUI events that don’t fit into other event types, they fall under the IMGUI event family. Currently, IMGUI events support mouse and keyboard inputs tailored for the Unity Editor. **UI** Toolkit runtime panels might receive events that don’t originate from IMGUI.

**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
IMGUIEvent | Sent to encapsulate IMGUI-specific events. | Yes | Yes | Yes  
  
## Event list

### IMGUIEvent

Event used to encapsulate IMGUI-specific events.