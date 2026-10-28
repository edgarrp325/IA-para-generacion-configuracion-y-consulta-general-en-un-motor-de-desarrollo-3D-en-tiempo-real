---
title: "Lighting Mode"
category: "General"
source_file: "lighting-mode.html"
doc_type: "manual"
---

# Lighting Mode

This section describes the effect of the **Lighting Mode** property of a Lighting Settings Asset.

The Lighting Mode determines the behavior of all Mixed Lights in all **Scenes** that use the Lighting Settings Asset. The available modes are:

  * Baked Indirect combines real-time direct lighting with baked indirect lighting. This mode provides real-time shadows with real-time shadowmaps. This Lighting Mode offers realistic lighting and reasonable shadow fidelity, and is suitable for mid-range hardware.
  * Shadowmask combines real-time direct lighting with baked indirect lighting. It supports baked shadows for distant **GameObjects** combines real-time direct lighting with baked indirect lighting. It supports baked shadows for distant **GameObjects** (with Shadow masks) and blends them automatically with real-time shadows (Shadow maps). Shadowmask Lighting Mode is the most realistic and the most resource-intensive Lighting Mode. You can use Quality Settings to configure its performance and visual fidelity. This Lighting Mode is suitable for high-end or mid-range hardware.
  * Subtractive provides baked direct and indirect lighting. It renders direct real-time shadows for one Directional Light only. This Lighting Mode doesn’t provide particularly realistic lighting results, and is suitable for stylized art or low-end hardware.

## Setting a Scene’s Lighting Mode

  1. Select the Lighting Settings Asset for the Scene.
  2. In the **Inspector** , navigate to **Mixed Lighting**.
  3. Use the drop-down menu to set the **Lighting Mode**.