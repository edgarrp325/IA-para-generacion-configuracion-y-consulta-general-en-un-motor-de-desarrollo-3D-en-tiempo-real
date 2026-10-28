---
title: "Event System Manager"
category: "General"
source_file: "script-EventSystem.html"
doc_type: "manual"
---

# Event System Manager

This subsystem is responsible for controlling all the other elements that make up eventing. It coordinates which Input Module is currently active, which **GameObject** is currently considered ‘selected’, and a host of other high level **Event System** is currently considered ‘selected’, and a host of other high level **Event System** concepts.

Each ‘Update’ the Event System receives the call, looks through its Input Modules and figures out which is the Input Module that should be used for this tick. It then delegates the processing to the modules.

## Properties

**_Property:_** | **_Function:_**  
---|---  
**First Selected** | The GameObject that was selected first.  
**Send Navigation Events** | Should the EventSystem allow navigation events (move / submit / cancel).  
**Drag Threshold** | The soft area for dragging in **pixels**.  
  
Beneath the Properies table is the “Add Default Input Modules” button.

EventSystem