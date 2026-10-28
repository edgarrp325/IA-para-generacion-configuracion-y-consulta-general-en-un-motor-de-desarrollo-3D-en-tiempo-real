---
title: "Audio Parametric Equalizer Effect"
category: "General"
source_file: "class-AudioParamEQEffect.html"
doc_type: "manual"
---

# Audio Parametric Equalizer Effect

The **Audio Param EQ Effect** is used to alter the frequency response of an audio system using linear filters.

## Properties

**_Property:_** | **_Function:_**  
---|---  
**Center freq** | The frequency in Hertz where the gain is applied (range 20.0 to 22000.0, default = 8000.0 Hz).  
**Octave Range** | The number of Octaves over which the gain is applied (Centered on the Center Frequency) (range 0.20 to 5.00, default = 1.0 octave).  
**Frequency Gain** | The gain applied (range 0.05 to 3.00, default = 1.00 - no gain applied).  
  
## Details

The graph shows the effect of the gain to be applied over the frequency range of the audio output.

AudioParamEQEffect