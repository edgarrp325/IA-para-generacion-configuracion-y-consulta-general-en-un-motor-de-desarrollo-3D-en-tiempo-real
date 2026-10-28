---
title: "View data persistence"
category: "General"
source_file: "UIE-ViewData.html"
doc_type: "manual"
---

# View data persistence

View data persistence preserves the view data associated with **visual elements** in the **UI** in the **UI**. View data refers to the state of the user interface that’s not part of the underlying data model of the UI. For example, view data could include the scroll position of a scroll bar or the selection of a list. 

View data persistence addresses the issue of UI view data not persisting during certain events in the Editor:

  * Domain reloads, such as when entering Play mode or changing a script
  * Window closes or reopens, such as when changing the Editor layout
  * Editor restarts

**Note** : View data persistence only works in the Editor UI.

To enable view data persistence for the elements that support it, set the view data key to a unique string within the Editor window (the `EditorWindow` type). You can set it in UI Builder, UXML, or C#:

  * In UI Builder, set the key to the **View Data Key** field in the **Attributes** section of the element’s **Inspector** panel.
  * In UXML, set the key with the `view-data-key` attribute.
  * In C#, set the key with the `viewDataKey` property.

The following elements currently support view data persistence:

  * ScrollView

  * ListView

  * Foldout

  * TreeView

  * MultiColumnListView

  * MultiColumnTreeView When you enable the view data persistence, those elements remember their internal view state:

  * For ScrollView, it remembers the scroll position.

  * For ListView, it remembers the selection. 

  * For Foldout, it remembers the expanded state.

  * For TreeView, it remembers the selection. 

  * For MultiColumnTreeView and MultiColumnListView, it remembers the selections and columns’ order, sorting and width. 

To enable view data persistence for a read-only element, set the view data key on the parent element. 

For example, a ScrollView has several read-only Scroller child elements. Each Scroller is given a view data key that’s unique within the ScrollView element. If you set a view data key for the Foldout, the Foldout has its view data persisted. Although Scrollers have keys, their view data isn’t persisted. You must set a view data key for their parent ScrollView to enable persistence. The Scrollers will combine their view data keys with the parent’s view data key to create a unique global view data key.

**Note** : Currently, the API necessary to add support for view data persistence is internal, which means you can’t enable view data persistence for your custom controls.

## Additional resources

  * `viewDataKey`