---
title: "Search for files"
category: "General"
source_file: "search-files.html"
doc_type: "manual"
---

# Search for files

The File Search Provider searches the file system to find files that match a specific pattern.

**NOTE:** This search requires a search token to execute it. You cannot make it an active Search Provider, or combine it with other Search Providers.

**Search token:** `find:`

**Default action:** Select the file.

**Context menu actions:**

Action | Function  
---|---  
**Select** | Selects the file in the **Project** window.  
**Open:** | Opens the file, either in Unity or an external editor.  
**Delete:** | Deletes the file.  
**Copy Path** | Copies the path of the file.  
**Reimport** | Reimports the file.  
**Reveal** | Selects the file in the operating system’s file browser.  
**Properties** | Opens the file’s property settings.  
  
Your search query can contain a C# regex to perform matching or glob expressions with the following wildcards. A glob expression is converted to a normal regex using the equivalency described in the table below:

Glob wildcards | Description | Example | Matches | Does not match | Equivalent regex  
---|---|---|---|---|---  
* | Matches any number of any characters including none | Law* | Law, Laws, Lawyer | Groklaw, La, aw | .*  
. | Matches any single character including none | Law. | Law, Laws | La, aw | .  
  
  
_File Search Provider_