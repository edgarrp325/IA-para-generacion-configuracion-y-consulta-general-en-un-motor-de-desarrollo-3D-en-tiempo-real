---
title: "Skybox shaders"
category: "General"
source_file: "skybox-shaders.html"
doc_type: "manual"
---

# Skybox shaders

Unity provides multiple **Skybox** Shaders for you to use. Each **Shader** Shaders for you to use. Each **Shader** uses a different set of properties and generation techniques. Each Shader falls into one of the following two categories:

**Textured** : Generates a skybox from one or multiple textures. The source textures represent the view of the background from all directions. The Skybox Shaders in this category are:

  * 6 Sided.
  * Cubemap.
  * Panoramic.

**Procedural** : Does not use textures and instead uses properties on the Material to generate a skybox. The Skybox Shader in this category is:

  * Procedural.

## Render pipeline compatibility

**Feature** | **Built-in**Render Pipeline**** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)**  
---|---|---|---  
**Skybox shaders** | Yes (1) | Yes (1) | No (2)  
  
**Notes** :

  1. The Built-in Render Pipeline, and the Universal Render Pipeline (URP) both exclusively use skyboxes to render a sky. They both support all of the above Shaders.
  2. The High Definition Render Pipeline (HDRP) does not support any of the above Shaders and instead includes multiple sky generation solutions.