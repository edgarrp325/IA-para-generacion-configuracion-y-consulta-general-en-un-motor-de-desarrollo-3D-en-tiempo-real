---
title: "Gradle templates"
category: "General"
source_file: "gradle-templates.html"
doc_type: "manual"
---

# Gradle templates

Gradle templates configure how to build an Android application using Gradle. Each Gradle template represents a single Gradle project. Gradle projects can include, and depend on, other Gradle projects.

## Gradle template files

A Gradle template consists of the following files:

File | Location | Contains  
---|---|---  
`baseProjectTemplate.gradle` | In the exported project, `root/build.gradle` folder | Configuration information that affects all modules in the final Gradle project. It specifies which Android Gradle Plugin version to use and locations of java plugins. The locations are a combination of online repositories and java plugins inside of this project.  
`launcherTemplate.gradle` | In the exported project, `root/launcher/build.gradle` folder | Instructions on how to build the Android application. This includes bundling, signing, and whether to split the **apk**. It depends on the unityLibrary project and outputs either an .apk file or an app bundle.  
`mainTemplate.gradle` | In the exported project, `root/unityLibrary/build.gradle` folder | Instructions on how to build Unity as a Library. This outputs an .aar file. You can override the Unity template with a custom template in the Unity Editor. Refer to the Providing a custom Gradle build template section on this page for more details.  
`libTemplate.gradle` | Varies | If an Android Library Project **plug-in**  
`settingsTemplate.gradle` | In the exported project, `root/settings.gradle` file | Specifies the names of modules that the Gradle build system should include when it builds the project. You can override the Unity template with a custom template in the Unity Editor. Refer to the Providing a custom Gradle build template section on this page for more details.  
`gradleTemplate.properties` | In the exported project, `root/gradle.properties` file | Configures the Gradle build system and specifies properties such as the size of the Java virtual machine (JVM) heap  
  
## Using a custom Gradle template

To have more control over the Gradle project files that Unity produces, you can override Unity’s default Gradle template files. To do this:

  1. Go to **Edit** > **Project Settings** to open the Project Settings window.
  2. Select the **Player** tab, then open Android Player Settings:  

  3. In the **Publishing Settings** section, enable the checkbox that corresponds to the Gradle project file type you want to create a custom template for. This creates a Gradle project template file and displays the path to the file.
  4. Modify the template file to control the format and contents of the final Gradle project file.

## Modifying the exported Gradle project using C#

To modify the Gradle project after Unity assembles it, create a class that inherits from IPostGenerateGradleAndroidProject and override the OnPostGenerateGradleAndroidProject function. This function receives the path to the unityLibrary module as a parameter and you can use it to reach the application’s manifest and resources through C# scripting.

**Warning** : Unity now uses an incremental build pipeline which means Unity reuses the same Gradle project for consecutive builds. This means that any modifications you do using this API accumulate since Unity no longer creates a new Gradle project for every build. For example, if you use this API to add an additional file to the Gradle project, the first build works as expected, but during the second build the file already exists. A second example is if you use this API to add a permission to a particular file. Each successive build adds another entry for the permission. It is crucial to make sure that modifications you want to make aren’t already present in the build.

## Additional resources

  * Gradle template variables