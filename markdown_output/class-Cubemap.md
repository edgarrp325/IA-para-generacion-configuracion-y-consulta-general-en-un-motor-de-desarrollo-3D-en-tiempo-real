---
title: "Cubemaps"
category: "General"
source_file: "class-Cubemap.html"
doc_type: "manual"
---

# Cubemaps

Switch to Scripting

A **Cubemap** is a collection of six square textures that represent the reflections on an environment. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back).

Cubemaps are often used to capture reflections or “surroundings” of objects; for example skyboxes and environment reflections often use cubemaps.

Cubemapped skybox and reflections

## Creating Cubemaps from Textures

The fastest way to create cubemaps is to import them from specially laid out Textures. Select the Texture in the **Project window** , to see the Import Settings in the **Inspector** , to see the Import Settings in the **Inspector** window. In the Import Settings, set the **Texture Type** to **Default** , **Normal Map** or **Single Channel** , and the **Texture Shape** to **Cube**. Unity then automatically sets the Texture up as a Cubemap.

Cubemap texture import type

Several commonly-used cubemap layouts are supported (and in most cases, Unity detects them automatically).

Vertical and horizontal cross layouts, as well as column and row of cubemap faces are supported:

Another common layout is `LatLong` (Latitude-Longitude, sometimes called cylindrical). Panorama images are often in this layout:

`SphereMap` (spherical environment map) images can also be found:

By default Unity looks at the **aspect ratio** of the imported texture to determine the most appopriate layout from the above. When imported, a cubemap is produced which can be used for skyboxes and reflections:

Selecting `Glossy Reflection` option is useful for cubemap textures that will be used by Reflection Probes. It processes cubemap mipmap levels in a special way (specular convolution) that can be used to simulate reflections from surfaces of different smoothness:

Cubemap used in a Reflection Probe on varying-smoothness surface

## Legacy Cubemap Assets

Unity also supports creating cubemaps out of six separate textures. Select **Assets > Create > Legacy > Cubemap** from the menu, and drag six textures into empty slots in the inspector.

Legacy Cubemap Inspector **_Property:_** | **_Function:_**  
---|---  
**Right..Back Slots** | Textures for the corresponding cubemap face.  
**Face Size** | Width and Height of each Cubemap face in **pixels**. The textures will be scaled automatically to fit this size.  
**Mipmap** | Should mipmaps be created?  
**Linear** | Should the cubemap use linear color?  
**Readable** | Should the cubemap allow **scripts** to access the pixel data?  
  
Note that it is preferred to create cubemaps using the Cubemap texture import type (see above) - this way cubemap texture data can be compressed; edge fixups and glossy reflection convolution be performed; and **HDR** cubemaps are supported.

## Other Techniques

Another useful technique is to generate the cubemap from the contents of a Unity **scene** using a script. The Camera.RenderToCubemap function can record the six face images from any desired position in the scene; the code example on the function’s script reference page adds a menu command to make this task easy.

* * *

2018–01–31 Page amended 

Cubemap