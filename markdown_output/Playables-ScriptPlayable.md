---
title: "ScriptPlayable and PlayableBehaviour"
category: "General"
source_file: "Playables-ScriptPlayable.html"
doc_type: "manual"
---

# ScriptPlayable and PlayableBehaviour

To create your own custom playable, it must be inherited from the PlayableBehaviour base class. ` public class MyCustomPlayableBehaviour : PlayableBehaviour { // Implementation of the custom playable behaviour // Override PlayableBehaviour methods as needed } `

To use a PlayableBehaviour as a custom playable, it also must be encapsulated within a ScriptPlayable<> object. If you don’t have an instance of your custom playable, you can create a ScriptPlayable<> for your object by calling:
    
    
    ScriptPlayable<MyCustomPlayableBehaviour>.Create(playableGraph);
    

If you already have an instance of your custom playable, you can wrap it with a ScriptPlayable<> by calling:
    
    
    MyCustomPlayableBehaviour myPlayable = new MyCustomPlayableBehaviour();
    ScriptPlayable<MyCustomPlayableBehaviour>.Create(playableGraph, myPlayable);
    

In this case, the instance is cloned before it is assigned to the ScriptPlayable<>. As it is, this code does exactly the same as the previous code; the difference is that `myPlayable` can be a public property that would be configured in the inspector, and you can then set up your behaviour for each instance of your script.

You can get the PlayableBehaviour object from the ScriptPlayable<> by using the `ScriptPlayable<T> .GetBehaviour()` method.

* * *

  * New in Unity 2017.1 NewIn20171