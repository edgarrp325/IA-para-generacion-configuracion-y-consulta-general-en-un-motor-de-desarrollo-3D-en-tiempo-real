---
title: "Managed stack traces with IL2CPP"
category: "General"
source_file: "IL2CPP-managed-stack-traces.html"
doc_type: "manual"
---

# Managed stack traces with IL2CPP

When an exception happens in managed code, the stack trace for the exception can help you understand the cause of the exception. This can often be found in the **player log** file. However, the managed stack trace might not appear the way you expect because the stack trace varies depending on the build configuration.​ ​

## C++ Compiler Configuration options

### Debug

When the C++ Compiler Configuration is set to Debug, **IL2CPP** reports a reliable managed stack trace, and includes each managed method in the call stack. The stack trace doesn’t include line numbers from the original C# source code. ​

### Release and master

When the C++ Compiler Configuration is set to Release or Master, IL2CPP might produce a call stack that’s missing one or more managed methods. This is because the C++ compiler has inlined the missing methods. Method inlining is usually good for performance at run time, but it can make call stacks more difficult to understand. IL2CPP always provides at least one managed method on the call stack. For stack traces created from managed exceptions, this is the method where the exception occurred. It also includes other methods if they aren’t inlined.​ ​

### Source code line numbers

IL2CPP call stacks do not include source code line number information in the debug or release configurations.