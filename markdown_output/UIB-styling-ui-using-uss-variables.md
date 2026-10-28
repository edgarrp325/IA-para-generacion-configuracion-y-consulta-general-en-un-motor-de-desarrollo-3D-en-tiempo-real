---
title: "Assign USS variables in UI Builder"
category: "General"
source_file: "UIB-styling-ui-using-uss-variables.html"
doc_type: "manual"
---

# Assign USS variables in UI Builder

USS variables define values that you can reuse in other USS rules. USS variables are primarily used for themes, with the default Unity themes exposing a long list of standard variables to make your **UI**

You can’t create USS variables with UI Builder. You must use a text editor to create a new USS variable in the USS file.

You can assign a USS variable that’s in the current theme or any assigned StyleSheets to the current UI Document (UXML) to a style property in UI Builder. When you work on an Editor UI, make sure to enable **Editor Extension Authoring** to see all available Editor variables.

To assign a variable:

  1. In the StyleSheet window, select the selector.

  2. In the **Inspector** window, right-click a style field.

  3. Select **Set Variable**. This converts the style field into a text field.

  4. Enter the name of the USS variable. As you type the name of the variable, a dropdown list displays the available variables.

USSVariablesSearch

You can also select a variable from the dropdown list, and see its current value and the StyleSheet asset it’s coming from. Pressing **Enter** sets the variable and reverts the style field back to its original type.

**Tip** : For style fields that are already text fields, you can also assign a variable by starting to type `--` instead of a number.

You can see which style fields already have a variable assigned by looking at the label of the field and seeing if it’s enclosed in a box:

USSVariablesSet

To remove a variable assignment, right-click a style field and select **Remove Variable**.

**Note** : Any inline styles set on a style property will override the USS variables.

## Additional resources

  * UI Builder