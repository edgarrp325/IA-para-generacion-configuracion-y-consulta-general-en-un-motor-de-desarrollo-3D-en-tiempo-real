---
title: "Profiling your application"
category: "General"
source_file: "profiler-profiling-applications.html"
doc_type: "manual"
---

# Profiling your application

When you use the Unity Profiler to profile your application, there are three main ways to record data:

  * Profile your application in a player on your target platform
  * Profile your application in Play mode in the Unity Editor
  * Profile the Unity Editor

The best way to get accurate timings about your application is to profile it on the end platform you intend to publish it on. This gives you accurate timings about what impacts the performance of your application.

However, it can be time-consuming to build your application every time you would like to improve elements of its performance. So, to quickly assess the performance of your application you can profile it directly in Play mode in the Editor. Profiling in Play mode doesn’t give you an accurate reflection of what the performance of your application looks like on a real device, but it is a useful tool to quickly check to see if the changes you make improve your application’s performance, after initially profiling on the end platform.

The Unity Editor might affect the performance of your application, because it uses the same resources as your application when it’s running in Play mode, so you can also profile the Editor separately to determine what resources it uses. This is particularly useful if your application has only been designed to work in Play mode, such as for movie making.

##  Profile your application on a target platform

To profile your application on its target release platform, connect the target device to your network or directly to your computer via cable. You can also connect to a device via IP address. You can only profile your application as a **Development Build**. To set this up, go to **Build Settings** (menu: **File** > **Build Settings**) and select your application’s target platform. Enable the **Development Build** setting. When you enable this setting, two settings related to the Profiler become available: **Autoconnect Profiler** and **Deep Profiling Support**.

Build Settings window with Profiling options enabled

When you enable the **Autoconnect Profiler** setting, the Unity Editor bakes its IP address into the built Player during the build process. When you start the Player, it attempts to connect to the Profiler in the Editor located at the baked IP address.

If you additionally enable the **Deep Profiling Support** setting, Unity performs Deep Profiling when the built Player starts, which means that the Profiler profiles every part of your code, and not just code timings explicitly wrapped in ProfilerMarkers. This is useful to get Deep Profiling information on your application’s start up times, however, this adds a small amount of overhead to your build.

### Connecting to your Player in the Profiler window

To use the Profiler to manually connect to a platform running your application, configure the settings in the **Attach to Player** dropdown. You can only do this if **Autoconnect Profiler** is disabled.

For a platform to appear in the **Attach to Player** dropdown, it must meet the following requirements:

  * The platform is visible on your local network or directly connected to your local machine by cable.
  * The platform is running a Player that you built with the ****Development Build**** option enabled. For instructions on how to enable this setting for a platform, refer to Profile your application on a target platform.
  * The platform is running your Player.

The **Attach to Player** dropdown displays all Unity Players that Unity detects through the network or by direct connection. You can identify these Players by **Player Name** and the **Product Name** that is running the Player; for example, iPhonePlayer (My iPhone).

You can also connect to a Player directly via its IP address. To do this, select the **Attach to Player** menu, and then select **< Enter IP>** in the dropdown. In the dialog box that appears, type the IP address and (optionally) the port of the Player you want to connect to.

To collect profiling information on your application, select the Player from the dropdown menu, and then click **Record**.

To continuously collect data while your application runs, enable the **Run In Background** setting in Player Settings (menu: **Edit** > **Project Settings** > **Player** > **Resolution and Presentation**). When you enable this setting, the Profiler collects data even when you leave your application running in the background. If you disable it, the Profiler only collects data when the application is running in an active window.

### Using the Attach to Player search bar

The **Attach to Player** dropdown includes a search bar that you can use to find information about your Player. You can search by **Player Name** or device category, for example **Remote**. When you search by category, the result displays all devices in that category.

Select the name of a development Player to view it in the profiler.

### Attach to Player properties

Each column provides the following information about when it is available:

**Property:** | **Description:**  
---|---  
**Player Name** | The name of the device that is running your application.  
  
To change this name, navigate to **Edit** > **Preferences** > **Analysis** > **Profiler** (macOS: **Unity > Settings > Analysis > Profiler**) and enter your desired name in the **Custom Connection ID** field.  
  
You can also set a Player Name set when you launch a Player from the command line using the `-connection-id` argument.  
  
For more information about the categories in this property, see Player name device categories  
**Product Name** | This is the value of the field that you set in **Project** > **PlayerSettings**.  
**IP** | The IP address of the Player.  
**Port** | The port of the Player.  
  
###  Player name device categories

The **Player Name** category includes the following categories that display information about particular device types:

**Property:** | **Description:**  
---|---  
**Play Mode** | Select this property to profile your application in Play Mode.  
**Edit Mode** | Select this property to profile the Unity Editor.  
**Local** | This list contains any device that is running on the local machine, in the Unity Editor or in a standalone player.  
  
It also displays information for players that are physically connected to the host machine with a cable.  
**Remote** | This section displays information for devices running on the local network.  
  
