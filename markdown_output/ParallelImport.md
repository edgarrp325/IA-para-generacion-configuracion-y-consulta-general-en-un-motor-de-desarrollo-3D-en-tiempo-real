---
title: "Unity"
category: "General"
source_file: "ParallelImport.html"
doc_type: "manual"
---

## Importing assets simultaneously

By default, Unity imports assets one after another sequentially on the main Editor process. However, Unity also supports parallel importing for some types of asset. Parallel importing uses multiple processes to import assets simultaneously, which is faster than the default sequential method of importing.

To enable parallel importing, go to **Edit** > **Project Settings** > **Editor** , then under the **Asset Pipeline** section, enable the **Parallel Import** checkbox.

The Parallel Import option in the Project Settings window.

## The scope of parallel imports

Unity’s **Parallel Import** feature supports only certain types of asset. It applies only when the Editor is performing its standard asset database refresh, which occurs when it detects new or modified assets in the Project folder and automatically imports them.

The specific types of asset which Unity can import in parallel are:

  * Image file types imported by the Texture Importer
  * **Model file** types imported by the Model Importer

Other types of asset are always imported sequentially during an asset database refresh.

Some Asset Database API methods also respect this setting, if you use them to import, refresh, or create Texture or Model assets. These are:

  * AssetDatabase.ImportAsset
  * AssetDatabase.Refresh
  * AssetDatabase.CreateAsset

## Implications for scripted importers

Because parallel imports operate on separate processes, any side effects of your scripted importer code also take effect in that process rather than the main Editor process. Side effects that run on separate processes can cause unexpected problems. For example, if you modify a static variable on a C# class during import on a worker thread, that modification is not automatically visible to code running on the Editor’s main thread.

Any code that you write for importing should always be self-contained, deterministic, and shouldn’t change the context it’s running in (for example, it shouldn’t change the Editor settings or create new assets on disk). Following these rules helps your importer code avoid parallel threading issues. It also ensures that your import results are always consistent, and that the Editor always uses cached artifacts instead of unnecessarily reimporting your assets.

## Controlling the import worker processes

In the Asset Pipeline settings, there are three settings that allow you to control the behaviour of the import worker processes. These settings are project-specific.

The import worker process controls, in the Project Settings window.

**Property name** | **Description**  
---|---  
**Desired Import Worker Count** | The number of import worker processes that the import pipeline considers the optimal number to run in parallel.  
**Standby Import Worker Count** | The minimum number of worker processes to keep, even if they’re idle.  
  
If there are more worker processes than this, Unity shuts down import workers that have been idle for some time, to free up system resources. This property allows you to manage how Unity balances system resources when some processes are idle, compared with the time it takes to start up new import worker processes.  
  
You might see an improvement in import performance by increasing this value if you are frequently iterating on model, animation or texture work, and are therefore frequently importing batches of models or image files.  
**Idle Import Worker Shutdown Delay** | The amount of time in seconds to wait before shutting down an idle worker.  
  
You can also control the default values that Unity sets the **Desired Import Worker Count** for new projects. To do this, go to **Preferences** > **Asset Pipeline** > **Import Worker Count %**.

The Importer Worker Count setting in the Preferences window.

When you create a new project, Unity uses the **Import Worker Count %** value to assign your project’s **Desired Import Worker Count** value to the percentage of the number of logical cores available on your system. 

For example, if your system has 16 logical cores and this preference is set to 25%, the **Desired Import Worker Count** for new projects is 4. If you set this value too high, your import worker processes need to compete over other processes and system resources such as reading and writing files. The default value of 25% is suitable for most situations.