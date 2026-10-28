---
title: "Expose custom control to UXML and UI Builder"
category: "General"
source_file: "UIE-expose-custom-control-to-uxml.html"
doc_type: "manual"
---

# Expose custom control to UXML and UI Builder

To use custom controls with UXML and **UI** Builder, you must expose them.

## Define a factory

To define new elements, derive a new class from `VisualElement` or one of its subclasses, and then implement the appropriate functionality within this new class. 

Your new class must implement a default constructor. For example:
    
    
    class StatusBar : VisualElement
    {
        public StatusBar()
        {
            m_Status = String.Empty;
        }
    
        string m_Status;
        public string status { get; set; }
    }
    

In order for UI Toolkit to instantiate a new class when it reads a UXML file, you must define a factory for your class. Unless your factory needs to do something special, you can derive the factory from `UxmlFactory<T>`. It’s recommended that you put the factory class within your component class.

For example, the following code snippet define a factory named `UxmlFactory` for the `StatusBar` class: 
    
    
    class StatusBar : VisualElement
    {
        public new class UxmlFactory : UxmlFactory<StatusBar> {}
    
        // ...
    }
    

With this factory defined, you can use the `<StatusBar>` element in UXML files.

## Define attributes on elements

You can define UXML traits for a new class and set its factory to use these traits.

For example, the following code snippet defines a UXML traits class to initialize the `status` property as a property of the `StatusBar` class. The status property initializes from UXML data.
    
    
    class StatusBar : VisualElement
    {
        public new class UxmlFactory : UxmlFactory<StatusBar, UxmlTraits> {}
    
        public new class UxmlTraits : VisualElement.UxmlTraits
        {
            UxmlStringAttributeDescription m_Status = new UxmlStringAttributeDescription { name = "status" };
    
            public override IEnumerable<UxmlChildElementDescription> uxmlChildElementsDescription
            {
                get { yield break; }
            }
    
            public override void Init(VisualElement ve, IUxmlAttributes bag, CreationContext cc)
            {
                base.Init(ve, bag, cc);
                ((StatusBar)ve).status = m_Status.GetValueFromBag(bag, cc);
            }
        }
    
        // ...
    }
    

**Note** : When you are authoring an element within UI Builder, UI Builder might call `UxmlTraits.Init()` multiple times to synchronize values from UXML files. You are recommended to use `GetValueFromBag` instead of `TryGetValueFromBag` to ensure that an element doesn’t retain the previous value when an attribute is unset in UI Builder.

The `UxmlTraits` serves two purposes:

  * The factory uses it to initialize the newly created object.
  * The schema generation process analyzes it to get information about the element. This information translates into XML schema directives.

The code example above does the following:

  * The declaration of `m_Status` defines an XML attribute named `status`.
  * The `uxmlChildElementsDescription` returns an empty `IEnumerable` which indicates that `StatusBar` element has no child.
  * The `Init()` member reads the value of the `status` attribute in a property bag from the XML parser and sets the `StatusBar.status` property to this value.
  * The `UxmlTraits` class is placed inside the `StatusBar` class. This allows the `Init()` method to access the private members of `StatusBar`.
  * The new `UxmlTraits` class inherits from the base class `UxmlTraits`, so it shares the attributes of the base class.
  * `Init()` calls `base.Init()` to initialize the base class properties.

The code example above declares a string attribute with the `UxmlStringAttributeDescription` class. UI Toolkit supports the following types of attributes and each links a C# type to a UMXL type:

**Attribute** | **Attribute value**  
---|---  
`UxmlStringAttributeDescription` | A string  
`UxmlFloatAttributeDescription` | A single precision floating point value in the range of the C# `float` type.  
`UxmlDoubleAttributeDescription` | A double precision floating point value in the range of the C# `double` type.  
`UxmlIntAttributeDescription` | An integer value in the range of the C# `int` type.  
`UxmlLongAttributeDescription` | A long integer value in the range of the C# `long` type.  
`UxmlBoolAttributeDescription` |  `true` or `false`  
`UxmlColorAttributeDescription` | A string that represents a color defined in USS format.  
`UxmlEnumAttributeDescription<T>` | A string that represents one of the values for the `Enum` type `T`.  
`UxmlTypeAttributeDescription<T>` | A string that represents the assembly-qualified name of the type.  
  
In the code example above, the `uxmlChildElementsDescription` returns an empty `IEnumerable` which indicates that the `StatusBar` element doesn’t accept child element descriptions to the XML schema.

To have an element accept children of any type, you must override the `uxmlChildElementsDescription` property. For example, for the `StatusBar` element to accept children of any type, you must specify the `uxmlChildElementsDescription` property as follows:
    
    
    public override IEnumerable<UxmlChildElementDescription> uxmlChildElementsDescription
    {
        get
        {
            yield return new UxmlChildElementDescription(typeof(VisualElement));
        }
    }
    

## Define a namespace prefix

Once you have defined a new element in C#, you can use the element in your UXML files. To categorize elements, create your class in a namespace. When you define a new namespace, you can define a prefix for the namespace. You must define namespace prefixes as attributes of the root `<UXML>` element and replace the full namespace name when scoping elements.

To define a namespace prefix, add a `UxmlNamespacePrefix` attribute to your assembly for each namespace prefix. For example:
    
    
    [assembly: UxmlNamespacePrefix("My.First.Namespace", "first")]
    [assembly: UxmlNamespacePrefix("My.Second.Namespace", "second")]
    

You can do this at the root level (outside any namespace) of any C# file of the assembly.

The schema generation system does the following:

  * Checks for these attributes and uses them to generate the schema.
  * Adds the namespace prefix definition as an attribute of the `<UXML>` element in newly created UXML files.
  * Includes the schema file location for the namespace in its `xsi:schemaLocation` attribute.

To ensure that your text editor recognizes the new element, select **Assets** > **Update UXML Schema** to update the schema definition.

To create a new UXML document with the prefix, select **Assets** > **Create** > **UI Toolkit** > **UI Document**.

## Additional resources

  * Create custom controls
  * Create a custom control with two attributes
  * Create a slide toggle custom control
  * Create a radial progress indicator
  * Create a bindable custom control
  * Create a custom style for a custom control