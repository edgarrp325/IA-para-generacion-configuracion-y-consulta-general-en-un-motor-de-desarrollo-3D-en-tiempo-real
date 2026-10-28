---
title: "The Unity linker"
category: "General"
source_file: "unity-linker.html"
doc_type: "manual"
---

# The Unity linker

The Unity build process uses a tool called the Unity linker to strip managed code. The Unity linker is a version of the IL Linker customized to work with Unity. The custom Unity Engine specific parts of the Unity linker aren’t publicly available.

The Unity linker is responsible for both managed code stripping and part of the process of engine code stripping, which is a separate process available through the **IL2CPP** script backend that removes unused engine code. For more information, see PlayerSettings.StripEngineCode].

## How the Unity linker works

The Unity linker analyzes all the assemblies in your project. First, it marks root types, methods, properties, and fields. For example, MonoBehaviour-derived classes you add to **GameObjects** in a **Scene** in a **Scene** are root types. The Unity linker then analyzes the roots it has marked to identify, and marks any managed code that these roots depend upon. Upon completion of this static analysis, any remaining unmarked code is unreachable by any execution path through your application code and the Unity linker deletes it from the assembly.

## How the Unity linker strips assemblies

The Unity Editor creates a list of the assemblies that contain types used in any of the Scenes in your Unity project and passes this list to the Unity linker. The Unity linker then processes those assemblies, any references of those assemblies, any assemblies declared in a link.xml file, and any assemblies with the AlwaysLinkAssembly attribute. In general, the Unity linker doesn’t process assemblies included in your project that don’t fall under one of these categories, and excludes them from the Player build.

For each assembly the Unity linker processes, it follows a set of rules based on the classification of the assembly, whether the assembly contains types used in a Scene, and the **Managed Stripping Level** you have selected for the build.

For the purpose of these rules, assemblies fall into the following classifications:

  * .NET Class Library assemblies — Includes the Mono class libraries such as mscorlib.dll and System.dll, as well as .NET class library facade assemblies like netstandard.dll.
  * Platform SDK assemblies — Includes the managed assemblies specific to a platform SDK. For example, the windows.winmd assembly that is part of the Universal Windows Platform SDK.
  * Unity Engine Module assemblies — Includes the managed assemblies that make up the Unity Engine, such as UnityEngine.Core.dll.
  * Project assemblies — Includes the assemblies specific to a project such as: 
    * Script assemblies such as Assembly-CSharp.dll
    * Precompiled assemblies
    * Assembly Definition Assemblies
    * Package assemblies

## Marking rules

When you build a project in Unity, the build process compiles your C# code to a .NET bytecode format called Common Intermediate Language (CIL). Unity packages this CIL byte code into files called assemblies. The .NET framework libraries and any C# libraries in the plugins you use in your project are also pre-packaged as assemblies of CIL bytecode.

When the Unity linker performs its static analysis, it follows sets of rules to determine which parts of the CIL bytecode the Unity linker marks as necessary for the build. Root marking rules determine how the Unity linker identifies and preserves top-level assemblies in the build. Dependency marking rules determine how the Unity linker identifies and preserves any code that the root assemblies depend on.

The **Managed Stripping Level** property changes the set of rules that the Unity linker uses. The following sections describe the marking rules for each possible setting for the **Managed Stripping Level** property.

### Root marking rules

The following table describes how the Unity linker identifies the top-level types in an assembly:

**Assembly type:** | **Marking rules:**  
---|---  
| **Minimal** | **Low** | **Medium** | **High**  
**.NET Class & Platform SDK and UnityEngine Assemblies** | Applies precautionary preservations and any preservations defined in any link.xml file. | Applies precautionary preservations and any preservations defined in any link.xml file. | Applies any preservations defined in any link.xml file. | Applies any preservations defined in any link.xml file.  
**Assemblies with types referenced in a scene** | Marks all types and members in the assembly. | Marks all types and members in the assembly. | Marks the following:  
•All methods which have the `[RuntimeInitializeOnLoadMethod]` or `[Preserve]` attribute.  
•Preservations defined in any link.xml file.  
•Marks all types derived from MonoBehaviour and ScriptableObject in precompiled, package, Unity Script or assembly definition assemblies. | Marks the following:  
•All methods which have the `[RuntimeInitializeOnLoadMethod]` or `[Preserve]` attribute.  
•Preservations defined in any link.xml file.  
•Marks all types derived from MonoBehaviour and ScriptableObject in precompiled, package, Unity Script or assembly definition assemblies.  
**All other** | Marks all types and members in the assembly. | Marks the following:  
•All public types and public members of those types.  
•All methods which have the `[RuntimeInitializeOnLoadMethod]` or `[Preserve]` attribute.  
•Preservations defined in any link.xml file.  
•All types derived from MonoBehaviour and ScriptableObject in precompiled, package, Unity Script or assembly definition assemblies. | Marks the following:  
•All public types and public members of those types.  
•All methods which have the `[RuntimeInitializeOnLoadMethod]` or `[Preserve]` attribute.  
•Preservations defined in any link.xml file.  
•All types derived from MonoBehaviour and ScriptableObject in precompiled, package, Unity Script or assembly definition assemblies. | Marks the following:  
•All methods which have the `[RuntimeInitializeOnLoadMethod]` or `[Preserve]` attribute.  
•Preservations defined in any link.xml file.  
•All types derived from MonoBehaviour and ScriptableObject in precompiled, package, Unity Script or assembly definition assemblies.  
**Test** | Marks any methods with the `[UnityTest]` attribute and any methods annotated with an Attribute defined in the NUnit.Framework.  
  
