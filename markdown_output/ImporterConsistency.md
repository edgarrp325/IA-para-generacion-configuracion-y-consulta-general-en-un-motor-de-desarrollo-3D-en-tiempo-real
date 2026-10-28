---
title: "Importer Consistency"
category: "General"
source_file: "ImporterConsistency.html"
doc_type: "manual"
---

# Importer Consistency

Asset importers, including any scripted importers that you write, should produce consistent (deterministic) results. This means they should always produce the same output from the same input and set of dependencies.

To verify that this is the case for your importers, the Asset Database has two ways that you can check the consistency of the import results of the assets currently in your project. The two ways to check consistency are:

  * Manually reimport one or more assets in the Editor

  * Use the **-consistencyCheck** command line argument to open the Editor

## Manual reimport consistency checks

Manually reimporting an asset causes Unity to check whether a new import result matches the previous cached import results.

To start a manual reimport, right-click on an asset and select **Reimport** from the context menu.

Unity then checks the resulting import for consistency. If it detects inconsistent results, Unity prints a warning in the **Console window** with details about which importer caused the issue, such as:

`Importer(<name of importer>) generated inconsistent result for asset(guid:<guid of the asset>) "<name of asset>"`

When you reimport a root asset, Unity also reimports and performs the consistency check on its child assets.

## Command line consistency checks

The second way of doing the consistency check is to open Unity with the **-consistencyCheck** command line argument. This performs a consistency check on all assets and importers in the project.

Command line argument | Description | Example(s)  
---|---|---  
`-consistencyCheck` | Tells the Editor to perform a consistency check on startup. By default it performs a “local” check (see below). | -consistencyCheck  
`-consistencyCheckSourceMode string` | Sets the source for the consistency checker to check against when it compares the asset imports. There are two possible values: “local” or “cacheserver”.  
  
“local” means that it forces a reimport of all assets locally and checks if imports differ from the previous import.  
  
“cacheserver” means that it asks the cacheserver for the metadata for the assets and compares if the results locally match what is on the cacheserver. In this case reimporting all assets does not happen. |  `-consistencyCheckSourceMode local`   
-consistencyCheckSourceMode cacheserver  
  
Any inconsistencies found during startup are logged to the Console, as well as the Editor log file.

The consistency checker only checks asset imports that are cacheable. So if you disable caching for your ScriptedImporter then the consistency check for that import will also be disabled. See AssetImporters.ScriptedImporterAttribute for details on how to disable caching for a scripted importer. 

To use the cache server as validation source, see the Unity Accelerator documentation.

### Editor log

When importer inconsistencies are detected, you can find more information about the issue in the Editor log. This includes:

  * Which asset caused the failed consistency check

  * The GUID of that asset

  * The content hash for the asset import result

  * How it compares to the previous revision of the asset

The following is an example of an Editor log that shows importer inconsistencies:
    
    
    ConsistencyChecker - guid: a1945cd7aab67441ba89015f97494624, dependenciesHash.value: fb8cfb407bba82d4daded6031688ba9b, artifactid: 07078a054d3f597b4c2cc47e8e4c0bde, producedFiles[0].extension: , producedFiles[0].contentHash: 8490a5ed35a4361d679e6055a386969e
    
    ConsistencyChecker - guid: a1945cd7aab67441ba89015f97494624, dependenciesHash.value: fb8cfb407bba82d4daded6031688ba9b, artifactid: 07078a054d3f597b4c2cc47e8e4c0bde, producedFiles[1].extension: .info, producedFiles[1].contentHash: 4bd9140e19d2e44782f1131172e514ba
    
    ConsistencyChecker - guid: a1945cd7aab67441ba89015f97494624, dependenciesHash.value: fb8cfb407bba82d4daded6031688ba9b, artifactid: 646d6432767729ea7d288c636183de97, producedFiles[0].extension: , producedFiles[0].contentHash: 5ca760170f85012ce16aa8c22e8d9ea1
    
    ConsistencyChecker - guid: a1945cd7aab67441ba89015f97494624, dependenciesHash.value: fb8cfb407bba82d4daded6031688ba9b, artifactid: 646d6432767729ea7d288c636183de97, producedFiles[1].extension: .info, producedFiles[1].contentHash: 4bd9140e19d2e44782f1131172e514ba
    
    Importer(ScriptedImporter:Assembly-CSharp::RandomImporter) generated inconsistent result for asset(guid:a1945cd7aab67441ba89015f97494624) "Assets/first.rand"
    

If the cache server is not available, the consistency checker prints out warnings in the Editor log.

If a cache server hasn’t been set up for the project, the following message is printed.

`ConsistencyChecker - Cacheserver is not enabled`

If Unity cannot connect to the cache server, this message is printed.

`ConsistencyChecker - Not connected to accelerator/cacheserver`

## Debugging

You can use the tool ‘binary2text’, located in the Data/Tools folder in your Unity Editor installation, to examine the contents of the library folder to see exactly what the importer generated. 

For example:

`./Data/Tools/binary2text ./myProject/Library/Artifacts/84/8490a5ed35a4361d679e6055a386969e output_file`

The hash value is the asset’s content hash. To find the reported inconsistency and see what content was generated during the check, look at the Editor log.