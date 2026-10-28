---
title: "Diagnose network issues"
category: "General"
source_file: "upm-network.html"
doc_type: "manual"
---

# Diagnose network issues

Use the Unity Package Manager Diagnostics tool to help diagnose common network issues associated with Unity Package Manager. The Diagnostics tool runs some basic network tests and creates files that the Unity support team needs to diagnose common network problems. After you run the tool, you can share the results with the Unity support team who can better guide you in resolving those issues.

To diagnose network issues:

  1. Run the Unity Package Manager Diagnostics tool by using either the Unity Package Manager Error dialog or by Manually running the script. 

  2. View the test results in the shell window. The tool output also lists the location of the `upm-diagnostic-report.txt` report and the `upm-diag.log` file that it created. 

  3. If you need help from the Unity support team, include `upm-diagnostic-report.txt` and `upm-diag.log` when you submit a bug.

## Method 1: Use the Unity Package Manager Error dialog

When Unity tries to launch, it starts the Package Manager process before it loads the project. If it encounters a critical error with Package Manager, Unity displays the following error message:

Critical error dialog appears prompting you for action

To run the Diagnostics tool, click **Diagnose**. Unity closes and launches the Diagnostics tool in a new window.

## Method 2: Manually run the script

Locate the `RunUnityPackageManagerDiagnostics` script in the `Diagnostics` folder within the installation folder for your Unity Editor:

**Operating system:** |  **Path to Diagnostics command line tool** :  
---|---  
Windows |  `<path-to-unity-installation-folder>`  
`\Unity`  
`\Data`  
`\Resources`  
`\PackageManager`  
`\Diagnostics`  
`\RunUnityPackageManagerDiagnostics.bat`  
macOS  
Linux |  `<path-to-unity-installation-folder>`  
`\Unity.app`  
`\Contents`  
`\Resources`  
`\PackageManager`  
`\Diagnostics`  
`\RunUnityPackageManagerDiagnostics`  
  
To launch the tool, either:

  * Run the script file from the command line.
  * Double-click the script file in your file browser. **Note:** On macOS, you must right-click `Unity.app` and select **Show Package Contents** to access the contents of `Unity.app`.

## Sample output

Diagnostic report on top of the tool results in the shell window

## Additional resources

  * Configuring your firewall
  * Configuring your proxy server