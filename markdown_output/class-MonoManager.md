---
title: "Script Execution Order settings"
category: "General"
source_file: "class-MonoManager.html"
doc_type: "manual"
---

# Script Execution Order settings

Use the **Script Execution Order** settings to specify the relative order that Unity invokes the event functions of different MonoBehaviour classes. For example, you can specify that Unity should run the event functions of your `Rotation` MonoBehaviour script before it runs those of your `MoveForward` MonoBehaviour script. 

The order applies to each category of event function separately, so Unity calls any Awake functions it needs to invoke during a frame in the specified order and, later, calls any Update functions of active **GameObjects**

You can adjust the script execution order in the Project Settings Inspector. Go to menu: **Edit** > **Project Settings** , and then select the **Script Execution Order** category.

**Note:** If you assign multiple script types to multiple GameObjects, the script execution order specifies that all **scripts** of one type are executed before all scripts of another type, regardless of which GameObject they are attached to.

Use the Plus (+) button to add scripts to the settings **Inspector** window and select the class name. To remove a script, use the Minus (-) button located to the right of each item in the list.

To specify the execution order, drag items in the list into the desired position or edit the order numbers of a class in the list. The assigned numbers express the relative order. Unity executes the list from top to bottom (from scripts with more negative order numbers to those with higher positive numbers). Unity executes any scripts not in the list during the **Default Time** slot, which occurs after any scripts with negative order numbers and before any scripts with positive order numbers.

The order numbers are arbitrary and do not represent any physical quantity. The Editor stores these values in the script metadata files. You can leave gaps between order numbers to help avoid extraneous file changes when you add or move other scripts in the list.

When multiple scenes are loaded additively, the configured script execution order is applied in full for one scene at a time. For example, if the configured execution order is `Script1` > `Script2` > `Script3`, Unity updates all instances of `Script1` in the first scene, then all instances of `Script2` in the first scene, then all instances of `Script3` in the first scene, before running any updates in the next scene.

If you prefer to specify the script execution order from code rather than configuring it in the Editor, you can do so by applying the `[DefaultExecutionOrder]` attribute to your MonoBehaviour-derived classes. For more information, refer to DefaultExecutionOrder in the Scripting API. 

**Note:** The execution order specified in this settings window does not affect the order of functions marked with the RuntimeInitializeOnLoadMethod attribute. (You cannot specify an order for runtime initialization.)

See Order of Execution for Event Functions for information about when Unity invokes each of the different categories of event functions in a frame.

MonoManager