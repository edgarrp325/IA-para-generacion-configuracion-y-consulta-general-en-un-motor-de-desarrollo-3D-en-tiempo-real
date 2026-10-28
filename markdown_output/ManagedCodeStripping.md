---
title: "Managed code stripping"
category: "General"
source_file: "ManagedCodeStripping.html"
doc_type: "manual"
---

# Managed code stripping

During the build process, Unity removes unused or unreachable code through a process called managed code stripping, which can significantly decrease your application’s final size. Managed code stripping removes code from managed assemblies, including assemblies built from the C# **scripts** in your project, assemblies that are part of packages and plugins, and assemblies in .NET Framework.

Unity uses a tool called the Unity linker to perform a static analysis of the code in your project’s assemblies. The static analysis identifies any classes, portions of classes, functions, or portions of functions that can’t be reached during execution. This analysis only includes code that exists at build time because runtime generated code doesn’t exist when Unity performs the static analysis.

You can configure the level of code stripping Unity performs for your project using the **Managed Stripping Level** setting. To prevent Unity removing specific parts of your code, use annotations to indicate which parts of your code base the Unity linker should preserve. For more information, see Unity linker.

## Configure managed code stripping

The Managed Stripping Level property

The **Managed Stripping Level** property determines the set of rules that the Unity linker follows when it analyzes and strips your application’s code. As you increase the setting from **Minimal** to **High** , the rules enable the linker to search through more assemblies for unreachable code. The Unity linker removes more code at the higher settings which reduces the final size of your build, though the expanded search means that each build takes longer to produce.

To change the **Managed Stripping Level** property:

  1. Go to **Edit** > **Project Settings** > **Player**.
  2. In Other Settings, navigate to the Optimization heading.
  3. Set the **Managed Stripping Level** property to the desired value.

**Property:** | **Function:**  
---|---  
**Disabled** | Unity doesn’t remove any code.  
  
This setting is visible only and is the default setting if you use the Mono scripting backend.  
**Minimal** | Unity searches only the UnityEngine and the .NET class libraries for unused code. Unity doesn’t remove any user-written code. This setting is the least likely to cause any unexpected runtime behavior.  
  
This setting is useful for projects where usability is of higher priority than build size.This is the default setting if you use the IL2CPP scripting backend.  
**Low** | Unity searches some user-written assemblies and all UnityEngine and .NET class libraries for unused code. This setting applies a set of rules that removes some unused code but minimizes the likelihood of unintended consequences, such as changes in behavior of runtime code that uses reflection.  
**Medium** | Unity partially searches all assemblies to find unreachable code. This setting applies a set of rules that strips more types of code patterns to reduce the build size. Although Unity doesn’t strip all possible unreachable code, this setting does increase the risk of undesirable or unexpected behavior changes.  
**High** | Unity performs an extensive search of all assemblies to find unreachable code. At this setting, Unity prioritizes size reduction more than code stability and removes as much code as possible.  
  
This search can take much longer than for lower stripping levels. Use this setting only for projects where a compact build size is extremely important. Test your application thoroughly and make careful use of `[Preserve]` attributes and link.xml files to ensure that the Unity linker doesn’t strip vital code.  
  
## Preserve code using annotations

You can use annotations to prevent the Unity linker from stripping specific sections of your code. This is helpful if your application produces runtime code which doesn’t exist when Unity performs the static analysis; for example, through reflection. Annotations either provide general guidance to the Unity linker about which code patterns it shouldn’t strip, or instructions not to strip a specific, defined section of code.

There are two broad approaches you can use to annotate your code to preserve it from the managed code stripping process:

  * Root annotations identify parts of your code as roots. The Unity linker doesn’t strip any code that is marked as a root. Root annotations are less complicated to use but can also lead to the Unity linker preserving some code that it should strip.
  * Dependency annotations define the connections between code elements. Dependency annotations can reduce the amount of over preservation of code compared to root annotations.

Each of these techniques provides more control over the amount of code that the Unity linker strips at higher stripping levels and reduces the chance of vital code being stripped. Annotations are especially useful when your code references other code through reflection, because the Unity linker can’t always detect uses of reflection.

Preserve code that uses reflection or generates other code at runtime to significantly reduce the likelihood of unexpected behavior when your application is executed. For examples of reflection patterns that the Unity linker can recognize, see the Unity Intermediate Language Linker reflection test suite.

## Root annotations

Root annotations force the Unity linker to treat code elements as roots, which aren’t stripped in the code stripping process. There are two types of root annotations you can use, depending on whether you need to preserve individual types with their constructors or assemblies:

  * Preserve Attribute: Annotates individual types as roots to preserve them.
  * Link.xml: Annotates assemblies and any types or other code entities within those assemblies as roots to preserve them.

### Annotate roots using the Preserve attribute

