---
title: "Panels"
category: "General"
source_file: "UIE-panels.html"
doc_type: "manual"
---

# Panels

The panel is the parent object of a visual tree. It owns the `rootVisualElement` but itself isn’t a **visual element**. It owns the `rootVisualElement` but itself isn’t a **visual element**. A visual tree must connect to a panel for the visual elements inside a tree to render. All panels belong to either an Editor Window or a runtime UIDocument. The panel also handles focus control and event dispatching for the visual tree.

Every element in a visual tree holds a direct reference to the panel that holds the visual tree. To verify the connection of a `VisualElement` to a panel, you can test the `panel` property of this element. When the visual element isn’t connected, the test returns `null`.

## Additional resources

  * Dispatch events
  * The visual tree
  * The Panel Settings asset
  * Relative and absolute positioning C# example