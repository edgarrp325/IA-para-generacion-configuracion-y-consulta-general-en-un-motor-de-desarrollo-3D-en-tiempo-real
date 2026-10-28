---
title: "Property paths"
category: "General"
source_file: "property-paths.html"
doc_type: "manual"
---

# Property paths

Property paths are strings that describe the location of a property within a container object.

## Concept

You can use property paths to get or set the data of an object at a specific path or accept a visitor on a sub-property of an object.

Property paths are constructed from strings and resolve a specific property instance from a root object. For example, the path `foo.bar.baz[12]` resolves the 13th element of the `baz` list container within the `bar` container, which is nested inside the `foo` container.

To create and manipulate property paths, use the `Unity.Properties.PropertyPath` class.

You can use property paths to do the following:

  * Get or set the data of an object at a specific path
  * Accept a visitor on a sub-property of an object

## Performance considerations

`Unity.Properties.PropertyPath` is an **immutable** struct type. When you construct a property path from a string, allocations occur for sub-string extraction.

The following table lists the allocation behaviors when a property path is constructed from a string:

String | Length | Allocations | Allocations reason  
---|---|---|---  
`"Path"` | 1 | 0 | Use the string as-is.  
`"Path.To"` | 2 | 2 | Split the string into two parts.  
`"Path.To[2]"` | 3 | 3 | Split the string into two parts and extract the index.  
`"Path.To[2].My"` | 4 | 4 |   
`"Path.To[2].My.Value"` | 5 | 6 | Allocate an array for the additional parts.  
  
The following table lists the allocation behaviors when a property path is constructed from parts:

String | Length | Allocations | Allocations reason  
---|---|---|---  
`PropertyPath.FromName("Path")` | 1 | 0 |   
`PropertyPath.AppendName(previous, "To")` | 2 | 0 |   
`PropertyPath.AppendIndex(previous, 2)` | 3 | 0 |   
`PropertyPath.AppendName(previous, "My")` | 4 | 0 |   
`PropertyPath.AppendName(previous, "Value")` | 5 | 1 | Allocate an array for the additional parts.  
  
To optimize performance and avoid allocating memory:

  * Initialize and cache property paths during initialization routines.
  * Combine or append property path parts instead of constructing it from a string, up to four parts.

## Additional resources

  * Property bags
  * Property visitors
  * Use `PropertyVisitor` to create a property visitor
  * Use low-level APIs to create a property visitor