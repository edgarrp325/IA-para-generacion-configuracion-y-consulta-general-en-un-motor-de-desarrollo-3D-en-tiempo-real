---
title: "Custom controls"
category: "General"
source_file: "UIE-custom-controls.html"
doc_type: "manual"
---

# Custom controls

You can create custom controls and implement custom logic for user interface elements. A good custom control is abstract, self-contained, and recurring. 

A Slide Toggle is a good example of a custom control:

  * It’s abstract. You use it to switch between one setting and another.
  * It’s self-contained. You give it a label and an initial value. A Slide Toggle triggers an event when its state changes.
  * It’s recurring. You can use it in multiple places in an application.

The menu bar of your application isn’t a good example of a custom control:

  * It’s not abstract. It’s specific to your application.
  * It’s not self-contained. It probably has dependencies to other parts of your application.
  * It’s not recurring. There is probably only one menu in your application.

After you have created a custom control, you can style it with USS, add logic to handle events in C#, and expose and use it in UI Builder.

**Topic** | **Description**  
---|---  
Create custom controls | Understand all aspects of creating and using custom controls.  
Expose custom controls to UXML and UI Builder | Understand how to expose your custom controls and define attributes for your custom controls.  
Customize UXML tag names and attributes | Understand how to customize a UXML tag name, override the default value of a base class attribute, or restrict the accepted attributes for your custom controls.  
  
## Additional resources

  * Create a custom control with two attributes
  * Create a slide toggle custom control
  * Create a radial progress indicator
  * Create a bindable custom control
  * Create a custom style for a custom control