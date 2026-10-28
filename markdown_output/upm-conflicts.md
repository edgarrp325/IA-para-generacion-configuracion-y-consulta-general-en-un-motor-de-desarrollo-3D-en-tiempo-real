---
title: "Resolution and conflict"
category: "General"
source_file: "upm-conflicts.html"
doc_type: "manual"
---

# Resolution and conflict

When you add a package to a **project manifest** , Unity considers that package a dependency of the project (a direct dependency). However, a package can also have dependencies on other packages, which create **indirect dependencies** , Unity considers that package a dependency of the project (a direct dependency). However, a package can also have dependencies on other packages, which create **indirect dependencies** in any projects that require that package. 

Since most projects require more than one package in order to develop games and apps, the Package Manager has to evaluate all the requested package versions to retrieve from the registry (whether direct or indirect), and decide which among those package versions to install. To do this, it computes the set of packages that satisfies all direct and indirect dependencies in the project, starting with the project dependencies and recursively exploring each indirect dependency, collecting all the dependency information, then picking a set of packages that satisfies the dependency requirements without any conflict. For example, this dependency graph represents a project with four **direct dependencies**

A graph of direct and indirect package dependencies for a project

In this example:

  * The light blue nodes represent the project’s direct dependencies.
  * The dark blue nodes show the same package and version as indirect dependencies in this project.
  * The red nodes show two different versions of the same package, which is a conflict.

**Note** : Only package dependencies declared with versions need to be resolved. The Package Manager selects packages installed from other sources, such as embedded packages

## Choosing the best solution

Depending on the set of packages defined in the project manifest, it could take a long time to evaluate all possible package combinations: a project could potentially depend on hundreds of packages, each of which depend on hundreds of other packages, most requiring different versions. 

### Lock files and resolutionStrategy

To provide the most efficient solution, the Package Manager prioritizes package versions that it previously used by tracking them in a lock file. This guarantees that subsequent dependency resolution using the same inputs results in the same outputs. It also minimizes time-consuming operations such as downloading, extracting, or copying packages.

Sometimes, the Package Manager cannot find a solution that only includes locked packages. In this case, the Package Manager uses the solution with the least risky upgrades, preferring patch upgrades over minor or major upgrades, and minor upgrades over major upgrades by default. However, you can customize how aggressive you want the Package Manager to be when considering a higher version with the resolutionStrategy property.

## Example

In this example, there are multiple versions of the following packages requested:

  * `burst@1.2.2` (twice) and `burst@1.3.0-preview.3`
  * `collections@0.5.1-preview.11` and `collections@0.5.2-preview.8`
  * `jobs@0.2.4-preview.11` (twice) and `jobs@0.2.5-preview.20`

Using the set of direct and indirect dependencies, the Package Manager selects the highest version of the burst package (`burst@1.3.0-preview.3`), which satisfies the `collections@0.5.2-preview.8` package’s dependency:

In the dependency graph, the blue nodes indicate which versions the Package Manager selected

  

* * *

  

  * New package dependency solver (SAT) added in Unity 2019.4 NewIn20194