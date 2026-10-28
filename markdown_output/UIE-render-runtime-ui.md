---
title: "Render UI in the Game view"
category: "General"
source_file: "UIE-render-runtime-ui.html"
doc_type: "manual"
---

# Render UI in the Game view

To render **UI** and react to input from the users in the Game view, connect the UXML Documents to a Panel Settings asset by a UI Document component.

Every UI Document component references a UXML Document that defines the UI and a Panel Settings that renders it. You can connect more than one UXML Document to a single Panel Settings asset.

## Configure a panel

A Panel Settings asset defines a panel in the **Scene**. The panel provides the root **visual element**. The panel provides the root **visual element** that UI hierarchies are attached to, and draws the UI in the Scene at runtime. How you configure the Panel Settings asset determines how the UI is rendered. It also determines how the UI reacts to input. For example, the panel that’s visually in the front intercepts clicks from the user before the panels that are visually in the back.

You can configure the Panel Settings asset to do the following:

  * Control scale and resolution
  * Apply default styles
  * Display UI on Render Textures
  * Set the panel’s sort order

To configure a panel:

  1. In your project, select **Assets** > **Create** > **UI Toolkit** > **Panel Settings** to create a Panel Settings asset if you don’t have it.
  2. In the **Inspector** window of the Panel Settings asset, configure the Panel Settings properties.

## Connect the UI to a panel

A panel can display UI from more than one UXML Document component. Each UI Document has a **Sort Order** property that sets the UXML Document rendering order: 

  * Child UI Document components are drawn on top of their parent UI Document components.
  * UI Documents components that are at the same level of the hierarchy are rendered in sequence according to their **Sort Order**.

To connect more than one UXML Document to a panel:

  1. Select or create a **GameObject** to host the UI. 

  2. Select **Component** > **UI Toolkit** > **UI Document** to add a UI Document component.

  3. In the Inspector window of the UI Document, do the following:

     * Set the **Panel Settings** to the Panel Settings to display the UI.
     * Set the **Source** to the UXML Document that contains the UI to display.
     * Set the **Sort Order** UI Document component with a smaller number rendered first.
  4. Repeat the process for each UXML Document.

**Note** : If there are multiple UI document components attached to the same Panel Settings, all these documents have a common focus navigation context. If they have distinct Panel Settings, navigation won’t jump automatically from one to the other even if you arrange them side by side. To make navigation jump from one to the other, you must set the `focusController` of the Panel Settings to the `FocusController` of the UI Document component you want to jump to.

## Lifecycle of UI Document components

Unity loads a UI Document component’s source UXML documents when it calls the `OnEnable()` method on the component. To ensure the **visual tree** loads correctly, add logic to interact with the controls inside the `OnEnable()` method. This means your script must respond to `OnEnable()` and `OnDisable()` to safely reference visual elements from your UXML documents.

A UI Document component clears its contents when it responds to the `OnEnable()` and `OnDisable()` methods. This approach removes UI elements that the UI Document won’t reuse soon and effectively clears the associated resources. Additionally, if a UI Document component isn’t assigned with a Panel Settings asset, it automatically clears its contents.

To hide a UI element that’s likely to be reused soon or needs to appear quickly to avoid an initialization penalty, set the `display` of the `UIDocument.rootVisualElement` to `none`. You can also use this to hide a UI element component that’s part of a larger UI hierarchy.

## Additional resources

  * Get started with runtime UI
  * Panel Settings properties reference
  * Runtime event system
  * FAQ for input and event systems with UI Toolkit