---
title: "Create a tabbed menu for runtime"
category: "General"
source_file: "UIE-create-tabbed-menu-for-runtime.html"
doc_type: "manual"
---

# Create a tabbed menu for runtime

**Version:** 2021.3+

Tabbed menus are common in video games and application **UI**. You can use UI Toolkit to create a tabbed menu for a custom Editor window or runtime. This example demonstrates how to create a tabbed menu in the sample **scene**. You can use UI Toolkit to create a tabbed menu for a custom Editor window or runtime. This example demonstrates how to create a tabbed menu in the sample **scene**. 

## Example overview

This example adds a menu in the sample scene. The menu has three tabs. Each tab presents certain content. When you click a tab, only the content associated with that tab is displayed. 

A preview of tabbed menu

To create tabbed content, you need to define the menu elements, styles, and logic.

You can find the completed files that this example creates in this GitHub repository.

## Prerequisites

This guide is for developers familiar with Unity, UI Toolkit, Flexbox, and C# scripting. Before you start, get familiar with the following:

  * Label
  * USS
  * UI Builder
  * Positioning elements with Flexbox

## Define the tabbed menu elements

Create two sections in your menu using the UI Builder, one for tabs and one for the content of tabs. In these sections, create three tab elements and three tab content elements.

  1. Create a project in Unity with any template.

  2. Click **GameObject** > **UI Toolkit** > **UI Document** to add a UI Document in the sample scene.

  3. Create a folder in `Assets` named `TabbedMenu` to store all your files.

  4. In the `TabbedMenu` folder, create a UI Document named `TabbedMenu.uxml`.

  5. Double-click `TabbedMenu.uxml` to open it in the UI Builder.

  6. Add two VisualElements named `tabs` and `tabContent` under the root.

  7. Under `tabs`, add three Label controls and give them the following Label texts:

     * `London`
     * `Paris`
     * `Ottawa`
  8. Under `tabContent`, add three Label controls and give them the following Label texts:

     * `London is the capital city of England`
     * `Paris is the capital of France`
     * `Ottawa is the capital of Canada`
  9. To associate the tab content with the tab, this example uses the same prefixes but different suffixes for the Label names. Each tab name has the `Tab` suffix and each tab content has the `Content` suffix. Set the tab Label names and content Label names to the following:

     * `LondonTab`
     * `ParisTab`
     * `OttawaTab`
     * `LondonContent`
     * `ParisContent`
     * `OttawaContent`

Your UI Builder Hierarchy looks like the following:

UI Builder Hierarchy

## Define the tabbed menu styles

Define the layout for tabs and tab content using USS. You can style the tabs and the tab content the way you like. This example arranges tabs in a row and on top of the tab content. It adds a background color for the selected tab and hides the un-selected tab content.

  1. In the `TabbedMenu` folder, create a stylesheet named `TabbedMenu.uss`.

  2. Open `TabbedMenu.uss` and add the following styling rules:
         
         /* Style for tabs */
         #tabs {
             flex-direction: row;
             background-color: rgb(229, 223, 223);
             -unity-font-style: bold;
             font-size: 14px;
         }
         
         /* Sets each label in tabs to have the same size. */
         .tab {
             flex-grow: 1;
         }
         
         /* Adds background color for the selected tab */
         .currentlySelectedTab {
             background-color: rgb(173, 166, 166);
         }
         
         /* Style for tabContent */
         #tabContent {
             background-color: rgb(255, 255, 255);
             font-size: 20px;
         }
         
         /* Hides the unselected tab content */
         .unselectedContent {
             display: none;
         }
         

  3. Open `TabbedMenu.uxml` in UI Builder.

  4. Click **Add Existing USS** and select `TabbedMenu.uss`.

  5. Apply your styles to the UI controls:

     * Apply `.tab` to each label under `tabs`
     * Apply `.currentlySelectedTab` to `LondonTab`
     * Apply `.unselectedContent` to `ParisContent` and `OttawaContent`

The finished `TabbedMenu.uxml` looks like the following:
    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" xsi="http://www.w3.org/2001/XMLSchema-instance" engine="UnityEngine.UIElements" editor="UnityEditor.UIElements" noNamespaceSchemaLocation="../../../UIElementsSchema/UIElements.xsd" editor-extension-mode="False">
       /* Your src might look different. If you save your UXML in UI Builder, USS file is referenced by the file location, fileID and guid. */
       <Style src="TabbedMenu-style.uss" />
       <ui:VisualElement>
            <ui:VisualElement name="tabs">
                <ui:Label name="LondonTab" text="London" class="tab currentlySelectedTab" />
                <ui:Label name="ParisTab" text="Paris" class="tab" />
                <ui:Label name="OttawaTab" text="Ottawa" class="tab" />
            </ui:VisualElement>
            <ui:VisualElement name="tabContent">
                <ui:Label text="London is the capital city of England" name="LondonContent" />
                <ui:Label text="Paris is the capital of France" name="ParisContent" class="unselectedContent" />
                <ui:Label text="Ottawa is the capital of Canada" name="OttawaContent" class="unselectedContent" />
            </ui:VisualElement>
       </ui:VisualElement>
    </ui:UXML>
    

