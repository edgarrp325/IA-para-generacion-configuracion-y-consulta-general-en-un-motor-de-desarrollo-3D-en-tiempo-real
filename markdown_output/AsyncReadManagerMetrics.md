---
title: "Asset loading metrics"
category: "General"
source_file: "AsyncReadManagerMetrics.html"
doc_type: "manual"
---

# Asset loading metrics

Use the AsyncReadManagerMetrics class to monitor runtime asset loading and file reading performance. This class records data about all the file read operations managed by the AsyncReadManager. 

The Unity Engine uses the AsyncReadManager to read most files at runtime. The files loaded with the AsyncReadManager include AssetBundles, Addressables and Resources. In addition, you can load files from **scripts**

The AsyncReadManagerMetrics class allows you to enable metrics collection and retrieve the recorded metrics data. You can also filter and summarize the recorded data to help your analysis. This metrics information can help you identify problem areas involving asset loading as well as measure the impact that your changes have on asset loading performance. 

The AsyncReadManagerMetrics class is _only_ available in **development builds**
    
    
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        AsyncReadManagerMetrics.StartCollectingMetrics();
    #endif
    

## Enabling metric collection

You must enable metrics collection before any data is recorded. Enable metrics collection with one of the following methods:

  * Calling AsyncReadManagerMetrics.StartCollectingMetrics
  * Passing **-enable-file-read-metrics** as a command line argument when launching your application

**Note:** you can pass **-enable-file-read-metrics** when launching the Unity Editor application to enable collection on entering Play mode. However, the Editor loads some categories of assets, such as textures, itself and does not reload them when you enter Playmode. To get a full picture of your file IO metrics, you must collect data from a development build of your application.

## Getting metric data

Retrieve the metrics collected by the AsyncReadManagerMetrics class by calling GetMetrics. Pass an AsyncReadManagerMetrics.Flags to this function to specify whether or not to clear the metrics after retrieval. Clear the metrics to remove all the completed (including cancelled and failed) reads from the stored metrics. Clearing doesn’t affect any queued or in-process operations; you can access the metrics for unfinished operations by calling GetMetrics again after they complete. By clearing the metrics regularly, you can avoid rereading the same data and also reduce the data overhead of the system. 
    
    
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        AsyncReadManagerRequestMetric[] metrics 
            = AsyncReadManagerMetrics.GetMetrics(AsyncReadManagerMetrics.Flags.ClearOnRead);
    #endif
    
    

Where possible, the metric data includes context information about a read operation. This information includes the AssetLoadingSubsystem that requested the read, the AssetName, and the AssetTypeID. When the AsyncReadManager doesn’t have access to this information, the value for these metrics fields is Other, empty, and zero, respectively. 

**Note:** The Asset TypeIDs currently known to be supported are shown in the table below. For other TypeIDs that may appear, please see YAML Class ID Reference.

TypeID | Type Name  
---|---  
28 | Texture2D  
117 | Texture3D  
89 | **CubeMap**  
43 | Mesh  
  
## Getting summarized data

You can get a summary of the AsyncReadManager metrics with the following methods:

  * GetCurrentSummaryMetrics – returns a summary of all the metrics collected since the last time you cleared the metric store.
  * GetSummaryOfMetrics – returns a summary of the metrics in an array of AsyncReadManagerRequestMetric, which you can get by calling GetMetrics.

For example:
    
    
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        AsyncReadManagerSummaryMetrics summaryOfMetrics 
            = AsyncReadManagerMetrics.GetCurrentSummaryMetrics(AsyncReadManagerMetrics.Flags.ClearOnRead);
    #endif
    

Or:
    
    
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        AsyncReadManagerRequestMetric[] metrics 
            = AsyncReadManagerMetrics.GetMetrics(AsyncReadManagerMetrics.Flags.ClearOnRead);
        AsyncReadManagerSummaryMetrics summaryOfMetrics 
            = AsyncReadManagerMetrics.GetSummaryOfMetrics(metrics);
    #endif
    

Summary data for the metrics includes statistics such as:

  * Average bandwidth
  * Average read size
  * Asset type with longest load time
  * Number of reads
  * Number of requests
  * Total bytes read

(See AsyncReadManagerSummaryMetrics for a complete list.)

By default, the summarized statistics include all read operations, including those that are queued or in-progress. You can use a filter to limit the summary to those operations you are specifically interested in. For example, you could use a filter to limit the summarized statistics to completed read operations for texture assets. 

**Note:** Calculating the summary statistics does require processing resources. To prevent these calculations from changing the measurements you are recording, you can collect the metrics first and only get the summary after the operations you are analyzing have finished. 

### Summary filters

Use AsyncReadManagerMetricsFilters with either of these methods to specify what types of data to summarize. Any metrics that do not match a filter are excluded from the summary. You can filter with the following categories:

  * Asset type (by YAML ID)
  * Processing state (whether the read operation is queued, reading, completed, and so on)
  * Read type (async or sync)
  * Priority (high or low)
  * Subsystem (AssetLoadingSubsystem)

You can set multiple categories for the same filter. A read operation must match all categories for the metrics of that operation to be included in the summary. For example, you can specify values for both the ProcessingState and the Subsystem of a filter to summarize only operations in the designated processing states initiated by the designated subsytems.

You can also specify multiple values for a category. In this case, a read operation can match any value you specify for a category for its metrics to be included in the summary. For example, you can specify both Mesh and Texture and Texture for the Subsystem category to summarize operations for both Mesh and Texture assets.