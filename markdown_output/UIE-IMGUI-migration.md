---
title: "Migrate from Immediate Mode GUI (IMGUI) to UI Toolkit"
category: "General"
source_file: "UIE-IMGUI-migration.html"
doc_type: "manual"
---

# Migrate from Immediate Mode GUI (IMGUI) to UI Toolkit

This guide is for developers experienced with Immediate Mode GUI (IMGUI) to migrate to **UI**

## Key differences

### Code-driven versus UI-driven

IMGUI is code-driven by calls to the `OnGUI` function in a C# script that implements it. UI Toolkit provides more options for Editor UI creation. With UI Toolkit, you define the behaviors in C# **scripts**. However, when defining UI elements and styles, in addition to C#, you can visually define UI controls in UI Builder or write in an XML-like text file (called UXML) directly. For more information, refer to Get started with UI Toolkit.

### Immediate versus retained mode

With IMGUI, you describe the UI tree when the UI is repainted within the `OnGUI()` function. You must call this function when an event enters the UI or when you repaint the UI. There is no persistent information pertaining to the UI tree between different events. Whereas, you create **visual elements**

### Constant versus state changes

IMGUI is based on the `OnGUI`()`function that runs at least once every frame. You define the look and the behaviors of the UI for every possible frame. The body of`OnGUI()` might contain many conditions and different states.

UI Toolkit operates in an event-driven system. You define the look of the UI in its default state and define the behaviors of the UI in response to events. Any changes you make in UI Toolkit cause persistent changes to the state of your UI.

For example, the declaration of a button in IMGUI looks like the following:
    
    
    if (GUILayout.Button("Click me!"))
    {
        //Code runs here in frames where the user clicks the button.
    
        //Code makes changes to the UI for frames where the user has just clicked the button.
    }
    else
    {
        //Code specifies what happens in all other frames.
    }
    

The example above looks like the following in UI Toolkit:
    
    
    UIDocument document = GetComponent<UIDocument>();
    
    //Create button.
    Button button = new Button();
    button.text = "Click me!";
    
    //Set up event handler.
    button.RegisterCallback<ClickEvent>((ClickEvent evt) =>
    {
        //Code runs here after button receives ClickEvent.
    });
    
    //Add button to UI.
    document.rootVisualElement.Add(button);
    

For a completed example of how to create a custom Editor window with UI Toolkit, refer to Get started with UI Toolkit.

## IMGUI support

Use the `IMGUIContainer` to place IMGUI code inside of a `VisualElement`. Everything you can do inside of `OnGUI()` is supported. 

You can arrange multiple `IMGUIContainer`s and lay them out by mixing `GUILayout` and UI Toolkit layouts. Note that it’s not possible to add `VisualElement` instances inside of an `IMGUIContainer`.

`IMGUIContainer` example

## From IMGUI to UI Toolkit conversion

The following table lists the equivalent functions between IMGUI and UI Toolkit:

**Action** | **IMGUI** | **UI Toolkit**  
---|---|---  
Create an Editor Window | `EditorWindow.OnGUI()` | `EditorWindow.CreateGUI()`  
Create a Property Drawer or a Property Attribute | `PropertyDrawer.OnGUI()` | `PropertyDrawer.CreatePropertyGUI()`  
Create a custom Editor for the ****Inspector**** | `Editor.OnInspectorGUI()` | `Editor.CreateInspectorGUI()`  
  
The following table lists the equivalent methods, classes, and attributes between IMGUI and UI Toolkit:

**IMGUI** | **IMGUI namespaces** | **UI Toolkit**  
---|---|---  
`AddCursorRect()` | EditorGUIUtility | Set `VisualElement.style.cursor`, or set a visual element’s cursor texture in the UI Builder or USS. For more detailed interactivity, use C# events.  
`AreaScope` | GUILayout | Scopes are generally not needed in UI Toolkit. See `BeginArea()`.  
`BeginArea()` | GUILayout | To define the area itself, create a visual element and set `style.position` to `Position.Absolute`. To create children for the area, create child visual elements under it.  
`BeginBuildTargetSelectionGrouping()` | EditorGUILayout | No equivalent.  
`BeginChangeCheck()` | EditorGUI | Register callbacks on each element in the change check range. If using a `PropertyField` as a stand-in for a serialized field in a custom Inspector, use `PropertyField.RegisterCallback<SerializedPropertyChangeEvent>()` or `PropertyField.RegisterValueChangeCallback()`. In all other cases, use `VisualElement.RegisterCallback<ChangeEvent<T>>()` or `VisualElement.RegisterValueChangedCallback<T>()`.  
`BeginDisabledGroup()` | EditorGUI | `VisualElement.SetEnabled(false)`  
`BeginFoldoutHeaderGroup()` | EditorGUI, EditorGUILayout | See `Foldout()`.  
`BeginGroup()` | GUI | See `BeginArea()`.  
`BeginHorizontal()` | EditorGUILayout, GUILayout | See `BeginArea()`.  
`BeginProperty()` | EditorGUI | If you use `BeginProperty()`/`EndProperty()` to bind a simple control to a serialized property, you can do that in UI Toolkit by calling `BindProperty()`, by setting `bindingPath`, or by setting the `binding-path` UXML attribute. If you use `BeginProperty()`/`EndProperty()` to make a single property out of complex custom UI, that is not supported well in UI Toolkit.  
`BeginScrollView()` | EditorGUILayout, GUI, GUILayout | `UnityEngine.UIElements.ScrollView`  
`BeginToggleGroup()` | EditorGUILayout | No equivalent.  
`BeginVertical()` | EditorGUILayout, GUILayout | See `BeginArea()`.  
`BoundsField()` | EditorGUI, EditorGUILayout | `BoundsField`  
`BoundsIntField()` | EditorGUI, EditorGUILayout | `BoundsIntField`  
`Box()` | GUI, GUILayout | `Box`  
`BringWindowToBack()` | GUI | See `Window()`.  
`BringWindowToFront()` | GUI | See `Window()`.  
`Button()` | GUI, GUILayout | `Button`  
`CanCacheInspectorGUI()` | EditorGUI | Not needed in retained mode.  
`ChangeCheckScope` | EditorGUI | Scopes are generally not needed in UI Toolkit. See `BeginChangeCheck()`.  
`ColorField()` | EditorGUI, EditorGUILayout | `ColorField`  
`CommandEvent()` | EditorGUIUtility | Generally not needed in retained mode. Use C# callbacks to handle events.  
`CurveField()` | EditorGUI, EditorGUILayout | `CurveField`  
`DelayedDoubleField()` | EditorGUI, EditorGUILayout |  `DoubleField` with `isDelayed` set to true.  
`DelayedFloatField()` | EditorGUI, EditorGUILayout |  `FloatField` with `isDelayed` set to true.  
`DelayedIntField()` | EditorGUI, EditorGUILayout |  `IntegerField` with `isDelayed` set to true.  
`DelayedTextField()` | EditorGUI, EditorGUILayout |  `TextField` with `isDelayed` set to true.  
`DisabledScope` | EditorGUI | Scopes are generally not needed in UI Toolkit. See `BeginDisabledGroup()`.  
`DoubleField()` | EditorGUI, EditorGUILayout | `DoubleField`  
`DragWindow()` | GUI | See `Window()`.  
`DrawPreviewTexture()` | EditorGUI | No equivalent.  
`DrawRect()` | EditorGUI | Use `VisualElement`. Set `style.position` to `Absolute`. Set `style.top` and `style.left` to define the position. Set `style.width` and `style.height` to define the size. Set `style.backgroundColor` to set the color.  
`DrawTexture()` | GUI |  `Image`. Set `tintColor` in place of `color`. There is no equivalent for a false `alphaBlend`. There are no equivalents for `borderWidth`, `borderWidths`, `borderRadius`, or `borderRadiuses`.  
`DrawTextureAlpha()` | EditorGUI | No equivalent.  
`DrawTextureWithTexCoords()` | GUI |  `Image`. Set `uv` in place of `texCoords`. There is no equivalent for a false `alphaBlend`.  
`DropdownButton()` | EditorGUI, EditorGUILayout | No exact equivalent. Use fully-fledged `DropdownField`s instead of just a `DropdownButton()`.  
`DropShadowLabel()` | EditorGUI |  `Label` with shadow values set in `style.textShadow`.  
`EditorToolbar()` | EditorGUILayout | Create a `Toolbar` with one `ToolbarButton` for each tool. For each `ToolbarButton`, register a callback when clicked to call either `ToolManager.SetActiveTool()` or `ToolManager.RestorePreviousTool()` to make that button activate the tool or deactivate it, respectively.  
`EndArea()` | GUILayout | See `BeginArea()`.  
`EndBuildTargetSelectionGrouping()` | EditorGUILayout | See `BeginBuildTargetSelectionGrouping()`.  
`EndChangeCheck()` | EditorGUI | See `BeginChangeCheck()`.  
`EndDisabledGroup()` | EditorGUI | See `BeginDisabledGroup()`.  
`EndFoldoutHeaderGroup()` | EditorGUI, EditorGUILayout | See `Foldout()`.  
`EndGroup()` | GUI | See `BeginArea()`.  
`EndHorizontal()` | EditorGUILayout, GUILayout | See `BeginArea()`.  
`EndProperty()` | EditorGUI | See `BeginProperty()`.  
`EndScrollView()` | EditorGUILayout, GUI, GUILayout | See `BeginScrollView()`.  
`EndToggleGroup()` | EditorGUILayout | See `BeginToggleGroup()`.  
`EndVertical()` | EditorGUILayout, GUILayout | See `BeginArea()`.  
`EnumFlagsField()` | EditorGUI, EditorGUILayout | `EnumFlagsField`  
`EnumPopup()` | EditorGUI, EditorGUILayout | `EnumField`  
`ExpandHeight()` | GUILayout | No equivalent.  
`ExpandWidth()` | GUILayout | No equivalent.  
`FlexibleSpace()` | GUILayout | See `Space()`.  
`FloatField()` | EditorGUI, EditorGUILayout | `FloatField`  
`FocusControl()` | GUI | `VisualElement.Focus()`  
`FocusTextInControl()` | EditorGUI | `TextField.Focus()`  
`FocusWindow()` | GUI | See `Window()`.  
`Foldout()` | EditorGUI, EditorGUILayout | `Foldout`  
`GetControlRect()` | EditorGUILayout | Only needed to convert from EditorGUILayout to EditorGUI. Not needed in UI Toolkit.  
`GetNameOfFocusedControl()` | GUI | `VisualElement.focusController.focusedElement`  
`GetPropertyHeight()` | EditorGUI | `PropertyField.layout.height`  
`GradientField()` | EditorGUI, EditorGUILayout | `GradientField`  
`GroupScope` | GUI | Scopes are generally not needed in UI Toolkit. See `BeginArea()`.  
`Height()` | GUILayout | `VisualElement.style.height`  
`HelpBox()` | EditorGUI, EditorGUILayout | `HelpBox`  
`HorizontalScope` | EditorGUILayout, GUILayout | Scopes are generally not needed in UI Toolkit. See `BeginArea()`.  
`HorizontalScrollbar()` | GUI, GUILayout |  `Scroller` with `direction` set to `Horizontal`.  
`HorizontalSlider()` | GUI, GUILayout |  `Slider` with `direction` set to `Horizontal`  
`InspectorTitlebar()` | EditorGUI, EditorGUILayout | No equivalent.  
`IntField()` | EditorGUI, EditorGUILayout | `IntegerField`  
`IntPopup()` | EditorGUI, EditorGUILayout | No equivalent.  
`IntSlider()` | EditorGUI, EditorGUILayout | `SliderInt`  
`Label()` | GUI, GUILayout | `Label`  
`LabelField()` | EditorGUI, EditorGUILayout |  `TextField` with `isReadOnly` set to true.  
`LayerField()` | EditorGUI, EditorGUILayout | `LayerField`  
`LinkButton()` | EditorGUI, EditorGUILayout | No equivalent.  
`Load()` | EditorGUIUtility | If using C#, you can use this function as is and assign its return value to the `VisualElement.style` property you want. If using USS, use function `resource()` with the same argument you would give to `Load()`.  
`LongField()` | EditorGUI, EditorGUILayout | `LongField`  
`MaskField()` | EditorGUI, EditorGUILayout | `MaskField`  
`MaxHeight()` | GUILayout | `VisualElement.style.maxHeight`  
`MaxWidth()` | GUILayout | `VisualElement.style.maxWidth`  
`MinHeight()` | GUILayout | `VisualElement.style.minHeight`  
`MinMaxSlider()` | EditorGUI, EditorGUILayout | `MinMaxSlider`  
`MinWidth()` | GUILayout | `VisualElement.style.minWidth`  
`ModalWindow()` | GUI | See `Window()`.  
`[NonReorderable]` attribute |  | Ensure that `ListView.reorderable` is false.  
`ObjectField()` | EditorGUI, EditorGUILayout | `ObjectField`  
`PasswordField()` | EditorGUI, EditorGUILayout, GUI, GUILayout |  `TextField` with `isPasswordField` set to true  
`PixelsToPoints()` | EditorGUIUtility | Valid for use with UI Toolkit.  
`PointsToPixels()` | EditorGUIUtility | Valid for use with UI Toolkit.  
`Popup()` | EditorGUI, EditorGUILayout | `PopupField<T0>`  
`ProgressBar()` | EditorGUI | `ProgressBar`  
`PropertyField()` | EditorGUI, EditorGUILayout | `PropertyField`  
`PropertyScope` | EditorGUI | Scopes are generally not needed in UI Toolkit. See `BeginProperty()`.  
`RectField()` | EditorGUI, EditorGUILayout | `RectField`  
`RectIntField()` | EditorGUI, EditorGUILayout | `RectIntField`  
`RepeatButton()` | GUI, GUILayout | `RepeatButton`  
`ScrollTo()` | GUI |  `ScrollView.ScrollTo()` or `ScrollView.scrollOffset`  
`ScrollViewScope` | EditorGUILayout, GUI, GUILayout | Scopes are generally not needed in UI Toolkit. See `BeginScrollView()`.  
`SelectableLabel()` | EditorGUI, EditorGUILayout |  `Label` with `isSelectable` and `focusable` set to true.  
`SelectionGrid()` | GUI, GUILayout | `RadioButton`  
`SetNextControlName()` | GUI | `VisualElement.name`  
`singleLineHeight` | EditorGUIUtility | Use USS variable `--unity-metrics-single_line-height`.  
`Slider()` | EditorGUI, EditorGUILayout | `Slider`  
`Space()` | EditorGUILayout, GUILayout | Use `flex` properties to configure spacing between visual elements.  
`TagField()` | EditorGUI, EditorGUILayout | `TagField`  
`TextArea()` | EditorGUI, EditorGUILayout, GUI, GUILayout |  `TextField` with `multiline` set to true, `style.whiteSpace` set to `Normal`, and `ScrollView.verticalScrollerVisibility` set to `Auto`.  
`TextField()` | EditorGUI, EditorGUILayout, GUI, GUILayout |  `TextField` with `multiline` set to true and `style.whiteSpace` set to `NoWrap`.  
`Toggle()` | EditorGUI, EditorGUILayout, GUI, GUILayout | `Toggle`  
`ToggleGroupScope` | EditorGUILayout | Scopes are generally not needed in UI Toolkit. See `BeginToggleGroup()`.  
`ToggleLeft()` | EditorGUI, EditorGUILayout |  `Toggle`, but instead of setting `label`, set `text`.  
`Toolbar()` | GUI, GUILayout | No equivalent.  
`UnfocusWindow()` | GUI | See `Window()`.  
`Vector2Field()` | EditorGUI, EditorGUILayout | `Vector2Field`  
`Vector2IntField()` | EditorGUI, EditorGUILayout | `Vector2IntField`  
`Vector3Field()` | EditorGUI, EditorGUILayout | `Vector3Field`  
`Vector3IntField()` | EditorGUI, EditorGUILayout | `Vector3IntField`  
`Vector4Field()` | EditorGUI, EditorGUILayout | `Vector4Field`  
`VerticalScope` | EditorGUILayout, GUILayout | Scopes are generally not needed in UI Toolkit. See `BeginArea()`.  
`VerticalScrollbar()` | GUI, GUILayout |  `Scroller` with `direction` set to `Vertical`.  
`VerticalSlider()` | GUI, GUILayout |  `Slider` with `direction` set to `Vertical`.  
`Width()` | GUILayout | `VisualElement.style.width`  
`Window()` | GUI, GUILayout | No equivalent.  
  
## Additional resources

  * Get started with UI Toolkit
  * Unity style sheets (USS)
  * Examples
  * IMGUI events