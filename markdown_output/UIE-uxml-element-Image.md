---
title: "Image"
category: "General"
source_file: "UIE-uxml-element-Image.html"
doc_type: "manual"
---

# Image

Use the Image element to add graphical assets to your application. It’s a versatile and powerful tool for displaying visual content in your **UI** , such as image galleries, product listings, a rendering preview, and user profiles.

## Create an image

You must use either UXML or C# code to add an Image element in your UI and provide the image source to the `--unity-image` USS custom property.

You can set the image scale mode with the `--unity-image-size` USS custom property. You can also set the image tint color with the `--unity-image-tint-color` USS custom property.

The following UXML example uses an inline style to add an image source:
    
    
    <ui:Image style="--unity-image: url('path/to/image');"/>
    

You can set the size and layout of the Image element, as well as the sizing and layout of the image within the element. This allows you to control how the image is displayed within your UI, such as resizing it to fit a particular area or aligning it with other UI elements. You can also add interactivity to the Image element, such as allowing the user to click or tap on the image to trigger an action. You can apply styles to the Image element and the image itself, such as adjusting the opacity or applying a color filter.

## Image versus `VisualElement.style.backgroundImage`

You can use both the Image element and the `VisualElement.style.backgroundImage` property to add visual content to your UI. The choice between the two depends on the specific usage and requirements of your application. 

The Image element is typically used to display an image within a specific area of a UI, such as an image gallery or an **avatar** in a user profile. It provides more fine-grained control over the appearance of the image, including options for resizing, scaling, and cropping. Use Image when you want the size of an image to drive the size of an element in the layout. You can also add additional elements to the Image element to create overlays or add interactivity. However, for performance reasons, specify a fixed width and height if you use many instances of Image.

The `VisualElement.style.backgroundImage` property is used to set an image as the background of a UI element. This is useful when you want to add visual interest to an element without detracting from the main content or functionality of the UI. The `VisualElement.style.backgroundImage` property also allows the convenience of using USS to change the source image for many different elements.

In general, it’s recommended to use the Image element when you need more control over the appearance and layout of an image; and to use the `VisualElement.style.backgroundImage` property when you simply want to add a background image to a UI element. However, both approaches are valid and you can use them together in the same UI if necessary.

**Note** : 

  * The Image element also supports the `backgroundImage` property. The background image won’t be visible if the Image element has an image source set and it’s not transparent.
  * UI Builder partially supports the Image element. It reads from and writes to UXML, and allows basic authoring as a standard **visual element**. Most of the Image-specific settings are defined as USS custom properties and aren’t visible in the **Attributes** section of the UI Builder **Inspector**. Most of the Image-specific settings are defined as USS custom properties and aren’t visible in the **Attributes** section of the UI Builder **Inspector**.

## C# base class and namespace

**C# class** : `Image`  
**Namespace** : `UnityEngine.UIElements`  
**Base class** : `VisualElement`

## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`focusable` | `boolean` | True if the element can be focused.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
  
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
`ussClassName` | `.unity-image` | USS class name of elements of this type.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
## USS custom properties

The following table outlines the custom properties that are available exclusively for the Image element in USS:

Property | Type | Description  
---|---|---  
`--unity-image` | string | The source of the image file. For information on how to reference an image asset, refer to Assets.  
`--unity-image-size` | string | The image scale mode. Available values are `stretch-to-fill`, `scale-and-crop` and `scale-to-fit`.  
`--unity-image-tint-color` | string | The image tint color.  
  
## Additional resources

  * Set background images
  * Button