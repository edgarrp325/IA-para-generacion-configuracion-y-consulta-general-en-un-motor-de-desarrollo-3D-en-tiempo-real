---
title: "Using Terrain at runtime"
category: "General"
source_file: "terrain-Runtime.html"
doc_type: "manual"
---

# Using Terrain at runtime

The **Terrain** system uses dedicated Unity engine resources to function correctly. Unity includes these resources in your application at build time when you have at least one Terrain instance in a **scene** system uses dedicated Unity engine resources to function correctly. Unity includes these resources in your application at build time when you have at least one Terrain instance in a **scene** that’s part of your build settings.

If your application only creates Terrain instances at runtime, make sure you include at least one Terrain component as a placeholder in a scene listed by your build settings. Unity detects the placeholder and includes the required resources at build time.

> **Tip:** If you’re not using the placeholder in your application, you can hide it. Either deactivate the GameObject that contains the Terrain component or put this GameObject in a scene that your application doesn’t load.