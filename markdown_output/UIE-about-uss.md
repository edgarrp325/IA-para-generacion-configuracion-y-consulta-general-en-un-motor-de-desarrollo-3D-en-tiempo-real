---
title: "Introduction to USS"
category: "General"
source_file: "UIE-about-uss.html"
doc_type: "manual"
---

# Introduction to USS

A Unity Style Sheet (USS) is a text file recognized as an asset that supports style rules. The USS text file must have the `.uss` extension. 

You can use USS files to define the appearance and styles for the **UI** elements in your games and applications. USS provides a way to separate the appearance and styling of UI elements from the rest of the code, making it easier to manage and maintain the look and feel of an application.

With USS, you can define styles for buttons, labels, images, and other UI elements in a separate USS file, and then apply these styles in your game or application code. This makes it possible to change the appearance of your application by modifying the USS file, without having to make changes to the code.

A USS consists of the following: 

  * Style rules that include a selector and a declaration block.
  * Selectors that identify which **visual element** the style rule affects.
  * A declaration block, inside curly braces, that has one or more style declarations. Each style declaration has a property and a value. Each style declaration ends with a semi-colon.

## Syntax

The following is the general syntax of a style rule:
    
    
    selector {
      property1: value;
      property2: value;
    }
    

## Style matching with rules

When you define a style sheet, you can apply it to a visual tree. Selectors match against elements to resolve which properties apply from the USS file. If a selector matches an element, the style declarations apply to the element.

For example, the following rule matches any `Button` object:
    
    
    Button {
      width: 200px;
    }
    

## Supported selector types

USS supports several types of simple and complex selectors that match elements based on different criteria, such as the following:

  * Element C# type name
  * An assigned `name` property
  * A list of USS classes
  * The element’s position in the visual tree and its relationship to other elements

USS also supports pseudo classes that you can use with selectors to target elements that are in a specific state or select the `:root` element.

If an element matches more than one selector, USS applies the styles from whichever selector takes precedence.

**Note** : All selectors are case-sensitive.

### Simple selectors

USS supports a set of simple selectors that are analogous, but not identical, to simple selectors in CSS. The following table provides a quick reference of USS simple selectors. 

**Selector type** | **Syntax** | **Matches**  
---|---|---  
Type selector | `Type {...}` | Elements of a specific C# or visual element type.  
Class selector | `.class {...}` | Elements with an assigned USS class.  
Name selector | `#name {..}` | Elements with an assigned `name` attribute.  
Universal selector | `* {...}` | Any elements.  
  
### Complex selectors

USS supports a subset of CSS complex selectors. The following table provides a quick reference of USS complex selectors. 

**Selector type** | **Syntax** | **Matches**  
---|---|---  
Descendant selector | `selector1 selector2 {...}` | Elements that are the descendant of another element in the visual tree.  
Child selector | `selector1 > selector2 {...}` | Elements that are the children of another element in the visual tree.  
Multiple selector | `selector1selector2 {...}` | Elements that match all the simple selectors.  
  
## Connect styles to elements

You can connect styles to elements by the following methods:

  * In UI Builder, style an element with inline styles or USS selectors. For more information, refer to Style UI with UI Builder
  * In UXML, style an element with inline styles or attach a style sheet with selectors matching this element. For more information, refer to Add styles to UXML.
  * In a C# script, set styles directly to the `style` properties or add a USS style sheet to the `styleSheet` property with selectors matching an element. For more information, refer to Apply styles in C# scripts.

## Supported characters

USS selectors support the following characters:

  * Alphanumeric: `a-z`, `A-Z`, `0-9`
  * Special Characters: `_` (underscore), `-` (hyphen)

USS selectors also support the following characters but you must escape them with a backslash (`\`):

  * Unicode characters
  * Special characters like `!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`, `(`, `)`, `+`, `=`, `[`, `]`, `{`, `}`, `|`, `;`, `:`, `'`, `"`, `,`, `.`, `<`, `>`, `/`, `?`.

**Note** : UI Builder doesn’t not support all special characters.

## Additional resources

  * USS selectors
  * Best practices for USS
  * Theme Style Sheet (TSS)