This section only appears when Unity finds a remote device running on the local network.  
**Connections without ID** | This section only appears when Unity finds a device running a player older than Unity 2021.2.   
These players do not have **Product Name** , **IP** , or **Port** information.  
**Direct Connection** | Use this option to connect to a specific IP and port combination. This category displays the most recent IP you connected to.  
  
### Platform specific profiling guidance

Different platforms behave in different ways when you connect them to the Unity Profiler. The following sections provide guidance on some common behaviors each platform has:

#### WebGL

You can use the Unity Profiler in WebGL, but you cannot attach to a running player built with WebGL via the Editor. This is because WebGL uses WebSockets for communication, which does not allow incoming connections on the browser side. To attach to a running player, you need to enable the **Autoconnect Profiler** checkbox in **Build Settings** (menu: **File** > **Build Settings**). Unity cannot profile draw calls for WebGL.

#### Profiling on mobile devices

Both iOS and Android devices support remote profiling over a network. If you are using a firewall, open ports 54998 to 55511 in your firewall’s outbound rules. These are the ports Unity uses for remote profiling.

When you set up remote profiling, the Unity Editor might sometimes not connect to the device automatically. If this happens, you can initiate the Profiler connection manually by selecting the **Attach to Player** dropdown menu in the Profiler window and choosing the appropriate device.

You can also plug the target device directly into your computer, to avoid network or connection issues.

**iOS remote profiling**

To enable remote profiling on iOS devices, follow these steps:

  1. Connect your iOS device to your WiFi network. The Profiler uses a local WiFi network to send profiling data from your device to the Unity Editor.
  2. Attach your device to your computer via cable. In the **Build Settings** window (menu: **File** > **Build Settings**), select the **Development Build** and **Autoconnect Profiler** checkboxes, then click **Build & Run**.
  3. When the application launches on the device, open the Profiler window in the Unity Editor (menu: **Window** > **Analysis** > **Profiler**).

**Android remote profiling**

Android devices support two methods of remote profiling: WiFi and Android Debug Bridge (adb).

For WiFi profiling, follow these steps:

  1. Disable mobile data on your Android device.
  2. Connect your Android device to your WiFi network. The Profiler uses a local WiFi network to send profiling data from your device to the Unity Editor.
  3. Attach your device to your computer via cable. In the **Build Settings** window (menu: **File** > **Build Settings**), select the **Development Build** and **Autoconnect Profiler** checkboxes, then click **Build & Run**.
  4. When the application launches on the device, open the Profiler window in the Unity Editor (menu: **Window** > **Analysis** > **Profiler**).

**Note** : The Android device and host computer that is running the Unity Editor must both be on the same subnet for device detection to work.

For Android Debug Bridge (adb) profiling, follow these steps:

  1. Make sure the device is in **Development mode** and enable the **USB debugging** setting
  2. Attach your device to your computer via cable and make sure that it shows in the **adb** devices list.
  3. In the **Build Settings** window (menu: **File** > **Build Settings**), select the **Development Build** checkbox, and then click **Build & Run.**
  4. When the application launches on the device, open the Profiler window in the Unity Editor (menu: **Window** > **Analysis** > **Profiler**).
  5. From the **Attach to Player** dropdown menu, select **AndroidProfiler(ADB@127.0.0.1:34999)**. The entry in the dropdown menu is only visible when the selected target is Android.

The Unity Editor automatically creates an adb tunnel for your application when you select **Build & Run**. If you want to profile another application, or you restart the adb server, you need to configure this tunnel manually. To do this, open a Terminal window or Command prompt and enter the following:

  * Required when Editor-to-Android connection is established via USB cable

`adb forward tcp:34999 localabstract:Unity-{insert bundle identifier here}`

  * Required when Android-to-Editor connection is established via USB cable

`adb reverse tcp:34998 tcp:34999`

To use Deep Profiling with an Android build, you need to enable the Mono Scripting Backend setting in the Android Player Settings (menu: **Edit** > **Project Settings** > **Player** > **Android** > **Other Settings**) and enter the following to start the game through an adb command:
    
    
    ~$ adb shell am start -n {insert bundle identifier here}/com.unity3d.player.UnityPlayerActivity -e 'unity' '-deepprofiling'
    

**ChromeOS remote profiling**

ChromeOS devices support remote profiling through adb over WiFi, unlike Android devices that support remote profiling through both WiFi and adb over USB connection.

To enable WiFi profiling on ChromeOS devices, follow these steps:

  1. Enable **Linux Development Environment** and **ADB debugging** settings on your Chromebook. You need not enable ChromeOS Developer Mode. For more information on how to do this, refer to Enable ADB Debug.
  2. Connect your Chromebook and the host computer running Unity Editor to the same WiFi network.
  3. Establish a connection between your Chromebook and the host computer through adb. For more information on how to do this, refer to Connect to ADB over a network.
  4. In the **Build Settings** window (menu: **File** > **Build Settings**), select the **Development Build** and **Autoconnect Profiler** checkboxes, and then click **Build & Run.**
  5. When the application launches on the device, open the Profiler window in the Unity Editor (menu: **Window** > **Analysis** > **Profiler**).   
