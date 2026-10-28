---
title: "Build Player Pipeline"
category: "General"
source_file: "BuildPlayerPipeline.html"
doc_type: "manual"
---

# Build Player Pipeline

When building a player, you sometimes want to modify the built player in some way. For example you might want to add a custom icon, copy some documentation next to the player or build an Installer. You can do this via editor scripting using BuildPipeline.BuildPlayer to run the build and then follow it with whatever postprocessing code you need:
    
    
    // C# example.
    using UnityEditor;
    using System.Diagnostics;
    
    public class ScriptBatch 
    {
        [MenuItem("MyTools/Windows Build With Postprocess")]
        public static void BuildGame ()
        {
            // Get filename.
            string path = EditorUtility.SaveFolderPanel("Choose Location of Built Game", "", "");
            string[] levels = new string[] {"Assets/Scene1.unity", "Assets/Scene2.unity"};
    
            // Build player.
            BuildPipeline.BuildPlayer(levels, path + "/BuiltGame.exe", BuildTarget.StandaloneWindows, BuildOptions.None);
    
            // Copy a file from the project folder to the build folder, alongside the built game.
            FileUtil.CopyFileOrDirectory("Assets/Templates/Readme.txt", path + "Readme.txt");
    
            // Run the game (Process class from System.Diagnostics).
            Process proc = new Process();
            proc.StartInfo.FileName = path + "/BuiltGame.exe";
            proc.Start();
        }
    }
    
    

## PostProcessBuild Attribute

You can also use the postprocessOrder parameter of the PostProcessBuildAttribute to define the execution order for your build methods, and call your external **scripts**