Use the Preserve attribute to individually exclude specific sections of your code from the Unity linker’s static analysis. To annotate a piece of code with this attribute, add `[Preserve]` immediately before the first part of the code you want to preserve. The following list describes what entities the Unity linker preserves when you annotate different code elements with the `[Preserve]` attribute:

  * **Assembly** : Preserves all types that are used and defined in the assembly. To assign the `[Preserve]` attribute to an assembly, place the attribute declaration in any C# file included in the assembly, before any namespace declarations.
  * **Type** : Preserves a class or type and its default constructor.
  * **Method** : Preserves the method, the type that declares the method, the type the method returns, and the types of all of its arguments.
  * **Property** : Preserves the property, the type that declares the property, the value type of the property, and methods that get and set the property value.
  * **Field** : Preserves the field, the field type, and the type that declares the field.
  * **Event** : Preserves the event, the type that declares the event, type, the type the event returns, the `[add]` accessor, and the `[remove]` accessor.
  * **Delegate** : Preserves the delegate type and all methods that the delegate invokes.

Use the `[Preserve]` attribute when you want to preserve both a type and its default constructor. If you want to keep one or the other but not both, use a link.xml file.

You can define the `[Preserve]` attribute in any assembly and in any namespace. You can use the UnityEngine.Scripting.PreserveAttribute class, create a subclass of UnityEngine.Scripting.PreserveAttribute, or create your own PreserveAttribute class. For example:
    
    
    class Foo
    {
        [Preserve]
        public void PreservedMethod(){}
    }
    

### Annotate roots using a Link XML file

You can include a .xml file entitled link.xml in your project to preserve a list of specific assemblies or parts of assemblies. The link.xml file must be present in the `Assets` folder or a subdirectory of the `Assets` folder in your project and must include the `<linker>` tag in the file. The Unity linker treats any assembly, type, or member preserved in a link.xml file as a root type.

You can use any number of link.xml files in your project. As a result, you can provide separate preservation declarations for each **plug-in**. You can’t include a link.xml file in a package, but you can reference package assemblies from non-package link.xml files.

The following examples illustrate the different ways that you can declare the root types of a project’s assemblies using a link.xml file:
    
    
    <linker>
      <!--Preserve types and members in an assembly-->
      <assembly fullname="AssemblyName">
        <!--Preserve an entire type-->
        <type fullname="AssemblyName.MethodName" preserve="all"/>
    
        <!--No "preserve" attribute and no members specified means preserve all members-->
        <type fullname="AssemblyName.MethodName"/>
    
        <!--Preserve all fields on a type-->
        <type fullname="AssemblyName.MethodName" preserve="fields"/>
    
        <!--Preserve all fields on a type-->
        <type fullname="AssemblyName.MethodName" preserve="methods"/>
    
        <!--Preserve the type only-->
        <type fullname="AssemblyName.MethodName" preserve="nothing"/>
    
        <!--Preserving only specific members of a type-->
        <type fullname="AssemblyName.MethodName">
            
          <!--Fields-->
          <field signature="System.Int32 FieldName" />
    
          <!--Preserve a field by name rather than signature-->
          <field name="FieldName" />
          
          <!--Methods-->
          <method signature="System.Void MethodName()" />
    
          <!--Preserve a method with parameters-->
          <method signature="System.Void MethodName(System.Int32,System.String)" />
    
          <!--Preserve a method by name rather than signature-->
          <method name="MethodName" />
    
          <!--Properties-->
    
          <!--Preserve a property, its backing field (if present), 
              getter, and setter methods-->
          <property signature="System.Int32 PropertyName" />
    
          <property signature="System.Int32 PropertyName" accessors="all" />
    
          <!--Preserve a property, its backing field (if present), and getter method-->
          <property signature="System.Int32 PropertyName" accessors="get" />
    
          <!--Preserve a property, its backing field (if present), and setter method-->
          <property signature="System.Int32 PropertyName" accessors="set" />
    
          <!--Preserve a property by name rather than signature-->
          <property name="PropertyName" />
    
          <!--Events-->
    
          <!--Preserve an event, its backing field (if present), add, and remove methods-->
          <event signature="System.EventHandler EventName" />
    
          <!--Preserve an event by name rather than signature-->
          <event name="EventName" />
    
        </type>
      </assembly>
    </linker>
    

The next example shows how you can declare entire assemblies:
    
    
    <!--Preserve an entire assembly-->
      <assembly fullname="AssemblyName" preserve="all"/>
    
      <!--No "preserve" attribute and no types specified means preserve all-->
      <assembly fullname="AssemblyName"/>
    
      <!--Fully qualified assembly name-->
      <assembly fullname="AssemblyName, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null">
        <type fullname="AssemblyName.Foo" preserve="all"/>
      </assembly>
    
      <!--Force an assembly to be processed for roots but don’t explicitly preserve anything in particular. Useful when the assembly isn't referenced.-->
      <assembly fullname="AssemblyName" preserve="nothing"/>
    

