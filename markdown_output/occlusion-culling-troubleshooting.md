---
title: "Troubleshooting occlusion culling"
category: "General"
source_file: "occlusion-culling-troubleshooting.html"
doc_type: "manual"
---

# Troubleshooting occlusion culling

Solve common problems when using occlusion culling, such as incorrect culling and slow processing.

## Hidden objects aren’t being culled

### Symptom

Objects are reported as visible in the occlusion data but are visibly occluded.

### Cause

Culling in Unity operates conservatively. This means that unless the object is explicitly set as invisible, Unity will assume objects are visible.

Occlusion data represents a conservatively simplified version of the **scene** ’s occluders, meaning some of the occlusion erodes and loses detail.

### Resolution

Decrease the value of the **Smallest Occluder** parameter. This will produce higher-resolution data that is less conservative. However, culling will decrease in speed and occlusion data will increase in size.

## Visible objects are being culled

### Symptom

Objects are occluded incorrectly.

### Resolution

  * Decrease the value of the **Smallest Hole** parameter.
  * Set the **Backface Threshold** to 100.
  * Remove the **Static Occluder** flag from **GameObjects** that you don’t want occluded.

## Slow culling

### Symptom

The culling process is too slow.

### Resolution

Increase the value of the **Smallest Occluder** parameter.

## Slow baking

### Symptom

The baking process is too slow.

### Resolution

Increase the value of the **Smallest Hole** parameter.

## Large occlusion data

### Symptom

The size of the occlusion data is too large.

### Resolution

  * Decrease the value of the **Backface Threshold**.
  * Increase the value of the **Smallest Occluder** parameter.

## Baking fails

### Symptom

Baking fails with the `Failure in split phase` error.

### Cause

The initial step of the bake tries to subdivide the scene into computation tiles. The subdivision is based on the **Smallest Occluder** parameter and when the scene is large in size, too many computation tiles can be created, resulting in an out of memory error.

### Resolution

Increase the value of the **Smallest Occluder** parameter and split up the scene into smaller chunks.

## Additional resources

  * Occlusion culling
  * Occlusion culling window reference
  * Troubleshooting cameras