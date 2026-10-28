---
title: "Search the Unity Asset Store"
category: "General"
source_file: "search-asset-store.html"
doc_type: "manual"
---

# Search the Unity Asset Store

The **Asset Store** Search Provider searches the Unity Asset Store. The Preview **Inspector** Search Provider searches the Unity Asset Store. The Preview **Inspector** displays a preview of each item. Open the Asset Store to see more information about an Asset, such as its name, price, publisher, and category.

**NOTE:** This search requires a search token to execute it. You cannot make it an active Search Provider, or combine it with other Search Providers.

**Search token:** `store:`

**Default action:** Opens the Unity Asset Store web site to the Asset’s page.

**Context menu actions:**

Action: | Function:  
---|---  
**Open Unity Asset Store** | Opens the Unity Asset Store web site to the Asset’s page.  
  
  
_Asset Store Search Provider_

## Sub-filters

Use these tokens to limit your search results.

Filter | Search token | Description  
---|---|---  
**Minimum price** | `store: min_price:number` |  `store: min_price:5 bolt`  
  
Searches for Assets with a minimum price of 5$ and the word `bolt` in their name.  
**Maximum price** | `store: max_price:number` |  `store: max_price:5 bolt`  
  
Searches for Assets with a maximum price of 5$ and the word `bolt` in their name.  
**Publisher** | `store: publisher:name` |  `store: publisher:Gargore`  
  
Searches for Assets published by the company Gargore. Note that the publisher name must be exact.  
**Version** | `store: version:number` |  `store: version:2017`  
  
Searches for Assets that minimally support Unity 2017.  
**Free** | `store: free:boolean` |  `store: free:true asteroid`  
  
Searches for Assets that are free and that have the word `asteroid` in their name.  
**On sale** | `store: on_sale:boolean` |  `store: on_sale:true max_price:5`  
  
Searches for Assets that are on sale and that have a max price of 5$.