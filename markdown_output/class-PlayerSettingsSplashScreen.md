---
title: "Splash Image Player settings"
category: "General"
source_file: "class-PlayerSettingsSplashScreen.html"
doc_type: "manual"
---

# Splash Image Player settings

The **Splash Image** section of the **Player** settings window (menu: **Edit > Project Settings > Player > Splash Image**) allows you to configure a splash screen for your project. The splash screen displays when your application starts. 

You can use the settings in the **Splash Image** window to customize how the splash screen appears in your application, including disabling the Unity logo, adding your own logos, or disabling the splash screen entirely. However, the full customization of the splash screen is only available to those on Plus, Pro, or Enterprise Unity plans. If you’re on a Personal Plan, the following limitations apply to the Splash Image settings:

  * You can’t disable the **Show Splash Screen** setting to disable the splash screen
  * You can’t disable the **Show Unity Logo** setting to disable the Unity logo
  * The **Overlay Opacity** setting has a minimum value of 0.5

The Unity Splash Screen is the same across all platforms. It displays immediately while the first **Scene** of your application loads asynchronously in the background. However, if you use your own introductory screens or animations, this might take longer to appear because Unity has to load the entire engine and first Scene before it can display your own custom splash screen.

**Note:** Unity copies these options directly to the `Package.appxmanifest` file.

## Unity Splash Image settings

To configure the options for your application’s splash screen, open the Player Settings window (menu: **Edit > Project Settings > Player > Splash Image**). You can also use the SplashScreen API to control the splash screen settings.

Splash Image Player settings window **Setting** | **Description**  
---|---  
**Virtual Reality** Splash Image | Set an image to use for applications that use virtual reality. The image must be a 2D Texture.  
**Splash Screen** | Settings for displaying the splash screen  
Show Splash Screen |  | Enabled by default. Disable this setting to not display a splash screen at the start of your application. **Important:** If you have a Unity Personal plan you can’t disable this setting.  
Preview | Select the **Preview** button to see a preview of the Splash Screen in the Game view. The preview reflects the resolution and **aspect ratio** of the Game view.  
Splash Style | Settings for the color style of the Unity logo.  
| Light on Dark | A light version of the Unity logo best suited to display on dark colored backgrounds. This is the default setting.  
| Dark on Light | A dark version of the Unity logo best suited to display on light colored backgrounds.  
Animation | Settings for how the splash screen appears and disappears on screen.  
| Static | Doesn’t apply any animation.  
| Dolly | The logo and background zoom to create a visual dolly effect. This is the default setting.  
| Custom | Choose this setting to configure the background and logo zoom amounts to modify the dolly effect.  
| Logo Zoom | The target zoom (from 0 to 1) for the logo when it reaches the end of the logo animation’s total duration.  
| Background Zoom | The target zoom (from 0 to 1) for the background when it reaches the end of the splash screen animation’s total duration.  
**Logos** |  | Settings to customize the logos in your splash screen  
Show Unity Logo | Enabled by default. Disable this option to not display the Unity logo on the splash screen. **Important:** If you have a Unity Personal plan you can’t disable this setting.  
Draw Mode | Select the mode for the order that the logos appear on the splash screen  
| Unity Logo Below | Displays the Unity logo underneath all logos in the **Logos** list.  
| All Sequential | Displays the Unity logo sequentially with all logos in the **Logos** list.  
Logos | The logos to include on the splash screen. Each logo must be a Sprite Asset. Set the Sprite Mode to **Single** to use the entire sprite as the logo. If you want to change the logo’s aspect ratio, set the Sprite Mode to Multiple and edit the dimensions with the Sprite Editor.  
  
To add and remove logos, use the plus (+) and minus (-) buttons.  
  
To reorder logos, drag them in the list.  
  
To create a delay between logos, add an entry to the Logos list with no Sprite Asset assigned.  
| Logo Duration | Set the length of time each **Sprite** Asset appears on the screen. Use a value between 2 and 10 seconds.  
Splash Screen Duration | Displays the total duration of the splash screen sequence, in seconds. This is the total of all logos plus 0.5 seconds for fading out. **Note:** Your application’s splash screen might display for longer if the first Scene isn’t ready to play. In this case, the splash screen shows only the background image or color and then fades out when the first Scene is ready to play.  
**Background** | Settings to customize the background of your application’s splash screen.  
Overlay Opacity | Adjust the value of the Overlay Opacity setting to make the logos stand out. This affects the background color and image color of the logo, based on how you set the **Splash Style** (Light on Dark, or Dark on Light).  
  
Set the opacity to a lower value to reduce this effect. You can also disable the effect by setting it to 0. For example, if the Splash Style is **Light on Dark** , with a white background, the background becomes gray if you set the Overlay Opacity to 1, and white if set to 0.   
  
**Important:** If you have a Unity Personal plan, this setting has a minimum value of 0.5.  
Background Color | Sets a color for the splash screen. Unity uses this color if you don’t set a **Background Image**.  
  
Note: The Overlay Opacity setting has an effect on the display of the Background Color, and might not match the assigned color.  
  
Note: On Android, Unity also uses this color to hide the default automatic splash screen which appears on Android 12+ devices. This happens even if the **Background Image** is being set, therefore make sure this color matches with **Background Image**.  
Blur Background Image | Enable this setting to blur the Background Image you set. If you disable this setting, it displays the Background Image with no blur effect.  
Background Image |  | Set a reference to a Sprite image to use as a background. Unity adjusts the background image so that it fills the screen. It uniformly scales the image until it fits both the width and height of the screen. This means that parts of the image might extend beyond the screen edges in some aspect ratios. To adjust the background image’s response to aspect ratio, change the Sprite’s **Position** values in the Sprite Editor.   
  
**Note:** Splash Screen backgrounds don’t support HDR images. Avoid using HDR image formats such as RGBA16 for Splash Screen background images.  
Alternate Portrait Image | Set an alternative image to use with portrait aspect ratios (for example, a mobile device in portrait mode). If you don’t assign an Alternate Portrait Image Sprite, the Unity Editor uses the Sprite assigned as the **Background Image** for both portrait and landscape mode.  
  
You can adjust the Position and dimensions of the Sprite in the Sprite Editor to control the aspect ratio and position of the background image on the Splash Screen.  
  
PlayerSettingsSplashScreen