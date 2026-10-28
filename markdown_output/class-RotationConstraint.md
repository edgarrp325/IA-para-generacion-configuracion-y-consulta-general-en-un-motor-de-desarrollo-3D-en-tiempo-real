---
title: "Rotation Constraints"
category: "General"
source_file: "class-RotationConstraint.html"
doc_type: "manual"
---

# Rotation Constraints

A Rotation Constraint component rotates a **GameObject** to match the rotation of its source GameObjects. 

Rotation Constraint component

### Properties

**Property:** | **Function:**  
---|---  
**Activate** | After you rotate the constrained GameObject and its source GameObjects, click **Activate** to save this information. **Activate** saves the current offset from the source GameObjects in **Rotation At Rest** and **Rotation Offset** then checks **Is Active** and **Lock**.  
**Zero** | Sets the rotation of the constrained GameObject to the source GameObjects. **Zero** resets the **Rotation At Rest** and **Rotation Offset** fields, then checks **Is Active** and **Lock**.  
**Is Active** | Toggles whether or not to evaluate the Constraint. To also apply the Constraint, make sure **Lock** is checked.  
**Weight** | The strength of the Constraint. A weight of 1 causes the Constraint to rotate this GameObject at the same rate as its source GameObjects. A weight of 0 removes the effect of the Constraint completely. This weight affects all source GameObjects. Each GameObject in the **Sources** list also has a weight.  
**Constraint Settings** |   
| Lock | Toggle to let the Constraint rotate the GameObject. Uncheck this property to edit the rotation of this GameObject. You can also edit the **Rotation At Rest** and **Rotation Offset** properties. If **Is Active** is checked, the Constraint updates the **Rotation At Rest** or **Rotation Offset** properties for you as you rotate the GameObject or its **Source** GameObjects. When you are satisfied with your changes, check **Lock** to let the Constraint to control this GameObject. This property has no effect in Play Mode.  
| Rotation At Rest | The X, Y, and Z values to use when **Weight** is 0 or when the corresponding **Freeze Rotation Axes** is not checked. To edit these fields, uncheck **Lock**.  
| Rotation Offset | The X, Y, and Z offset from the transform that is imposed by the Constraint. To edit these fields, uncheck **Lock**.  
| Freeze Rotation Axes | Check X, Y, or Z to allow the Constraint to control the corresponding axes. Uncheck an axis to stop the Constraint from controlling it. This allows you to edit, animate, or script the unfrozen axis.  
**Sources** | The list of GameObjects that constrain this GameObject. Unity evaluates source GameObjects in the order they appear in this list. This order affects how this Constraint rotates the constrained GameObject. To get the result you want, drag and drop items in this list. Each source has a weight from 0 to 1.  
  
* * *

  * 2018–04–11 Page published 

  * Constraints added in 2018.1

RotationConstraint