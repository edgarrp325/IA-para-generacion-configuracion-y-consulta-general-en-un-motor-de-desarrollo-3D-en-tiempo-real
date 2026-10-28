---
title: "TemplateContainer"
category: "General"
source_file: "UIE-uxml-element-TemplateContainer.html"
doc_type: "manual"
---

# TemplateContainer

The TemplateContainer is the root element of a UXML file and acts as the parent of all other elements in the file. 

A TemplateContainer instance is automatically generated for the following scenarios:

  * When you use `VisualTreeAsset.Instantiate()` in C#, a TemplateContainer instance is generated to represent the root of the hierarchy.
  * When you work with UXML templates, a TemplateContainer is generated to represent the template instance and inserted into the hierarchy of the parent UXML file.

## C# base class and namespace

## Additional resources

  * Reuse UXML files