This example shows how to preserve either nested or generic types:
    
    
    <!--Examples with generics-->
        <type fullname="AssemblyName.G`1">
    
          <!--Preserve a field with generics in the signature-->
          <field signature="System.Collections.Generic.List`1&lt;System.Int32&gt; FieldName" />
    
          <field signature="System.Collections.Generic.List`1&lt;T&gt; FieldName" />
    
          <!--Preserve a method with generics in the signature-->
          <method signature="System.Void MethodName(System.Collections.Generic.List`1&lt;System.Int32&gt;)" />
    
          <!--Preserve an event with generics in the signature-->
          <event signature="System.EventHandler`1&lt;System.EventArgs&gt; EventName" />
    
        </type>
    
        <!--Preserve a nested type-->
        <type fullname="AssemblyName.H/Nested" preserve="all"/>
    
        <!--Preserve all fields of a type if the type is used.  If the type isn't used, it will be removed-->
        <type fullname="AssemblyName.I" preserve="fields" required="0"/>
    
        <!--Preserve all methods of a type if the type is used. If the type isn't used, it will be removed-->
        <type fullname="AssemblyName.J" preserve="methods" required="0"/>
    
        <!--Preserve all types in a namespace-->
        <type fullname="AssemblyName.SomeNamespace*" />
    
        <!--Preserve all types with a common prefix in their name-->
        <type fullname="Prefix*" />
    

### Additional Assembly XML attributes

The `<assembly>` element of the link.xml file has three special-purpose attributes that you can enable for more control over the annotations.

  * `ignoreIfMissing`: Use this attribute if you need to declare preservations for an assembly that doesn’t exist during all Player builds.

    
    
    <linker>
      <assembly fullname="Foo" ignoreIfMissing="1">
        <type name="TypeName"/>
      </assembly>
    </linker>
    

  * `ignoreIfUnreferenced:` In some cases, you might want to preserve entities in an assembly only when that assembly is referenced by another assembly. Use this attribute to preserve the entities in an assembly only when at least one type is referenced in an assembly.

    
    
    <linker>
      <assembly fullname="Bar" ignoreIfUnreferenced="1">
        <type name="TypeName"/>
      </assembly>
    </linker>
    

  * `windowsruntime:` When you define preservations for a Windows Runtime Metadata (.winmd) assembly, you must add the `windowsruntime` attribute to the `<assembly>` element in the link.xml file:

    
    
    <linker>
      <assembly fullname="Windows" windowsruntime="true">
        <type name="TypeName"/>
     </assembly>
    </linker>
    

## Dependency annotations

Dependency annotations define dependencies between various code elements. These annotations are useful for preserving code patterns that the Unity linker can’t statically analyze, such as reflection. These annotations also ensure that these code elements aren’t erroneously preserved when no root element uses them. There are two methods you can use to change how the Unity linker processes code elements:

  * Annotation attributes: these attributes indicate that the Unity linker should preserve a particular code pattern, such as any type that derives from the annotated type.
  * AlwaysLinkAssemblyAttribute: use this attribute to indicate that the Unity linker should process an assembly even if it’s not referenced by any other assemblies in your Project.

### Annotation attributes

The `[Preserve]` attribute is useful for situations when an API is always needed. Other attributes can be useful for more general preservations. For example, you can preserve all types that implement a particular interface by annotating the interface with the RequireImplementorsAttribute.

To annotate specific coding patterns, use one or more of the following attributes:

  * RequireImplementorsAttribute: marks all types that implement this interface as dependencies.
  * RequireDerivedAttribute: marks all types that derive from this type as dependencies.
  * RequiredInterfaceAttribute: marks interface implementations on types as dependencies.
  * RequiredMemberAttribute: marks all members of a type as dependencies.
  * RequireAttributeUsagesAttribute: marks custom attributes as dependencies.

You can combine these attributes in various ways to more precisely control how the Unity linker preserves your code.

### AlwaysLinkAssembly attribute

The `[assembly: UnityEngine.Scripting.AlwaysLinkAssembly]` attribute forces the Unity linker to search an assembly regardless of whether or not the assembly is referenced by another assembly that is included in the build. You can apply the AlwaysLinkAssembly attribute only to an assembly.

The attribute doesn’t directly preserve code within the assembly. Instead, this attribute instructs the Unity linker to apply the root marking rules to the assembly. If no code elements match the root marking rules for the assembly, the Unity linker still removes the assembly from the build.

Use this attribute on precompiled or package assemblies that contain one or more methods with the `[RuntimeInitializeOnLoadMethod]` attribute, but which might not contain types used directly or indirectly in any **Scenes** in a project.

If an assembly defines `[assembly: AlwaysLinkAssembly]` and is also referenced by another assembly included in the build, the attribute has no effect on the output.