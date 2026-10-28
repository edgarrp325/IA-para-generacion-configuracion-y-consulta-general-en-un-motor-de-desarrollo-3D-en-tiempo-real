---
title: "Prepare Sprite Packer Legacy packed assets to work after deprecation"
category: "General"
source_file: "spritepacker-prep-for-deprecation.html"
doc_type: "manual"
---

# Prepare Sprite Packer Legacy packed assets to work after deprecation

This page provides the **scripts** required to allow existing assets packed with ****Sprite** required to allow existing assets packed with ****Sprite** Packer** to continue working after its deprecation from Unity 2020.1 onwards with the following constraints:**

  1. The **Packing Tags** property in the Texture Importer settings is set to read-only.
  2. Unity will not automatically pack Atlases based on **Packing Tags**. You will need to call the script provided here, using `IPreprocessBuildWithReport`.
  3. The Sprite Packer Mode setting will only display the **Disabled** and different **Sprite Atlas** options. The ****Sprite Packer****

## Custom Script to force Unity to pack an Atlas for Packing Tags

Use the following script to have Unity pack textures assigned the Packing Tag into an Atlas.
    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEditor;
    using UnityEditor.Build;
    using UnityEditor.Build.Reporting;
    using UnityEngine;
    class BuildPreProcessor : IPreprocessBuildWithReport
    {
        public int callbackOrder { get { return 0; } }
        public void OnPreprocessBuild(BuildReport report)
        {
            EditorSettings.spritePackerMode = SpritePackerMode.BuildTimeOnly;
    UnityEditor.Sprites.Packer.RebuildAtlasCacheIfNeeded(BuildTarget.StandaloneWindows64, false);
        }
    }
    

**Note:** The `BuildPreProcessor` class inherits from `IPreprocessBuildWithReport` and will only trigger when building.

## Conversion script

Use the following conversion script to migrate an existing Packing Tag based Atlas to the Sprite Atlas system:
    
    
    using UnityEditor;
    using UnityEngine;
    using System.Collections;
    using System.Collections.Generic;
    using UnityEditor.U2D;
    using UnityEngine.U2D;
     
    public class PrintAtlas : MonoBehaviour
    {
        [MenuItem("Atlas/ConvertTags")]
        static void ConvertTags()
        {
            Dictionary<string, List<string>> TagSpriteMap = new Dictionary<string, List<string>>();
     
            foreach (string s in AssetDatabase.GetAllAssetPaths())
            {
                TextureImporter ta = AssetImporter.GetAtPath(s) as TextureImporter;
                if (ta != null)
                {
                    if (ta.spritePackingTag != "")
                    {
                        if (!TagSpriteMap.ContainsKey(ta.spritePackingTag))
                        {
                            List<string> newList = new List<string>();
                            TagSpriteMap[ta.spritePackingTag] = newList;
                        }
                        TagSpriteMap[ta.spritePackingTag].Add(s);
                    }
                }
            }
     
            AssetDatabase.CreateFolder("Assets", "SpriteAtlas");
            foreach (var tagSprite in TagSpriteMap)
            {
                List<string> assetsforTag = tagSprite.Value;
                string alasPath = "Assets/SpriteAtlas/" + tagSprite.Key + ".spriteatlas";
                SpriteAtlas sa = new SpriteAtlas();
                AssetDatabase.CreateAsset(sa, alasPath);
     
                foreach (var asset in assetsforTag)
                {
                    Debug.Log(tagSprite.Key + " = " + asset);
                    Texture2D tex = AssetDatabase.LoadAssetAtPath<Texture2D>(asset);
                    sa.Add(new Object[1] { tex } );
                }
            }
     
            AssetDatabase.SaveAssets();
        }
    }
    

## Additional Resources

  * Sprite Atlas
  * Sprite Atlas V2