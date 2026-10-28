---
title: "Scoped registries"
category: "General"
source_file: "upm-scoped.html"
doc_type: "manual"
---

# Scoped registries

Scoped registries allow Unity to communicate the location of any custom package registry server to the Package Manager so that the user has access to several collections of packages at the same time. Here are some important concepts to help you understand this feature:

**Concept:** | **Description:**  
---|---  
**package registry server** | An application that keeps track of packages and provides a place to store them. In Unity’s Package Manager window, all packages registered on Unity’s registry appear in the list view when you select the Unity Registry context.  
**package manager** | An application that tells the user what packages are available, and downloads and installs whatever package the user requests for their project. Unity has implemented its own version of a package manager, but there are several similar applications in other organizations.  
**scope** | Defines a package name or namespace (in reverse domain format), such as `com.example.mycompany.animation` or `com.example`. When a user requests a package, the Package Manager fetches the package from the registry that best matches the scope. For more information, see Managing scoped registries for a project below.  
  
  
The way you interact with scoped registries depends on your role:

  * Package providers set up custom registry servers to host and distribute custom packages in addition to the Unity registry.
  * Package consumers set up scoped registries for each project to access a custom package provider’s registry server.

## Integrity and security of scoped registries

As a package provider, make sure any package registry servers you set up conform to Unity’s Terms of Service and Unity’s Package Guiding Principles & Guidelines. Unity provides access to the Package Manager to facilitate sharing knowledge and creations, but not as a marketplace for third-party products. 

As a package consumer, when you install a scoped registry, use the same level of caution that you use when installing any other third-party software:

  * Install scoped registries only from trusted sources, since the packages in those registries can contain executable code.
  * Beware of third-party registries that may be harmful or capture data without appropriate controls. Also beware of third parties misrepresenting themselves as Unity, or sanctioned or supported by Unity.

## Benefits of scoped registries

Scoped registries can help to:

  * **Provide new functionality by distributing tools, libraries, and other assets**.

As a provider, you can create your own registry to distribute tools and **scripts** (or other types of assets) with version numbers that indicate how mature the package is. Version numbers also indicate whether updates introduce breaking API changes or minor fixes, based on Semantic Versioning. Your code can depend on code in other packages, because the Package Manager supports package dependencies. 

As a consumer, your experience of browsing and installing third-party custom packages in the Package Manager is the same as browsing Unity’s packages.

  * **Extend existing Unity’s package features**.

As a consumer, you can have a seamless experience where the custom package overrides the Unity package without having to manually switch registries or explicitly install a different package version. This is because you can map packages to a specific registry so that Package Manager fetches from either the Unity registry or a custom package registry server.

  * **Access packages in a closed network environment**.

Some organizations work inside a closed network, which makes it difficult to access Unity’s own package registry. In these cases, the organization can set up their own package registry on a server inside their closed network. The network administrators can then periodically synchronize with Unity’s package registry to make sure the scoped registry has the latest set of packages available.

If you are a package consumer, see Managing scoped registries for a project for information about connecting to an existing custom package registry server in your Unity project. If you are a package producer, see Sharing your package for information about supported package registry servers, and to get links to information on how to set them up to use with scoped registries.

**Note:** If you are setting up a scoped registry that points to a package registry server with restricted access, you can configure Package Manager to pass your `npm` authentication token to the server. For more information, see Scoped registry authentication.

## Adding and removing scoped registries

Use the **Package Manager** category of the Project Settings window to add, modify, or remove scoped registries for your project.

## Importing scoped registries

If you are working in a shared project, and another user adds a scoped registry to the project, Unity warns you that another user added a new scoped registry.

Unity warns you if there is a change to the list of scoped registries for your project

When you click the **Close** button, the Package Manager project settings window appears so you can add, modify, or remove scoped registries for your project.

If you click the **Read more** button instead, Unity opens the page you’re currently reading in your default web browser.

**Tip:** To access the Package Manager project settings window at any time, use the main menu in Unity (**Edit > Project Settings**, then the **Package Manager** category) or select **Advanced Project Settings** from the advanced settings menu in the Package Manager window.

## Managing scoped registries for a project

To manage the scoped package registries in your project, you can either edit your project manifest file directly or use the Package Manager project settings window to let Unity modify the manifest for you.

The project manifest uses a scopedRegistries property, which contains an array of scoped registry configuration objects. Each object contains the following properties:

**Property** | **JSON Type** | **Description**  
---|---|---  
**name** | String | The scope name as it appears in the user interface. The Package Manager window displays this name in the package details view.   
  
For example, `"name": "Tools"`.  
**url** | String | The URL to the npm-compatible registry server.   
  
For example, `"url": "https://mycompany.example.com/tools-registry"`  
  
**Note** : Not all registry providers are compatible with Unity’s Package Manager. Make sure the package registry server you are trying to add implements the `/-/v1/search` or `/-/all` endpoints.  
**scopes** | Array of Strings | Array of scopes that you can map to a package name, either as an exact match on the package name, or as a namespace. Wildcards and other glob patterns aren’t supported.  
  
For example, `"scopes": [ "com.example", "com.example.tools.physics" ]`   
  
**Note** : This configuration type assumes that packages follow the Reverse domain name notation. This ensures that `com.unity` is equivalent to any package name that matches the `com.unity` namespace, such as `com.unity.timeline` or `com.unity.2d.animation`.  
  
**Warning:** Unity doesn’t support npm’s scope notation.  
  
When the Package Manager decides which registry to fetch a package from, it compares the package **name** to the **scopes** values and finds the registry whose **scopes** value is the closest match.

For example, in the project manifest below, there are two scoped registries, “General” and “Tools”:
    
    
    {
        "scopedRegistries": [
            {
                "name": "General",
                "url": "https://example.com/registry",
                "scopes": [
                    "com.example", "com.example.tools.physics"
                ]
            },
            {
                "name": "Tools",
                "url": "https://mycompany.example.com/tools-registry",
                "scopes": [
                    "com.example.mycompany.tools"
                ]
            }
        ],
        "dependencies": {
            "com.unity.animation": "1.0.0",
            "com.example.mycompany.tools.animation": "1.0.0",
            "com.example.tools.physics": "1.0.0",
            "com.example.animation": "1.0.0"
        }
    }
    
    

When the Package Manager looks up the `com.example.animation` package, it finds that the `com.example` namespace is the closest match to its name, and fetches that package from the “General” registry.

When the Package Manager looks up the `com.example.tools.physics` package, the “General” registry has a scope that exactly matches the package name.

When the Package Manager looks up the `com.example.mycompany.tools.animation` package, the Package Manager finds that the `com.example.mycompany.tools` namespace is the closest match to its name and fetches that package from the “Tools” registry. Even though it also matches the “General” scope, the `com.example` namespace isn’t as close a match.

When the Package Manager looks up the `com.unity.animation` package, the Package Manager doesn’t find a match in any of the scoped registries, so it fetches the package from the default registry.

## Additional resources

  * Project Settings window (Package Manager)