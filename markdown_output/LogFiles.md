---
title: "Log files"
category: "General"
source_file: "LogFiles.html"
doc_type: "manual"
---

# Log files

Unity produces log files for the Editor, package manager, licensing, development players, and Hub. You can use these log files to understand where any problems happened in your application.

Unity adds all messages, warnings, and errors from the Console window to the log files. To add your own messages to the Console window, and the logs, use the Debug class.

Each operating system stores the log files in different locations. The default locations are outlined on this page, but you can also use certain command line arguments to control when and where Unity generates log files. For more information, see the Command line arguments documentation.

**Note:** Not all platforms support this feature. See platform specific documentation for further information.

## Editor-related log locations

You can access the Editor logs from the console window. To do this, open a Console Window (**menu: Window > General > Console**) and select **Open Editor Log** from the Console window menu. 

You can access the other logs by using your operating system’s file manager application.

### Linux

**Log type** | **Log location**  
---|---  
**Editor** | `~/.config/unity3d/Editor.log`  
**Package manager** | `~/.config/unity3d/upm.log`  
**Licensing client** | `~/.config/unity3d/Unity/Unity.Licensing.Client.log`  
**Licensing audits** | `~/.config/unity3d/Unity/Unity.Entitlements.Audit.log`  
  
### macOS

On macOS, you can also access Unity’s logs via the Console.app utility

**Log type** | **Log location**  
---|---  
**Editor** | `~/Library/Logs/Unity/Editor.log`  
**Package manager** | `~/Library/Logs/Unity/upm.log`  
**Licensing client** | `~/Library/Logs/Unity/Unity.Licensing.Client.log`  
**Licensing audits** | `~/Library/Logs/Unity/Unity.Entitlements.Audit.log`  
  
### Windows

On Windows, the Package Manager and Editor logs are placed in folders which aren’t shown in the Windows Explorer by default. To view the AppData folder, you must enable the Hidden Items setting on Windows. For more information on how to do this, see Microsoft’s documentation on View hidden files and folders in Windows.

On Windows, a standard out stream doesn’t exist by default, so you must launch the Editor with a valid configured `stdout` stream, as a child process from a CI system. If you specify `-` to send output` `to`stdout`, then you won’t see the output in the console window.

**Log type** | **Log location**  
---|---  
**Editor** | `%LOCALAPPDATA%\Unity\Editor\Editor.log`  
**Package manager** | User account: `%LOCALAPPDATA%\Unity\Editor\upm.log`   
SYSTEM account: `%ALLUSERSPROFILE%\Unity\Editor\upm.log`  
**Licensing client** | `%LOCALAPPDATA%\Unity\Unity.Licensing.Client.log`  
**Licensing audits** | `%LOCALAPPDATA%\Unity\Unity.Entitlements.Audit.log`  
**Crash files** |  `%TMP%\CompanyName\ProductName\Crashes`   
  
**Note:** You can overwrite the location of the folder location with the `-crash-report-folder` command line argument.  
  
## Player-related log locations

To view the Player log, open a Console Window (**menu: Window > General > Console**) and select **Open Player Log** from the Console window menu. You can also navigate to the following folder:

**Operating system** | ****Player log** location**  
---|---  
**Android** | To access the Player log for an Android application, use Android logcat. For more information, see View Android logs.  
**iOS** | Use the GDB console, or the Organizer Console through XCode to access iOS device logs. For more information on device logs, see Apple’s documentation.  
**Linux** | `~/.config/unity3d/CompanyName/ProductName/Player.log`  
**macOS** |  `~/Library/Logs/Company Name/Product Name/Player.log`  
  
**Note:** You can also use the Console.app utility to find the log file.  
**Universal Windows Platform** | `%USERPROFILE%\AppData\Local\Packages\<productname>\TempState\UnityPlayer.log`  
****WebGL**** | Unity writes the log output to your browser’s JavaScript console.  
**Windows** | `%USERPROFILE%\AppData\LocalLow\CompanyName\ProductName\Player.log`  
  
## Unity Hub log locations

You can access the Hub logs by using your operating system’s file manager application. You can also access these logs from within the Hub. For more information, see Hub documentation.

**Operating system** | **Player log location**  
---|---  
**Linux** | `~/.config/UnityHub/logs/info-log.json`  
**macOS** | `~/Library/Application\ Support/UnityHub/logs/info-log.json`  
**Windows** | `%UserProfile%\AppData\Roaming\UnityHub\logs\info-log.json`