**Note** : If your application is not deploying to the Chromebook, check the **Run Device** dropdown in the **Build Settings**. If your device isn’t listed, but the adb connection between the host computer and Chromebook is established, enter the IP address of the device through the **< Enter IP>** option in the **Run Device** dropdown. After you enter the IP address, you can profile your application as usual.

## Profiling in the Unity Editor

When you use the Profiler window to run and profile your application in the Editor, the results are only an approximation of your application’s behavior when the target platform runs it. This is because Play mode runs in the same process as the Editor, so you can’t fully isolate your application’s CPU, GPU, and memory usage from the Unity Editor’s usage. This skews the resulting profiling data.

To get better profiling results, you should always profile your application on a target device, and only profile in the Editor to quickly iterate over issues you have already identified on a device.

You can also profile in Play mode or profile the Editor to identify issues unrelated to the performance of your application, such as whether long load times or an unresponsive Editor slows down iteration time, or if your application performs badly in Play mode.

Whenever you profile in the Editor, you should make sure that you open Play mode in maximized view, and reduce the amount of open Editor windows. This ensures that other Editor windows don’t use up time on the render thread and GPU, and therefore affect the performance data. When Play mode is in a maximized view it runs your application at a resolution closer to that of your target device, which directly affects performance issues such as those related to fill rate.

### Profiling in Play mode

The Profiler’s default target is Play mode, which records activities when the Editor is running Play mode. Play mode profiling is useful to test out quick changes without having to rebuild a player, but you should not use it as a replacement for validating builds on your application’s target platform and devices. This is because Play mode runs in the same application and main thread as the Editor, which means that when you profile in Play mode, the Editor’s systems such as the **UI** , **Inspectors** , **Inspectors** , **Scene** , **Scene** View rendering, and asset management affect the performance and memory profiling measurements of your application.

To effectively profile in Play mode, you should regularly make builds of your application and deploy them to a range of target devices (both high and low spec devices), and test and profile your application on these devices. If you identify performance issues with your application on these devices, narrow down the area that needs the most attention.

You can then profile your application in Play mode and quickly iterate over any changes you make to your application. You can use the information you got from profiling your application on target devices to identify if there is any similar behavior after profiling your application in Play mode. You can then make changes to your application and profile again in Play mode to quickly see the effects that your changes made. Once you are satisfied with your changes, build and deploy your application to the target devices again to validate your changes.

#### PlayerLoop and EditorLoop samples

To reduce the amount of noise and misleading measurements in the profiling data that the Editor creates while running Play mode, the CPU and GPU Profiler modules split their timings into those that happen in the **PlayerLoop** and those that happen in the **EditorLoop.** Unity assigns **Profiler samples** of these types with the PlayerLoop and EditorLoop markers.

When the Profiler targets Play mode, it only collects timing samples that happened inside the PlayerLoop.

Unity categorizes any EditorLoop samples as **Others** in the CPU Profiler module charts. As a result, EditorLoop samples are the biggest contributors to that category. If you want to see what the Editor does in this time and also get a more detailed breakdown of what else contributes to the **Others** category, change the Profiler target to the Editor instead.

**Important:** If you use Deep Profiling, and target Play mode, it has a performance impact on every function call that happens in both PlayerLoop and EditorLoop. This is because Deep Profiling hooks into the beginning and end of any scripting method call on domain reload and it doesn’t detect which parts are never called from the PlayerLoop. The method calls that happen in the EditorLoop don’t incur the full overhead of creating a sample, but they still check if they should emit one, which causes a smaller but still present overhead.

### Profiling the Editor

When you change the Profiler’s target to **Editor** , all the samples that were previously hidden under the EditorLoop marker contribute to their respective categories. This means that the information in the CPU Profiler module’s detail pane and its charts changes significantly.

To profile the Editor’s startup times, start the Editor with the command line option `-profiler-enable`.

To reduce the impact that the Profiler window has on Editor performance, you can use the Standalone Profiler, which opens the Profiler window in its own process. This is especially useful if you select the Editor as the profiling target, or are Deep Profiling your application, because the Profiler window itself usually uses resources that might skew the performance data.

## Best practices for profiling your application

When you profile your application, there are a few things that you can do to ensure consistency across profiling sessions, and to make sure that the processes that Unity uses do not affect your profiling data:

  * Only add the Profiler modules related to the area that you want to investigate to the Profiler window. To add and remove modules to the Profiler, select the dropdown in the top left of the Profiler window.
  * Avoid using Deep Profiling, because it might create a high overhead when you use it. If you want to see more details on samples with markers such as `GC.Alloc` or `JobFence.Complete`, go to the Profiler window **toolbar**
  * Disable the **Live** setting, if you do not need to see the **Hierarchy** or **Timeline** view updating as the Profiler collects data. To see the data update in the window, you can stop recording.
  * Use the F9 shortcut to enable or disable the Profiler. You can use this shortcut to capture performance data without the Profiler window needing to be open. If you have the Standalone Profiler open, using this shortcut starts recording in this window.

* * *

  * Added Deep Profiling Support in 2019.3 NewIn20193