## Set up the scene

Create a UIDocument **GameObject** in the SampleScene and add the UI Document as the source asset.

  1. In the SampleScene, select **GameObject** > **UI Toolkit** > **UI Document**.
  2. Select the **UIDocument** GameObject in the hierarchy and drag **TabbedMenu.uxml** from your **Project window** to the **Source Asset** field of the UI Document component in the **Inspector** to the **Source Asset** field of the UI Document component in the **Inspector** window. This references the source asset to the UXML file you created.

## Define the tabbed menu logic

Create a C# script that change the displayed tab content. When a user clicks a tab, the tab’s content displays and the current content hides. Create a MonoBehaviour script that attaches the tabbed menu logic to the game.

  1. In the `TabbedMenu` folder, create a C# script named `TabbedMenuController.cs` with the following contents:
         
         // This script defines the tab selection logic.
         using UnityEngine.UIElements;
         
         public class TabbedMenuController
         {
             /* Define member variables*/
             private const string tabClassName = "tab";
             private const string currentlySelectedTabClassName = "currentlySelectedTab";
             private const string unselectedContentClassName = "unselectedContent";
             // Tab and tab content have the same prefix but different suffix
             // Define the suffix of the tab name
             private const string tabNameSuffix = "Tab";
             // Define the suffix of the tab content name
             private const string contentNameSuffix = "Content";
         
             private readonly VisualElement root;
         
             public TabbedMenuController(VisualElement root)
             {
                 this.root = root;
             }
         
             public void RegisterTabCallbacks()
             {
                 UQueryBuilder<Label> tabs = GetAllTabs();
                 tabs.ForEach((Label tab) => {
                     tab.RegisterCallback<ClickEvent>(TabOnClick);
                 });
             }
         
             /* Method for the tab on-click event: 
         
                - If it is not selected, find other tabs that are selected, unselect them 
                - Then select the tab that was clicked on
             */
             private void TabOnClick(ClickEvent evt)
             {
                 Label clickedTab = evt.currentTarget as Label;
                 if (!TabIsCurrentlySelected(clickedTab))
                 {
                     GetAllTabs().Where(
                         (tab) => tab != clickedTab && TabIsCurrentlySelected(tab)
                     ).ForEach(UnselectTab);
                     SelectTab(clickedTab);
                 }
             }
             //Method that returns a Boolean indicating whether a tab is currently selected
             private static bool TabIsCurrentlySelected(Label tab)
             {
                 return tab.ClassListContains(currentlySelectedTabClassName);
             }
         
             private UQueryBuilder<Label> GetAllTabs()
             {
                 return root.Query<Label>(className: tabClassName);
             }
         
             /* Method for the selected tab: 
                -  Takes a tab as a parameter and adds the currentlySelectedTab class
                -  Then finds the tab content and removes the unselectedContent class */
             private void SelectTab(Label tab)
             {
                 tab.AddToClassList(currentlySelectedTabClassName);
                 VisualElement content = FindContent(tab);
                 content.RemoveFromClassList(unselectedContentClassName);
             }
         
             /* Method for the unselected tab: 
                -  Takes a tab as a parameter and removes the currentlySelectedTab class
                -  Then finds the tab content and adds the unselectedContent class */
             private void UnselectTab(Label tab)
             {
                 tab.RemoveFromClassList(currentlySelectedTabClassName);
                 VisualElement content = FindContent(tab);
                 content.AddToClassList(unselectedContentClassName);
             }
         
             // Method to generate the associated tab content name by for the given tab name
             private static string GenerateContentName(Label tab) =>
                 tab.name.Replace(tabNameSuffix, contentNameSuffix);
         
             // Method that takes a tab as a parameter and returns the associated content element
             private VisualElement FindContent(Label tab)
             {
                 return root.Q(GenerateContentName(tab));
             }
         }
         

  2. In the `TabbedMenu` folder, create a C# script named`TabbedMenu.cs` with the following contents:
         
         // This script attaches the tabbed menu logic to the game.
         using UnityEngine;
         using UnityEngine.UIElements;
         
         //Inherits from class `MonoBehaviour`. This makes it attachable to a game object as a component.
         public class TabbedMenu : MonoBehaviour
         {
             private TabbedMenuController controller;
         
             private void OnEnable()
             {
                 UIDocument menu = GetComponent<UIDocument>();
                 VisualElement root = menu.rootVisualElement;
         
                 controller = new(root);
         
                 controller.RegisterTabCallbacks();
             }
         }
         

  3. Select **UIDocument** in the SampleScene and drag the `TabbedMenu.cs` to **Add Component** in the Inspector. 

  4. Enter Play mode and click different tabs to see different contents.

## Additional resources

  * Get started with runtime UI
  * Render UI in the Game view
  * Panel Settings properties
  * Runtime event system