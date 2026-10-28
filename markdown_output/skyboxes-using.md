---
title: "Using skyboxes"
category: "General"
source_file: "skyboxes-using.html"
doc_type: "manual"
---

# Using skyboxes

In Unity, a **skybox** is a Material that uses a skybox **Shader** is a Material that uses a skybox **Shader**. For information on what skybox Shaders are available, see skybox Shaders.

## Render pipeline compatibility

**Feature** | **Built-in**Render Pipeline**** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)**  
---|---|---|---  
**Skyboxes** | Yes (1) | Yes (1) | No (2)  
  
**Notes** :

  1. The Built-in Render Pipeline, and the Universal Render Pipeline (URP) both exclusively use skyboxes to render a sky. These skyboxes are Materials that use a skybox Shader.
  2. The High Definition Render Pipeline (HDRP) does not support skybox Materials and instead includes multiple sky generation solutions.

## Creating a skybox Material

To create a new skybox Material:

  1. From the menu bar, click **Assets > Create > Material**.
  2. In the **Shader** drop-down, click **Skybox** then the skybox Shader you want to use.
  3. You can now fill out the properties on the Material to set up the skybox. The properties available on the Material depend on the skybox Shader the Material uses.

**Note** : Each skybox Shader has its own set of prerequisite Textures that differ in number and **Texture format**. For information on the Textures a particular skybox Shader requires, see the documentation for that skybox Shader. You can find the list of skybox Shaders and their documentation on the skybox Shaders page.

## Drawing a skybox in your Scene

After you create a skybox Material, you can render it in your **Scene**. To do this:

  1. From the menu bar, click **Window > Rendering > Lighting Settings**.
  2. In the window that appears, click the **Environment** tab.
  3. Assign the skybox Material to the **Skybox Material** property.

This draws the skybox in the background of every **Camera** in your Scene. If you instead only want to draw the skybox for a particular Camera, see Drawing a skybox for a particular Camera.

## Using a skybox Material for ambient light settings

After you create a skybox Material, Unity can use it to generate ambient lighting in your Scene. To make Unity do this:

  1. Open the Lighting window (menu: **Window > Rendering > Lighting Settings**).
  2. Assign your chosen skybox to the **Skybox Material** property.
  3. Click the **Source** drop-down and, from the list, click **Skybox**.

You can also specify when Unity updates the ambient lighting. To do this, change the **Ambient Mode**. The two values are:

  * **Realtime** : Unity constantly regenerates ambient lighting for your Scene. This is useful if you alter the skybox at run-time
  * **Baked** : Unity only generates ambient lighting for your Scene when you click the **Generate Lighting** button at the bottom of the Lighting window. This is useful if your skybox does not change during run-time because it saves computational resources.

## Drawing a skybox for a particular Camera

If you only want to draw a skybox in the background of a particular Camera, use the Skybox component. When you attach this component to a **GameObject**

  1. Select a Camera in your Scene and view it in the **Inspector** window.
  2. Click **Add Component > Rendering > Skybox**.
  3. On the Skybox component, assign the skybox Material to the **Custom Skybox** property.

## Best Practices

If your Skybox includes a sun, moon, or other light in it, set up a Directional Light that points in the same direction as the light. This makes it appear as though the light in your skybox creates shadows in your Scene. If there are multiple Directional Lights in your Scene, you can choose which Directional Light the Skybox uses. To do this:

  1. From the menu bar, click **Window > Rendering > Lighting Settings**.
  2. Click the **Scene** tab.
  3. Assign the Directional Light you want to use to the **Sun Source** property.

If you want to have fog in your Scene, match the fog color to the color of the skybox. This makes the fog blend to the color of the Scene sky. To do this:

  1. From the menu bar, click **Window > Rendering > Lighting Settings**.
  2. Click the **Environment** tab.
  3. In the **Other Settings** section, enable the **Fog** checkbox.
  4. Set the **Color** property to a color that suits your skybox. For this, you can use the ink dropper tool to select a color from the Scene.