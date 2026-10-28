---
title: "Garbage collection best practices"
category: "General"
source_file: "performance-garbage-collection-best-practices.html"
doc_type: "manual"
---

# Garbage collection best practices

Garbage collection is automatic, but the process requires a significant amount of CPU time. 

C#’s automatic memory management reduces the risk of memory leaks and other programming errors, in comparison to other programming languages like C++, where you must manually track and free all the memory you allocate. 

Automatic memory management allows you to write code quickly and easily, and with few errors. However, this convenience might have performance implications. To optimize your code for performance, you must avoid situations where your application triggers the garbage collector a lot. This section outlines some common issues and workflows that affect when your application triggers the garbage collector.

  * Temporary allocations
  * Reusable object pools
  * Repeated string concatenation
  * Method returning an array value
  * Collection and array reuse
  * Closures and anonymous methods
  * Boxing
  * Array-valued Unity APIs
  * Empty array reuse

## Temporary allocations

It’s common for an application to allocate temporary data to the managed heap in each frame; however, this can affect the performance of the application. For example:

  * If a program allocates one kilobyte (1KB) of temporary memory each frame, and it runs at 60 **frames per second** , then it must allocate 60 kilobytes of temporary memory per second. Over the course of a minute, this adds up to 3.6 megabytes of memory available to the garbage collector.
  * Invoking the garbage collector once per second has a negative effect on performance. If the garbage collector only runs once per minute, it has to clean up 3.6 megabytes spread across thousands of individual allocations, which might result in significant garbage collection times.
  * Loading operations have an impact on performance. If your application generates a lot of temporary objects during a heavy asset-loading operation, and Unity references those objects until the operation completes, then the garbage collector can’t release those temporary objects. This means that the managed heap needs to expand, even though Unity releases a lot of the objects that it contains a short time later.

To get around this, you should try to reduce the amount of frequently managed heap allocations as possible: ideally to 0 bytes per frame, or as close to zero as you can get. 

## Reusable object pools

There are a lot of cases where you can reduce the number of times that your application creates and destroys objects, to avoid generating garbage. There are certain types of objects in games, such as projectiles, which might appear over and over again even though only a small number are ever in play at once. In cases like this, you can reuse the objects, rather than destroy old ones and replace them with new ones. 

For example, it’s not optimal to instantiate a new projectile object from a **Prefab** every time one is fired. Instead, you can calculate the maximum number of projectiles that could ever exist simultaneously during gameplay, and instantiate an array of objects of the correct size when the game first enters the gameplay **scene** every time one is fired. Instead, you can calculate the maximum number of projectiles that could ever exist simultaneously during gameplay, and instantiate an array of objects of the correct size when the game first enters the gameplay **scene**. To do this:

  * Start with all the projectile **GameObjects** set to being inactive.
  * When a projectile is fired, search through the array to find the first inactive projectile in the array, move it to the required position and set the GameObject to be active.
  * When the projectile is destroyed, set the GameObject to inactive again.

You can use the ObjectPool class, which provides an implementation of this reusable object pool technique. 

The code below shows a simple implementation of a stack-based object pool. You might find it useful to refer to if you’re using an older version of Unity which doesn’t contain the ObjectPool API, or if you’d like to see an example of how a custom object pool might be implemented.
    
    
    using System.Collections.Generic;
    using UnityEngine;
    
    public class ExampleObjectPool : MonoBehaviour {
    
       public GameObject PrefabToPool;
       public int MaxPoolSize = 10;
      
       private Stack<GameObject> inactiveObjects = new Stack<GameObject>();
      
       void Start() {
           if (PrefabToPool != null) {
               for (int i = 0; i < MaxPoolSize; ++i) {
                   var newObj = Instantiate(PrefabToPool);
                   newObj.SetActive(false);
                   inactiveObjects.Push(newObj);
               }
           }
       }
    
       public GameObject GetObjectFromPool() {
           while (inactiveObjects.Count > 0) {
               var obj = inactiveObjects.Pop();
              
               if (obj != null) {
                   obj.SetActive(true);
                   return obj;
               }
               else {
                   Debug.LogWarning("Found a null object in the pool. Has some code outside the pool destroyed it?");
               }
           }
          
           Debug.LogError("All pooled objects are already in use or have been destroyed");
           return null;
       }
      
       public void ReturnObjectToPool(GameObject objectToDeactivate) {
           if (objectToDeactivate != null) {
               objectToDeactivate.SetActive(false);
               inactiveObjects.Push(objectToDeactivate);
           }
       }
    }
    

## Repeated string concatenation

Strings in C# are **immutable** reference types. A reference type means that Unity allocates them on the managed heap and are subject to garbage collection. Immutable means that once a string has been created, it can’t be changed; any attempt to modify the string results in an entirely new string. For this reason, you should avoid creating temporary strings wherever possible.

