---
title: "Precomputed lighting data"
category: "General"
source_file: "lighting-precomputed-data.html"
doc_type: "manual"
---

# Precomputed lighting data

Precomputed lighting data and baked lighting are not the same.

Baked lighting data is static. For example, the appearance of a **GameObject** can change as it moves around a **Light Probe** can change as it moves around a **Light Probe** (if that GameObject has Contribute Global Illumination enabled). However, the data in the Light Probe itself does not change. Unity can store baked lighting data in **lightmaps** , Light Probes, and **Reflection Probes** , Light Probes, and **Reflection Probes**.

Enlighten Realtime **Global Illumination** does not rely on baked lighting. Instead, it uses precomputed visibility data to speed up the process of determining how a light moving in real-time affects the surfaces that its rays can reach.

This section contains information on the following topics:

  * Generating lighting data
  * The Lighting Data Asset
  * The GI cache