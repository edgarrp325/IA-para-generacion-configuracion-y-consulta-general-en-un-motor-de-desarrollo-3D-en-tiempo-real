---
title: "Performance consideration for runtime UI"
category: "General"
source_file: "UIE-performance-consideration-runtime.html"
doc_type: "manual"
---

# Performance consideration for runtime UI

This section describes how you can improve the performance for runtime **UI**.

**Topic** | **Description**  
---|---  
Use usage hints to reduce draw calls and geometry regeneration | Use usage hints to set how an element is used at runtime. Usage hints can reduce draw calls and avoid geometry regeneration.  
Control textures of the dynamic atlas | Use an atlas to reduce the number of batches broken by texture changes and achieve good performance.  
Platform and mesh consideration | Consider device capabilities and avoid **mesh** tessellation.  
  
## Additional resources

  * Panel Settings asset
  * `usageHints`