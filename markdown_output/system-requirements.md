---
title: "System requirements for Unity 2022.3"
category: "General"
source_file: "system-requirements.html"
doc_type: "manual"
---

# System requirements for Unity 2022.3

This page outlines the system requirements you need to run Unity 2022.3 on all supported platforms.

  * Unity Editor system requirements
  * Unity Editor platform limitations
  * Unity Player system requirements: 
    * Mobile
    * Console
    * Desktop
    * Server platform
    * Web platform
    * XR platform
      * Standalone XR devices
      * Meta
      * OpenXR
      * Windows Mixed Reality
      * Magic Leap
      * Google ARCore
      * Apple ARKit
      * Apple visionOS
    * Embedded Systems

## Unity Editor system requirements

This section lists the hardware and software requirements to run the Unity Editor. Actual performance and rendering quality might vary depending on the complexity of your project.

For all operating systems, the Unity Editor is supported on workstations or laptop form factors running without emulation, container, or compatibility layer.

**Operating system** | **Operating system version** | **CPU** | **Graphics API** | **Additional requirements**  
---|---|---|---|---  
**Windows** | Windows 7 (SP1+), Windows 10 and Windows 11, 64-bit versions only. | X64 architecture with SSE2 instruction set support. | DX10, DX11, and DX12-capable GPUs. | Hardware vendor officially supported drivers.  
**macOS** | Mojave 10.14+ (Intel processors).  
Big Sur 11.0 (Apple silicon-based processors). | X64 architecture with SSE2 instruction set support (Intel processors).  
Apple M1 or above (Apple silicon-based processors). | Metal-capable Intel and AMD GPUs. | Apple officially supported drivers (Intel processor)   
Rosetta 2 is required for Apple silicon devices running on either Apple silicon or Intel versions of the Unity Editor.  
**Linux** | Ubuntu 20.04 and Ubuntu 18.04. | X64 architecture with SSE2 instruction set support. | OpenGL 3.2+ or Vulkan-capable Nvidia and AMD GPUs. | Gnome desktop environment running on top of X11 windowing system, Nvidia official proprietary graphics driver, or AMD Mesa graphics driver. Other configuration and user environment as provided stock with the supported distribution (Kernel, Compositor, etc.)  
  
**Note** : Microsoft support for Windows 7 ended January 14, 2020.

### RAM recommendations for the Unity Editor

To run the Unity Editor on Windows, macOS, or Linux, a minimum of 8 GB RAM is recommended.

However, the amount of RAM required to load and run your project depends on your project’s size and complexity. Larger and more complex projects require additional RAM.

## Unity Editor platform limitations

### Apple

On macOS, secondary Editor windows only maximize, and don’t enter full screen mode.

#### Apple silicon devices

Unity doesn’t support CPU lightmapping for Apple silicon devices, only GPU lightmapping.

### Linux

The Linux Editor has the following limitations:

  * Video importing is limited to the VP8 video format.
  * File systems are case sensitive.
  * If the Editor generates a `Pipe error !` message, you must increase the maximum open file limit in your current Editor session. For example, run `ulimit -n 4096` in the terminal before launching the Editor. For more information, refer to the Troubleshooting Linux Editor issues page.

## Unity Player system requirements

This section lists the minimum requirements to build and run the Unity Player. Actual performance and rendering quality might vary depending on the complexity of your project.

### Mobile

**Operating system** | **Operating system version** | **CPU** | **Graphics API** | **Additional requirements**  
---|---|---|---|---  
**Android** | 5.1 (API 22)+   
Customized versions of Android must include all supported Google standard APIs. | ARMv7 with Neon Support (32-bit and 64-bit) or ARM64. | OpenGL ES 2.0+, 3.0+, Vulkan  
**Note** : OpenGL ES 2.0 support is deprecated. | \- 1GB+ RAM   
\- Supported hardware devices must meet or exceed Google’s Android Compatibility Definition (Version 9.0) limited to the following Device Types:   
1\. Handheld (Section 2.2)   
2\. Television (Section 2.3)  
3\. Tablets (Section 2.6)  
\- Hardware must be running Android OS natively. With the exception of Android for ChromeOS, Android within a container or emulator isn’t supported.  
\- For development: Android SDK (12/API 31), Android NDK (r23b) and OpenJDK (11), which are installed by default with Unity Hub.  
**ChromeOS** | R89+ on stable release channel (Android API 28+) | ARMv7, ARM64, x86, and x86_64 | OpenGL ES 2.0+, 3.0+, Vulkan  
**Note** : OpenGL ES 2.0 support is deprecated. | \- Support for ChromeOS devices launched after 2019, such as Chromebooks, Chromebases, Chromeboxes, and tablets that can run Android apps and are within their Auto Update Expiration date.  
\- Support for script debugging and profiling using Android Debug Bridge (adb) over WiFi or Ethernet only.  
**iOS/iPadOS** | 12+   
  