Consider the following example code, which combines an array of strings into a single string. Every time a new string is added inside the loop, the previous contents of the result variable become redundant, and the code allocates a whole new string.
    
    
    // Bad C# script example: repeated string concatenations create lots of
    // temporary strings.
    using UnityEngine;
    
    public class ExampleScript : MonoBehaviour {
        string ConcatExample(string[] stringArray) {
            string result = "";
    
            for (int i = 0; i < stringArray.Length; i++) {
                result += stringArray[i];
            }
    
            return result;
        }
    
    }
    

If the input stringArray contains `{ “A”, “B”, “C”, “D”, “E” }`, this method generates storage on the heap for the following strings:

  * `“A”`
  * `“AB”`
  * `“ABC”`
  * `“ABCD”`
  * `“ABCDE”`

In this example, you only need the final string, and the others are redundant allocations. The more items that there are in the input array, the more strings this method generates, each longer than the last. 

If you need to concatenate a lot of strings together then you should use Mono library’s `System.Text.StringBuilder` class. An improved version of the script above looks like this:
    
    
    // Good C# script example: StringBuilder avoids creating temporary strings,
    // and only allocates heap memory for the final result string.
    using UnityEngine;
    using System.Text;
    
    public class ExampleScript : MonoBehaviour {
        private StringBuilder _sb = new StringBuilder(16);
    
        string ConcatExample(string[] stringArray) {
            _sb.Clear();
    
            for (int i = 0; i < stringArray.Length; i++) {
                _sb.Append(stringArray[i]);
            }
    
            return _sb.ToString();
        }
    }
    

A repeated concatenation doesn’t decrease performance too much unless it’s called frequently, like on every frame update. The following example allocates new strings each time Update is called, and generates a continuous stream of objects that garbage collector must handle:
    
    
    // Bad C# script example: Converting the score value to a string every frame
    // and concatenating it with “Score: “ generates strings every frame.
    using UnityEngine;
    using UnityEngine.UI;
    
    public class ExampleScript : MonoBehaviour {
        public Text scoreBoard;
        public int score;
        
        void Update() {
            string scoreText = "Score: " + score.ToString();
            scoreBoard.text = scoreText;
        }
    }
    

To prevent this continuous requirement for garbage collection, you can configure the code so that the text only updates when the score changes: 
    
    
    // Better C# script example: the score conversion is only performed when the
    // score has changed
    using UnityEngine;
    using UnityEngine.UI;
    
    public class ExampleScript : MonoBehaviour {
        public Text scoreBoard;
        public string scoreText;
        public int score;
        public int oldScore;
        
        void Update() {
            if (score != oldScore) {
                scoreText = "Score: " + score.ToString();
                scoreBoard.text = scoreText;
                oldScore = score;
            }
        }
    }
    

To improve this further, you can store the score title (the part that says `“Score: ”`) and the score display in two different `UI.Text` objects, which means that there is no need for string concatenation. The code must still convert the score value into a string, but this is an improvement on the previous versions:
    
    
    // Best C# script example: the score conversion is only performed when the
    // score has changed, and the string concatenation has been removed
    using UnityEngine;
    using UnityEngine.UI;
    
    public class ExampleScript : MonoBehaviour {
       public Text scoreBoardTitle;
       public Text scoreBoardDisplay;
       public string scoreText;
       public int score;
       public int oldScore;
    
       void Start() {
           scoreBoardTitle.text = "Score: ";
       }
    
       void Update() {
           if (score != oldScore) {
               scoreText = score.ToString();
               scoreBoardDisplay.text = scoreText;
               oldScore = score;
           }
       }
    }
    

## Method returning an array value

Sometimes it might be convenient to write a method that creates a new array, fills the array with values and then returns it. However, if this method is called repeatedly, then new memory gets allocated each time. 

The following example code shows an example of a method which creates an array every time it’s called:
    
    
    // Bad C# script example: Every time the RandomList method is called it
    // allocates a new array
    using UnityEngine;
    using System.Collections;
    
    public class ExampleScript : MonoBehaviour {
        float[] RandomList(int numElements) {
            var result = new float[numElements];
            
            for (int i = 0; i < numElements; i++) {
                result[i] = Random.value;
            }
            
            return result;
        }
    }
    

One way you can avoid allocating memory every time is to make use of the fact that an array is a reference type. You can modify an array that’s passed into a method as a parameter, and the results remain after the method returns. To do this, you can configure the example code as follows:
    
    
    // Good C# script example: This version of method is passed an array to fill
    // with random values. The array can be cached and re-used to avoid repeated
    // temporary allocations
    using UnityEngine;
    using System.Collections;
    
    public class ExampleScript : MonoBehaviour {
        void RandomList(float[] arrayToFill) {
            for (int i = 0; i < arrayToFill.Length; i++) {
                arrayToFill[i] = Random.value;
            }
        }
    }
    

