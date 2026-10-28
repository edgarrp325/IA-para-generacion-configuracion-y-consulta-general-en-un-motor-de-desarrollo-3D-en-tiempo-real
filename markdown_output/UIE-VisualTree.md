---
title: "Introduction to visual elements and the visual tree"
category: "General"
source_file: "UIE-VisualTree.html"
doc_type: "manual"
---

# Introduction to visual elements and the visual tree

The most basic building block in **UI** Toolkit is a **visual element** Toolkit is a **visual element**. The visual elements are ordered into a hierarchy tree with parent-child relationships. This is called the **visual tree**.

The diagram below displays a simplified example of the visual tree, and the rendered result in UI Toolkit.

Simplified hierarchy of the visual tree

The Root in the diagram represents the `EditorWindow.rootVisualElement` in the Editor UI and the `UIDocument.rootVisualElement` in a runtime UI. 

The `VisualElement` class is the base for all nodes in the visual tree. The `VisualElement` base class contains properties such as styles, layout data, and event handlers. Visual elements can have children and descendant visual elements. For example, in the diagram above, the first `Box` visual element has three child visual elements: `Label`, `Checkbox`, and `Slider`.

You can customize the appearance of visual elements through inline styles and stylesheets. You can also use event callbacks to modify the behavior of a visual element.

`VisualElement` derives into subclasses that define additional behavior and functionality, such as controls. UI Toolkit includes a variety of built-in controls with specialized behavior. A control is an element of a graphical user interface. For example, the following items are available as built-in controls:

  * Buttons
  * Toggles
  * Text input fields

A control includes the visual of the control, and the scripted logic to operate and interact with the control. It can consist of a single visual element, or a combination of multiple visual elements. For example, the Toggle control contains three elements:

  * A text label
  * An image of a box
  * An image of a checkmark

Toggle control

The implementation of the Toggle control defines the behavior of the control. It has an internal value of whether the toggle state is true or false. This logic alternates the visibility of the checkmark image when the value changes.

You can also combine visual elements together and modify their behavior to create custom controls. 

To use a control in a UI, add it to the visual tree. 

## Additional resources

  * Structure UI with UXML
  * Structure UI with C# scripts
  * UXML elements Reference