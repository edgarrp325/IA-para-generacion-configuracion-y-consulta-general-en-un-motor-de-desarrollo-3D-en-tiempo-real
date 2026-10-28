---
title: "Optimize Metal graphics"
category: "General"
source_file: "metal-optimize.html"
doc_type: "manual"
---

# Optimize Metal graphics

Metal supports multiple optimizations that you can use to increase the performance of your application.

## Use memoryless render targets

Metal supports memoryless render targets which enables you to render to a RenderTexture without backing it up in system memory. Unity only stores the contents temporarily in the on-tile memory during rendering.

Metal supports memoryless render targets on mobile devices from iOS and tvOS 10.0, and desktop devices (including Apple silicon) from macOS 11.

## Additional resources

  * RenderTexture.memorylessMode