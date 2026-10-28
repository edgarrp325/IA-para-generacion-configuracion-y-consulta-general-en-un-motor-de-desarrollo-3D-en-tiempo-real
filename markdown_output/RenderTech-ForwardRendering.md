---
title: "Forward rendering path"
category: "General"
source_file: "RenderTech-ForwardRendering.html"
doc_type: "manual"
---

# Forward rendering path

This page describes the Forward rendering path in Unity’s Built-in **Render Pipeline** in Unity’s Built-in **Render Pipeline**.

Forward rendering renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by **Forward Rendering** , depending on their settings and intensity.

## Implementation Details

In Forward rendering, some number of brightest lights that affect each object are rendered in fully per-pixel lit mode. Then, up to 4 point lights are calculated per-vertex. The other lights are computed as Spherical Harmonics (SH), which is much faster but is only an approximation. Whether a light will be a per-pixel light or not is dependent on this:

  * Lights that have their Render Mode set to **Not Important** are always per-vertex or SH.
  * Brightest directional light is always per-pixel.
  * Lights that have their Render Mode set to **Important** are always per-pixel.
  * If the above results in fewer lights than current **Pixel Light Count** Quality Setting, then more lights are rendered per-pixel, in order of decreasing brightness.

Rendering of each object happens as follows:

  * Base Pass applies one per-pixel directional light and all per-vertex/SH lights.
  * Other per-pixel lights are rendered in additional passes, one pass for each light.

For example, if there is some object that’s affected by a number of lights (a circle in a picture below, affected by lights A to H): 

Let’s assume lights A to H have the same color and intensity and all of them have Auto rendering mode, so they would be sorted in exactly this order for this object. The brightest lights will be rendered in per-pixel lit mode (A to D), then up to 4 lights in per-vertex lit mode (D to G), and finally the rest of lights in SH (G to H):

Note that light groups overlap; for example last per-pixel light blends into per-vertex lit mode so there are less “light popping” as objects and lights move around.

### Base Pass

Base pass renders object with one per-pixel directional light and all SH/vertex lights. This pass also adds any **lightmaps** , ambient and emissive lighting from the **shader** , ambient and emissive lighting from the **shader**. Directional light rendered in this pass can have Shadows. Note that Lightmapped objects do not get illumination from SH lights.

Note that when “OnlyDirectional” pass flag is used in the shader, then the forward base pass only renders main directional light, ambient/lightprobe and lightmaps (SH and vertex lights are not included into pass data).

### Additional Passes

Additional passes are rendered for each additional per-pixel light that affect this object. Lights in these passes by default do not have shadows (so in result, Forward Rendering supports one directional light with shadows), unless multi_compile_fwdadd_fullshadows variant shortcut is used.

## Performance Considerations

### Per-pixel lights

Per-pixel dynamic lighting adds significant rendering work to every affected **pixel** , and can lead to objects being rendered in multiple passes. Avoid having more than one **Pixel Light** illuminating any single object on less powerful devices, like mobile or low-end PC GPUs, and use lightmaps to light static objects instead of calculating their lighting every frame. Per-vertex dynamic lighting can add significant work to vertex transformations, so try to avoid situations where multiple lights illuminate a single object.

Avoid combining meshes that are far enough apart to be affected by different sets of pixel lights. When you use pixel lighting, each **mesh** has to be rendered as many times as there are pixel lights illuminating it. If you combine two meshes that are very far apart, it increase the effective size of the combined object. All pixel lights that illuminate any part of this combined object are taken into account during rendering, so the number of rendering passes that need to be made could be increased. Generally, the number of passes that must be made to render the combined object is the **sum of the number of passes for each of the separate objects** , so nothing is gained by combining meshes.

During rendering, Unity finds all lights surrounding a mesh and calculates which of those lights affect it most. The settings on the Quality window are used to modify how many of the lights end up as pixel lights, and how many as vertex lights. Each light calculates its importance based on how far away it is from the mesh and how intense its illumination is - and some lights are more important than others purely from the game context. For this reason, every light has a **Render Mode** setting which can be set to **Important** or **Not Important** ; lights marked as **Not Important** have a lower rendering overhead.

**Example** : Consider a driving game in which the player’s car is driving in the dark with headlights switched on. The headlights are probably the most visually significant light source in the game, so their **Render Mode** should be set to **Important**. There may be other lights in the game that are less important, like other cars’ rear lights or distant lampposts, and which don’t improve the visual effect much by being pixel lights. The **Render Mode** for such lights can safely be set to **Not Important** to avoid wasting rendering capacity in places where it has little benefit.

Optimizing per-pixel lighting saves both the CPU and GPU work: the CPU has fewer draw calls to do, and the GPU has fewer vertices to process and pixels to rasterize for all the additional object renders.

### Spherical Harmonics lights

Spherical Harmonics lights are _very_ fast to render. They have a tiny cost on the CPU, and are _actually free_ for the GPU to apply (that is, base pass always computes SH lighting; but due to the way SH lights work, the cost is exactly the same no matter how many SH lights are there).

The downsides of SH lights are:

  * They are computed at object’s vertices, not pixels. This means they do not support light Cookies or **normal maps**.
  * SH lighting is very low frequency. You can’t have sharp lighting transitions with SH lights. They are also only affecting the diffuse lighting (too low frequency for specular highlights).
  * SH lighting is not local; point or spot SH lights close to some surface will “look wrong”.

In summary, SH lights are often good enough for small dynamic objects.