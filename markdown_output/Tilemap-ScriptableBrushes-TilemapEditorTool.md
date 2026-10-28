---
title: "TilemapEditorTool"
category: "General"
source_file: "Tilemap-ScriptableBrushes-TilemapEditorTool.html"
doc_type: "manual"
---

# TilemapEditorTool

The `TilemapEditorTool` is an inheritable class that defines **editor tools** for the Tile Palette window. To create a new editor tool for the Tile Palette window, create a new class inheriting from `TilemapEditorTool`. Override any required methods for your new `TilemapEditorTool`class.

You can override the following methods from `TilemapEditorTool`:
    
    
    protected abstract string tooltipStringFormat { get; }
    

Define this to show the tooltip for your `TilemapEditorTool`. The shortcut for your `TilemapEditorTool`will be passed in to this and formatted for the final tooltip.

* * *
    
    
    protected abstract string shortcutId { get; }
    

Define this to assign a Shortcut Id for identifying your keyboard shortcut for your tool.

* * *
    
    
    public virtual GUIContent toolbarIcon { get; }
    

Define this to show the icon for your `TilemapEditorTool`. If this is not defined, the **toolbar** displays the **Tool Mode** icon.

* * *
    
    
    public virtual bool HandleTool(bool isHotControl, GridLayout gridLayout, GameObject brushTarget, Vector3Int gridMousePosition)
    

Override this to determine any custom behavior for handling your `TilemapEditorTool`. The following parameters are passed into the method for additional information:

Name | Function  
---|---  
**isHotControl** | Whether the tool is a hot control under `UnityGUI` (refer to GUIUtility.hotControl for more information).  
**gridLayout** | The GridLayout being handled by the Tool.  
**brushTarget** | The **GameObject** being handled by the Tool.  
**gridMousePosition** | The Grid Cell position where the mouse cursor currently is.  
  
* * *
    
    
    public override bool IsAvailable()
    

Whether your `TilemapEditorTool`can be activated at the current time. Use this to validate whether the prerequisites for activating your `TilemapEditorTool`are available.

The custom `TilemapEditorTool`can be added as a default tool in the Tile Palette using the Tile Palette Preferences or as a tool for specific Grid Brushes when your `GridBrush`has a `BrushTool`attribute with the type of your custom `TilemapEditorTool`.

* * *

TilemapEditorTool page added in 2021.2 .