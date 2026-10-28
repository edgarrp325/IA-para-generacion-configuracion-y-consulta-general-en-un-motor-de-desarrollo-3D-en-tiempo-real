---
title: "Search usage"
category: "General"
source_file: "search-usage.html"
doc_type: "manual"
---

# Search usage

To use Search, do the following:

  1. Launch Search
  2. Search
  3. Perform actions on items in the results

## Launch Search

There are several ways to open the Search window:

  * From the Unity menu, choose **Edit** > **Search All**.
  * Click the magnifying glass icon in the top right in the **Editor** window.

Shortcuts:

Shortcut: | Function:  
---|---  
**Ctrl + K** | Open Search  
  
> **Tip:** You can change the keyboard shortcuts used to launch Search from the Shortcuts Manager.
> 
> **Note:** The last search term you used appears in the search field and the last changes you made to the filter configuration are still in effect.

### Keep the Search window opening

To keep the window open after selecting a search item, select **Keep Open** from the **More Options** (**:**) menu.

## Perform searches

To perform searches, type a query into the search field.

For most search queries, using the **Search All** window and the default Asset index created with your project will find your content effectively.

For more refined searches, use specific Search Providers and Search Expressions.

To include packages in your search, select **Show package results** from the **More Options** (**:**) menu.

## View search results

Use **Alt + ↑** (up arrow) and **↓** (down arrow) cycle through the search history, or choose a saved search from the left pane.

### Change the search results view

Use the sizing slider to change from a list to grid view with thumbnails, or use the List view icon, the Grid view icon, or the Table view icon in the bottom right of the **Search** window to change the search view.

### Add favorite search result items

Click the star next to a search result item to tag that item to appear at the top of the search list the next time you perform the same search to find it more easily.

### Search status

To see the search time and the number of results at the bottom of the search window, select **Show Status** from the **More Options** (**:**) menu.

## Save searches

Saving searches allows you to keep useful searches to reuse as needed. Save the search to your personal Unity for your own use (User), or to project to save it as an Asset to make the search available to anyone working on the project.

To save a search to your personal version of Unity:

  1. Create your search.
  2. Click the drop-down menu next to the Save icon at the top-right of the Search window and choose **Save User**.   
Your search is added to the **Saved Searches** panel in the **Search** window.
  3. To save again after making changes, highlight the search in the **Saved Searches** window and from the Save drop-down menu at the top-right of the Search window, choose **Save <search name>**

You may also click the Save icon next to User in the **Saved Searches** panel.

To save a search to the project:

  1. Create your search.
  2. Click the drop-down menu next to the Save icon at the top-right of the **Search** window and choose **Save Project**.
  3. Enter a file name in the **Save search query** window, and chose **Save**.   
Your search is added to the **Saved Searches** panel in the Search window.
  4. To save again after making changes, highlight the search in the **Saved Searches** window and from the Save drop-down menu at the top-right of the Search window, choose **Save <search name>**

You may also click the Save icon next to Project in the **Saved Searches** panel.

## Find saved searches

To find a saved search:

  1. Click the magnifying glass icon in the **Saved Searches** panel.
  2. Enter your saved search name, or a part of the name. If found, it will appear in the panel.

## Actions

After you search, you can perform actions on the items Search returns in the Preview **Inspector** pane or through **More Options** (**⋮**) . The actions you can perform depend on the type of item.

For example, if Search returns a package, you can install/uninstall it. If Search returns an Asset, you can select, open, or highlight it in the Hierarchy window.

  * Every type of item has a default action.
  * Some items support additional actions via a context menu.
  * Some items also support drag and drop actions.

To find out which actions you can perform on different types of items, see the Search Provider pages for individual search filters.

### Default actions

Every type of item has a default action.

To perform the default action for an item do one of the following:

  * Double-click the item.
  * Select the item and use **Enter**.

**Note:** You can edit the default actions in the **Search** section of the **Preferences** page.

### Additional actions

Some items support additional actions that you access from the Preview Inspector menu.

To access the additional actions context menu for an item, do one of the following:

  * Right-click the item.
  * In the item entry, select **More Options** (**⋮**).

You can also use the **Alt + Enter** shortcut to perform a secondary action on a selected item without opening the context menu.

### Drag and drop actions

Some Search Providers (for example, the Asset and Scene and Scene providers) support drag and drop actions. You can drag items from the results area to any part of Unity that supports them, for example, the Hierarchy window, the **Scene view** providers) support drag and drop actions. You can drag items from the results area to any part of Unity that supports them, for example, the Hierarchy window, the **Scene view** , or the Inspector.