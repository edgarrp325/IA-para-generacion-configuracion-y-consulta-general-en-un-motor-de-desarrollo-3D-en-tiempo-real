---
title: "Configurable Enter Play Mode"
category: "General"
source_file: "ConfigurableEnterPlayMode.html"
doc_type: "manual"
---

# Configurable Enter Play Mode

Play Mode is one of Unity’s core features. It allows you to run your project directly inside the Editor, via the Play button in the Toolbar. When you enter Play Mode, your project starts and runs as it would in a build. Any changes you make in the Editor during Play Mode reset when you exit Play Mode.

When you enter Play Mode in the Editor, Unity performs two significant actions to ensure your project starts in the Editor in the same way as it would in a build:

  * It resets the scripting state (this is also called a “Domain Reload”)
  * It reloads the Scene

These two actions take some time to perform, and the amount of time increases as your **scripts** and **Scenes** and **Scenes** become more complex.

The ability to quickly enter and exit Play Mode is an important factor while you are developing your game or app. The faster you can enter and exit Play Mode, the faster you can make and test changes.

Because a rapid speed of iteration while developing is important, and because the time to reset the Scene and scripting state can become an obstacle to that, Unity offers the ability to configure what happens when you enter Play Mode, giving you the option to disable either, or both, of the “Domain Reload” and “Scene Reload” actions. These two options are provided by the Configurable Enter Play Mode feature.

The diagram below shows the effects of disabling the Reload Domain and Reload Scene settings.

The effects of disabling the Reload Domain and Reload Scene settings

## How to configure Play Mode

To configure the Enter Play Mode settings, go to **Edit** > **Project Settings** > **Editor** and enable **Enter Play Mode Options**. When you enable this, the options to **reload domain** and **reload scene** become available. 

The Enter Play Mode settings in the Editor Project Settings window

Enable **Reload Domain** to enable Domain Reloading. Enable **Reload Scene** to enable Scene Reloading.