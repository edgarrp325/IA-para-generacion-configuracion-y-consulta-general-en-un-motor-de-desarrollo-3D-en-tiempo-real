---
title: "Instantiate UXML from C# scripts"
category: "General"
source_file: "UIE-LoadingUXMLcsharp.html"
doc_type: "manual"
---

# Instantiate UXML from C# scripts

To build **UI** from a UXML file, you must first load the file into a `VisualTreeAsset`, and then use the `Instantiate()` to instantiate without a parent, which creates a new `TemplateContainer`, or `CloneTree(parent)`) to clone inside a parent.

Once the UXML is instantiated, you can retrieve specific elements from the **visual tree** with UQuery.

The following example creates a custom Editor window and loads a UXML file as its content:
    
    
    using UnityEditor;
    using UnityEngine;
    using UnityEngine.UIElements;
    using UnityEditor.UIElements;
    
    public class MyWindow : EditorWindow  {
        [MenuItem ("Window/My Window")]
        public static void  ShowWindow () {
            EditorWindow w = EditorWindow.GetWindow(typeof(MyWindow));
    
            VisualTreeAsset uiAsset = AssetDatabase.LoadAssetAtPath<VisualTreeAsset>("Assets/MyWindow.uxml");
            VisualElement ui = uiAsset.Instantiate();
    
            w.rootVisualElement.Add(ui);
        }
    }
    

## Additional resources

  * Load UXML and USS from C# scripts
  * UQuery