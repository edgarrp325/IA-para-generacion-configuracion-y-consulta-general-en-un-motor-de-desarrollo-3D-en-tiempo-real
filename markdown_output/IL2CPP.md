---
title: "IL2CPP Overview"
category: "General"
source_file: "IL2CPP.html"
doc_type: "manual"
---

# IL2CPP Overview

The ****IL2CPP**** (Intermediate Language To C++) **scripting backend** is an alternative to the Mono backend. IL2CPP provides better support for applications across a wider range of platforms. The IL2CPP backend converts MSIL (Microsoft Intermediate Language) code (for example, C# code in scripts) into C++ code, then uses the C++ code to create a native binary file (for example, .exe, .apk, or .xap) for your chosen platform.

This type of compilation, in which Unity compiles code specifically for a target platform when it builds the native binary, is called ahead-of-time (AOT) compilation. The Mono backend compiles code at runtime, with a technique called just-in-time compilation (JIT).

On this page:

  * Building a project using IL2CPP
  * How IL2CPP works
  * Optimising IL2CPP build times
  * Enabling runtime checks using IL2CppSetOption

Some platforms don’t support **AOT compilation** , so the IL2CPP backend doesn’t work on every platform. Other platforms support AOT and IL2CPP, but don’t allow JIT compilation, and so can’t support the Mono backend. When a platform can support both backends, Mono is the default. For more information, see Scripting restrictions.

IL2CPP can improve performance across a variety of platforms, but the need to include machine code in built applications increases both the build time and the size of the final built application. For more information, see How IL2CPP works and the blog series An introduction to IL2CPP internals.

IL2CPP supports the debugging of managed code in the same way as the Mono scripting backend. For more information, see Debugging C# code in Unity.

##  Building a project using IL2CPP

To build a project with IL2CPP, you need to have the backend installed in your Unity installation. You can select IL2CPP as an optional module when you first install a version of Unity, or add IL2CPP support to an existing installation through the Unity Hub. For more information, see Installing the Unity Hub and Add modules to the Unity Editor.

IL2CPP also requires some systems native to the target platform to generate the C++ code. This means that to use IL2CPP on a specific platform, you need to build the application on that platform. For example, to use IL2CPP with MacOS as a build target, you need to build the application on a machine that uses MacOS. For more information about system requirements for desktop platforms, including IL2CPP requirements for individual platforms, see the Desktop section of System Requirements for Unity.

You can change the scripting backend Unity uses to build your application in one of two ways:

  * Through the ****Player Settings**** menu in the Editor. Perform the following steps to change the scripting backend through the **Player Settings** menu:

    1. Go to **Edit** > **Project Settings**.
    2. Click on the **Player Settings** button to open the **Player** settings for the current platform in the **Inspector**.
    3. Navigate to the **Configuration** section heading under the **Other Settings** sub-menu.
    4. Click on the **Scripting Backend** dropdown menu, then select **IL2CPP**.

You can also open the **Player Settings** menu from inside the **Build Settings** menu; go to **File** > **Build Settings** and click on the **Player Settings** button.

  * Through the Editor scripting API. Use the PlayerSettings.SetScriptingBackend property to change the scripting backend that Unity uses.

The **Configuration** section of the **Player** settings

To start the build process, open the **Build Settings** window and click the **Build** button. Unity then converts your C# code and assemblies into C++ and finally produces a binary file for your target platform.

##  How IL2CPP works

When you start a build using IL2CPP, Unity automatically performs the following steps:

  1. The Roslyn C# compiler compiles your application’s C# code and any required package code to .NET DLLs (managed assemblies).
  2. Unity applies managed bytecode stripping. This step can significantly reduce the size of a built application.
  3. The IL2CPP backend converts all managed assemblies into standard C++ code.
  4. The C++ compiler compiles the generated C++ code and the runtime part of IL2CPP with a native platform compiler.
  5. Unity creates either an executable file or a DLL, depending on the platform you target.

Both IL2CPP and Mono provide a few useful options which you can control with attributes in your **scripts**. For more information, see Platform-dependent compilation.

IL2CPP enables Unity to pre-compile code for specific platforms. The binary file Unity produces at the end of this process already contains necessary machine code for the target platform, while Mono has to compile this machine code at runtime during execution. AOT compilation does increase build time, but it also improves compatibility with the target platform and can improve performance.

Both scripting backends require a new build for each platform you want to target. For example, to support both the Android and iOS platforms, you need to build your application twice and produce two binary files.

The assembly stripping stage helps reduce the final binary size. Unity removes any bytecode that the final built application doesn’t use.

##  Optimizing IL2CPP build times

Project build times when using IL2CPP can be significantly longer than when using Mono. However, you can do several things to reduce build time.

**Exclude your project from anti-malware software scans**

You can exclude your Unity project folder and target build folders from anti-malware software scans before you build your project.

**Store your project and target build folder on a solid-state drive (SSD)**

Solid-state drives (SSDs) have faster read/write speeds than traditional hard disk drives (HDD). Converting IL code to C++ and compiling it involves a large number of read/write operations, so a faster storage device speeds up this process.

**Change the IL2CPP Code Generation option in the Build Settings**

To change how IL2CPP generates code, open the Build Settings and configure the IL2CPP Code Generation option By default, the Faster runtime option is enabled, which produces more machine code that reduces the impact of IL2CPP at runtime. To reduce build times, you can set this option to Faster (smaller) builds. This method produces and includes less machine code in the binary executable and so can reduce performance at runtime, but also significantly reduces build times and binary size.

##  Enabling runtime checks using Il2CppSetOption

When you use the IL2CPP scripting backend, you can control how **il2cpp.exe** generates C++ code. You can use the **Il2CppSetOption** attribute to enable or disable the following runtime checks:

**Property:** | **Description:** | **Default:**  
---|---|---  
**Null checks** | If this option is enabled, the C++ code that IL2CPP generates contains null checks and throws managed NullReferenceException exceptions as necessary. If this option is disabled, IL2CPP doesn’t emit the null checks into the generated C++ code. For some projects, disabling this option might improve runtime performance.  
  
When this setting is disabled, Unity doesn’t prevent attempts to access null values in the generated code, which might lead to incorrect behavior. Your application is likely to crash soon after it dereferences the null value. Unity recommends that you don’t disable this option. | Enabled  
**Array bounds checks** | If this option is enabled, the C++ code that IL2CPP generates contains array bounds checks and throws managed IndexOutOfRangeException exceptions as necessary. If this option is disabled, IL2CPP doesn’t emit the array bounds checks into the generated C++ code.   
  
For some projects, disabling this option might improve runtime performance. However, when this option is disabled, Unity doesn’t prevent attempts to access an array with invalid indices in the generated code, which might lead to incorrect behavior, including reading from or writing to arbitrary memory locations. In most cases, these memory accesses occur without any immediate side effects, and can corrupt the state of the application with no obvious warning signs. This can make debugging these errors extremely difficult. Unity recommends that you keep this option enabled. | Enabled  
**Divide by zero checks** | If this option is enabled, C++ code generated by IL2CPP contains divide by zero checks for integer division and throw managed DivideByZeroException exceptions as necessary. If this option is disabled, IL2CPP doesn’t emit the divide by zero checks on integer division into the generated C++ code.   
  
These checks have an impact on performance at runtime. You should only enable this option if you need to run divide by zero checks; otherwise, leave it disabled. | Disabled  
  
To use the **Il2CppSetOption** attribute:

  1. In the directory where your Unity version is installed, navigate to the **Data\il2cpp** directory on Windows, or the **Contents/Frameworks/il2cpp** directory on OS X.
  2. Find the **Il2CppSetOptionAttribute.cs** source file.
  3. Copy the source file into your project’s **Assets** directory.

The below example describes how to use the **Il2CppSetOption** attribute:
    
    
    [Il2CppSetOption(Option.NullChecks, false)]
    public static string MethodWithNullChecksDisabled()
    {
        var tmp = new object();
        return tmp.ToString();
    }
    

You can apply the **Il2CppSetOption** attribute to assemblies, types, methods, and properties. Unity uses the attribute from the most local scope.
    
    
    [Il2CppSetOption(Option.NullChecks, false)]
    public class TypeWithNullChecksDisabled
    {
        public static string AnyMethod()
        {
            // Unity doesn’t perform null checks in this method.
            var tmp = new object();
            return tmp.ToString();
        }
    
        [Il2CppSetOption(Option.NullChecks, true)]
        public static string MethodWithNullChecksEnabled()
        {
            // Unity performs null checks in this method.
            var tmp = new object();
            return tmp.ToString();
        }
    }
    
    public class SomeType
    {
        [Il2CppSetOption(Option.NullChecks, false)]
        public string PropertyWithNullChecksDisabled
        {
            get
            {
                // Unity doesn’t perform null checks here.
                var tmp = new object();
                return tmp.ToString();
            }
            set
            {
                // Unity doesn’t perform null checks here.
                value.ToString();
            }
        }
    
        public string PropertyWithNullChecksDisabledOnGetterOnly
        {
            [Il2CppSetOption(Option.NullChecks, false)]
            get
            {
                // Unity doesn’t perform null checks here.
                var tmp = new object();
                return tmp.ToString();
            }
            set
            {
                // Unity performs null checks here.
                value.ToString();
            }
        }
    }
    

* * *

• 2018–05–15 Page amended