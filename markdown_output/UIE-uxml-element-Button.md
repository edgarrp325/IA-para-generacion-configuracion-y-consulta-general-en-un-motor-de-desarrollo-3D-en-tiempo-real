---
title: "Button"
category: "General"
source_file: "UIE-uxml-element-Button.html"
doc_type: "manual"
---

# Button

Use the Button element to create clickable buttons in a **UI**. For example, when a user clicks or taps on a Button element, it triggers an action or event, such as opening a new window, submitting a form, or playing a sound effect.

## Create a Button

You can create a Button with UI Builder, UXML, or C#. The following C# example creates a Button with a label:
    
    
    var button = new Button(() => { Debug.Log("Button clicked"); }) { text = "Click me" };
    

## Use sub-elements of a Button

You can use the `text` and the `background-image` properties of the Button to provide additional information to the user. You can also add sub-elements in a button’s hierarchy, such as a Label or Image, to provide additional information to the user if you want to have more fine-grained control over the appearance and behavior of those elements.

In general, use sub-elements in the following situations:

  * Customization: Using sub-elements allows you to customize the appearance and behavior of each individual element separately. For example, you may want to use a custom font or color for the label text or add a specific animation to the image. When you add an Image element to your Button, you can add the element from your **scene** directly. In addition, an Image element also supports scale mode and repeat mode.
  * Dynamic content: If the content of the label or image is dynamic, using sub-elements allows you to update the content of each element separately without affecting the other properties of the button.
  * Interaction: If you want to add interactivity to a specific element within the button, such as allowing the user to click only the label (disregarding clicks on other elements of the button) to trigger an action, using sub-elements makes this possible.

Use properties for the following purposes:

  * Simple designs: If the design of the button is simple and doesn’t require customization or dynamic content, using properties is recommended.
  * Performance: If you have many buttons in your UI, using sub-elements for each one may negatively impact performance. In this case, it’s more efficient to use properties to set the appearance of the button.
  * Consistency: If you want to maintain consistency across your UI, using properties can ensure that all buttons have a consistent appearance and behavior.

## Examples

The following UXML example creates a Button:
    
    
    <UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <Button text="UXML Button" name="the-uxml-button" />
    </UXML>
    

The following C# example illustrates some of the customizable functionalities of the Button:
    
    
    /// <sample>
    // Action to perform when button is pressed.
    // Toggles the text on all buttons in 'container'.
    Action action = () =>
    {
        container.Query<Button>().ForEach((button) =>
        {
            button.text = button.text.EndsWith("Button") ? "Button (Clicked)" : "Button";
        });
    };
    
    // Get a reference to the Button from UXML and assign it its action.
    var uxmlButton = container.Q<Button>("the-uxml-button");
    uxmlButton.RegisterCallback<MouseUpEvent>((evt) => action());
    
    // Create a new Button with an action and give it a style class.
    var csharpButton = new Button(action) { text = "C# Button" };
    csharpButton.AddToClassList("some-styled-button");
    container.Add(csharpButton);
    /// </sample>
    

To try this example live in Unity, go to **Window** > **UI Toolkit** > **Samples**.

## C# base class and namespace

**C# class** : `Button`  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : `TextElement`

## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`binding-path` | `string` | Path of the target property to be bound.  
`display-tooltip-when-elided` | `boolean` | When true, a tooltip displays the full version of elided text, and also if a tooltip had been previously provided, it will be overwritten.  
`enable-rich-text` | `boolean` | When false, rich text tags will not be parsed.  
`focusable` | `boolean` | True if the element can be focused.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
`text` | `string` | The text to be displayed.  
  
Changing this value will implicitly invoke the `INotifyValueChanged{T}.value` setter, which will raise a `ChangeEvent_1` of type string.  
  
This element also inherits the following attributes from `VisualElement`:

**Name** | **Type** | **Description**  
---|---|---  
`content-container` | `string` | Child elements are added to it, usually this is the same as the element itself.  
`name` | `string` | The name of this VisualElement.  
  
Use this property to write USS selectors that target a specific element. The standard practice is to give an element a unique name.  
`picking-mode` | `UIElements.PickingMode` | Determines if this element can be pick during mouseEvents or `IPanel.Pick` queries.  
`style` | `string` | Reference to the style object of this element.  
  
Contains data computed from USS files or inline styles written to this object in C#.  
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor UI.  
`usage-hints` | `UIElements.UsageHints` | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence (ie. tree expanded states, scroll position, zoom level).  
  
This is the key used to save/load the view data from the view data store. Not setting this key will disable persistence for this `VisualElement`.  
  
## USS classes

The following table lists all the C# public property names and their related USS selector.

**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-button` | USS class name of elements of this type.  
  
Unity adds this USS class to every instance of the Button element. Any styling applied to this class affects every button located beside, or below the stylesheet in the visual tree.  
`ussClassName` | `.unity-text-element` | USS class name of elements of this type.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the Matching Selectors section in the Inspector or the UI Toolkit Debugger to see which USS selectors affect the components of the `VisualElement` at every level of its hierarchy.

## Additional resources

  * Image