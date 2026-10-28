---
title: "Audio Low Pass Effect"
category: "General"
source_file: "class-AudioLowPassEffect.html"
doc_type: "manual"
---

# Audio Low Pass Effect

The **Audio Low Pass Effect** passes low frequencies of an AudioMixer group while removing frequencies higher than the **Cutoff Frequency**.

## Properties

**_Property:_** | **_Function:_**  
---|---  
**Cutoff freq** | Lowpass cutoff frequency in Hertz (range 10.0 to 22000.0, default = 5000.0).  
**Resonance** | Lowpass resonance quality value (range 1.0 to 10.0, default = 1.0).  
  
## Details

The **Resonance** (short for Lowpass Resonance Quality Factor) determines how much the filter’s self-resonance is dampened. Higher lowpass resonance quality indicates a lower rate of energy loss, that is the oscillations die out more slowly.

AudioLowPassEffect