This code replaces the existing contents of the array with new values. This workflow requires the calling code to do the initial allocation of the array, but the function doesn’t generate any new garbage when it’s called. The array can then be re-used and re-filled with random numbers the next time this method is called without any new allocations on the managed heap.

## Collection and array reuse

When you use arrays or classes from the `System.Collection` namespace (for example, Lists or Dictionaries), it’s efficient to reuse or pool the allocated collection or array. Collection classes expose a Clear method, which eliminates a collection’s values but doesn’t release the memory allocated to the collection.

This is useful if you want to allocate temporary “helper” collections for complex computations. The following code example demonstrates this:
    
    
    // Bad C# script example. This Update method allocates a new List every frame.
    void Update() {
    
        List<float> nearestNeighbors = new List<float>();
    
        findDistancesToNearestNeighbors(nearestNeighbors);
    
        nearestNeighbors.Sort();
    
        // … use the sorted list somehow …
    }
    

This example code allocates the nearestNeighbors List once per frame to collect a set of data points. 

You can hoist this List out of the method and into the containing class, so that your code doesn’t need to allocate a new List each frame:
    
    
    // Good C# script example. This method re-uses the same List every frame.
    List<float> m_NearestNeighbors = new List<float>();
    
    void Update() {
    
        m_NearestNeighbors.Clear();
    
        findDistancesToNearestNeighbors(NearestNeighbors);
    
        m_NearestNeighbors.Sort();
    
        // … use the sorted list somehow …
    }
    

This example code retains and reuses the List’s memory across multiple frames. The code only allocates new memory when the List needs to expand.

## Closures and anonymous methods

In general, you should avoid closures in C# whenever possible. You should minimize the use of anonymous methods and method references in performance-sensitive code, and especially in code that executes on a per-frame basis.

Method references in C# are reference types, so they’re allocated on the heap. This means that if you pass a method reference as an argument, it’s easy to create temporary allocations. This allocation happens regardless of whether the method you pass is an anonymous method or a predefined one.

Also, when you convert an anonymous method to a closure, the amount of memory required to pass the closure to a method increases a lot.

Here’s a code sample in which a list of randomized numbers need to be sorted in a particular order. This uses an anonymous method to control the sorting order of the list, and the sorting doesn’t create any allocations. 
    
    
    // Good C# script example: using an anonymous method to sort a list. 
    // This sorting method doesn’t create garbage
    List<float> listOfNumbers = getListOfRandomNumbers();
    
    
    listOfNumbers.Sort( (x, y) =>
    
    (int)x.CompareTo((int)(y/2)) 
    
    );
    

To make this snippet reusable, you might substitute the constant 2 for a variable in local scope:
    
    
    // Bad C# script example: the anonymous method has become a closure,
    // and now allocates memory to store the value of desiredDivisor
    // every time it is called.
    List<float> listOfNumbers = getListOfRandomNumbers();
    
    
    int desiredDivisor = getDesiredDivisor();
    
    listOfNumbers.Sort( (x, y) =>
    
    (int)x.CompareTo((int)(y/desiredDivisor))
    
    );
    

The anonymous method now needs to access the state of a variable which is outside of its scope, and so the method has become a closure. The `desiredDivisor` variable must be passed into the closure so that the closure’s code can use it.

To ensure that the correct values are passed in to the closure, C# generates an anonymous class that can retain the externally scoped variables that the closure needs. A copy of this class is instantiated when the closure is passed to the Sort method, and the copy is initialized with the value of the desiredDivisor integer.

Executing the closure requires instantiating a copy of its generated class, and all classes are reference types in C#. For this reason, executing the closure requires allocation of an object on the managed heap.

## Boxing

Boxing is one of the most common sources of unintended temporary memory allocations found in Unity projects. It happens when a value-typed variable gets automatically converted to a reference type. This most often happens when passing primitive value-typed variables (such as int and float) to object-typed methods. You should avoid boxing when writing C# code for Unity.

In this example, the integer in x is boxed so that it can be passed to the `object.Equals` method, because the `Equals` method on an object requires that an object is passed to it.
    
    
    int x = 1;
    
    object y = new object();
    
    y.Equals(x);
    

C# IDEs and compilers don’t issue warnings about boxing, even though boxing leads to unintended memory allocations. This is because C# assumes that small temporary allocations are efficiently handled by generational garbage collectors and allocation-size-sensitive memory pools.

While Unity’s allocator does use different memory pools for small and large allocations, Unity’s garbage collector isn’t generational, so it can’t efficiently sweep out the small, frequent temporary allocations that boxing generates.

