---
title: "Style text with USS"
category: "General"
source_file: "UIB-styling-ui-text.html"
doc_type: "manual"
---

# Style text with USS

You can style text with USS text properties inline in UXML, a USS file, or directly in UI Builder.

## Style text in USS and UXML

Text properties are regular USS style properties. You can set text style properties on any element. Unlike most USS style properties, text style properties propagate to child elements. 

The following USS example styles the `Label` text to bold, italic, and have a font size of `39px`:
    
    
    Label {
        -unity-font-style: bold-and-italic; 
        font-size: 39px;
    }
    

The following UXML inline style example applies the same style to the `Label` text:
    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <ui:VisualElement>
            <ui:Label text="Label" style="-unity-font-style: bold-and-italic; font-size: 39px;" />
        </ui:VisualElement>
    </ui:UXML>
    

## Style text in UI builder

To style text in **UI** Builder, you can use the **Text** section in a UI control’s **Inspector** Builder, you can use the **Text** section in a UI control’s **Inspector** window to style text.

If the UI control is a text element that inherits from TextElement, such as Label or Button, you can also set the following text styles directly in the **Canvas** on selected text elements:

  * Horizontal text align
  * Vertical text align
  * Text wrap

Text styles are exposed as toggles in the Canvas on selected elements

## Additional resources

  * Get started with text
  * Font assets
  * Rich text tags
  * Style sheet assets
  * Include sprites in text