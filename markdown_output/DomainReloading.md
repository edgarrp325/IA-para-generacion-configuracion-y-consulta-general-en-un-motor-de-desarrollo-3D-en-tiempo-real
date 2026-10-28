---
title: "Domain Reloading"
category: "General"
source_file: "DomainReloading.html"
doc_type: "manual"
---

# Domain Reloading

Domain Reloading resets your scripting state, and is enabled by default. It provides you with a completely fresh scripting state, and resets all static fields and registered handlers each time you enter Play Mode. This means each time you enter Play Mode in the Unity Editor, your Project begins playing in a very similar way to when it first starts up in a build.

Domain Reloading takes time, and this time increases with the number and complexity of the **scripts** in your Project. When it takes a long time to enter Play Mode, it becomes harder to rapidly iterate on your Project. This is the reason Unity provides the option to turn off Domain Reloading.

## Disabling Domain Reloading

To disable Domain Reloading:

  1. Go to Edit > Project Settings > Editor
  2. Make sure Enter Play Mode Options is enabled.
  3. Disable Reload Domain

For more information, see How to configure Play Mode

When Domain Reloading is disabled, entering Play Mode is faster, because Unity does not reset the scripting state each time. However, it is then up to you to ensure your scripting state resets when you enter Play Mode. To do this, you need to add code that resets your scripting state when Play Mode starts.

When Domain Reloading is disabled, Unity still refreshes the scripting state when you update or re-import a script, based on your auto-refresh settings.

## Modifying your scripts to perform correctly when Domain Reload is disabled:

To ensure your scripting states correctly reset at Play Mode, you need to make adjustments to static fields and static event handlers in your scripts.

### Static fields

When Domain Reloading is disabled, the values of **static fields** in your code do not automatically reset to their original values. You need to add code that explicitly does this.

The following code example has a static counter field which increments when the user presses the Jump button. When Domain Reloading is enabled, the counter automatically resets to zero when entering Play Mode. When Domain Reloading is disabled, the counter does not reset; it keeps its value in and out of Play Mode. This means that on a second run of your Project in the Editor, the counter might not be at zero if it changed in the previous run.
    
    
    using UnityEngine;
    
    public class StaticCounterExample : MonoBehaviour
    {
    // this counter will not reset to zero when Domain Reloading is disabled
        static int counter = 0; 
    
        // Update is called once per frame
        void Update()
        {
                if (Input.GetButtonDown("Jump"))
                {
                        counter++;
                        Debug.Log("Counter: " + counter);
                }
        }
    }
    

To make sure the counter resets even when Domain Reloading is disabled, you must use the [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)] attribute, and reset the value explicitly: 
    
    
    using UnityEngine;
    
    public class StaticCounterExampleFixed : MonoBehaviour
    {
        static int counter = 0;
    
        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]
        static void Init()
        {
                Debug.Log("Counter reset.");
                counter = 0;   
        }
    
        // Update is called once per frame
        void Update()
        {
                if (Input.GetButtonDown("Jump"))
                {
                    counter++;
                    Debug.Log("Counter: " + counter);
                }
        }
    }
    

### Static event handlers

With Domain Reloading disabled, Unity will not unregister methods from static event handlers when you exit Play Mode. This can lead to complications if you have code that registers methods with static event handlers. For example, on the first Play of your project in the editor, methods would be registered as normal. However on the second Play of your project, those methods would be registered a second time in addition to the first, causing those methods to be called twice when the event occurs.

For example, this code registers a method with the static event handler `Application.quitting` With Domain Reloading enabled, Unity automatically resets the event handler when Play Mode starts, so the method is only ever registered once. However, with Domain Reloading disabled, the event handler is not cleared, so on the second run of your Project in the editor, the method is registered a second time, and is called twice when the event occurs - which is usually undesirable.
    
    
    using UnityEngine;
    public class StaticEventExample : MonoBehaviour
    {
        void Start()
        {
                Debug.Log("Registering quit function");
                Application.quitting += Quit;
        }
    
    
        static void Quit()
        {
            Debug.Log("Quitting!");
        }
    }
    

When Domain Reloading is disabled, the above example adds the `Quit` method again each time you enter Play Mode. This results in an additional “Quitting” message each time you exit Play Mode.

To ensure the event handler resets even when Domain Reloading is disabled, you must use the [RuntimeInitializeOnLoadMethod] attribute, and unregister the method explicitly so that it is not added twice.
    
    
    using UnityEngine;
    public class StaticEventExampleFixed : MonoBehaviour
    {
        [RuntimeInitializeOnLoadMethod]
        static void RunOnStart()
        {
                Debug.Log("Unregistering quit function");
                Application.quitting -= Quit;
        }
    
        void Start()
        {
                Debug.Log("Registering quit function");
                Application.quitting += Quit;
        }
    
        static void Quit()
        {
            Debug.Log("Quitting the Player");
        }
    }
    

For runtime scripts, you must use the `[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]` attribute to reset static fields and event handlers.

For Editor scripts such as custom Editor windows or **Inspectors** that use statics, you must use the `[InitializeOnEnterPlayMode]` attribute to reset static fields and event handlers.