---
title: "Graphic Raycaster"
category: "General"
source_file: "script-GraphicRaycaster.html"
doc_type: "manual"
---

# Graphic Raycaster

The Graphic Raycaster is used to raycast against a Canvas. The Raycaster looks at all Graphics on the canvas and determines if any of them have been hit. 

The Graphic Raycaster can be configured to ignore backfacing Graphics as well as be blocked by 2D or **3D objects** that exist in front of it. A manual priority can also be applied if you want processing of this element to be forced to the front or back of the Raycasting.

## Properties

**_Property:_** | **_Function:_**  
---|---  
**Ignore Reversed Graphics** | Should graphics facing away from the raycaster be considered?  
**Blocked Objects** | Type of objects that will block graphic raycasts.  
**Blocking Mask** | Type of objects that will block graphic raycasts.  
  
GraphicRaycaster