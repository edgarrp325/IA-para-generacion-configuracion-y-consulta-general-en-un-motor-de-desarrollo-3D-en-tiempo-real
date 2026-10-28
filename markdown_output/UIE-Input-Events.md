---
title: "Input events"
category: "General"
source_file: "UIE-Input-Events.html"
doc_type: "manual"
---

# Input events

The `InputEvent` is sent when the user submits text into a text field. This event updates when there is a change in focus, such as a `PointerCaptureOutEvent` that on a touch screen.

For default keyboard inputs, the `inputEvent` fires for each keystroke. `InputEvent` doesn’t fire when the TextField populates from an indirect source, such as an automated script.

**Event** | **Description** | **Trickles down** | **Bubbles up** | **Cancellable**  
---|---|---|---|---  
InputEvent | Sent when data is input to a **visual element** , typically a control. |  |  |   
  
## Unique properties

**`previousData`** : The former data.

**`newData`** : The new data.

## Event list

### InputEvent

Event sent when data is input to visual elements that implement TextInputBaseField. This event differs from `ChangeEvent` in that it’s sent for every input event in the control, even if the value of the control hasn’t changed.

**`target`** : The element where the input occurred.