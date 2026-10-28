---
title: "Audio Low Pass Simple Effect"
category: "General"
source_file: "class-AudioLowPassSimpleEffect.html"
doc_type: "manual"
---

# Audio Low Pass Simple Effect

The **Audio Low Pass Simple Effect** passes low frequencies of an AudioMixer group while removing frequencies higher than the **Cutoff Frequency**.

## Properties

**_Property:_** | **_Function:_**  
---|---  
**Cutoff freq** | Lowpass cutoff frequency in Hertz (range 10.0 to 22000.0, default = 5000.0).  
  
## Details

The **Resonance** (short for Lowpass Resonance Quality Factor) determines how much the filter’s self-resonance is dampened. Higher lowpass resonance quality indicates a lower rate of energy loss, that is the oscillations die out more slowly.

For additional control over the resonance value of the low pass filter use the Audio Low Pass effect.

AudioLowPassSimpleEffect