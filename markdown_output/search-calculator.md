---
title: "The calculator"
category: "General"
source_file: "search-calculator.html"
doc_type: "manual"
---

# The calculator

The Calculator Search Provider computes expressions directly in Search. Enter any expression that is valid in a numerical text field in Unity, and Search displays the result in the results area.

**NOTE:** This search requires a search token to execute it. You cannot make it an active Search Provider, or combine it with other Search Providers.

**Search token:** `=` (equals sign)

**Default action:** Logs the result of the expression to the console, and copies it to the clipboard.

**Context menu actions:**

Action: | Function:  
---|---  
**Exec** | Logs the result of the expression to the console, and copies it to the clipboard.  
  
> **Note:** To query this provider you need to explicitly add `=` to the query.  
  
---  
**Supported operators** | `+ - * / % ^ ( )` |  **Example:**  
`=42/34 + (56 % 6)`  
  
`=23 * 9 ^ 3`  
  
  
_Calculator Search Provider_