---
title: "Draw order"
category: "General"
source_file: "UIE-draw-order.html"
doc_type: "manual"
---

# Draw order

The draw order of elements in the **visual tree** follows a depth-first search. Child **visual elements** follows a depth-first search. Child **visual elements** appear on top of parent elements. **UI** appear on top of parent elements. **UI** Toolkit draws child elements in the order of the sibling list. The draw order is the following:

  1. The top visual element.
  2. The first child element of that visual element.
  3. The child elements of the descendant element.

The diagram below shows the draw order of a visual tree:

Visual element draw order

To change the draw order of visual elements in C#, use the following functions:

  * BringToFront()
  * SendToBack()

To change the draw order of sibling visual elements, use the following functions:

  * PlaceBehind()
  * PlaceInFront()