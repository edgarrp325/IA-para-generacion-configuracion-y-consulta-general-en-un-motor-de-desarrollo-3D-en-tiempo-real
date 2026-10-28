---
title: "Skybox component reference"
category: "General"
source_file: "class-Skybox.html"
doc_type: "manual"
---

# Skybox component reference

Switch to Scripting

The **Skybox** component overrides the skybox that Cameras on the same **GameObject** draw. It gives you control over what skybox a **Camera** draw. It gives you control over what skybox a **Camera** renders and is useful when you have multiple Cameras in your **Scene** renders and is useful when you have multiple Cameras in your **Scene** and want to draw different skyboxes depending on the Camera.

## Render pipeline compatibility

**Feature** | **Built-in**Render Pipeline**** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)**  
---|---|---|---  
**Skybox component** | Yes (1) | Yes (1) | No (2)  
  
**Notes** :

  1. The Built-in Render Pipeline, and the Universal Render Pipeline (URP) both support this component.
  2. The High Definition Render Pipeline (HDRP) does not support this component and instead includes multiple sky generation solutions.

## Properties

**Property** | **Description**  
---|---  
**Custom Skybox** | The skybox that Cameras draw if they are on the same GameObject as this component. The Material you assign to this property should use a skybox Shader.  
  
Skybox