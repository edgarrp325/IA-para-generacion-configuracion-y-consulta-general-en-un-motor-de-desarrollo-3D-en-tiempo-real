---
title: "Package states and lifecycle"
category: "General"
source_file: "upm-lifecycle.html"
doc_type: "manual"
---

# Package states and lifecycle

Starting from Unity Editor version 2021.1, a package may travel through the following states during its lifecycle:

Package lifecycle with Unity Package Manager  
---  
**Birth** **(A)** | While the package developer creates the package, it is in the “Custom” state.   
  
When it is ready for Unity users to test it and provide feedback, a package enters the “Experimental” state. Unity does not support experimental packages and does not guarantee that experimental packages will be fully released and verified to be safe to use in production until they enter the release track.   
  
Experimental packages either use `0` as the major portion of their version or the `-exp.#` suffix on the patch portion of their version. For example, `mypackage@0.1.2` or `mypackage@1.2.3-exp.1`.  
  
**Release track** | As soon as a package passes quality testing and doesn’t contain any experimental features or functionality (including having dependencies on experimental packages), it enters the “Pre-release” state, which is on the release track. That means that Unity fully supports it and commits to officially releasing them by the end of the current LTS cycle (for example, 2021.3) at the latest. For a list of pre-release packages available for this version, see Pre-release packages.  
  
Unity’s release management only grants a package the “Released” status after it passes several testing stages and validation procedures, which also include checks for appropriate documentation, changelog, and license files. Packages in this state appear in the Unity Editor with the  label and never use non-numeric suffixes as part of their version. For a list of released packages available for this version, see Released packages.   
  
If the package developer updates or changes a released package, that package might return to another state depending on the severity:  
|  | **Type of change:** | **New state:** | **Version bump:**  
| **(B)** | Major API change that breaks an API | Experimental |  `1.2.3` => `2.0.0-exp`  
| **(C)** | Minor API change that does not break the API but affects usage | Pre-release |  `1.2.3` => `1.3.0-pre`  
| **(D)** | Bug fixes, trivial changes, and documentation updates typical of patch updates | Released (same state) |  `1.2.3` => `1.2.4`  
**Death** **(E)** | Packages that reach their end of life are no longer supported in Editors where they’re marked “Deprecated”. Packages in that state shouldn’t be used as they might be nonfunctional or unsafe to use.  
  
Specific package versions can also be individually marked as deprecated across all Editors. Unity usually applies this designation when they discover a critical issue in a specific version of a package that hasn’t yet reached its end of life. Custom package authors can also apply this designation based on their own deprecation flow.  
  
Some experimental packages go directly to the deprecated state without passing through the release cycle track.  
  
The Package Manager window displays a label that corresponds to some of these states.

**Note** : These package states only apply to packages that Unity develops internally. Contact third-party package developers to ask about their specific processes. 

  

* * *

  

  * Some advanced or support packages are no longer discoverable in the Package Manager window 2020.1 NewIn20201
  * New package lifecycle (V2) for the Package Manager 2021.1 NewIn20211