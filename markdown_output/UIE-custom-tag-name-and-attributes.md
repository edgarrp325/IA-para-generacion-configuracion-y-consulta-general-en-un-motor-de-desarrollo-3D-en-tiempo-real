---
title: "Customize UXML tag names and attributes"
category: "General"
source_file: "UIE-custom-tag-name-and-attributes.html"
doc_type: "manual"
---

# Customize UXML tag names and attributes

You can customize a UXML tag name, override the default value of a base class attribute, or restrict the accepted attributes for your custom control.

## Customize a UXML tag name

By default, the tag name in UXML for your custom control is the C# class name. It’s not recommended that a tag has a different name than the C# class. However, you can customize the tag name if there are name conflicts.

To customize a UXML tag name, override its `IUxmlFactory.uxmlName` and `IUXmlFactory.uxmlQualifiedName` properties. Make sure of the following:

  * `uxmlName` is unique in your namespace
  * `uxmlQualifiedName` is unique in your project

If both names aren’t unique, Unity throws an exception when it loads the assembly.

The following code example overrides and customizes the UXML tag name:
    
    
    public class FactoryWithCustomName : UxmlFactory<..., ...>
    {
        public override string uxmlName
        {
            get { return "UniqueName"; }
        }
    
        public override string uxmlQualifiedName
        {
            get { return uxmlNamespace + "." + uxmlName; }
        }
    }
    

## Select a factory for an element

By default, `IUxmlFactory` instantiates an element and selects the element by the name of the element. To consider attribute values on the element for the selection, override `IUXmlFactory.AcceptsAttributeBag()`. The factory examines the element attributes to decide if it can instantiate an object for the UXML element.

If your `VisualElement` class is generic, it can be useful to have the factory examine element attributes. In this case, the class factory for a specialization of your class could examine the value of a UXML `type` attribute. Depending on the value, instantiation can be accepted or refused.

If more than one factory can instantiate an element, the first registered factory is selected.

## Override the default value of a base class attribute

To change the default value of an attribute declared in a base class, set its `defaultValue` in the derived `UxmlTraits` class.

The following code example changes the default value of `m_TabIndex`:
    
    
    class MyElementTraits : VisualElement.UxmlTraits
        {
            public MyElementTraits()
            {
                m_TabIndex.defaultValue = 0;
            }
        }
    

## Restrict accepted attributes

By default, the generated UXML schema states that an element can have any attribute. This is in contrast to XML validators that check that the value of a declared attribute matches its declaration.

The `IUxmlAttributes` bag includes additional attributes that are passed to the `IUxmlFactory.AcceptsAttributeBag()` and `IUxmlFactory.Init()` functions. The factory implementation decided whether to use these additional attributes. The default behavior is to discard additional attributes. These additional attributes aren’t attached to the instantiated `VisualElement` and you can’t query these attributes with UQuery.

To restrict the accepted attributes to those explicitly declared in the `IUxmlAttributes` bag when you define a new element, set the `UxmlTraits.canHaveAnyAttribute` property to `false` in your `UxmlTraits` constructor.

## Additional resources

  * Create custom controls
  * Expose custom controls to UXML and UI Builder