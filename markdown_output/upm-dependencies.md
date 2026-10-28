---
title: "Dependency and resolution"
category: "General"
source_file: "upm-dependencies.html"
doc_type: "manual"
---

# Dependency and resolution

When you work in the Package Manager window, you can install packages from several sources (a registry, a local folder or tarball, and a Git URL). However, while the Package Manager installs packages from these sources seamlessly, it first has to make a series of calculations to decide which version to install, and which other packages and versions to install to support it.

****Direct dependencies****

When you select a package version to install through the Package Manager window, you are adding a “dependency” to your project manifest. This is a declaration that you need a specific version of a particular package in order for the project to work. To add a dependency to your project, you add a reference to the package and version in the form `package-name@package-version` to the dependencies property of the `<project-root>/Packages/manifest.json` file. These are called “direct” dependencies because your project directly depends on them.

****Indirect dependencies****

Packages can also require other packages in order to work. These are called “indirect” (or transitive) dependencies. The package developer adds these to the dependencies property of the package manifest file during development (`<package-root>/package.json`). For example, in the diagram below, the `alembic@1.0.7` package has a dependency on the `timeline@1.0.0` package, so the timeline package is an “indirect” dependency. On the other hand, the project has dependencies on the `cinemachine@2.6.0` and `alembic@1.0.7` packages, so those are both “direct” dependencies.

**Version overrides**

When you add a package version as a dependency, that version is not necessarily the version that the Package Manager installs, because it has to consider all of the dependencies in your project, whether direct or indirect. For example, in this case, the **XR** Plugin Management package requested was version 4.0.3, but the installed version is actually version 4.0.6 because another package depended on the higher version, as indicated in the information message **(B)** :

When you click the information button in the details pane (A), a text box appears (B) explaining why this version was installed instead of the one you requested

**Dependency graph**

The Package Manager can only install one package version at a time, so it has to construct a dependency graph, which is a list of every direct and indirect dependency for the project. The dependency graph determines which version of each package to install.

**Lock file**

When the Package Manager successfully resolves all version conflicts, it saves the resolution in a lock file to ensure determinism (so that the same packages are reliably installed every time), and to reduce the amount of time and resources it takes to compute the dependency graph again.