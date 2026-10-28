---
title: "Position Constraints"
category: "General"
source_file: "class-PositionConstraint.html"
doc_type: "manual"
---

# Position Constraints

A Position Constraint component moves a **GameObject** to follow its source GameObjects. 

Position Constraint component

## Properties

**Property:** | **Function:**  
---|---  
**Activate** | After you position the constrained GameObject and its source GameObjects, click **Activate** to save this information. **Activate** saves the current offset from the source GameObjects in **Position At Rest** and **Position Offset** , then checks **Is Active** and **Lock**.  
**Zero** | Sets the position of the constrained GameObject to the source GameObjects. **Zero** resets the **Position At Rest** and **Position Offset** fields, then checks **Is Active** and **Lock**.  
**Is Active** | Toggles whether or not to evaluate the Constraint. To also apply the Constraint, make sure **Lock** is checked.  
**Weight** | The strength of the Constraint. A weight of 1 causes the Constraint to move this GameObject at the same rate as its source GameObjects. A weight of 0 removes the effect of the Constraint completely. This weight affects all source GameObjects. Each GameObject in the **Sources** list also has a weight.  
**Constraint Settings** |   
| Lock | Toggle to let the Constraint move the GameObject. Uncheck this property to edit the position of this GameObject. You can also edit the **Position At Rest** and **Position Offset** properties. If **Is Active** is checked, the Constraint updates the **At Rest** or **Offset** properties for you as you move the GameObject or its Source GameObjects. When you are satisfied with your changes, check **Lock** to let the Constraint control this GameObject. This property has no effect in Play Mode.  
| Position At Rest | The X, Y, and Z values to use when **Weight** is 0 or when the corresponding **Freeze Position Axes** is not checked. To edit these fields, uncheck **Lock**.  
| Position Offset | The X, Y, and Z offset from the Transform that is imposed by the Constraint. To edit these fields, uncheck Lock.  
| Freeze Position Axes | Check X, Y, or Z to allow the Constraint to control the corresponding axes. Uncheck an axis to stop the Constraint from controlling it. This allows you to edit, animate, or script the unfrozen axis.  
**Sources** | The list of GameObjects that constrain this GameObject. Each source has a weight from 0 to 1.  
  
* * *

  * 2018–03–13 Page published 

  * Constraints added in 2018.1

PositionConstraint