**Note** : From Unity 2022.3.72f1 and later, the minimum supported version of iOS is 13. This requirement supports updates to the UIScene lifecycle. For more information, refer to Update your editor to receive UIScene lifecycle support (Unity Discussions). | A7 SoC+ | Metal | For development and debugging: refer to Apple documentation on XCode support.  
  
For App Store submission: refer to Apple’s submission guidelines for the required Xcode version.  
**tvOS** | 12+ | A8 SoC+ | Metal | Apple TV 4th generation+  
  
For information on PlayStation®4 (including PS VR), PlayStation®5 (including PS VR2), Xbox One, Xbox Series X|S, and Nintendo Switch™, refer to the Game Development For Console Platforms page. To build on console platforms, only Windows versions of Unity are supported. For specific requirements on any additional platform specific software needed, please refer to the developer documentation on the platform holders website, or contact your platform representative directly for further information.

### Console

For specific system requirements of the Unity Editor, refer to the version of Unity you’re using on the Unity downloads page.

**Platform** | **Operating system**  
---|---  
**Nintendo Switch™** | Microsoft Windows 10 Pro (64-bit) English or Japanese version  
**Xbox Series X|S** | Windows 10 64-bit (Version 1709 or higher): Home, Professional, and Enterprise  
**Xbox One** | Windows 10 64-bit (Version 1709 or higher): Home, Professional, and Enterprise  
**PlayStation®4 (including PS VR)** | Windows 10 Pro 64-bit (x64) Version 22H2  
**PlayStation®5 (including PS VR2)** | Windows 10 Pro 64-bit (x64) Version 22H2  
  
### Desktop

For all operating systems, the Unity Player is supported on workstations, laptop or tablet form factors, running without emulation, container or compatibility layer.

**Operating system** | **Operating system version** | **CPU** | **Graphics API** | **Additional requirements**  
---|---|---|---|---  
**Windows** | Windows 7 (SP1+), Windows 10 and Windows 11 | x86, x64 architecture with SSE2 instruction set support. | DX10, DX11, DX12 capable. | Hardware vendor officially supported drivers.  
For development: IL2CPP scripting backend requires Visual Studio 2015 with C++ Tools component or later and Windows 10+ SDK.  
**Universal Windows Platform** | Windows 10+, Xbox One, Xbox Series X|S, HoloLens | x86, x64 architecture with SSE2 instruction set support, ARM, ARM64. | DX10, DX11, DX12 capable GPUs. | Hardware vendor officially supported drivers.  
For development: Windows 10+ (64-bit), Visual Studio 2015 with C++ Tools component or later and Windows 10+ SDK.  
**macOS** | Mojave 10.14+ | Apple Silicon, x64 architecture with SSE2. | Metal capable Intel and AMD GPUs. | Apple officially supported drivers.  
For development: IL2CPP scripting backend requires Xcode. Targeting Apple Silicon with IL2CPP scripting backend requires macOS Catalina 10.15.4 and Xcode 12.2 or newer.  
**Linux** | Ubuntu 20.04, Ubuntu 18.04, and CentOS 7 | x64 architecture with SSE2 instruction set support. | OpenGL 3.2+, Vulkan capable. | Gnome desktop environment running on top of X11 windowing system  
Other configuration and user environment as provided stock with the supported distribution (such as Kernel or Compositor)  
Nvidia and AMD GPUs using Nvidia official proprietary graphics driver or AMD Mesa graphics driver.  
  
**Note** : Microsoft support for Windows 7 ended January 14, 2020.

### Server platform

