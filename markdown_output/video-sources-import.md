---
title: "Import video sources"
category: "General"
source_file: "video-sources-import.html"
doc_type: "manual"
---

# Import video sources

The Video Player component plays content imported from a variety of sources, such as video clips, URLs, Asset Bundles, and from the Streaming Assets folder.

## Video Clip

The Video Player component plays videos from a Video Clip Asset. To create and use a Video Clip Asset, you must first import a video file. 

There are two ways to import a video file into Unity:

  * Drag a video file and drop it into the **Project window** to create a Video Clip.

A Video Clip created by dragging and dropping a video file into the Project window
  * Navigate to **Assets** > **Import New Asset…** to import a video file. 

After the video file is imported, you can select the newly created Video Clip in the Video Player component window using the **Select VideoClip** option by clicking the circle button to the right of the video clip, or by dragging and dropping the Video Clip Asset into the corresponding Video Player component field.

A **Video Player** component

## URLs

Use the **Source** drop-down to set the video source to **URL**. By default, the Source is set to **Video Clip**.

The Source field in the Video Player component

On native build platforms, setting Source to URL allows direct use of files in the filesystem, with or without a `file://` prefix. On the Web platform however, the Source must point to a web URL because playback from local filesystem and `Application.persistentDataPath` isn’t supported.

**Note:** Certain web browsers allow you to manually disable browser CORS security for `file://` URL access for local development and testing purposes. For example, in Chrome, you can start the browser with the `--allow-file-access-from-files` command line option, but this isn’t a recommended approach.

The URL source option bypasses Asset management; therefore, you must manually ensure that Unity is able to locate the source video. For example, a web URL needs a web server to host the source video, while a normal file must be located somewhere where Unity can find it, indicated with scripting. This helps in situations where the content isn’t under Unity’s direct control, or if you want to avoid storing large video files locally.

You can also set the Video Player component source to URL to read videos from web sources via `http://` and `https://`. In these cases, Unity performs the necessary pre-buffering and error management.

## Asset Bundles

Video Clips can also be read from Asset Bundles. 

After the video clips are imported, you can use them by assigning it in the Video Player component window **Video Clip** field. 

## Streaming Assets

Files placed in Unity’s StreamingAssets folder are used via the Video Player component’s **URL** option, or by using the platform-specific path `Application.streamingAssetsPath`.

## Additional resources

  * Video Player component
  * Video Clip
  * Asset Bundles
  * StreamingAssets folder