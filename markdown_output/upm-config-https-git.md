---
title: "Using private repositories with HTTPS Git URLs"
category: "General"
source_file: "upm-config-https-git.html"
doc_type: "manual"
---

# Using private repositories with HTTPS Git URLs

When you use Git in a terminal to access a private repository over HTTPS, Git prompts you to enter a username and password. Then, Git submits these credentials to the server and proceeds with the command if the server accepts those credentials and allows access to the repository.

When the Unity Package Manager fetches packages using Git URLs, there’s no terminal for users to enter credentials. As a result, when the server requests credentials from Git, Git doesn’t issue a prompt. Instead, it reports an error to the Unity Package Manager. To solve this problem, you must configure Git with a Git credential helper, and that helper must already have the required credentials loaded for that repository. If the credentials are valid, Git can successfully run the commands issued by the Unity Package Manager.

**Note** : A Git credential helper has no effect when using Git URLs with the SSH protocol, including the SCP-like syntax. For information about accessing a private Git repository over SSH, refer to Using passphrase-protected SSH keys with SSH Git URLs.

## Git Credential Manager

Although Git supports several credential helpers to store credentials, the Git Credential Manager (GCM) is the recommended credential helper. GCM is flexible, easy to install, and is actively supported. It’s built on .NET, which means it can run on Windows, macOS, and Linux distributions that support .NET.

By default, GCM uses Windows Credential Manager (on Windows) and macOS Keychain (on macOS) as the configured credential store. GCM doesn’t have a default store configured for Linux. Refer to the GCM credential stores documentation for more information on the different credential store configurations supported by GCM.

## Prerequisites

Before you can fetch packages from private Git repositories using HTTPS URLs, make sure you install GCM.

The Git for Windows installer includes a step to install and configure GCM automatically. You can also install GCM separately if you:

  * Used a different method to install Git on Windows.
  * Use macOS or Linux.

Refer to the GCM install instructions for more information about installing GCM.

## Procedure

Follow these steps to access packages in private repositories that use HTTPS Git URLs:

  1. Configure Git to use GCM by running the following command in a terminal:
         
         git config --global credential.helper manager
         

  2. Access the repository one time by using a terminal. For example, run the following command:
         
         git ls-remote --heads https://<url-to-repository> HEAD
         

  3. When Git prompts you, enter your credentials. If your user account has access to the remote Git server and the server accepts your credentials, then the Git credential helper will securely store your credentials.

  4. Use the Unity Package Manager. It will use your stored credentials, when necessary, to fetch packages from HTTPS-based repositories that you have permissions to access.

## Additional resources

  * Troubleshooting Git issues
  * Using passphrase-protected SSH keys with SSH Git URLs