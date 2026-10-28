---
title: "Grid snapping"
category: "General"
source_file: "GridSnapping.html"
doc_type: "manual"
---

# Grid snapping

Unity provides a visual grid in the Editor’s ****Scene** view** window, which can help precisely align **GameObjects** view window, which can help precisely align **GameObjects** by snapping (moving) them to the nearest grid location.

The same view displaying the grid lines along the x, y, and z axes

You can snap a GameObject to a grid projected along the X, Y, or Z axes in several ways:

  * Align selected GameObjects to the nearest grid point.
  * Turn on grid snapping while you move, rotate, or scale a GameObject.

You can also transform a GameObject in increments without aligning it with the gridlines. If you need to change how much you are moving, rotating, or scaling, you can change the increment snap values.

By default, the grid is hidden, but you can make it visible and change which axis it appears along. You can customize the grid in appearance and behavior by changing the following:

  * The size of the grid (adjust the distance between the lines).
  * The color of the grid lines themselves.
  * How transparent or opaque the grid lines appear.

Many of these actions support keyboard shortcuts. You can see which key combinations are assigned to these actions and use the Shortcuts Manager to customize them.

## Grid and Snap toolbar Overlay

Grid and Snap toolbar Overlay Icon | Actions  
---|---  
Grid visibility |  Toggle grid on or off  
Change grid axis  
Change grid opacity  
Move grid to gizmo handle or back to origin  
Grid snapping |  Toggle grid snapping on or off  
Change grid size   
Align a GameObject to an axis  
Snap increment | Change the default increment snap values  
  
**Note** : The settings on the **Grid and Snap** Overlay are global to all **Scene views**

## Align, snap, and incremental movements

This section provides information on how to perform these actions:

  * Aligning (pushing) to the grid
  * Activating auto-snapping
  * Moving, rotating, and scaling in increments

### Align (push) to the grid

You can align a GameObject to either the closest grid point on a single axis, or on all axes at once.

To align a GameObject to the closest point on a grid for a specific axis:

  1. In the **Grid and Snap** Overlays **toolbar** , open the grid snapping drop-down menu ().

  2. In the **Align Selected** section, click the **X** , **Y** , or **Z** button that matches the axis you want to push to.

Align Selection to Grid section of the Grid and Snap window

To align a GameObject on all axes at once:

  1. Select the GameObject(s) you want to align to the grid.

  2. Use the **Ctrl** +**\** (Windows) or **Cmd** +**\** (macOS) shortcut to push the GameObject(s) onto the grids on all axes.

Alternatively, from the **Grid and Snap** Overlays toolbar, open the grid visibility drop-down menu () and in the **Align Selected** section, click **All Axes**.

### Activate auto-snapping

To turn on automatic snapping to the grid:

  1. Activate the **Move** tool and make sure the handle orientation in the Tool Settings Overlay is set to Global ().
  2. Click the grid snapping icon () in the **Grid and Snap** toolbar Overlay. The icon is blue when activated.

When you enable automatic grid snapping, the **Move** , **Rotate** , and **Scale** transform tools snap the selected GameObject(s) to the grid along the active **gizmo** axis. If you need the GameObject to move in smaller increments, you can also transform it incrementally.

### Move, rotate, and scale in increments

To move, rotate, or scale by increment snap values:

  * Hold down the **Control** key (Windows) or **Command** key (macOS) while using one of the transform gizmos.

To change the default increment snap values:

  1. From the **Grid and Snap** Overlays toolbar, open the snap increment drop-down menu ().

  2. The **Increment Snap** section contains several properties that let you set the same value for all axes or different values:

Increment Snap section of the Grid and Snap window

**Move** : With the link icon selected, enter a uniform increment snap value for all axes, or unlink the axes and set different increment snap values in the **X** , **Y** , and **Z** axis properties.

**Rotate** : Enter a rotation increment value in degrees.

**Scale** : Enter a scale increment value as a scale factor. For example, if the Scale value is 2, the selected GameObject will scale at an increment of twice its original size.

## Customize the grid

This section provides information on customizing the following:

  * Show and hide grid lines
  * Change the axis where the grid appears
  * Resize the grid
  * Change the default color of the grid lines
  * Change the opacity of the grid
  * Move the grid to the handle of a GameObject
  * Reset values and settings to default