**Operating system** | **Operating system version** | **CPU** | **GPU** | **Additional requirements**  
---|---|---|---|---  
**Windows** | Windows 7 (SP1+), Windows 10 and Windows 11, running on workstation and rack form factors, without emulation or compatibility layer. | x86, x64 architecture with SSE2 instruction set support. | No explicit GPU support. | Hardware vendor officially supported drivers.  
**macOS** | Mojave 10.14+ running on workstation and rack form factors, without emulation or compatibility layer. | x64 architecture with SSE2 instruction set support. | No explicit GPU support. | Hardware vendor officially supported drivers.  
**Linux** | Ubuntu 20.04, Ubuntu 18.04, and CentOS 7, running on workstation and rack form factors, without emulation or compatibility layer. | x64 architecture with SSE2 instruction set support. | No explicit GPU support. | Hardware vendor officially supported drivers.  
  
**Note** : Microsoft support for Windows 7 ended January 14, 2020.

### Web platform

**Operating system running browsers** | **Hardware** | **Additional requirements**  
---|---|---  
**Windows, macOS, and Linux** | Workstation and laptop form factors. | Versions of Chrome, Firefox, Safari or Edge (Chromium-based) that are:  
\- WebGL 2.0 capable  
\- HTML 5 standards compliant  
\- 64-bit  
\- WebAssembly capable  
**Note** : WebGL 1.0 support is deprecated.  
**Android and iOS** | Android or iOS device | Browser requirements:   
\- iOS Safari 15 and newer  
\- Chrome 58 and newer  
  
### XR platform system requirements

To enable **XR** and properly configure your Unity project, follow the steps outlined in the XR plug-in architecture page.

### Standalone XR devices

**Device** | **Device software**  
---|---  
Magic Leap 2 | Magic Leap 2 Core OS version 1.0+  
Meta Quest 1 | Quest software version 50 or earlier (See Quest 1 support for more information.)  
Meta Quest 2 | Quest software version 39+  
Meta Quest Pro | Quest software version 46+  
Microsoft HoloLens 1 | Windows 10 Holographic version 1809+  
Microsoft HoloLens 2 | Windows Holographic version 1903+  
  
### Meta desktop XR: Rift, Rift S

**Specification** | **Minimum requirement**  
---|---  
**Operating system version** | Windows 10+  
**CPU** | See Oculus recommended specifications.  
**GPU** | See Oculus recommended specifications.  
**Graphics API** | DX11  
  
### OpenXR

Refer to the OpenXR Plugin documentation for a list of compatible runtimes.

### Windows Mixed Reality

**Specification** | **Minimum requirement**  
---|---  
**Operating system version** | Windows 10 RS4+  
**CPU** | Intel 64-bit  
**Graphics API** | DX11  
  
### Google ARCore

**Specification** | **Minimum requirement**  
---|---  
**Operating system version** | See list of ARCore-supported devices.  
**CPU** | ARM 32-bit and 64-bit  
**Graphics API** | OpenGL ES 3.0+  
**Latest supported SDK version** | ARCore 1.24  
  
### Apple ARKit

**Specification** | **Minimum requirement**  
---|---  
**Operating system version** | iOS 12  
**CPU** | A9+  
**Graphics API** | Metal  
**Latest supported SDK version** | ARKit 5  
**Additional requirements** | You must use Xcode 12.5 or later when compiling an iOS Player that includes the ARKit XR Plugin.  
  
### Apple visionOS

**Specification** | **Minimum requirement**  
---|---  
**Operating system version** | visionOS 1.0+  
**Graphics API** | Metal or RealityKit  
**Additional requirements** | You must use Xcode 15.2 or later on an Apple silicon (M1+) computer to build the final app in Xcode. **Mixed reality** development requires Unity PolySpatial.  
  
### Embedded systems

Support for embedded platforms such as Embedded Linux and QNX is available on request for a wide variety of chipsets as part of Unity Industry, including Linux on ARM based chipsets and additional APIs for Android Automotive. Support for specific embedded configurations is available through Unity’s Embedded systems support plans.

The following table lists the recommended system requirements for Unity on embedded systems.

**Operating system** | **RAM** | **CPU** | **GPU**  
---|---|---|---  
Embedded Linux | 1GB+ | Dualcore x64, ARM64 | OpenGL ES 3 or Vulkan 1.1 Capable  
QNX | 1GB+ | Dualcore x64, ARM64 | OpenGL ES 3  
  
Android (Automotive) system requirements are the same as Android under Mobile.