---
title: "AssetBundle Download Integrity and Security"
category: "General"
source_file: "AssetBundles-Integrity.html"
doc_type: "manual"
---

# AssetBundle Download Integrity and Security

AssetBundles can be distributed with your game build, but can also be downloaded from remote servers. When downloading AssetBundles, you should take precaution to prevent AssetBundle data corruption as well as attacks by malicious actors. Even though AssetBundles cannot contain executable code, changing serialized data could allow an attacker to exploit a vulnerability in the game code or the Unity runtime.

## Download With a Secure Protocol

UnityWebRequestAssetBundle can be used to download and cache AssetBundles from the internet. When using this API you should use the HTTPS protocol in your URL, unless your URL refers to a local web server that runs on the same machine. The HTTP protocol is not secure and is vulnerable to a malicious man in the middle attack.

## CRC Checksums

A 32-bit checksum is generated during the AssetBundle build process. When you provide this CRC through the AssetBundle loading APIs, the loading system calculates the checksum of the AssetBundle before loading it. If the CRC of the AssetBundle does not match the provided CRC, the AssetBundle will not load. Checking the CRC ensures the AssetBundle data was not corrupted or tampered with after it was built.

## User Generated Content

If you allow users to upload content that is distributed to other players (User Generated Content), it is your responsibility to filter this data for inappropriate or malicious content. We do not recommend that you let users build and upload binary AssetBundle files. It is preferable to have your users upload their source assets and let you, the developer, build the AssetBundle binary file for them. This will make it easier for you to filter out malicious or inappropriate content through manual and automated processes. It also enables you to rebuild the AssetBundles as needed if you upgrade to a later Unity version.