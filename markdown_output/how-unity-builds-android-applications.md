---
title: "How Unity builds Android applications"
category: "General"
source_file: "how-unity-builds-android-applications.html"
doc_type: "manual"
---

# How Unity builds Android applications

Unity uses Gradle to build Android applications so it is useful to understand the build process and how Unity interacts with Gradle. Gradle lets you use Player Settings to build Android applications so it is useful to understand the build process and how Unity interacts with Gradle. Gradle lets you use Player Settings and other Unity windows to configure most aspects of the final build, however for more control, you must overwrite manifest and template files, or export your project and edit it in Android Studio.

## The build process

To build Android applications:

  1. Unity collects project resources, code libraries, **plug-ins** , Gradle templates, and manifest templates from your Unity project and uses them to create a valid Gradle project.
  2. Unity adds and updates values inside Gradle templates and manifest files based on the Unity project’s Player Settings and Build Settings.
  3. If you chose to export the project and not build it, and use the **IL2CPP** scripting backend scripting backend, Unity places C++ source files produced from your C# **scripts** , Unity places C++ source files produced from your C# **scripts** into the Gradle project. Otherwise, if you chose to build the project, Unity places the `libil2cpp.so` library into the Gradle project.
  4. Unity calls OnPostGenerateGradleAndroidProject for all IPostGenerateGradleAndroidProject interfaces. You can use this callback to modify or move files before Gradle builds the application.
  5. Unity runs Gradle to build the application from the Gradle project. Gradle merges the Unity Library Manifest, Unity Launcher Manifest, and plug-in manifests into one Android App Manifest file.

## Incremental build pipeline

Unity uses the incremental build pipeline when it builds the Player for Android. See the following Android-specific incremental build pipeline behaviors:

  * Unity incrementally builds/generates: 
    * Gradle files
    * Manifest files
    * Assets packs
    * APK expansion files (obbs)
    * Uncompressed asset splits
    * Android symbols zip files
  * Unity incrementally copies: 
    * Player binaries
    * Gradle resources
  * The last step in the build process is to run Gradle. From this point, the build process doesn’t use the incremental build pipeline and it’s up to Gradle to track dependencies.

If you implement callbacks that modify or move any Android file or asset that the incremental build pipeline uses, see Creating non-incremental builds.

## Additional resources

  * Build your application for Android