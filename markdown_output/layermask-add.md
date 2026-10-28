---
title: "Add a layer to a layerMask"
category: "General"
source_file: "layermask-add.html"
doc_type: "manual"
---

# Add a layer to a layerMask

To add a layer to a layermask, use the logical OR operator on the original layermask and the layer to add.
    
    
    originalLayerMask |= (1 << layerToAdd);
    

## Additional resources

  * Set a layermask
  * Remove a layer from a layermask