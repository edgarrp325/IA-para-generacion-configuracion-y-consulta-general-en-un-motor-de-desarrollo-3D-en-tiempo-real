---
title: "Gizmos menu"
category: "General"
source_file: "GizmosMenu.html"
doc_type: "manual"
---

# Gizmos menu

The Scene view and the Game view both have a **Gizmos** and the Game view both have a **Gizmos** menu. Click the **Gizmos** button in the **toolbar** menu. Click the **Gizmos** button in the **toolbar** of the **Scene** of the **Scene** view or the Game view to access the **Gizmos** menu.

The **Gizmos** button in the Scene view The **Gizmos** button in the Game view The Gizmos menu at the top of the Scene view and Game view window **Property** | **Function**  
---|---  
**3D Icons** | The **3D Icons** checkbox controls whether component icons (such as those for Lights and Cameras) are drawn by the Editor in 3D in the Scene view.  
  
When the **3D Icons** checkbox is ticked, component icons are scaled by the Editor according to their distance from the Camera, and obscured by GameObjects in the Scene. Use the slider to control their apparent overall size. When the **3D Icons** checkbox is not ticked, component icons are drawn at a fixed size, and are always drawn on top of any GameObjects in the Scene view.  
  
See Gizmos and Icons, below, for images and further information.  
**Fade Gizmos** | Fade out and stop rendering gizmos that are small on screen.  
**Selection Outline** | Check **Selection Outline** to display selected GameObjects with a colored outline, and their children with a different colored outline. By default, Unity highlights the selected GameObject in orange, and child GameObjects in blue.  
  
**NOTE:** This option is only available in the Scene view Gizmos menu; you cannot enable it in the Game view Gizmos menu.   
  
See Selection Outline and Selection Wire, below, for images and further information.  
**Selection Wire** | Check **Selection Wire** to show the selected GameObjects with their wireframe Mesh visible. To change the colour of the Selection Wire, go to **Edit > Preferences** (macOS: **Unity > Settings**) in the main menu, select **Colors** , and alter the **Selected Wireframe** setting.  
  
This option is only available in the Scene view Gizmos menu; you cannot enable it in the Game view Gizmos menu.  
  
See Selection Outline and Selection Wire, below, for images and further information.  
**Recently Changed** | Controls the visibility of the icons and gizmos for components and scripts that you modified recently.  
  
This section appears the first time you change one or more items, and updates after subsequent changes.  
  
For more information, see Built-in components, scripts, and recently changed items, below.  
**Scripts** | Controls the visibility of the icons and gizmos for scripts in the Scene.  
  
This section appears only when your Scene uses scripts that meet specific criteria.  
  
See Built-in components, scripts, and recently changed items, below, for further information.  
**Built-in Components** | Controls the visibility of the icons and gizmos for all component types that have an icon or gizmo.  
  
See Built-in components, scripts, and recently changed items, below, for further information.  
  
## Gizmos and Icons

### Gizmos

**Gizmos** are graphics associated with GameObjects in the Scene. Some Gizmos are only drawn when the **GameObject** is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. They are usually wireframes, drawn with code rather than bitmap graphics, and can be interactive. The ****Camera** is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. They are usually wireframes, drawn with code rather than bitmap graphics, and can be interactive. The ****Camera**** Gizmo and **Light direction** Gizmo (shown below) are both examples of built-in Gizmos; you can also create your own Gizmos using script. See documentation on Understanding Frustum for more information about the Camera.**

Some Gizmos are passive graphical overlays, shown for reference (such as the **Light direction** Gizmo, which shows the direction of the light). Other Gizmos are interactive, such as the AudioSource **spherical range** Gizmo, which you can click and drag to adjust the maximum range of the AudioSource.

The **Move** , **Scale** , **Rotate** and **Transform** tools are also interactive Gizmos. See documentation on Positioning GameObjects to learn more about these tools.

The Camera Gizmo and a Light Gizmo. These Gizmos are only visible when they are selected.

See the Script Reference page for the OnDrawGizmos function for further information about implementing custom Gizmos in your **scripts**

### Icons

You can display **icons** in the Game view or Scene view. They are flat, billboard-style overlays which you can use to clearly indicate a GameObject’s position while you work on your game. The **Camera** icon and **Light** icon are examples of built-in icons; you can also assign your own to GameObjects or individual scripts (see documentation on Assigning Icons to learn how to do this).

