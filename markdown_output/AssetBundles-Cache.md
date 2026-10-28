---
title: "AssetBundle compression"
category: "General"
source_file: "AssetBundles-Cache.html"
doc_type: "manual"
---

# AssetBundle compression

Use this page to learn about the AssetBundle **compression** formats and cache types that Unity supports.

## AssetBundle compression formats

By default, Unity creates AssetBundles with LZMA compression, and caches them with LZ4 compression. This section describes both compression formats.

Unity’s AssetBundle build pipeline creates AssetBundles with LZMA compression. This compression format is a stream of data representing the entire AssetBundle, which means that if you need to read an Asset from these archives, you must decompress the entire stream. This is the preferred format for AssetBundles downloaded from a Content Delivery Network (CDN), because the file sizes are smaller than those with LZ4 compression.

LZ4 compression is a chunk-based compression algorithm. If Unity needs to access an Asset from an LZ4 archive, it only needs to decompress and read the chunks that contain bytes of the requested Asset. This is the compression method that Unity uses in both of its AssetBundle caches. Use the BuildAssetBundleOptions.ChunkBasedCompression value when building AssetBundles to force LZ4(HC) compression.

Uncompressed AssetBundles that Unity builds when you use BuildAssetBundleOptions.UncompressedAssetBundle require no decompression, but occupy more disk space. Uncompressed AssetBundles are 16-byte aligned.

## AssetBundle cache

To optimize the fetching, recompressing, and versioning of LZMA AssetBundles using WWW or UnityWebRequest (UWR), Unity maintains two caches:

  * **The Memory Cache** stores AssetBundles in UncompressedRuntime format in RAM.

  * **The Disk Cache** stores fetched AssetBundles on writable media in the compression format described later.

AssetBundles loaded into the Memory Cache consume a large amount of memory. Unless you specifically want to frequently and rapidly access the contents of an AssetBundle, the Memory Cache is likely not worth the Memory cost. Instead, you should use the Disk Cache.

If you provide a version parameter to the UWR API, Unity stores your AssetBundle data in the Disk Cache. If you don’t provide a version parameter, Unity uses the Memory Cache. The version parameter can be either a version number or a hash. If Caching.compressionEnabled is set to true, Unity applies LZ4 compression when it writes AssetBundles to disk for all subsequent downloads. It doesn’t compress existing uncompressed data in the cache. If Caching.compressionEnabled is false, Unity applies no compression when it writes AssetBundles to disk.

It takes longer to initially load cached LZMA AssetBundles, because Unity must recompress the archive to the destination format. Subsequent loads use the cached version.

AssetBundle.LoadFromFile or AssetBundle.LoadFromFileAsync always use the Memory Cache for LZMA AssetBundles, so you should use the UWR API. If it’s not possible to use the UWR API, you can use AssetBundle.RecompressAssetBundleAsync to rewrite an LZMA AssetBundle on disk.

**Note:** **WebGL** doesn’t support LZMA compression for AssetBundles. Use LZ4 compression with AssetBundles on WebGL platforms. For more information, refer to AssetBundles in WebGL.

Internal testing shows significant difference in RAM usage between using the Disk Cache instead of the Memory Cache. You must weigh the trade-off between memory impact versus added disk space requirements and Asset instantiation time for your application.