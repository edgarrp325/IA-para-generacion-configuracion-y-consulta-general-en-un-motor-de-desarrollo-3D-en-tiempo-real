---
title: "Bind to a UXML template"
category: "General"
source_file: "UIE-bind-uxml-template.html"
doc_type: "manual"
---

# Bind to a UXML template

**Version** : 2021.3+

This example demonstrates how to set binding paths with UXML templates.

## Example overview

This example creates an asset menu item. The menu creates a `GameSwitch` asset with three template instances that bind to properties of the `GameSwitch` object.

A preview of the GameSwitch Inspector

You can find the completed files that this example creates in this GitHub repository.

## Prerequisites

This guide is for developers familiar with the Unity Editor, **UI** Toolkit, and C# scripting. Before you start, get familiar with the following:

  * UI Builder
  * Visual Tree
  * UXML
  * USS

## Create the GameSwitch asset

Create **scripts** to define the `GameSwitch` struct and a custom asset to hold properties of the `GameSwitch` struct.

  1. Create a project in Unity with any template.

  2. In your **Project window** , create a folder named `bind-uxml-template` to store all your files.

  3. Create a C# script named `GameSwitch.cs` and replace its content with the following:
         
         using System;
         
         [Serializable]
         public struct GameSwitch
         {
             public string name;
             public bool enabled;
         }
         

  4. Create a C# script named `GameSwitchesAsset.cs` and replace its contents with the following: 
         
         using UnityEngine;
         
         [CreateAssetMenu(menuName = "UIToolkitExamples/GameSwitches")]
         public class GameSwitchesAsset : ScriptableObject
         {
             public GameSwitch useLocalServer;
             public GameSwitch showDebugMenu;
             public GameSwitch showFPSCounter;
         
             // Use the Reset function to provide default values
             public void Reset()
             {
                 useLocalServer = new GameSwitch() { name = "Use Local Server", enabled = false };
                 showDebugMenu = new GameSwitch() { name = "Show Debug Menu", enabled = false };
                 showFPSCounter = new GameSwitch() { name = "Show FPS Counter", enabled = true };
             }
         }
         

## Create the UXML template and files

Create a UXML template that you can use for each `GameSwitch` struct instance, and a UXML file that uses the template.

  1. Create a UI Document named `game_switch.uxml` and replace its contents with the following:
         
         <UXML xmlns="UnityEngine.UIElements" xmlns:ue="UnityEditor.UIElements">
             <Box style="flex-direction: row;">
                 <Toggle binding-path="enabled" />
                 <TextField binding-path="name" readonly="true" style="flex-grow: 1;"/>
             </Box>
         </UXML>
         

  2. In the **bind-uxml-template** folder, create a folder named `Editor`.

  3. In the **Editor** folder, create a UI Document named `game_switches_editor.uxml` and replace its contents with the following: 
         
         <UXML xmlns="UnityEngine.UIElements" xmlns:ue="UnityEditor.UIElements">
             <Template name="switch" src="../game_switch.uxml"/>
             <Instance template="switch" binding-path="useLocalServer" />
             <Instance template="switch" binding-path="showDebugMenu" />
             <Instance template="switch" binding-path="showFPSCounter" />
         </UXML>
         

**Note** : This is the main UXML file for the custom Editor. Each property binds to an instance of `game_switch.uxml` through the `binding-path` attribute of `Instance` .

## Create the asset menu and the asset

Create a script to register a custom Editor for `GameSwitchesAsset`.

  1. Create a C# script named `GameSwitchesEditor.cs` and replace its content with the following:
         
         using UnityEditor;
         using UnityEngine;
         using UnityEngine.UIElements;
         
         namespace UIToolkitExamples
         {
             [CustomEditor(typeof(GameSwitchesAsset))]
             public class GameSwitchesEditor : Editor
             {
                 [SerializeField]
                 VisualTreeAsset visualTreeAsset;
         
                 public override VisualElement CreateInspectorGUI()
                 {
                     return visualTreeAsset.CloneTree();
                 }
             }
         }
         

  2. In the **Inspector** window of `GameSwitchesEditor.cs`, assign the `game_switches_editor.uxml` file to the **Visual Tree Asset** field.

## Test the binding

  1. In Unity, select **Assets** > **Create** > **UIToolkitExamples** > **GameSwitches** to create a new asset in your project’s `Assets` folder.
  2. Select the newly created asset. The Inspector shows toggles and text fields that bind to the `GameSwitchesAsset.useLocalServer`, `GameSwitchesAsset.showDebugMenu`, and `GameSwitchesAsset.showFPSCounter` properties.

## Additional resources

  * SerializedObject data binding
  * Bindable elements
  * Binding data type conversion
  * Implementation details
  * Binding examples