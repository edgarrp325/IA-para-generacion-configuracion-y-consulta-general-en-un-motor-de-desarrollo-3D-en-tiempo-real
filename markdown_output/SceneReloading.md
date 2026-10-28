---
title: "Scene Reloading"
category: "General"
source_file: "SceneReloading.html"
doc_type: "manual"
---

# Scene Reloading

By default, **Scene** Reloading is enabled. This means that when you enter Play Mode, Unity destroys all existing Scene **GameObjects** Reloading is enabled. This means that when you enter Play Mode, Unity destroys all existing Scene **GameObjects** and reloads the Scene from disk. The time it takes for Unity to do this increases with the complexity of the Scene, which means that as your project gets more complex, you have to wait longer between the moment you press the Play button and the moment the Scene fully loads in the Editor.

When you disable Scene Reloading, the process takes less time. This allows you to more rapidly iterate on the development of your project. Instead of reloading the Scene from disk, Unity only resets the Scene’s modified contents. This avoids the time and performance impact of unloading and reloading the Scene. Unity still calls the same initialization functions (such as `OnEnable`, `OnDisable` and `OnDestroy`) as if it were freshly loaded.

## Effects of skipping Scene Reload

To disable Scene Reloading:

  1. Go to Edit > Project Settings > Editor
  2. Make sure Enter Play Mode Options is enabled.
  3. Disable Reload Scene

For more information, see How to configure Play Mode

When you disable Scene Reloading, the time it takes to start your application in the Editor is no longer representative of the startup time in the built version. Therefore, if you want to debug or profile exactly what happens during your project’s startup, you should enable Scene Reloading to more accurately represent the true loading time and processes that happen in the built version of your application.

Disabling Scene Reload should have minimal side effects on your project. However, because Scene Reloading is tightly connected to Domain Reload, there are a couple of important differences:

  1. ScriptableObject and MonoBehaviour fields that are not serialized into the build (`[NonSerialized]`, private, or internal) keep their values. This is because Unity does not recreate existing objects and does not call constructors. Additionally, Unity converts null private and internal fields of array/List type to an empty array/List object during Domain Reload and stay non-null for runtime (non-Editor) **scripts**.

  2. Scripts that use `ExecuteInEditMode`, or `ExecuteAlways` scripts do not receive `OnDestroy` or `Awake` calls. Unity does not call Awake, and only calls OnEnable when `EditorApplication.isPlaying` is already true on Play Mode change with Awake/OnEnable methods that check the `EditorApplication.isPlaying` property. Nonserialized fields for runtime (non-Editor) scripts should not be an issue because these are not active in Edit Mode, however scripts marked with `ExecuteInEditMode` or `ExecuteAlways` might change themselves or touch fields of other runtime scripts. To work around this, initialize any affected fields in an OnEnable callback yourself.