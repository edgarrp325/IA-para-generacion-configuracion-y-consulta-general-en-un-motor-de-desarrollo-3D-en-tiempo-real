---
title: "Loading texture and mesh data"
category: "General"
source_file: "LoadingTextureandMeshData.html"
doc_type: "manual"
---

# Loading texture and mesh data

Unity can load texture and **mesh** data from disk and upload it to the GPU in two different ways: synchronously or asynchronously. These two processes are called the synchronous upload pipeline and the asynchronous upload pipeline.

When Unity uses the synchronous upload pipeline, it cannot perform other tasks while it loads and uploads the data. This can cause visible pauses in your application. When Unity uses the asynchronous upload pipeline, it can perform other tasks while it loads and uploads the data in the background.

If a texture or mesh is eligible for the asynchronous upload pipeline, Unity uses the asynchronous upload pipeline automatically. If a texture or mesh is ineligible for the asynchronous upload pipeline, Unity uses the synchronous upload pipeline automatically.

## How it works

The main difference between the synchronous and asynchronous upload pipelines is where Unity saves the data at build time, which affects how Unity loads it at runtime.

In the synchronous upload pipeline, Unity must load both the metadata (header data) and the texel or vertex data (binary data) for the texture or mesh in a single frame. In the asynchronous upload pipeline, Unity must load only the header data in a single frame, and it can stream the binary data to the GPU over subsequent frames.

In the synchronous upload pipeline:

  * At build time, Unity writes both the header and the binary data for the mesh or texture to the same .res file.
  * At runtime, when the application needs the texture or mesh, Unity loads both the header data and binary data for that texture or mesh from the .res file into memory. When all of the data is in memory, Unity then uploads the binary data from memory to the GPU. The loading and uploading operations occur mainly on the main thread, in a single frame.

In the asynchronous upload pipeline:

  * At build time, Unity writes the header data to a .res file and the binary data to a separate .resS file.
  * At runtime, when the application needs the texture or mesh, Unity loads the header from the .res file into memory. When the header is in memory, Unity then streams the binary data from the .resS file to the GPU using a fixed-sized ring buffer. Unity streams the binary data using multiple threads, over the course of several frames. Note that on some console platforms where Unity already knows the GPU hardware, Unity skips the ring buffer and loads straight into the GPU memory.

## Texture and mesh data eligibility

A texture is eligible for the asynchronous upload pipeline if the following conditions are met:

  * The texture is not read/write enabled.
  * The texture is not in the Resources folder.
  * If the build target is Android, LZ4 **compression** is enabled in the Project’s Build Settings.

Note that if you load a texture using `LoadImage(byte[] data)`, this forces Unity to use the synchronous upload pipeline, even if the above conditions are met.

A mesh is eligible for the asynchronous upload pipeline if the following conditions are met:

  * The mesh is not read/write enabled.
  * The mesh is not in the Resources folder.
  * The mesh has no BlendShapes.
  * Unity has not applied **Dynamic Batching** to the mesh, either because the mesh is ineligible for Dynamic Batching or because Dynamic Batching is disabled. For more information on Dynamic Batching, see Draw call batching.
  * The mesh vertex/index data is not needed by a **Particle System** , a **Terrain** , a **Terrain** , or a Mesh **Collider** , or a Mesh **Collider**.
  * The mesh has no bone weights.
  * The mesh topology is not quads
  * The meshCompression for the mesh asset is set to Off. If the build target is Android, LZ4 compression is enabled in the Project’s Build Settings.

In all other circumstances, Unity loads textures and meshes synchronously.

## How to identify which upload pipeline Unity is using

You can use the Profiler or another profiling tool to identify when Unity is using the asynchronous upload pipeline, by observing thread activity and **profiler markers** or another profiling tool to identify when Unity is using the asynchronous upload pipeline, by observing thread activity and **profiler markers**.

The following indicate that Unity is using the asynchronous upload pipeline to upload textures or meshes:

  * The `AsyncUploadManager.ScheduleAsyncRead`, `AsyncReadManager.ReadFile`, and `Async.DirectTextureLoadBegin` profiler markers.
  * Activity on the `AsyncRead` thread.

If you do not see this activity, then Unity is not using the asynchronous upload pipeline.

Note that the following profiler markers do not indicate that Unity is using the asynchronous upload pipeline; Unity calls them to check whether any asynchronous upload work needs to occur:

  * `Initialization.AsyncUploadTimeSlicedUpdate`
  * `AsyncUploadManager.AsyncResourceUpload`
  * `AsyncUploadManager.ScheduleAsyncCommands`

## Configuring the asynchronous upload pipeline

You can configure these settings for the asynchronous upload pipeline. Note that you cannot configure settings for the synchronous upload pipeline.

The Async Upload settings in the Quality settings

### Async Upload Buffer

Unity re-uses a single ring buffer to stream texture and mesh data to the GPU. This reduces the number of memory allocations required.

The **Async Upload Buffer** determines the size of this ring buffer. It has a minimum size of 2 megabytes, and a maximum size of 2047 megabytes.

Unity automatically resizes the buffer to fit the largest texture or mesh that is currently loading. This can be a slow operation, especially if Unity has to perform it more than once; for example, if you are loading many textures that are larger than the default buffer size. To reduce the number of times that Unity must resize the buffer, set this value to fit the largest value that you expect to load. This is usually the largest texture in the **Scene**. 

You can configure this value in the Quality settings window, or using the QualitySettings.asyncUploadBufferSize API.

### Async Upload Time Slice

**Async Upload Time Slice** is the amount of time the CPU spends uploading texture or mesh data to the GPU, in milliseconds per frame.

A larger value means the data will be ready on the GPU sooner, but the CPU will spend more time on upload operations during those frames. Note that Unity only uses this time for uploading if there is data waiting in the buffer to be uploaded to the GPU; if there is no data waiting, Unity can use this time for other operations.

You can configure this value in the Quality settings window, or using the QualitySettings.asyncUploadTimeSlice API. 

## Further information

For more information on uploading texture and mesh data asynchronously, see the Unity blog post Optimizing loading performance: Understanding the Async Upload Pipeline.