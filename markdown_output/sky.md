---
title: "Sky"
category: "General"
source_file: "sky.html"
doc_type: "manual"
---

# Sky

A sky is a type of background that a **Camera** draws before it renders a frame. This type of background greatly benefits 3D games and applications because it provides a sense of depth and makes the environment seem much larger than it actually is. The sky itself can contain anything, such as clouds, mountains, buildings, and other unreachable objects, to create the illusion of distant three-dimensional surroundings. Unity can also use a sky to generate realistic ambient lighting in your **Scene** draws before it renders a frame. This type of background greatly benefits 3D games and applications because it provides a sense of depth and makes the environment seem much larger than it actually is. The sky itself can contain anything, such as clouds, mountains, buildings, and other unreachable objects, to create the illusion of distant three-dimensional surroundings. Unity can also use a sky to generate realistic ambient lighting in your **Scene**.

The High Definition Render Pipeline’s Physically Based Sky in the Fontainebleau demo.

## Sky and render pipelines

The sky solutions you can use depend on which render pipeline your Project uses.

**Render pipeline** | **Sky Solution**  
---|---  
**Built-in Render Pipeline** | The Built-in Render Pipeline uses a skybox Material to define a sky for Cameras to draw. You can specify the sky on a per-Scene basis and also override the sky for an individual Camera.  
  
• For information on how to set the sky on a per-Scene basis, see the Lighting window documentation.  
• For information on how to override the sky for a specific Camera, see the Skybox component documentation.  
**Universal Render Pipeline (URP)** | URP uses the same sky solution as the Built-in Render Pipeline and allows you to specify the sky on a per-Scene basis and override the sky for an individual Camera.  
  
• For information on how to set the sky on a per-Scene basis, see the Lighting window documentation.  
• For information on how to override the sky for a specific Camera, see the Skybox component documentation.  
**High Definition Render Pipeline (HDRP)** | HDRP includes its own sky solution that uses the Volume system. Each Volume can include an override to specify a type of sky to draw. Each Camera interpolates between the sky settings for every Volume that affects it and draws the result.  
  
For information on how to create a sky in HDRP, see the Visual Environment documentation.