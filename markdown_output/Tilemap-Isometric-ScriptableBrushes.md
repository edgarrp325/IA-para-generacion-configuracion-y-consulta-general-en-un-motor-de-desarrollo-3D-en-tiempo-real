---
title: "Scriptable Brushes"
category: "General"
source_file: "Tilemap-Isometric-ScriptableBrushes.html"
doc_type: "manual"
---

# Scriptable Brushes

The GridBrushBase class has methods that you can override to handle changes in Z position. This allows you to have custom behaviours for your customised Scriptables Brushes. These methods are:

public virtual void ChangeZPosition(int change):   
Changes the Z Position of the Brush. The `change` argument is the amount that is changed by using the Hotkeys or the Z Position Inspector. 

public virtual void ResetZPosition():   
Resets the Z Position of the Brush. You define what value to reset the Z Position to.

* * *

  * Isometric Tilemaps added in 2018.3 NewIn20183