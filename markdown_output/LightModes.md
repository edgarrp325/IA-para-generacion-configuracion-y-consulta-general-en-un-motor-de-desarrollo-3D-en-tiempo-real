---
title: "Light Modes"
category: "General"
source_file: "LightModes.html"
doc_type: "manual"
---

# Light Modes

This page contains information about the **Mode** property of a Light component. The **Mode** property of a Light defines its intended use.

The Modes are:

  * Baked: Unity pre-calculates the illumination from **Baked** Lights before runtime, and does not include them in any runtime lighting calculations. For more information, see Baked Lights
  * Realtime: Unity calculates and updates the lighting of **Realtime** Lights every frame at runtime. Unity does not precompute any calculations for Realtime Lights. For more information, see Realtime Lights
  * Mixed: Unity performs some calculations for Mixed Lights in advance, and some calculations at runtime. For more information, see Mixed Lights

## Setting the Mode property of a Light

To assign a **Mode** , select the Light in your **Scene** and, in the Light Inspector window, select **Mode**.