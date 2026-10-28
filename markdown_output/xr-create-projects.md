---
title: "Create an XR project"
category: "General"
source_file: "xr-create-projects.html"
doc_type: "manual"
---

# Create an XR project

To create an **XR** project, you can use an XR template from the Unity Hub or start with a non-XR project.

  * Create a new XR project
  * Start from a non-XR project

## Prerequisites

To create an XR project, you must first perform the following tasks:

  * Install the Unity Editor.
  * Add Editor modules to support the platform build targets on which the XR devices that you want to support run. For example, to support Android devices with ARCore or Meta Quest devices, you must add the Android module to your Editor using the Unity Hub.

**Note:** The makers of some XR devices might impose additional requirements, such as signing up for a developer account, in order to create applications for their platform. Such requirements are outside the scope of Unity documentation.

## XR templates

The quickest way to create a new XR project is with one of the XR templates in the Unity Hub. Projects you create with these templates are already configured with the XR **Plug-in** Management system, common XR plug-in and support packages, and a starting **scene** Management system, common XR plug-in and support packages, and a starting **scene** set up with the XR components.

The XR templates available for this version of Unity include:

Template | Version | Description  
---|---|---  
AR Mobile template | 1.0 | For mobile **augmented reality** projects. The template configures the project for URP, **AR** projects. The template configures the project for URP, **AR** Foundation, iOS, Android and the XR Interaction Toolkit. It includes an example scene and assets to demonstrate how to set up a project that is ready for AR development on mobile devices.  
Mixed Reality template | 1.0 | For **mixed reality** projects. The template configures the project for URP, OpenXR, AR Foundation, and the XR Interaction Toolkit. It includes an example scene and assets to demonstrate how to set up a project that is ready for Mixed Reality.  
VR template | 6.0 | For **virtual reality** projects. The template configures the project for URP, OpenXR, and the XR Interaction Toolkit. It includes an example scene and assets to demonstrate how to set up a project that is ready for interactive **VR** projects. The template configures the project for URP, OpenXR, and the XR Interaction Toolkit. It includes an example scene and assets to demonstrate how to set up a project that is ready for interactive **VR**.  
  
Choose a template in the Unity Hub when you create a new project.

## Create a new XR project

To create an XR project using a template:

  1. Open the Unity Hub.
  2. In the Hub, click the **New Project** button.
  3. Select the desired template: **Mixed Reality** , **VR** , or **AR Mobile**.
  4. If necessary, click **Download template**.
  5. Set a project name and save location.
  6. Click **Create project**. (Refer to the Unity Hub documentation for more information about creating projects in the Unity Hub.
  7. After the project opens in the Editor, configure the project’s XR plug-ins with the **XR Plug-in Management** system.
  8. Add additional XR packages, such as AR Foundation and the XR Interaction Toolkit, using the Package Manager. (A template might include these and other packages already.)
  9. Set up an XR scene.

**Tip:** After you create an XR project, go to the **XR Plug-in Management** section in your ****Project Settings**** and enable the plug-ins for the platforms you want to support. If you don’t see a platform tab on the XR Plug-in Management page, add the platform module to your Editor installation using the Unity Hub.

## Start from a non-XR project

You can always convert an existing non-XR project:

  1. Use the Unity Hub to open the project.
  2. In the Editor, configure the project’s XR plug-ins with the **XR Plug-in Management** system.
  3. Add additional XR packages, such as AR Foundation and the XR Interaction Toolkit, using the Package Manager.
  4. Set up an XR scene.