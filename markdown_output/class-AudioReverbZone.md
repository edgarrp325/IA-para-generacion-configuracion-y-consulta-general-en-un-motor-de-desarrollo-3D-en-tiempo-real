---
title: "Reverb Zones"
category: "General"
source_file: "class-AudioReverbZone.html"
doc_type: "manual"
---

# Reverb Zones

Switch to Scripting

**Reverb Zones** take an Audio Clip and distorts it depending where the **audio listener** and distorts it depending where the **audio listener** is located inside the reverb zone. They are used when you want to gradually change from a point where there is no ambient effect to a place where there is one, for example when you are entering a cavern.

## Properties

**_Property:_** | **_Function:_**  
---|---  
**Min Distance** | Represents the radius of the inner circle in the **gizmo** , this determines the zone where there is a gradually reverb effect and a full reverb zone.  
**Max Distance** | Represents the radius of the outer circle in the gizmo, this determines the zone where there is no effect and where the reverb starts to get applied gradually.  
**Reverb Preset** | Determines the reverb effect that will be used by the reverb zone.  
  
This diagram illustrates the properties of the reverb zone.

How the sound works in a reverb zone

## Hints

You can mix reverb zones to create combined effects.

AudioReverbZone