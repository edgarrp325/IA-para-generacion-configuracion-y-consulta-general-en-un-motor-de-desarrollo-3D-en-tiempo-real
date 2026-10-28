---
title: "Creating a custom module details panel"
category: "General"
source_file: "Profiler-customizing-details-view.html"
doc_type: "manual"
---

# Creating a custom module details panel

The module details panel appears in the bottom of the **Profiler** window when you select a module. You can customize this section to show additional details relevant to your module or to display a custom visualization of your performance data. 

To create a custom Module details panel for your Profiler module:

  * Create a module details panel Controller script to draw a custom module details panel.
  * Create a Profiler module script to connect your custom module details panel controller to your custom profiler module .

### Creating a script to control the module details panel

You can use the ProfilerModuleViewController base class to customize the module details panel in the profiler window. To do this, create a script that controls what appears in the module details panel when you select a specific module. 

The script you create to customize the module details panel must:

  * Define a public constructor for the view controller that calls the base constructor `base(profilerWindow)`.
  * Override `CreateView` to build the custom module details panel.

For example: 
    
    
     public class CustomDetailsViewController : ProfilerModuleViewController
     {   
        public CustomDetailsViewController(ProfilerWindow profilerWindow) : base(profilerWindow) { }
    
        protected override VisualElement CreateView()
        {
            // Create your UI.
        }
    }
    

For an example of a full module details panel controller script, see module details panel controller script example.

#### Module details panel controller script example

The below example script creates a module details panel controller that draws a single label in the module details panel that displays text:

This module details panel controller script example does the following: 

  * Defines and creates a label to display the value you want to capture, and adds this label to the module details panel.
  * Defines a constructor to control the module details panel and uses CreateView to build the custom module details panel.
  * Populates the label with data from the current frame, and updates the label after each frame.
  * Fetches a counter value as a string that you can display in the module details panel.
  * Specifies the text to display in the module details panel, and tells the Profiler to automatically update it each frame.

    
    
     using UnityEditor;
     using UnityEditorInternal;
     using Unity.Profiling.Editor;
     using UnityEngine.UIElements;
     
     public class TankEffectsDetailsViewController : ProfilerModuleViewController
     {
        // Define a label, which will display the total particle count for tank trails in the selected frame.
        Label m_TankTrailParticleCountLabel;
    
    
        // Define a constructor for the view controller, which calls the base constructor with the Profiler Window passed from the module.
        public TankEffectsDetailsViewController(ProfilerWindow profilerWindow) : base(profilerWindow) { }
     
        // Override CreateView to build the custom module details panel.6666666667reateView()
        {
            var view = new VisualElement();
    
            // Create the label and add it to the view.
            m_TankTrailParticleCountLabel = new Label() { style = { paddingTop = 8, paddingLeft = 8 } };
            view.Add(m_TankTrailParticleCountLabel);
    
            // Populate the label with the current data for the selected frame. 
            ReloadData();
    
            // Be notified when the selected frame index in the Profiler Window changes, so we can update the label.
            ProfilerWindow.SelectedFrameIndexChanged += OnSelectedFrameIndexChanged;
    
            return view;
        }
    
        // Override Dispose to do any cleanup of the view when it is destroyed. This is a standard C# Dispose pattern.
        protected override void Dispose(bool disposing)
        {
            if (!disposing)
                return;
    
            // Unsubscribe from the Profiler window event that we previously subscribed to.
            ProfilerWindow.SelectedFrameIndexChanged -= OnSelectedFrameIndexChanged;
    
            base.Dispose(disposing);
        }
    
        void ReloadData()
        {
            // Retrieve the TankTrailParticleCount counter value from the Profiler as a formatted string.
            var selectedFrameIndexInt32 = System.Convert.ToInt32(ProfilerWindow.selectedFrameIndex);
            var value = ProfilerDriver.GetFormattedCounterValue(selectedFrameIndexInt32, GameStatistics.TanksCategory.Name, GameStatistics.TankTrailParticleCountName);
    
            // Update the label's text with the value.
            m_TankTrailParticleCountLabel.text = $"The value of '{GameStatistics.TankTrailParticleCountName}' in the selected frame is {value}.";
        }
    
        void OnSelectedFrameIndexChanged(long selectedFrameIndex)
        {
            // Update the label with the current data for the newly selected frame.
            ReloadData();
        }
    }
    

#### Creating custom UI elements in the module details panel

You can use Unity’s UIToolkit to build custom **UI** for the module details panel. For more information, see UI Toolkit.

The following example image shows a custom module details panel that belongs to a custom Adaptive Performance module:

### Connect a custom module details panel to a Profiler module

To display a custom module details panel, you need to instantiate your module details panel controller when you select your Profiler module. To do this, override `CreateDetailsViewController` to create and draw a new module details panel controller. Unity then invokes this method when it displays your module’s details panel.

The following code example instantiates a custom module details panel for a module called `TankEffectsProfilerModule`:
    
    
     using Unity.Profiling.Editor;
    
     [System.Serializable]
     [ProfilerModuleMetadata("Tank Effects")]
     public class TankEffectsProfilerModule : ProfilerModule
     {
        static readonly ProfilerCounterDescriptor[] k_Counters = new ProfilerCounterDescriptor[]
        {
            new ProfilerCounterDescriptor(GameStatistics.TankTrailParticleCountName, GameStatistics.TanksCategory),
            new ProfilerCounterDescriptor(GameStatistics.ShellExplosionParticleCountName, GameStatistics.TanksCategory),
            new ProfilerCounterDescriptor(GameStatistics.TankExplosionParticleCountName, GameStatistics.TanksCategory),
        };
    
        public TankEffectsProfilerModule() : base(k_Counters) { }
    
        public override ProfilerModuleViewController CreateDetailsViewController()
        {
            return new TankEffectsDetailsViewController(ProfilerWindow);
        }
    }
    

## Visualizing additional counters in the module details panel

You can display counters in the module details panel that are not included in your module’s chart view. This is useful when you want to show additional data for a frame you select.

The Profiler automatically captures the categories of all counters that belong to a module’s chart view when that module is active. To capture additional counters, write a script to tell the Profiler to capture specific categories when your module is active.

For example, the script below uses the `autoEnabledCategoryNames` constructor argument to specify the **Scripts** and Memory categories. This enables these categories when the module is active:
    
    
     
     using Unity.Profiling;
     using Unity.Profiling.Editor;
    
     [System.Serializable]
     [ProfilerModuleMetadata("Tank Effects")]
     public class TankEffectsProfilerModule : ProfilerModule
     {
        static readonly ProfilerCounterDescriptor[] k_Counters = new ProfilerCounterDescriptor[]
        {
            new ProfilerCounterDescriptor(GameStatistics.TankTrailParticleCountName, ProfilerCategory.Scripts),
            new ProfilerCounterDescriptor(GameStatistics.ShellExplosionParticleCountName, ProfilerCategory.Scripts),
            new ProfilerCounterDescriptor(GameStatistics.TankExplosionParticleCountName, ProfilerCategory.Scripts),
        };
    
        // Enable the ProfilerCategory.Scripts and ProfilerCategory.Memory categories when the module is active.
        static readonly string[] k_AutoEnabledCategoryNames = new string[]
        {
            ProfilerCategory.Scripts.Name,
            ProfilerCategory.Memory.Name
        };
    
        // Pass the auto-enabled category names to the base constructor.
        public TankEffectsProfilerModule() : base(k_Counters, autoEnabledCategoryNames: k_AutoEnabledCategoryNames) { }