### Dependency marking rules

After the Unity linker identifies the roots in an assembly, it needs to identify any code that those roots depend on. The following table describes how the Unity linker identifies dependencies of root types in an assembly:

**Rule Target** | **Action at each stripping level**  
---|---  
| **Minimal** | **Low** | **Medium** | **High**  
**MonoBehaviour** | The Unity linker marks all members of a MonoBehavior type when it marks the type.  
**ScriptableObject** | The Unity linker marks all members of a ScriptableObject type when it marks the type.  
**Attributes** | When the Unity linker marks an assembly, type or other code structure, it also marks all attributes of those structures. | When the Unity linker marks an assembly, type or other code structure, it also marks all attributes of those structures. | When the Unity linker marks an assembly, type or other code structure, it only marks attributes of those structures if the attribute type is also marked. | When the Unity linker marks an assembly, type or other code structure, it only marks attributes of those structures if the attribute type is also marked.  
**Debugging Attributes** | When script debugging is enabled, the Unity linker marks all members that have the `[DebuggerDisplay]` attribute, even when there isn’t a code path that uses those members. | When script debugging is enabled, the Unity linker marks all members that have the `[DebuggerDisplay]` attribute, even when there isn’t a code path that uses those members. | The Unity linker always removes debugging attributes such as DebuggerDisplayAttribute and DebuggerTypeProxyAttribute. | The Unity linker always removes debugging attributes such as DebuggerDisplayAttribute and DebuggerTypeProxyAttribute.  
**.NET Facade Class Library** | Removes facade assemblies since they aren’t necessary at runtime.  
  
## Link XML feature tag exclusions

Link.xml files support an uncommonly used “features” XML attribute. In the example, the mscorlib.xml file embedded in mscorlib.dll uses this attribute, but you can use it in any link.xml file, when appropriate.

When you use the **High** stripping level, the Unity linker excludes preservations for features that aren’t supported based on the settings for the current build:

  1. remoting — Excluded when targeting the IL2CPP **scripting backend**.
  2. sre — Excluded when targeting the IL2CPP scripting backend.
  3. com — Excluded when targeting platforms that don’t support COM.

For example, the following link.xml file preserves one method of a type on platforms that support COM, and one method on all platforms:
    
    
    <linker>
    
        <assembly fullname="Foo">
    
            <type fullname="Type1">
    
                <!--Preserve FeatureOne on platforms that support COM-->
    
                <method signature="System.Void FeatureOne()" feature="com"/>
    
                <!--Preserve FeatureTwo on all platforms-->
    
                <method signature="System.Void FeatureTwo()"/>
    
            </type>
    
        </assembly>
    
    </linker>
    

## Editing of method bodies

When you use the **High** stripping level, the Unity linker edits method bodies to further reduce code size. This section summarizes some of the notable edits that the Unity linker makes to method bodies.

The Unity linker only edits method bodies in the .NET Class Library assemblies. After method body editing, the source code of the assembly no longer matches the compiled code in the assembly, which can make debugging more difficult.

The following list describes actions that the Unity linker can perform to edit a method body:

  * Remove unreachable branches - The Unity linker removes If-statement blocks that check System.Environment.OSVersion.Platform and aren’t reachable for the currently targeted platform.
  * Inline methods that only access fields - The Unity linker replaces calls to methods that get or set a field with direct access to the field. This often makes it possible to strip away the method entirely. When you use the Mono backend, the Unity linker only makes this change when the caller of the method is allowed to directly access the field, based on the field’s visibility. For IL2CPP, visibility rules don’t apply, so the Unity linker makes this change where appropriate.
  * Inline methods that return a const value - The Unity linker inlines calls to methods that only return a const value.
  * Remove empty non-returning calls - The Unity linker removes calls to methods that are empty and have a void return type.
  * Remove empty scope - The Unity linker removes Try/Finally blocks when the Finally block is empty. Removing empty calls can create empty Finally blocks. When that happens during method editing, Unity linker removes the entire Try/Finally block. One scenario where this can occur is when the compiler generates Try/Finally blocks as part of foreach loops in order to call Dispose().