### Identifying boxing

Boxing appears in CPU traces as calls to one of a few methods, depending on the scripting back end in use. These take one of the following forms, where `<example class>` is the name of a class or struct, and `…` is a number of arguments:
    
    
    <example class>::Box(…)
    Box(…)
    <example class>_Box(…)
    

To find boxing, you can also search the output of a decompiler or IL viewer, such as the IL viewer tool built into ReSharper or the dotPeek decompiler. The IL instruction is `box`.

## Array-valued Unity APIs

A subtle cause of unintended allocation array is the repeated accessing of Unity APIs that return arrays. All Unity APIs that return arrays create a new copy of the array each time they’re accessed. If your code accesses an array-valued Unity API more often than necessary, there is likely to be a detrimental impact on performance.

As an example, the following code unnecessarily creates four copies of the vertices array per loop iteration. The allocations happen each time the `.vertices` property is accessed.
    
    
    // Bad C# script example: this loop create 4 copies of the vertices array per iteration
    void Update() {
        for(int i = 0; i < mesh.vertices.Length; i++) {
            float x, y, z;
    
            x = mesh.vertices[i].x;
            y = mesh.vertices[i].y;
            z = mesh.vertices[i].z;
    
            // ...
    
            DoSomething(x, y, z);   
        }
    }
    
    

You can refactor this code into a single array allocation, regardless of the number of loop iterations. To do this, configure your code to capture the vertices array before the loop:
    
    
    // Better C# script example: create one copy of the vertices array
    // and work with that
    void Update() {
        var vertices = mesh.vertices;
    
        for(int i = 0; i < vertices.Length; i++) {
    
            float x, y, z;
    
            x = vertices[i].x;
            y = vertices[i].y;
            z = vertices[i].z;
    
            // ...
    
            DoSomething(x, y, z);   
        }
    }
    

A better way of doing this is to maintain a List of vertices which is cached and re-used between frames, and then use Mesh.GetVertices to populate it when required.
    
    
    // Best C# script example: create one copy of the vertices array
    // and work with that.
    List<Vector3> m_vertices = new List<Vector3>();
    
    void Update() {
        mesh.GetVertices(m_vertices);
    
        for(int i = 0; i < m_vertices.Length; i++) {
    
            float x, y, z;
    
            x = m_vertices[i].x;
            y = m_vertices[i].y;
            z = m_vertices[i].z;
    
            // ...
    
            DoSomething(x, y, z);   
        }
    }
    

While the CPU performance implications of accessing a property once isn’t high, repeated accesses within tight loops create CPU performance hotspots. Repeated accesses expand the managed heap.

This problem is common on mobile devices, because the Input.touches API behaves similarly to the above. It’s also common for projects to contain code similar to the following, where an allocation occurs each time the `.touches` property is accessed.
    
    
    // Bad C# script example: Input.touches returns an array every time it’s accessed
    for ( int i = 0; i < Input.touches.Length; i++ ) {
       Touch touch = Input.touches[i];
    
        // …
    }
    

To improve this, you can configure your code to hoist the array allocation out of the loop condition:
    
    
    // Better C# script example: Input.touches is only accessed once here
    Touch[] touches = Input.touches;
    
    for ( int i = 0; i < touches.Length; i++ ) {
    
       Touch touch = touches[i];
    
       // …
    }
    

The following code example converts the previous example to the allocation-free Touch API:
    
    
    // BEST C# script example: Input.touchCount and Input.GetTouch don’t allocate at all.
    int touchCount = Input.touchCount;
    
    for ( int i = 0; i < touchCount; i++ ) {
       Touch touch = Input.GetTouch(i);
    
       // …
    }
    

**Note:** The property access (`Input.touchCount`) remains outside the loop condition, to save the CPU impact of invoking the property’s get method.

### Alternative non-allocating APIs

Some Unity APIs have alternative versions that don’t cause memory allocations. You should use these when possible. The following table shows a small selection of common allocating APIs and their non-allocating alternatives. The list isn’t exhaustive, but should indicate the kind of APIs to watch out for.

**Allocating API** | **Non-allocating API alternative**  
---|---  
Physics.RaycastAll | Physics.RaycastNonAlloc  
Animator.parameters |  Animator.parameterCount and Animator.GetParameter  
Renderer.sharedMaterials | Renderer.GetSharedMaterials  
  
## Empty array reuse

Some development teams prefer to return empty arrays instead of null when an array-valued method needs to return an empty set. This coding pattern is common in a lot of managed languages, particularly C# and Java.

In general, when returning a zero-length array from a method, it’s more efficient to return a pre-allocated static instance of the zero-length array than to repeatedly create empty arrays. 

## Further resources

  * Garbage collector overview
  * Managed memory overview
  * Incremental garbage collection