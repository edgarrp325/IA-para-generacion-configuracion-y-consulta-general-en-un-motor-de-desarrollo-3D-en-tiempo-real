---
title: "Shadow mapping"
category: "General"
source_file: "shadow-mapping.html"
doc_type: "manual"
---

# Shadow mapping

Unity uses a technique called shadow mapping to render real-time shadows.

## How shadow mapping works

Shadow mapping uses textures called shadow maps. Shadow maps are similar to depth textures. A Light generates a shadow map in a similar way to how a **Camera** generates a depth texture. If you imagine a Camera at the same location as the Light, the areas of the **Scene** generates a depth texture. If you imagine a Camera at the same location as the Light, the areas of the **Scene** that the Camera cannot see are the same areas of the Scene that rays from the Light cannot reach; therefore, they are in shadow.

Unity populates the shadow map with information about how far rays from the Light travel before they hit a surface, and then samples the shadow map to calculate real-time shadows for **GameObjects** that the Light hits.

For more information on shadow mapping, see the Wikipedia Page on shadow mapping.

## Shadow map resolution

To calculate the resolution of a shadow map, Unity:

  1. Determines the area of the screen view that the Light can illuminate. For directional lights, the whole screen can be illuminated. For Spot Lights and Point Lights, the area is the onscreen projection of the shape of the light’s extent: a sphere for point lights, or a cone for Spot Lights. The projected shape has a width and height in pixels on the screen; the larger of those two values is then taken. This value is called the Light’s **pixel** size.

  2. Determines the shadow quality multiplier. Unity uses the **Shadow Resolution** setting for this, which is set in the Quality Settings window). The quality settings correspond to the following values: 
     * Very High: 1.0
     * High: 0.5
     * Medium: 0.25
     * Low: 0.125
  3. Performs the following calculation, and then clamps the result to the maximum size:

**Light type:** | **Formula:** | **Maximum resolution, in pixels:**  
---|---|---  
Directional |  NextPowerOfTwo (pixel size * shadow quality multiplier * 3.8) | 4096 x 4096 when Shadow Resolution is Very High Quality and/or if the GPU has 512MB or more of RAM, 2048 x 2048 otherwise.  
Spot Lights |  NextPowerOfTwo (pixel size * shadow quality multiplier * 2.0) | 2048 x 2048 if the GPU has 512MB or more of RAM, 1024 x 1024 otherwise.  
Point Lights |  NextPowerOfTwo (pixel size * shadow quality multiplier * 1.0) | 1024 x 1024 if the GPU has 512MB or more of RAM, 512 x 512 otherwise.  
  
Point lights have a lower limit on size than the other types because they use cubemaps for shadows. This means that six **cubemap** faces at this resolution must be kept in video memory at once. They are also quite expensive to render, as potential shadow casters might need to be rendered into all six cubemap faces.

### Overriding the shadow map resolution

In the Built-in **Render Pipeline** , you can set the resolution of a Light’s shadow map by setting the Light.shadowCustomResolution property to a value greater than 0. When this value is greater than 0, Unity performs the following calculation for all Light types:

NextPowerOfTwo (shadowCustomResolution)

It then clamps the maximum resolution based on Light type and hardware, as shown in the table above.

See render pipeline feature comparison for more information about support for shadow mapping across render pipelines.