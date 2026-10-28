---
title: "Audio High Pass Effect"
category: "General"
source_file: "class-AudioHighPassEffect.html"
doc_type: "manual"
---

# Audio High Pass Effect

The **Highpass Effect** passes high frequencies of an AudioMixer group and cuts off signals with frequencies lower than the **Cutoff Frequency**.

## Properties

**_Property:_** | **_Function:_**  
---|---  
**Cutoff freq** | Highpass cutoff frequency in Hertz (range 10.0 to 22000.0, default = 5000.0).  
**Resonance** | Highpass resonance quality value (range 1.0 to 10.0, default = 1.0).  
  
## Details

The **Resonance** (short for Highpass Resonance Quality Factor) determines how much the filter’s self-resonance is dampened. Higher highpass resonance quality indicates a lower rate of energy loss, that is the oscillations die out more slowly.

AudioHighPassEffect