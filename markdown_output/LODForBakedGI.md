---
title: "Lightmaps and LOD"
category: "General"
source_file: "LODForBakedGI.html"
doc_type: "manual"
---

# Lightmaps and LOD

This page provides advice on baking light into models that use Unity’s LOD (level of detail) system.

When you use the Progressive **Lightmapper** , there is no need to place Light Probes around an **LOD** , there is no need to place Light Probes around an **LOD** Group to generate baked indirect lighting.

Enlighten Baked **Global Illumination** can only compute direct lighting for lower LODs, and the LOD system must rely on Light Probes can only compute direct lighting for lower LODs, and the LOD system must rely on Light Probes to sample indirect lighting.

Enlighten Baked Global Illumination is deprecated and no longer visible in the user interface by default. See Lightmapping using Enlighten Baked Global Illumination for more information.

If you do not place Light Probes, your lower LOD models may appear visually incorrect because they only receive direct light.

The LOD 1 and LOD 2 models here are lit incorrectly because light probes have not been placed around the model in the scene. They only show direct lighting.

To set up LOD models correctly for baked lighting, mark the LOD GameObjects as **Contribute GI**. To do this, select the **GameObject** , and at the top of the **Inspector** , and at the top of the **Inspector** window, select the drop-down menu next to the **Static** checkbox:

In this example, the LODs are assumed to be children of this GameObject

Use the Light Probes component to place Light Probes around the LOD GameObjects.

Light probes placed around an LOD model.

**Note** : Only the most detailed model affects the lighting on the surrounding geometry (for example, shadows or bounced light on surrounding buildings). In most cases this should not be a problem, because your lower level-of-detail models should closely resemble the highest level-of-detail model.