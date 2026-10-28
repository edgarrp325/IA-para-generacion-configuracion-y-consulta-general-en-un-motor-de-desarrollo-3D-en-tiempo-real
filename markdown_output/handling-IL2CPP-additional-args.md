---
title: "Handling platform specific settings for IL2CPP additional arguments"
category: "General"
source_file: "handling-IL2CPP-additional-args.html"
doc_type: "manual"
---

# Handling platform specific settings for IL2CPP additional arguments

If your project has the additional **IL2CPP** arguments set, then compiling for more than one platform might not work as expected, especially when cross compiling for Linux. 

To find out if any additional IL2CPP arguments are already set, do one of the following:

  * Check if the environment variable `IL2CPP_ADDITIONAL_ARGS` is set.
  * In `ProjectSettings/ProjectSettings.asset`, check if the editor script has a value called `additionalIl2CppArgs`.

Note that the methods for setting additional IL2CPP arguments are globally applied to all platforms, which can cause compilation issues if set for a platform other than the desired platform. Use the `IPreprocessBuildWithReport` hook (as shown below) to ensure IL2CPP arguments are set only for the platform that requires them.

## IPreprocessBuildWithReport hook

Use the `IPreprocessBuildWithReport` hook to build **scripts** or the Build dialog to set the additional arguments:
    
    
    class MyCustomPreprocessBuild: IPreprocessBuildWithReport
    {
        public int callbackOrder { get { return 0; } }
        public void OnPreprocessBuild(BuildReport report)
        {
            string addlArgs = "";
            if (report.summary.platform == BuildTarget.StandaloneWindows || report.summary.platform == BuildTarget.StandaloneWindows64)
                addlArgs = "--compiler-flags=\"d2ssa-cfg-jt\"";
            UnityEngine.Debug.Log($"Setting Additional IL2CPP Args = \"{addlArgs}\" for platform {report.summary.platform}");
            PlayerSettings.SetAdditionalIl2CppArgs(addlArgs);
        }
    }