---
title: "Details of disabling Domain and Scene Reload"
category: "General"
source_file: "ConfigurableEnterPlayModeDetails.html"
doc_type: "manual"
---

# Details of disabling Domain and Scene Reload

## What Unity skips when Domain Reload and Scene Reload is disabled

From a high-level perspective, entering Play Mode consists of the following main stages:

  * **Backup current Scenes**. This only happens when the **Scene** has been modified. Allows Unity to revert the Scenes when Play Mode is exited to the state they were in before Play Mode started.
  * **Domain Reload**. Resets the scripting state, by reloading the scripting domain.
  * **Scene Reload**. Resets the Scene state, by reloading the Scene.
  * **Update Scene**. This happens twice; once without rendering, and once with rendering.

The combined tasks of **Domain Reload** and **Scene Reload** resets the scripting domain and simulates the startup behavior of your application as it would run in the player. Unity skips these steps when you disable them in your **Project Settings**.

The diagram below provides detailed information about the exact events which Unity skips when Domain Reload and Scene Reload are disabled. Blue indicates the events Unity skips when Domain Reload is disabled, and green indicates the events Unity skips when Scene Reload is disabled.

## What Unity performs when Scene Reloading and Domain Reloading are both enabled

With Scene Reloading and Domain Reloading enabled, this is the full list of all processes and events that Unity performs when entering Play Mode:

  1. The AssemblyReloadEvent `beforeAssemblyReload` event is raised.
  2. The C# domain is stopped:  
a. `OnDisable()` is called for all ScriptableObjects and MonoBehaviours.  
b. Unity waits for all async operations to finish.
  3. The state of all MonoBehaviours and ScriptableObjects is serialized.  
a. `OnBeforeSerialize()` is called.  
b. All public and private field values are serialized, except those marked with `[NonSerialized]`.
  4. Managed wrappers are disconnected from native Unity objects.
  5. The Unity Child Domain is reloaded:  
a. Mono domain unload:  
i. The `AppDomain.DomainUnload` event is raised.  
ii. The Unity Child Domain is destroyed  
1\. GC and finalizers are called.  
2\. Threads are terminated.  
3\. All JIT info is deleted.  
b. The new Unity Child Domain is created.
  6. The assemblies are loaded:  
a. System assemblies are loaded.  
b. Unity assemblies are loaded.  
c. User assemblies are loaded.
  7. The synchronization context is initialized.
  8. The scripting state is restored.  
a. The scriptable part of all Unity objects is recreated.  
i. Constructors are called, and statics are assigned their default values.  
b. The state of all Unity objects is deserialized:  
i. The serialized stated of all Unity objects are restored.  
1\. The `OnAfterDeserialize` event is raised.  
ii. `OnValidate()` is called.  
iii. For **scripts** using the `[ExecuteInEditMode]` attribute:  
1\. `OnEnable()` is called.  
2\. `OnDisable()` is called.  
3\. `OnDestroy()` is called.
  9. Methods with the InitializeOnLoad and InitializeOnLoadMethod are called.
  10. The AssemblyReloadEvent `afterAssemblyReload` is called.