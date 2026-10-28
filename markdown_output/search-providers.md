---
title: "Search Providers"
category: "General"
source_file: "search-providers.html"
doc_type: "manual"
---

# Search Providers

Each type of search has its own Search Provider. A Search Provider allows you to search and filter content. Each Search Provider has a unique search token. A search token is a text string that you can use in the search field to search using only a specific Search Provider.

By default, all searches use Project, Hierarchy, and Settings Search Providers unless you exclude them.

Search provides additional opt-in Search Providers. Search ignores opt-in Search Providers unless you explicitly use them. Opt-in Search Providers differ from default Search Providers in the following ways:

You can only execute them using their search tokens. You cannot combine an opt-in Search Provider with any other Search Provider.

  * To perform a search using all default Search Providers, enter the search terms in the search field. Results appear as you type.

  * To perform a search using an opt-in Search Provider, prefix the search terms with the Search Provider’s search token.  
  
Open the **More**(**⋮**) menu to view a list of Search Providers and their prefixes.  

## Default Search Providers

Provider: | Function: | Search token: | Example:  
---|---|---|---  
Project | Searches Project Assets. |  `p:` (for “project”) |  `p:Player`   
  
Searches for Assets that match the term “Player”.  
Hierarchy | Searches GameObjects in the Scene. |  `h:` (for “hierarchy”) |  `h:Main Camera`   
  
Searches the current Scene for GameObjects that match the term “Main Camera”.  
Settings | Searches all Project Settings and Preferences. | `set:` |  `set:VFX`   
  
Finds Project Settings and Preferences pages that match the term “VFX”.  
  
## Opt-in Search Providers

Provider: | Function: | Search token: | Example:  
---|---|---|---  
Expression | This token is not required. Search expressions are recognized without a token. |  |   
Menus | Searches the Unity main menu. | `m:` |  `m:TextMesh Pro`  
  
Searches the Unity main menu for commands that contain “TextMesh Pro.”  
Asset Database | Searches the AssetDatabase. This is useful when searching the Editor resource bundle (containing all icons/resources used to build the editor) because those binary resources are not indexed. | `adb:`  
Help | Searches the help. | `?` |  `?asset`   
  
Searches for help entries containing the word “Asset”.  
Calculator | Computes mathematical expressions. | `=` |  `=2*3+29/2`   
  
Calculates the answer to the expression `2*3+29/2`.  
Files | Searches for files | `find:` |  `find:Paint Mat`  
  
Searches for all assets paths containing the words paint AND the word mat (e.g.: PaintBrush_Mat.mat, DryWallPainted_Mat.mat)  
Static API Method | Finds and executes static API methods. | `api` |  `#Mesh`   
  
Searches for static API methods with “Mesh” in their names.  
Packages | Searches the Unity package database. | `pkg:` |  `pkg:vector`  
  
Searches the Unity package database for packages that match the term “vector”.  
Asset Store | Searches the Unity Asset Store. | `store:` |  `store:texture`   
  
Searches the Unity Asset Store for Assets that match the term “texture”.  
Performance | Searches all the performance trackers available in Unity. This is useful for searching for performance bottlenecks. | `performance:` |   
Saved Queries | Searches for saved queries | `q:` |  `q:enemies`   
  
Searches all Search Query assets containing the word enemies.  
Logs | Searches the `Editor.log` file | `log:` |  `log:cache`  
  
Searches the `Editor.log` file for information that matches “cache”. |   
  
You can also create your own Search Providers.

## Exclude Search Providers

You can exclude specific Search Providers from a regular search. To exclude a provider, do one of the following:

  * Mute a provider from the Filters pane. When you mute a provider, Search does not use it in searches, but its background activities (such as indexing parts of Unity) continue to run.
  * Disable a provider from the preferences. When you disable a provider, Search does not use it at all, and stops all of its background activities.