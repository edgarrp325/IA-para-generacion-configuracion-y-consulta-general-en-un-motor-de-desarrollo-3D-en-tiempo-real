---
title: "Built-in Importers"
category: "General"
source_file: "BuiltInImporters.html"
doc_type: "manual"
---

# Built-in Importers

Unity supports many asset file types via its collection of built-in importers. Most of these importers are implemented in the Unity Editor’s native code, and are named “native importers”. They provide the import functionality for most of Unity’s basic asset types, such as 3D models, Textures, and audio files.

## Built in native importers

Importer | File Formats  
---|---  
AssemblyDefinitionImporter | asmdef  
AssemblyDefinitionReferenceImporter | asmref  
AudioImporter | ogg, aif, aiff, flac, wav, mp3, mod, it, s3m, xm  
ComputeShaderImporter | compute  
DefaultImporter | rsp, unity  
FBXImporter | fbx, mb, ma, max, jas, dae, dxf, obj, c4d, blend, lxo  
IHVImageFormatImporter | astc, dds, ktx, pvr  
LocalizationImporter | po  
Mesh3DSImporter | 3ds  
NativeFormatImporter | anim, animset, asset, blendtree, buildreport, colors, controller, **cubemap** , curves, curvesNormalized, flare, fontsettings, giparams, gradients, guiskin, ht, mask, mat, **mesh** , curves, curvesNormalized, flare, fontsettings, giparams, gradients, guiskin, ht, mask, mat, **mesh** , mixer, overrideController, particleCurves, particleCurvesSigned, particleDoubleCurves, particleDoubleCurvesSigned, physicMaterial, physicsMaterial2D, playable, preset, renderTexture, shadervariants, spriteatlas, state, statemachine, texture2D, transition, webCamTexture, brush, terrainlayer, signal  
PackageManifestImporter | json  
PluginImporter | dll, winmd, so, jar, java, kt, aar, suprx, prx, rpl, cpp, cc, c, h, jslib, jspre, bc, a, m, mm, swift, xib, bundle, dylib, config  
PrefabImporter | **prefab**  
RayTracingShaderImporter | raytrace  
ShaderImporter | cginc, cg, glslinc, hlsl, **shader**  
SketchUpImporter | skp  
SpeedTreeImporter | spm, st  
SubstanceImporter | .sbsar  
TextScriptImporter | txt, html, htm, xml, json, csv, yaml, bytes, fnt, manifest, md, js, boo, rsp  
TextureImporter | jpg, jpeg, tif, tiff, tga, gif, png, psd, bmp, iff, pict, pic, pct, exr, **hdr**  
TrueTypeFontImporter | ttf, dfont, otf, ttc  
VideoClipImporter | avi, asf, wmv, mov, dv, mp4, m4v, mpg, mpeg, ogv, vp8, webm  
VisualEffectImporter | vfx, vfxoperator, vfxblock  
  
## Built-in scripted importers

Scripted importers allow you to write your own custom importers for formats that Unity does not natively support. However, in addition to the built-in native importers listed above, some of Unity’s own built-in importers are themselves implemented as scripted importers. This is because they are implemented in C# in core packages, rather than within the Editor’s native code itself. Unity imports scripted importer assets after native importer assets.

Importer | File Formats  
---|---  
StyleSheetImporter | .uss  
UIElementsViewImporter | .uxml