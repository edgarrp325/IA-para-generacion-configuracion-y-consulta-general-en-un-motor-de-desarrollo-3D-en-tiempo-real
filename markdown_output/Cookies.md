---
title: "Cookies"
category: "General"
source_file: "Cookies.html"
doc_type: "manual"
---

# Cookies

A cookie is a mask that you place on a Light to create a shadow with a specific shape or color, which changes the appearance and intensity of the Light. Cookies are an efficient way of simulating complex lighting effects with minimal or no runtime performance impact. Effects you can simulate with cookies include caustics, soft shadows, and light shapes.

To apply a cookie to a Light in Unity, assign a texture to the **Cookie** field of a a Light component.

Cookies may support different features depending on the **render pipeline** you are using. If you are using Universal Render Pipeline (URP) see the Light component reference for more information on using Cookies.

An example of baked fake caustics achieved using baked light cookies.

## Render pipeline compatibility

See render pipeline feature comparison for more information about support for cookies across render pipelines.

## Enabling and disabling baked cookies

For Projects created in Unity 2020.1 or above, baked cookies are enabled for **Baked Lights** and Mixed Lights in the Progressive **Lightmapper** and Mixed Lights in the Progressive **Lightmapper** by default. For Projects created in versions of Unity prior to 2020.1, baked cookies are disabled for Baked Lights and Mixed Lights in the Progressive Lightmapper by default. This is to provide backwards compatibility.

You can toggle whether cookies are enabled for Baked Lights and Mixed Lights in the Progressive Lightmapper in the Editor settings window.

  1. Open the Project Settings window (**Edit > Project Settings**).
  2. Choose **Editor** to open the Editor settings.
  3. Navigate to the **Graphics** section.
  4. Toggle **Enable baked cookies support**.

## Additional information

  * Unity blog post: Create high-quality light fixtures in Unity
  * Unity forum: New Feature - Baked Light Cookies

* * *

  * Support for baked light cookies added in 2020.1 NewIn20201