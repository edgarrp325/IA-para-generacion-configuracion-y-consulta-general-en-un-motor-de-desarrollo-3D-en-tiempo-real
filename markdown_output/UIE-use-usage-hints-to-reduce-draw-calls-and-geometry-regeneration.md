---
title: "Use usage hints to reduce draw calls and geometry regeneration"
category: "General"
source_file: "UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html"
doc_type: "manual"
---

# Use usage hints to reduce draw calls and geometry regeneration

You can use usage hints to set how an element is used at runtime. Usage hints can reduce draw calls and avoid geometry regeneration.

You can set the usage hints in **UI** Builder, UXML, or C#. The following examples set the usage hints to `DynamicTransform`:

**UXML** :
    
    
    <ui:VisualElement usage-hints="DynamicTransform" />
    

**C#** :
    
    
    visualElement.usageHints = UsageHints.DynamicTransform;
    

The supported usage hints are:

  * `DynamicTransform`
  * `GroupTransform`
  * `MaskContainer`
  * `DynamicColor`

## Additional resources

  * `usageHints`
  * `VisualElement.usageHints`