---
title: "Remove a layer from a layerMask"
category: "General"
source_file: "layermask-remove.html"
doc_type: "manual"
---

# Remove a layer from a layerMask

To remove a layer from a layermask, use the logical AND operator on the original layermask and the bitwise complement of the layer to remove it.
    
    
    originalLayerMask &= ~(1 << layerToRemove);
    

## Additional resources

  * Set a layermask
  * Add a layer to a layermask