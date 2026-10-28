---
title: "Introduction to lighting"
category: "General"
source_file: "LightingInUnity.html"
doc_type: "manual"
---

# Introduction to lighting

This page introduces you to how lighting works in Unity.

Lighting in Unity works by approximating how light behaves in the real world. Unity uses detailed models of how light works for a more realistic result, or simplified models for a more stylized result.

## Direct and indirect lighting

Direct light is light that is emitted, hits a surface once, and is then reflected directly into a sensor (for example, the eye’s retina or a camera). Indirect light is all other light that is ultimately reflected into a sensor, including light that hits surfaces several times, and sky light. To achieve realistic lighting results, you need to simulate both direct and indirect light.

Unity can calculate direct lighting, indirect lighting, or both direct and indirect lighting. The lighting techniques that Unity uses depends on how you configure your Project.

## Real-time and baked lighting

Real-time lighting is when Unity calculates lighting at runtime. Baked lighting is when Unity performs lighting calculations in advance and saves the results as lighting data, which is then applied at runtime. In Unity, your Project can use real-time lighting, baked lighting, or a mix of the two (called mixed lighting).

For information on configuring Light components to contribute real-time, baked, or mixed lighting, see Light Modes. 

## Global illumination

Global illumination is a group of techniques that model both direct and indirect lighting to provide realistic lighting results. Unity has two **global illumination** systems, which combine direct and indirect lighting.

The Baked Global Illumination system consists of lightmaps, Light Probes, Light Probes, and Reflection Probes, and Reflection Probes. You can bake with the Progressive **Lightmapper**. You can bake with the Progressive **Lightmapper** (CPU or GPU) or **Enlighten** (CPU or GPU) or **Enlighten** Baked Global Illumination. However, Enlighten Baked Global Illumination is deprecated and no longer visible in the user interface by default. See Lightmapping using Enlighten Baked Global Illumination for more information.

The real-time Global Illumination system is Enlighten Realtime Global Illumination.

See render pipeline feature comparison for more information about support for Lighting features across **render pipelines**