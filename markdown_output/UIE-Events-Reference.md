---
title: "Event reference"
category: "General"
source_file: "UIE-Events-Reference.html"
doc_type: "manual"
---

# Event reference

UI Toolkit raises an event when a user interacts with and changes the state of elements from **UI** Toolkit. The event design is similar to the Event interface for HTML elements.

Event types fit into a hierarchy based on the EventBase class. Each event family implements an interface that defines the common characteristics of all events of the same family. For example, `BlurEvent` and `FocusEvent` use the FocusEventBase class.

Select any of the event types listed below for more information on the event, its parent class, and links to the API documentation.

Topic | Description  
---|---  
Capture events | Events that capture the user’s interaction with the UI.  
Change events | Events that occur when the user changes the state of an element.  
Click events | Events that occur when the user clicks an element.  
Command events | Events that occur when the user invokes a command.  
Drag and drop events | Events that occur when the user drags and drops an element.  
Layout events | Events that occur when the layout engine changes the layout of an element.  
Focus events | Events that occur when the user focuses on an element.  
Input events | Events that occur when the user inputs text.  
Keyboard events | Events that occur when the user presses a key.  
Mouse events | Events that occur when the user moves the mouse.  
Navigation events | Events that occur when the user navigates through the UI.  
Panel events | Events that occur when the user interacts with a panel.  
Pointer events | Events that occur when the user interacts with a pointer device.  
Tooltip events | Events that occur when the user interacts with a tooltip.  
Transition events | Events that inform you of changes to the state of transition.  
ContextualMenu events | Events that occur when the user interacts with a contextual menu.  
IMGUI events | Events that occur when the user interacts with an IMGUI element.  
  
## Additional resources

  * Dispatch events
  * Handle events
  * Synthesize and send events