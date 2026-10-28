---
title: "Set a layerMask"
category: "General"
source_file: "layermask-set.html"
doc_type: "manual"
---

# Set a layerMask

This page explains how to set up a layerMask correctly so you can use it in API calls that use a serialized layerMask property.

## Use a serialized layerMask property

The simplest way to set a layermask in the Unity Editor is to create a property that uses Unity’s LayerMask class. If the property is `public` or uses the SerializeField attribute, Unity provides an interface in the **Inspector**
    
    
    using UnityEngine;
    
    public class LayerMaskExample : MonoBehaviour
    {
        [SerializeField] private LayerMask layermask;
    }
    

## Convert from a layer

If you want to convert a layer to a layermask in a script at runtime, use the binary left-shift operator to left-shift `1` by the layer. The result is a layermask that represents the single layer.
    
    
    using UnityEngine;
    
    public class LayerExample : MonoBehaviour
    {
        [SerializeField] private int layer = 10;
        private int layerAsLayerMask;
    
        private void Start()
        {
            layerAsLayerMask = (1 << layer);
        }
    }
    

## Additional resources

  * Add a layer to a layermask
  * Remove a layer from a layermask