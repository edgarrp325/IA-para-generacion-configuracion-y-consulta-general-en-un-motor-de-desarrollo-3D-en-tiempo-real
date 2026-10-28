---
title: "Archives"
category: "General"
source_file: "Archives.html"
doc_type: "manual"
---

# Archives

An **archive** is a generic packaging format which can store any type of file, similar to a .zip file.

## Archive File System

Unity loads archives to a mount point within a ContentNamespace. Once Unity mounts the file, your application can access the files inside an Archive through any Unity systems that use Unity’s virtual file system. Use the AsyncReadManager to access the virtual file system directly.

## Create and mount an archive

The following example describes how to create an archive with the ContentBuildInterface.ArchiveAndCompress function and mount the archive with the ArchiveFileInterface.MountAsync function. This example produces and archive that uses LZ4 **compression** and contains one text file.
    
    
    using Unity.Collections.LowLevel.Unsafe;
    using Unity.Content;
    using Unity.IO.Archive;
    using Unity.IO.LowLevel.Unsafe;
    using UnityEngine;
    #if UNITY_EDITOR
    using UnityEditor.Build.Content;
    #endif
    
    public class SampleBehaviour : MonoBehaviour
    {
    #if UNITY_EDITOR
      unsafe void CreateAndMountArchive()
      { 
        // Create the Archive
        ResourceFile[] rFiles = new ResourceFile[1];
        ResourceFile rf = new ResourceFile();
        rf.fileAlias = "file1.txt";
        rf.fileName = "Assets/file1.txt";
        rFiles[0] = rf;
    
        string archivePath = System.IO.Path.Combine(Application.streamingAssetsPath, "myArchive");
        ContentBuildInterface.ArchiveAndCompress(rFiles, archivePath, UnityEngine.BuildCompression.LZ4);
    
        // Mount the Archive
        var ns = ContentNamespace.GetOrCreateNamespace("MyNamespace123");
        ArchiveHandle ahandle = ArchiveFileInterface.MountAsync(ns, archivePath, "a:");
        ahandle.JobHandle.Complete();
    
        string textFilePath = ahandle.GetMountPath() + "file1.txt"; // ns:/MyNamespace123/a:/file1.txt
        ReadCommand cmd;
        cmd.Size = 1024;
        cmd.Buffer = UnsafeUtility.Malloc(cmd.Size, 4, Unity.Collections.Allocator.Temp);
        cmd.Offset = 0;
        
        NativeArray<ReadCommand> cmds = new NativeArray<ReadCommand>(1, Allocator.Persistent);
        cmds[0] = cmd;
    
        ReadHandle rHandle = AsyncReadManager.Read(textFilePath, (ReadCommand*)cmds.GetUnsafePtr(), 1);
        rHandle.JobHandle.Complete();
    
        rHandle.Dispose();
        UnsafeUtility.Free(cmd.Buffer, Unity.Collections.Allocator.Temp);
        cmds.Dipose():
      }
    #endif
    }