The built-in icons for a Camera and a Light **Left** : icons in 3D mode. **Right** : icons in 2D mode.

## Selection Outline and Selection Wire

### Selection Outline

When **Selection Outline** is enabled, an outline appears around selected GameObjects and their child GameObjects. By default, Unity outlines selected GameObjects in orange, and child GameObjects in blue. You can change these colors in the Unity preferences (see Selection Colors, below).

Selecting a GameObject (the far left box) outlines it in orange, and outlines its child GameObjects (the middle and right boxes) in blue.

When you select a GameObject, Unity outlines all of its child GameObjects (and their child GameObjects, and so on), but does not outline parent GameObjects (or their parent GameObjects, and so on).

Selecting the middle box highlights it in orange, and highlights its child GameObject (the far right box) in blue, but does not highlight its parent GameObject (the far left box).

If selected GameObjects extend beyond the edges of the Scene view, the selection outline runs along the edge of the window:

### Selection Wire

When **Selection Wire** is enabled, then when you select a GameObject in the Scene view or Hierarchy window, the wireframe **Mesh** for that GameObject is made visible in the Scene view:

### Selection colors

You can set custom colors for selection wireframes.

  1. Go to **Unity** > **Preferences** (macOS) or **Edit** > **Preferences** (Windows) to open the Preferences editor.
  2. On the colors tab, change one or more of the following colors: 
     * **Selected Children Outline** : outline color for selected GameObjects’ children.
     * **Selected Outline** : outline color for selected GameObjects.
     * **Wireframe Selected** : outline color for selected GameObjects’ wireframes.

## Built-in components, scripts, and recently changed items

Use the list in the **Gizmos** menu to control the visibility of icons and gizmos for various components. The list is divided into sections:

The Gizmos menu, displaying items with custom icons and some recently modified items

### Recently Changed

The **Recently Changed** section controls the visibility of the icons and gizmos for items that you’ve modified recently. It appears the first time you change one or more items. Unity updates the list after subsequent changes.

### Scripts

The **Scripts** section controls the visibility of the icons and gizmos for scripts that:

  * Have an icon assigned to them (see documentation on Assigning Icons).

  * Implement the OnDrawGizmos function.

  * Implement the OnDrawGizmosSelected function.

This section appears when your Scene contains one or more scripts that meet the above criteria.

### Built-in Components

The **Built-in Components** section controls the visibility of the icons and gizmos for all component types that have an icon or gizmo.

Built-in component types that do not have an icon or gizmo shown in the Scene view (for example, Rigidbody) are not listed here.

### Toggling icon visibility

The **icon** column shows or hides the icons for each component type. Full-color icons are displayed in the main Scene view window, faded icons are not.

The **Light** icon is faded, indicating that the Editor does not display light icons in the Scene view. The **Camera** icon is full-color, indicating that the Editor does display camera icons in the Scene view.

To toggle an icon’s visibility in the Scene view, click any icon in the **icon** column.

**Note:** If an item in the list has a gizmo but no icon, the **icon** column for that item is empty.

### Changing script icons

Scripts with custom icons show a small drop-down menu arrow in the **icon** column. To change a custom icon, click the arrow to open the Select Icon menu.

### Toggling gizmo visibility

To control whether the Editor draws gizmo graphics for a particular component type (for example, a **Collider’s** wireframe gizmo or a **Camera’s** view frustum gizmo) or script, use the checkboxes in the **Gizmo** column.

  * When a checkbox is checked, the Editor draws gizmos for that component type.

  * When a checkbox is cleared, the Editor does not draw gizmos for that component type.

**Note:** If an item in the list has an icon but no gizmo, the **Gizmo** column for that item is empty.

To toggle gizmo visibility for an entire section (all **Built-in Components** , all **Scripts** , and so on), use the checkboxes next to the section names.

The **Built-in Components** checkbox toggles gizmo visibility for every type of component listed in that section

When the checkbox is toggled on, gizmo visibility is toggled on for one or more item types in the section.

* * *

  * Selection outline for child GameObjects added in 2018.3 NewIn20183

  * Gizmo menu option to toggle Gizmo visibility for all components in a section added in 2019.1 NewIn20191