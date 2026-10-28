---
title: "Synthesize and send events"
category: "General"
source_file: "UIE-Events-Synthesizing.html"
doc_type: "manual"
---

# Synthesize and send events

Before you synthesize and send custom events, understand how the UI Toolkit event system allocates and sends operating system events. 

The event system uses a pool of events to avoid allocating event objects repeatedly. To synthesize and send your own events:

  1. Get an event object from the pool of events.
  2. Fill in the event properties.
  3. Enclose the event in a `using` block to ensure it’s returned to the event pool.
  4. Pass the event to `panel.visualTree.SendEvent()`.

You can send operating system events, such as keyboard and mouse events. To do so, use a `UnityEngine.Event` to initialize the **UI** Toolkit event. 

The following example demonstrates how to synthesize and send events: 
    
    
    void SynthesizeAndSendKeyDownEvent(IPanel panel, KeyCode code,
         char character = '\0', EventModifiers modifiers = EventModifiers.None)
    {
        // Create a UnityEngine.Event to hold initialization data.
        var evt = new Event() {
            type = EventType.KeyDownEvent,
            keyCode = code,
            character = character,
            modifiers = modifiers
        };
    
        using (KeyDownEvent keyDownEvent = KeyDownEvent.GetPooled(evt))
        {
            panel.visualTree.SendEvent(keyDownEvent);
        }
    }
    
    

**Note** : Don’t send events that don’t come from the operating system and can’t be found in the `UnityEngine.Event` types. Some events are sent by UI Toolkit as a reaction to internal state changes and must not be sent by external processes. For example, if you send `PointerCaptureEvent`, visual elements assume that the underlying conditions for that event are met and won’t set pointer capture for them. This might break the internal configurations of the **visual element** and cause undefined behaviors.

## Additional resources

  * Dispatch events
  * Handle events
  * Events reference