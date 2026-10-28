---
title: "SkyManager"
category: "General"
source_file: "using-skymanager.html"
doc_type: "manual"
---

# SkyManager

## Understanding the SkyManager

Unity includes a dedicated manager—the SkyManager—to ensure that environment lighting affects your **scene** by default. The SkyManager automatically generates an ambient probe and default reflection probe to capture environment lighting.

Unity updates these probes each time environment lighting in your scene changes, until the moment you generate lighting. After you generate lighting, Unity bakes the current environment light values into the probes.

When you specifically use the **Generate Lighting** control to manually bake your lighting, Unity stops updating the probes from that point onward and only updates them again at the next bake. If you want Unity to continue to update the probes each time the environment lighting changes, enable the **Auto Generate** option.

If you remove the Lighting Data Asset from your project, Unity continues to update the probes each time the environment lighting changes.

## Disabling the SkyManager

To prevent the environment contribution from automatically affecting the lighting result for a scene or **GameObject** that does not have manually created light maps and **Light Probes** that does not have manually created light maps and **Light Probes** , disable the default **Reflection Probe** , disable the default **Reflection Probe** and the ambient probe.

To disable these probes, navigate to **Window** > **Rendering** > **Lighting Settings** > **Environment** , then make one of the following changes:

  * Option 1: Set **Intensity Multiplier** to 0.
  * Option 2: Use a black ****Skybox** Material**.
  * Option 3: Set either the **Color** or **Gradient** for the **Source** to black.

### Disable the SkyManager for all scenes

To prevent the environment contribution from automatically affecting the lighting result for all scenes, navigate to **Window** > **Rendering** > **Lighting Settings** > **Scene** , then disable **Recalculate Environment Lighting**.