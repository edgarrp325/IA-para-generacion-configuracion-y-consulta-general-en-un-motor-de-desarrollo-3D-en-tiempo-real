---
title: "Audio Low Pass Filter"
category: "General"
source_file: "class-AudioLowPassFilter.html"
doc_type: "manual"
---

# Audio Low Pass Filter

Switch to Scripting

The **Audio Low Pass Filter** passes low frequencies of an AudioSource or all sound reaching an AudioListener while removing frequencies higher than the **Cutoff Frequency**.

## Properties

**_Property:_** | **_Function:_**  
---|---  
**Cutoff Frequency** | Lowpass cutoff frequency in Hertz (range 0.0 to 22000.0, default = 5000.0).  
**Lowpass Resonance Q** | Lowpass resonance quality value (range 1.0 to 10.0, default = 1.0).  
  
## Details

The **Lowpass Resonance Q** (short for Lowpass Resonance Quality Factor) determines how much the filter’s self-resonance is dampened. Higher lowpass resonance quality indicates a lower rate of energy loss, that is the oscillations die out more slowly.

The **Audio Low Pass Filter** has a Rolloff curve associated with it, making it possible to set **Cutoff Frequency** over distance between the AudioSource and the AudioListener.

Sounds propagates very differently given the environment. For example, to compliment a visual fog effect add a subtle low-pass to the **Audio Listener**. The high frequencies of a sound being emitted from behind a door will be filtered out by the door and so won’t reach the listener. To simulate this, simply change the Cutoff Frequency when opening the door.

AudioLowPassFilter