### Show and hide grid lines

Toggle grid visibility by clicking the grid visibility icon () on the Grid and Snap Overlay toolbar to display or hide the grid on any axis (X, Y, Z). If you are in orthographic mode (Iso), Unity chooses the view.

The grid appears in the **Scene view** window when you click the grid visibility button

### Change the axis where the grid appears

To change which axis the grid appears on:

  1. From the **Grid and Snap** Overlays toolbar, open the grid visibility drop-down menu ().

  2. From the **Grid Plane** section, select the axis you want to appear.

The Grid Axis section under the grid visibility drop-down menu

### Resize the grid

You can set the size of the grid lines that display in the **Scene view** window. The size of the grid affects how your grid looks and how your GameObjects automatically snap to the grid, but doesn’t affect how your GameObjects move, rotate, or scale in increments.

If you set a size for all axes at once, a uniform, square-based, grid displays. However, you can also use different values on any of the three axes to display a non-uniform, rectangular-based, grid. By default, the grid is set to a uniform distance of 1 on all axes.

To resize the grid:

  1. In the **Grid and Snap** overlay, select the arrow next to the **Grid Snapping** button to open the **Grid Snapping** menu.
  2. To enter a uniform value for the grid size and make all grid lines the same length: 
     1. Select the link icon in the **Size** property.
     2. Enter a value for the **X** property to set the size of the grid lines on all axes.
  3. To enter non-uniform values for the grid size and specify the size of the grid lines on for each axis separately: 
     1. Make sure that the link icon in the **Size** property is not selected.
     2. Enter a value for the **X** , **Y** , and **Z** properties to set the size of the grid lines on each axis.

**Tip** : Use these keyboard shortcuts to increase or decrease the size of the grid:

  * To increase the grid size, press **Ctrl** +**]** (MacOS: **Cmd** +**]**).
  * To decrease the grid size, press **Ctrl** +**[** (MacOS: **Cmd** +**[**).

### Change the default color of the grid lines

To change the color of the visible grid lines in the **Scene view** window:

  1. Open the Preferences window.

  2. Click on the Colors category from the list to see the **Colors** page.

The grid preference properties on the Preferences page
  3. Select a new color using the **Grid** property’s color picker.

### Change the opacity of the grid

If the grid lines are too light or too dark, you can adjust them:

  1. From the **Grid and Snap** Overlays toolbar, open the grid visibility drop-down menu ().

  2. Adjust the **Opacity** using the slider.

Adjust opacity in the grid visibility drop-down menu

### Move the grid to the handle of a GameObject

From the grid visibility drop-down menu () in the Grid and Snap Overlay toolbar, use the **Move To** section to move the grid to the handle of the selected GameObject (**Handle**) or back to the default position (**Origin**).

### Reset values and settings to default

To reset the grid axis and opacity settings to their defaults:

  1. From the **Grid and Snap** Overlays toolbar, open the grid visibility drop-down menu ().

  2. Click the **More** menu (⋮) and then click **Reset**.

To reset the size of the grid to the default:

  1. From the **Grid and Snap** Overlays toolbar, open the grid snapping drop-down menu ().

  2. Click the **More** menu (⋮) and then click **Reset**.

To reset the increment snap values to the default:

  1. From the **Grid and Snap** Overlays toolbar, open the snap increment drop-down menu ().

  2. Click the **More** menu (⋮) and then click **Reset**.

Only the values under the **Increment Snap** section return to their original default values.

## Shortcut defaults

You can perform the following actions with these default Unity shortcuts:

**Action** | **Default shortcut**  
---|---  
Increase Grid Size |  **Ctrl** +**]** (Windows) or   
**Command** +**]** (macOS)  
Decrease Grid Size |  **Ctrl** +**[** (Windows) or   
**Command** +**[** (macOS)  
Push to Grid (Align Selection to Grid) |  **Ctrl** +**\** (Windows) or   
**Command** +**\** (macOS)  
Reset Grid | (no shortcut by default)  
  
To change these default keyboard shortcuts, use the Shortcuts Manager.

* * *

  * Native grid improvements updated in 2019.3 NewIn20193
  * Grid and snap moved to Overlays toolbar updated in 2021.2 NewIn20212