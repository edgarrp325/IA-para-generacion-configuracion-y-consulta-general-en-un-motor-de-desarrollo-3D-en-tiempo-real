---
title: "Lens Flare component"
category: "General"
source_file: "class-LensFlare.html"
doc_type: "manual"
---

# Lens Flare component

Switch to Scripting

A **Lens Flare** component displays a lens flare that is configured by a Flare asset.

You can display a Flare asset with a Light component. If you do this, Unity automatically tracks the position and direction of the Light and uses those values to configure the appearance of the lens flare.

Use this component instead to configure the values of the lens flare yourself, which gives you more precise control.

**Note:** This workflow is compatible only with the Built-in **Render Pipeline**. For similar functionality in other render pipelines, see Lens flares and halos.

## Using a Lens Flare component

  1. Create a new **GameObject** (menu bar: **GameObject > Create Empty**).
  2. In the Inspector, click **Add Component > Effects > Lens Flare**.
  3. Assign a Flare Asset to the **Flare** property.
  4. If you want a Camera to see lens flares, attach a Flare Layer component to the Camera’s GameObject.
  5. To see the lens flare effect in the **Scene View** , enable the Effect toggle in the **Scene** , enable the Effect toggle in the **Scene** View **toolbar** View **toolbar** and, in the drop-down, enable **Flares**.

Enable the Effect toggle to view lens flares in the Scene view

## Properties

**_Property:_** | **_Function:_**  
---|---  
**Flare** | The Flare asset to render.  
  
**Note** : The other properties in the Lens Flare Inspector are stored in this Flare asset. They are not stored in the Lens Flare component.  
**Color** | The color to tint the Flare to. You can use this to make the lens flare better fit the Scene’s mood.  
**Brightness** | The size and brightness the lens flare appears. If you use a very bright lens flare, make sure its direction fits with your Scene’s primary light source. Can only affect properties that Flare has enabled.  
**Fade Speed** | The speed at which Unity fades the lens flare in and out.  
**Ignore Layers** | A mask that determins which Layers can see the lens flare.  
**Directional** | Indicates whether Unity orients the Flare along the positive z-axis of the GameObject. It appears as if it was infinitely far away, and does not track the GameObject’s position, only the direction of its z-axis.  
  
LensFlare