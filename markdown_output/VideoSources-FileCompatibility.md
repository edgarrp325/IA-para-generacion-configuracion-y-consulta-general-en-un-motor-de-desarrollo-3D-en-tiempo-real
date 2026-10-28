---
title: "Video file compatibility"
category: "General"
source_file: "VideoSources-FileCompatibility.html"
doc_type: "manual"
---

# Video file compatibility

You can import many video file formats into Unity. Unity stores imported video files as VideoClip assets.

For Unity to preview video files, the files must be compatible with the platform where you run the Unity Editor. Your files must also be compatible with the target build platforms. Unity provides options for transcoding files to commonly supported formats, but you can also manage compatibility yourself. See Compatibility with target platforms below for more information.

## Compatibility with Editor platforms

Video source files must use a format that your Editor platform supports. Each platform supports different video file formats.

Extension | Windows | macOS | Linux  
---|---|---|---  
.asf | X |  |   
.avi | X |  |   
.dv | X | X |   
.m4v | X | X |   
.mov | X | X |   
.mp4 | X | X |   
.mpg | X | X |   
.mpeg | X | X |   
.ogv | X | X | X  
.vp8 | X | X | X  
.webm | X | X | X  
.wmv | X |  |   
  
The optimal supported video codec for most platforms is H.264. However, the optimal encoding for Linux is a .webm container with VP8 for video and Vorbis for audio.

  * For video tracks, VP8.
  * For audio, Vorbis.

For information about codec support, see the official platform documentation for your Editor. See the links below for codec compatibility for Windows and macOS:

  * Windows codec compatibility
  * macOS codec compatibility

### WebM videos - Supported video and audio codecs 

Unity usually only supports the import of WebM videos with VP8 (video) and Vorbis (audio) codecs. However, you can use the `StreamingAssets` folder to add WebM videos with the other codecs to the project. When you use this folder, the Editor doesn’t interpret the file itself, instead the Editor imports the raw file into the build. For more information about this folder, refer to Include additional files in a build.

You can then use code to assign the raw file to the VideoPlayer component (refer to VideoPlayer.url). This allows the target platform to read the file directly and bypass the Editor’s support limitations. However, the imported video clip isn’t visible in the Editor and you can’t drag the asset onto a Video Player in the **scene**

When you use a video file in this way, it unlocks the following target platform capabilities:

**Platform** | **Supported video codecs** | **Supported audio codecs**  
---|---|---  
Android | Supports the video codecs that WebM files support on Android. Refer to the Android documentation on Supported media formats. | Supports the audio codecs that WebM files support on Android. Refer to the Android documentation on Supported media formats.  
Nintendo Switch | VP8, VP9 | Vorbis  
Web | VP8, VP9 | Vorbis, Opus  
  
### Video Clip Importer

The Video Clip Importer can transcode video files that you import into Unity. This is useful when your videos use a codec that the Editor platform supports, but the files aren’t compatible with your target platform.

### Using unsupported video files in the Editor

To use video files that are compatible with your target platforms, but not your Editor platform, set them up as streaming assets. For example, you might want to use the VP9 codec for an Android build, even though the Editor only supports VP8.

To set video files up as streaming assets, place them in the `StreamingAssets` folder of your project. Use the URL property to point the Video Player component to streaming assets.

You can also use Application.streamingAssetsPath to access platform-specific paths to streaming assets via **scripts**

If you want to have placeholder versions that are compatible with your Editor but use a different version for your target platform, you can include both versions in your project, use Editor-compatible versions as placeholders, and decide which version to use at run time.

The example below demonstrates how to use different video URLs for different platforms. For more information, see the documentation on Platform-dependent compilation.
    
    
    void SetupMovieFile(VideoPlayer vp)
    {
    #if UNITY_EDITOR || UNITY_LINUX
    vp.url = pathToMyVp8File;
    #elif UNITY_ANDROID
    vp.url = pathToMyVp9File;
    #elif UNITY_STANDALONE_WIN
    vp.url = pathToMyWmvFile;
    #else
    vp.url = pathToMyMp4File;
    #endif
    }
    

## Compatibility with target platforms

The Video Player component uses the native audio and video decoding libraries of your Editor platform to play video files in the Editor. You must confirm that the files also meet the requirements for the target platform.

### Encoding recommendations

  * The best natively supported video codec for hardware acceleration is H.264

  * When cross-platform support is a high priority, VP8 is a good choice. It’s widely supported and has a comprehensive **feature set**

  * H.265 is available on devices that support it. See H.265 Compatibility below, for more information.

  * Android supports VP8 using native libraries, so VP8 might also be hardware-assisted on some Android devices.

  * The Unity Editor supports the .ogv format, but it isn’t widely supported on other platforms. Transcode .ogv files into .mp4 (H.264) or .webm (VP8) depending on the target platform.

#### Key encoding values

The table below lists key values to look for in your encoding parameters:

Parameter | Description  
---|---  
Video Codec |  H.264, H.265 or VP8.  
Resolution | The resolution of your display. For example: 1280 × 720.  
Profile | The profile is a set of capabilities and constraints, often specified by the vendor, such as Baseline or Main. Applies to H.264/H.265.See H.264 or H.265.  
Profile Level | Applies for H.264/H.265. Within a given profile, the level specifies performance requirements, for example, Baseline 3.1.  
Audio Codec |  AAC (for mp4 videos using H.264/H.265) or Vorbis (for webm videos using VP8).  
Audio Channels | Dependent on the platform. Refer to the developer guide for your platform. For example, the article on Supported media formats for Android.  
  
### Encoding VideoClips with an external program

If you use videos that the target system definitely supports, you can leave the Video Clip Importer’s transcoding options disabled. If disabled, Unity doesn’t modify the files. You can manage encoding with an external program, which allows for finer control.

### Compatibility notes

This section provides useful information about video compatibility, and links to external resources.

#### Vendor recommendations for media support

Follow vendor recommendations for codec support. On older mobile platforms, codec choices are limited . You might need to inspect and convert or re-encode videos that you intend to include in a game running on multiple devices.

  * **Android:** Supported Media Formats
  * **Windows:** Supported Media Formats, H.265
  * **iPhone:** Compare iPhone Models
  * **UWP:** Supported Codecs

#### H.265 compatibility

The table below provides platform-specific requirements and information for the H.265 codec.

Platform | Requirements | Encoding/Decoding | Notes  
---|---|---|---  
**macOS** | SDK 10.13+ |  **Hardware encoding:** 6th Generation Intel Core processor   
  
**Software encoding:** All Macs   
  
**Hardware decoding:** 6th Generation Intel Core processor   
  
**Software decoding:** All Macs |   
**Windows** | Windows 10 + HEVC extensions |  Encoder  
  
Decoder |  HEVC extension (Hardware only)  
  
HEVC extension (Hardware + software support)  
**iOS** | SDK 11.0+ |  **Hardware decoding:** A9 Chip   
  
**Software decoding:** All iOS Devices |   
**tvOS** | SDK 11.0+ |  |   
**UWP** | Windows 10+ |  | If a device lists support for H.265, that might not apply to all devices within the device family.  
**Android** | 5.0+ |  |   
  
The optimal supported video codec for most platforms is H.264. However, the optimal encoding for Linux is a .webm container with VP8 for video and Vorbis for audio.

## Additional resources

  * Video file compatibility with target platforms
  * Transcoding video files
  * Understand video files
  * Video transparency support