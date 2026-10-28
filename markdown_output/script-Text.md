---
title: "Text"
category: "General"
source_file: "script-Text.html"
doc_type: "manual"
---

# Text

The **Text** control displays a non-interactive piece of text to the user. This can be used to provide captions or labels for other GUI controls or to display instructions or other text.

## Properties

**_Property:_** | **_Function:_**  
---|---  
**Text** | The text displayed by the control.  
**Character**  
**Font** | The Font used to display the text.  
**Font Style** | The style applied to the text. The options are _Normal_ , _Bold_ , _Italic_ and _Bold And Italic_.  
**Font Size** | The size of the displayed text.  
**Line Spacing** | The vertical separation between lines of text.  
**Rich Text** | Should markup elements in the text be interpreted as Rich Text styling?  
**Paragraph**  
**Alignment** | The horizontal and vertical alignment of the text.  
**Align by Geometry** | Use the extents of glyph geometry to perform horizontal alignment rather than glyph metrics.  
**Horizontal Overflow** | The method used to handle the situation where the text is too wide to fit in the rectangle. The options are _Wrap_ and _Overflow_.  
**Vertical Overflow** | The method used to handle the situation where wrapped text is too tall to fit in the rectangle. The options are _Truncate_ and _Overflow_.  
**Best Fit** | Should Unity ignore the size properties and simply try to fit the text to the control’s rectangle?  
|   
**Color** | The color used to render the text.  
**Material** | The Material used to render the text.  
  
A default text element looks like this:

A Text element.

## Details

Some controls (such as Buttons and Toggles

The Text control offers the usual parameters for font size, style, etc, and text alignment. When the _Rich Text_ option is enabled, markup elements within the text will be treated as styling information, so you can have just a single word or short section in boldface or in a different color, say (see the page about Rich Text for details of the markup scheme).

## Hints

  * See the Effects page for how to apply a simple shadow or outline effect to the text.

Text