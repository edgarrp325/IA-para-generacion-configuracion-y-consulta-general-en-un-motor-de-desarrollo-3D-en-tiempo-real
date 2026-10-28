---
title: "Realtime Global Illumination using Enlighten"
category: "General"
source_file: "realtime-gi-using-enlighten.html"
doc_type: "manual"
---

# Realtime Global Illumination using Enlighten

Unity uses a middleware solution called **Enlighten** for Realtime **Global Illumination**.

By default, Realtime Lights contribute only direct lighting to a **Scene** contribute only direct lighting to a **Scene**. If you enable **Realtime Global Illumination** (Enlighten Realtime Global Illumination) in your Scene, Realtime Lights also contribute indirect lighting to a Scene.

## Render pipeline support

See render pipeline feature comparison for more information about support for Realtime Global Illumination using Enlighten across **render pipelines**

## When to use Enlighten Realtime Global Illumination

Enlighten Realtime Global Illumination (Realtime GI) is useful for Lights that change slowly and have a significant visual impact on your Scene, such as the sun moving across the sky, or a slowly pulsating light in a closed corridor. This feature is not intended for special effects or Lights that change quickly, because latency and the number of CPU cycles needed make that sort of application impractical. Enlighten Realtime Global Illumination is suitable for games targeting mid-level to high-end PC systems and consoles. Some high-end mobile devices may also be powerful enough to make use of this feature, but you should keep Scenes small and the resolution for real-time **lightmaps** low to ensure acceptable performance.

## Using Enlighten Realtime Global Illumination

To enable Enlighten Realtime Global Illumination in your Scene, open the Lighting window (menu: **Window** > **Rendering** > **Lighting**) and enable **Realtime Global Illumination**.

To disable the effect of **Realtime GI** on a specific Light, select the Light **GameObject** and, in the Light component, set the **Indirect Multiplier** to 0. This means that the Light doesn’t contribute any indirect light to the Scene.

To disable **Realtime GI** altogether, open the Lighting window (menu: **Window** > **Rendering** > **Lighting**) and uncheck **Realtime Global Illumination**.

For detailed step-by-step advice on using Enlighten Realtime Global Illumination, see the Unity tutorial on Precomputed Realtime GI.

## How Enlighten Realtime Global Illumination works

Enlighten Realtime Global Illumination splits the Scene into small surface patches and determines the degree to which these patches are visible to each other. At runtime, Enlighten Realtime Global Illumination uses this precomputed visibility information to approximate how Realtime Lights bounce in the Scene, saves the results in a set of lightmaps, and then uses these lightmaps to apply indirect lighting to the Scene. It is computationally intensive to update the lightmaps, and so the process is split across several frames. It takes Enlighten Realtime Global Illumination several frames to propagate changes to indirect lighting throughout the Scene.

## Light Probes and Enlighten Realtime Global Illumination

Note that Light Probes behave differently when you enable Enlighten Realtime Global Illumination.

In order to react to runtime changes in Scene lighting, they sample lighting iteratively at runtime.

When you disable Enlighten Realtime Global Illumination in a Scene, Light Probes only use baked lighting data. This means that they don’t react to runtime changes in Scene lighting.

## Shadows and Enlighten Realtime Global Illumination

If a Light also casts shadows, Unity renders both dynamic and static GameObjects in the Scene into the Light’s shadow map. The Material Shaders of both static and dynamic GameObjects sample this shadow map so that these GameObjects cast real-time shadows onto each other. The **Shadow Distance** setting determines the maximum distance at which shadows begin to fade out and disappear entirely, which in turn affects performance and image quality.

Enlighten Realtime Global Illumination results also include soft shadows, unless the Scene is very small. These shadows are typically more coarse-grained than what lightmapping can achieve.

To modify **Shadow Distance** settings, navigate to **Edit** > **Project Settings** > **Quality** > **Shadows**.

## Performance considerations

Enlighten Realtime Global Illumination uses a set of lightmaps to store real-time indirect bounces. For this reason, enabling it increases memory requirements, even if you are using it along with Baked Global Illumination.

The number of **shader** calculations needed to generate lighting also increases when you use Enlighten Realtime Global Illumination because it samples an additional set of lightmaps and Light Probes.

## Optimizing Enlighten Realtime Global Illumination

If Enlighten Realtime Global Illumination doesn’t respond quickly enough to changes in your Scene lighting, there are several ways to address this problem:

  * Reduce the real-time lightmap resolution to speed up calculation at runtime.
  * Increase the CPU Usage setting for **Realtime GI** in the Quality Settings window. The tradeoff is that other systems receive less CPU time to do their work. Whether this is acceptable depends on your Project. This is a per-Scene setting, so you can dedicate more or less CPU time based on the complexity of each individual Scene in your Project.

## Disabling the default environment contribution

Unity automatically generates an ambient probe and a default Reflection Probe to ensure that environment lighting affects your scene and the GameObjects in it by default.

To disable the environment contribution in the lighting result for a scene or GameObject that does not have manually created light maps and Light Probes, disable the default **Reflection Probe** and the ambient probe. For more information, see Disabling the SkyManager.