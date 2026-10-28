---
title: "Batching with the AssetDatabase"
category: "General"
source_file: "AssetDatabaseBatching.html"
doc_type: "manual"
---

# Batching with the AssetDatabase

You can use batching to reduce the amount of time and processing taken when making changes to Assets in your code.

If you make changes to multiple Asset in your code (for example, copying or moving Asset files), the Asset Database’s default behavior is to process each change in turn, and perform a full Refresh process for the Asset before moving on to the next line of code.

In the example below, three Assets are changed. Asset1 is copied, Asset2 is moved, and Asset3 is deleted:
    
    
    AssetDatabase.CopyAsset("Assets/Asset1.txt", "Assets/Text/Asset1.txt");
    AssetDatabase.MoveAsset("Assets/Asset2.txt", "Assets/Text/Asset2.txt");
    AssetDatabase.DeleteAsset("Assets/Asset3.txt");
    

Without batching, Unity processes each change before moving on to the next line of code. This not only takes an unnecessarily long amount of time, but also triggers many callbacks that you can avoid if you use batching.

Instead, you can specify that the Asset Database should process a group of operations at once. To do this, you need to tell the Asset Database to pause its normal behavior before you make your changes, then tell it to resume after your changes are complete.

In particular, you should try to use batching if you are doing more than one of any of the following operations:

  * AssetDatabase.ImportAsset
  * AssetDatabase.MoveAsset
  * AssetDatabase.CopyAsset
  * AddObjectToAsset

## Methods to process operations

To specify that the Asset Database should process a group of operations at once, you can use the following methods: AssetDatabase.StartAssetEditing and AssetDatabase.StopAssetEditing.

**AssetDatabase.StartAssetEditing**

This method tells the Asset Database that you are starting to make edits to Assets. The Asset Database enters a paused state, and does not process any further changes to your Assets until you call the corresponding **StopAssetEditing** method to tell it you are finished.

**AssetDatabase.StopAssetEditing**

Once you perform all of your Asset changes, call this method to tell the Asset Database to process your changes and resume its normal behavior of automatically processing changes immediately. The Asset Database then processes the changes you made between `StartAssetEditing` and `StopAssetEditing` in a Batch, which is faster than if they had been processed one by one. 

### Nested calls to StartAssetEditing and StopAssetEditing

If you make more than one call to `StartAssetEditing`, you must make the corresponding number of calls to `StopAssetEditing` to make the Asset Database resume its normal behavior of automatically processing changes.

This is because these functions increment and decrement a counter, rather than acting as a simple on/off switch. Calling `StartAssetEditing` increments the counter, and calling `StopAssetEditing` decrements the counter. The Asset Database resumes its normal behavior when the counter reaches zero. 

The reason Unity uses a counter rather than a simple on/off boolean is so that if your code executes multiple nested “start” and “stop” pairs, the inner pairs do not accidentally re-enable the Asset Database’s normal behavior too early. Instead, each pair increments and decrements the counter by one, and if your code is correctly nested, the final outer call to `StopAssetEditing` sets the counter to zero.

**Note:** Your code should never cause the counter to go below zero. Doing so generates an error.

## Example

The following example shows the recommended way to use these methods:
    
    
    using UnityEditor;
    public class StartStopAssetEditingExample : MonoBehaviour
    {
        [MenuItem("APIExamples/StartStopAssetEditing")]
        static void CallAssetDatabaseAPIsBetweenStartStopAssetEditing()
        {
            try
            {
                //Place the Asset Database in a state where
                //importing is suspended for most APIs
                AssetDatabase.StartAssetEditing();
                AssetDatabase.CopyAsset("Assets/Asset1.txt", "Assets/Text/Asset1.txt");
                AssetDatabase.MoveAsset("Assets/Asset2.txt", "Assets/Text/Asset2.txt");
                AssetDatabase.DeleteAsset("Assets/Asset3.txt");
            }
            finally
            {
                //Adding a call to StopAssetEditing inside
                //a "finally" block ensures that the AssetDatabase
                //state will be reset when leaving this function
                AssetDatabase.StopAssetEditing();
            }
        }
    }
    

## Using try…finally for Asset Editing

When you call `AssetDatabase.StartAssetEditing`, Unity puts the entire Editor’s AssetDatabase in a paused state. As such, if you do not make a corresponding call to AssetDatabase.`StopAssetEditing`, the Editor appears to be unresponsive when it comes to any Asset-related operations (Importing, Refreshing, etc.), and requires an Editor restart to restore its normal operation. 

Without using a `try` … `finally` block, if any of your code which modifies Assets causes an error, it might prevent the `StopAssetEditing` from being called. To avoid this situation, wrap the calls inside a `try`…`finally` block, with the `StartAssetEditing`, and your Asset modification code in the `try` block, and the `StopAssetEditing` call placed in the `finally` block. This ensures that if any exceptions happen while your changes are made in the `try` block, it’s still guaranteed that `AssetDatabase.StopAssetEditing` will be called.