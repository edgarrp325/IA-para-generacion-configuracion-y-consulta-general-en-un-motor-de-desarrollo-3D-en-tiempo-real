---
title: "Procedural skybox"
category: "General"
source_file: "shader-skybox-procedural.html"
doc_type: "manual"
---

# Procedural skybox

The Procedural **skybox** **Shader** **Shader** does not require any input Textures and instead generates a skybox purely from the properties set in the Material **Inspector** does not require any input Textures and instead generates a skybox purely from the properties set in the Material **Inspector**.

For information on how to create a Material that uses this skybox Shader, as well as details on how to render the skybox in your **Scene** , see Using skyboxes.

## Render pipeline compatibility

**Feature** | **Built-in**Render Pipeline**** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)**  
---|---|---|---  
**Procedural skybox** | Yes | Yes | No  
  
## Properties

**Property** | **Description**  
---|---  
**Sun** | The method Unity uses the generate a sun disk in the skybox. The options are:  
• **None:** Disables the sun disk in the skybox.  
• **Simple:** Draws a simplified sun disk into the skybox  
• **High Quality:** Draws a sun disk into the skybox. This is similar to the **Simple** sun disk, but with this mode, you can use **Sun Size Convergence** to further customize the appearance of the sun disk.  
**Sun Size** | The size modifier for the sun disk. Larger values make the sun disk appear larger and setting this value to **0** makes the sun disk disappear.  
**Sun Size Convergence** | The size convergence of the sun. Smaller values make the sun disk appear larger. This property only appears if you set **Sun** to **High Quality**.  
**Atmosphere Thickness** | The density of the atmosphere. An atmosphere of higher density absorbs more light. Unity uses the Rayleigh scattering method to absorb light.  
**Sky Tint** | The color to tint the sky to.  
**Ground** | The color of the ground (the area below the horizon).  
**Exposure** | Adjusts the sky’s exposure. This allows you to change tonal values in the skybox this Material generates. Larger values produce a more exposed, seemingly brighter, skybox. Smaller values produce a less exposed, seemingly darker, skybox.  
  
## Positioning the sun

If you choose to render a sun disk in your skybox (see **Sun** in Properties), this Shader uses the rotation of the active Light to position the sun in the skybox. To find the active Light:

  1. Open the Lighting window (menu: **Window > Rendering > Lighting**).
  2. Navigate to the **Environment** tab.
  3. The Light assigned to **Sun Source** is your Scene’s active Light.
  4. If there is no Light assigned to **Sun Source** , assign the Light in your Scene you want to become the active Light to **Sun Source**.

You can use this behaviour to create a simple day-night cycle. To do this, continuously rotate your main Directional Light around a particular axis.