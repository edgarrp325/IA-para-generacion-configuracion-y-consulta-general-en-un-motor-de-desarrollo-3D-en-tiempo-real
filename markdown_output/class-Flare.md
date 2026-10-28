---
title: "Flare asset"
category: "General"
source_file: "class-Flare.html"
doc_type: "manual"
---

# Flare asset

Switch to Scripting

A Flare asset allows you to create and configure the appearance of lens flares. Lens flares simulate the effect of lights refracting inside a camera lens. Use them to represent bright lights or to add a bit more atmosphere to your **Scene**.

**Note:** This workflow is compatible only with the Built-in **Render Pipeline**. For similar functionality in other render pipelines, see Lens flares and halos.

## Using Flare assets

  1. Assign the Flare asset to a Light component or a Lens flare component. 
     * If you assign it to the **Flare** property of a Light component, Unity automatically tracks the position and direction of the Light and uses those values to configure the appearance of the lens flare.
     * If you assign it to the **Flare** property of a Lens flare component, you can use the Lens Flare component to configure additional values for more precise control.
  2. If you want a Camera to see lens flares, attach a Flare Layer component to the Camera’s **GameObject** to see lens flares, attach a Flare Layer component to the Camera’s **GameObject**.
  3. To see the lens flare effect in the **Scene View** , enable the Effect toggle in the Scene View **toolbar** , enable the Effect toggle in the Scene View **toolbar** and, in the drop-down, enable **Flares**.

## Flare Inspector reference

Flares work by containing several Flare **Elements** on a single **Texture**. Within the Flare, you pick and choose which **Elements** you want to include from any of the Textures.

The Flare Inspector **_Property:_** | **_Function:_**  
---|---  
**Elements** | The number of Flare images included in the Flare.  
**Image Index** | Which Flare image to use from the **Flare Texture** for this Element. See the _Flare Textures_ section below for more information.  
**Position** | The Element’s offset along a line running from the containing GameObject’s position through the screen center. 0 = GameObject position, 1 = screen center.  
**Size** | The size of the element.  
**Color** | Color tint of the element.  
**Use Light Color** | If the Flare is attached to a Light, enabling this will tint the Flare with the Light’s color.  
**Rotate** | If enabled, bottom of the Element will always face the center of the screen, making the Element spin as the Lens Flare moves around on the screen.  
**Zoom** | If enabled, the Element will scale up when it becomes visible and scale down again when it isn’t.  
**Fade** | If enabled, the Element will fade in to full strength when it becomes visible and fade out when it isn’t.  
**Flare Texture** | A texture containing images used by this Flare’s **Elements**. It must be arranged according to one of the **TextureLayout** options.  
**Texture Layout** | How the individual Flare Element images are laid out inside the **Flare Texture** (see _Texture Layouts_ below for further details).  
**Use Fog** | If enabled, the Flare will fade away with distance fog. This is used commonly for small Flares.  
  
## Configuring Flare assets

A Flare consists of multiple **Elements** , arranged along a line. The line is calculated by comparing the position of the GameObject containing the Lens Flare to the center of the screen. The line extends beyond the containing GameObject and the screen center. All Flare **Elements** are strung out on this line.

For performance reasons, all **Elements** of one Flare must share the same Texture. This Texture contains a collection of the different images that are available as Elements in a single Flare. The **Texture Layout** defines how the **Elements** are laid out in the **Flare Texture**. If you use many different Flare assets, using a shared single **Flare Texture** that contains all the **Elements** will give you best rendering performance.

Lens Flares are blocked by **Colliders**. A Collider in-between the Flare GameObject and the Camera will hide the Flare, even if the Collider does not have a **Mesh Renderer**. A Collider in-between the Flare GameObject and the Camera will hide the Flare, even if the Collider does not have a **Mesh Renderer**. If the in-between Collider is marked as Trigger it will block the flare if and only if **Physics.queriesHitTriggers** is true.

To override the **shader** used for Flares, open the Graphics window and set **Lens Flares** used for Flares, open the Graphics window and set **Lens Flares** to the shader that you would like to use as the override.

## Texture Layouts

These are the options you have for different Flare **Texture Layouts**. The numbers in the images correspond to the **Image Index** property for each **Element**.

### 1 Large 4 Small

Designed for large sun-style Flares where you need one of the **Elements** to have a higher fidelity than the others. This is designed to be used with Textures that are twice as high as they are wide.

### 1 Large 2 Medium 8 Small

Designed for complex flares that require 1 high-definition, 2 medium and 8 small images. This is used in the standard assets “50mm Zoom Flare” where the two medium Elements are the rainbow-colored circles. This is designed to be used with textures that are twice as high as they are wide.

### 1 Texture

A single image.

## 2x2 grid

A simple 2x2 grid.

### 3x3 grid

A simple 3x3 grid.

### 4x4 grid

A simple 4x4 grid.

Flare