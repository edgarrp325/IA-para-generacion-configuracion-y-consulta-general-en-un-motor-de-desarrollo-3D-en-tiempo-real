---
title: "Creating cookies for the Built-in Render Pipeline"
category: "General"
source_file: "creating-cookies-built-in-render-pipeline.html"
doc_type: "manual"
---

# Creating cookies for the Built-in Render Pipeline

The most convenient way to create a cookie for use with the Built-in **Render Pipeline**

Note that in the Built-in Render Pipeline, cookies only use data from the alpha channel. This means that you can define a shape for a cookie, but not a color.

A simple grayscale cookie for a window light The same cookie simulating light from a window

To do this:

  1. Create a grayscale texture in the image editor of your choice. If you are creating a cookie to use with a Point Light, lay your texture out as a **cubemap**. If you are creating a cookie to use with a Spot Light or Directional Light, lay your texture out as a regular 2D texture.
  2. Place the texture in your Project’s Asset folder to import the texture into Unity.
  3. In your Project view, select the Texture Asset that represents the texture. Unity displays the Texture import settings in the **Inspector**
  4. In the Inspector, set the following values: 
     * Set **Texture Type** to **Cookie**
     * Set **Light Type** to match the Type of the Light that you are creating the cookie for
     * Set **Alpha Source** to **From Gray Scale**
  5. At the bottom of the Inspector, click **Apply**. Unity applies the updated import settings to the Texture Asset.

Note that the **pixels** of a cookie does not need to be completely transparent or opaque, but can also incorporate any values in between. You can use in-between values to simulate dust or dirt in the path of the light, or to simulate caustic effects such as those produced by the ridges in a car’s headlight.

For more information on configuring the import settings for cookies in the Built-in Render Pipeline, see Texture Type: Cookie.