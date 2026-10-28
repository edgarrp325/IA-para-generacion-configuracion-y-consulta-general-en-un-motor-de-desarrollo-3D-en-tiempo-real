---
title: "Aim Constraints"
category: "General"
source_file: "class-AimConstraint.html"
doc_type: "manual"
---

# Aim Constraints

An Aim Constraint rotates a **GameObject** to face its source GameObjects. It can also maintain a consistent orientation for another axis. For example, you can add an Aim Constraint to a **Camera** to face its source GameObjects. It can also maintain a consistent orientation for another axis. For example, you can add an Aim Constraint to a **Camera**. To keep the Camera upright while the Constraint aims it, specify the up axis of the Camera and an up direction to align it to.

Use the **Up Vector** to specify the up axis of a constrained GameObject. Use the **World Up Vector** to specify the upward direction. As the Aim Constraint rotates the GameObject to face its source GameObjects, the Constraint also aligns the up axis of the constrained GameObject with the upward direction.

Aim Constraint component

### Properties

**Property:** | **Function:**  
---|---  
**Activate** | After you rotate the constrained GameObject and move its source GameObjects, click **Activate** to save this information. **Activate** saves the current offset from the source GameObjects in **Rotation At Rest** and **Rotation Offset** , then checks **Is Active** and **Lock**.  
**Zero** | Sets the rotation of the constrained GameObject to the source GameObjects. Zero resets the **Rotation At Rest** and **Rotation Offset** fields, then checks **Is Active** and **Lock**.  
**Is Active** | Toggles whether or not to evaluate the Constraint. To also apply the Constraint, make sure **Lock** is checked.  
**Weight** | The strength of the Constraint. A weight of 1 causes the Constraint to rotate the GameObject at the same rate that its source GameObjects move. A weight of 0 removes the effect of the Constraint completely. This weight affects all source GameObjects. Each GameObject in the **Sources** list also has a weight.  
**Aim Vector** | Specifies the axis which faces the direction of its source GameObjects. For example, to specify that the GameObject should orient only its positive Z axis to face the source GameObjects, enter an **Aim Vector** of 0, 0, 1 for the X, Y, and Z axes, respectively.  
**Up Vector** | Specifies the up axis of this GameObject. For example, to specify that the GameObject should always keep its positive Y axis pointing upward, enter an **Up Vector** of 0, 1, 0 for the X, Y, and Z axes, respectively.  
**World Up Type** | Specifies the axis for the upward direction. The Aim Constraint uses this vector to align the up axis of the GameObject the upward direction.  
| **Scene** Up | The Y axis of the scene.  
| Object Up | The Y axis of the GameObject referred to by **World Up Object**.  
| Object Up Rotation | The axis specified by **World Up Vector** of the GameObject referred to by **World Up Object**.  
| Vector | The World Up Vector.  
| None | Do not use a World Up vector.  
**World Up Vector** | Specifies the vector to use for the **Object Up Rotation** and **Vector** choices in **World Up Type**.  
**World Up Object** | Specifies the GameObject to use for the **Object Up** and **Object Up Rotation** choices in **World Up Type**.  
**Constraint Settings** |   
| Lock | Enable this setting to let the Constraint rotate the GameObject. Uncheck this property to edit the rotation of this GameObject. You can also edit the Rotation At Rest and Rotation Offset properties. If Is Active is checked, the Constraint updates the Rotation At Rest or Rotation Offset properties for you as you rotate the GameObject or its source GameObjects. When you are satisfied with your changes, check Lock to let the Constraint control this GameObject. This property has no effect in Play Mode.  
| Rotation At Rest | The X, Y, and Z values to use when Weight is 0 or when the corresponding Freeze Rotation Axes are not checked. To edit these fields, uncheck Lock.  
| Rotation Offset | The X, Y, and Z offset from the rotation that is calculated by the Constraint. To edit these fields, uncheck Lock.  
| Freeze Rotation Axes | Check X, Y, or Z to allow the Constraint to control the corresponding axes. Uncheck an axis to stop the Constraint from controlling it. This allows you to edit, animate, or script the unfrozen axis.  
**Sources** | The list of GameObjects that constrain this GameObject. Unity evaluates source GameObjects in the order that they appear in this list. This order affects how this Constraint rotates the constrained GameObject. To get the result you want, drag and drop items in this list. Each source has a weight from 0 to 1.  
  
AimConstraint