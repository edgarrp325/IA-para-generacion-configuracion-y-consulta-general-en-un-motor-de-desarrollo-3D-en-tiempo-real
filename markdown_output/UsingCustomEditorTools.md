---
title: "Custom Editor tools"
category: "General"
source_file: "UsingCustomEditorTools.html"
doc_type: "manual"
---

# Custom Editor tools

You can create Editor tools with the EditorTool API. 

An Editor tool’s context determines what that tool affects in the Editor. Tools can be either global tools or component tools.

Access Editor tools in the Scene view from these overlays: 

  * The Tools overlay
  * The Tools Settings overlay

## Tool context

The `EditorToolContext API` changes what the Editor’s built-in Transform tools affect.

The default tool context is GameObject. A tool with the GameObject tool context affects the Transform values of a GameObject. Other contexts can affect different elements. For example, the Spline tool context makes it so the **Move** , **Rotate** , and **Scale** tools affect Spline knots and tangents.

If your project contains multiple tool contexts, you can use the first button in the Tools overlay to select a tool context. If the tool context button isn’t selected, then the default GameObject tool context is active. The tool context button isn’t available from the Tools overlay if there are no extra tool contexts in your project. 

## Global tools vs. component tools

Tools you create with the EditorTool API can either be global or component tools.

### Global tools

A global tool affects any GameObject. 

A global tool is always available regardless of the type of GameObject you select. For example, you can always access a Transform tool because the Transform tool works with any GameObject. 

The Tools overlay displays global tools in the section after the built-in Transform tools, such as **Move** , **Rotate** , **Scale** , and **Rect**. 

### Component tools

A component tool affects a specific component. 

A component tool is only available when you select a GameObject with the component the tool comes from attached to it. For example, you can only use a custom manipulator tool for lights when you select a GameObject with a Light component.

The last buttons in the Tools overlay are component tools. Component tools are divided into groups based on their component. The availability of component tools depends on what you have actively selected in the **Scene**

## Additional resources

  * Overlays
  * `EditorTool`
  * `EditorToolContext`
  * `GameObjectToolContext`