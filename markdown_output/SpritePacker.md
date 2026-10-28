---
title: "Sprite Packer"
category: "General"
source_file: "SpritePacker.html"
doc_type: "manual"
---

# Sprite Packer

When designing **Sprite** graphics, it is convenient to work with a separate Texture file for each character. However, a significant portion of a Sprite Texture will often be taken up by the empty space between the graphic elements and this space will result in wasted video memory at runtime. For optimal performance, it is best to pack graphics from several Sprite textures tightly together within a single Texture known as an atlas. Unity provides a ****Sprite Packer**** utility to automate the process of generating atlases from the individual Sprite textures.

Unity handles the generation and use of Sprite atlas textures behind the **scenes** so that the user needs to do no manual assignment. The atlas can optionally be packed on entering Play mode or during a build and the graphics for a Sprite object will be obtained from the atlas once it is generated.

Users are required to specify a Packing Tag in the Texture Importer to enable packing for Sprites of that Texture.

**Warning:** Please note that **Sprite Packer** is deprecated for Unity 2020.1 and newer, and will no longer be available as an option from Sprite Packer Modes from Unity 2020.1 onwards. Any new Project created in 2020.1 onwards will default to the Sprite Atlas

## Using the Sprite Packer

The Sprite Packer is disabled by default but you can configure it from the Editor window (menu: **Edit** > **Project Settings** , then select the **Editor** category). The Sprite packing mode can be changed from **Disabled** to **Enabled for Builds** (packing is used for builds but not Play mode) or **Always Enabled** (packing is enabled for both Play mode and builds).

If you open the Sprite Packer window (menu: **Window** > **2D** > **Sprite Packer**) and click the **Pack** button in the top-left corner, you will see the arrangement of the textures packed within the atlas.

If you select a Sprite in the Project panel, this will also be highlighted to show its position in the atlas. The outline is actually the render **mesh** outline and it also defines the area used for tight packing.

The **toolbar** at the top of the Sprite Packer window has a number of controls that affect packing and viewing. The **Pack** buttons initiates the packing operation but will not force any update if the atlas hasn’t changed since it was last packed. (A related **Repack** button will appear when you implement a custom packing policy as explained in **Customizing the Sprite Packer** below). The **View Atlas** and **Page #** menus allow you to choose which page of which atlas is shown in the window (a single atlas may be split into more than one “page” if there is not enough space for all Sprites in the maximum Texture size). The menu next to the page number selects which “packing policy” is used for the atlas (see below). At the right of the toolbar are two controls to zoom the view and to switch between color and alpha display for the atlas.

## Packing policy

The Sprite Packer uses a **packing policy** to decide how to assign Sprites into atlases. It is possible to create your own packing policies (see below) but the **Default Packer Policy** , **Tight Packer Policy** and **Tight Rotate Enabled Sprite Packer Policy** options are always available. With these policies, the **Packing Tag** property in the Texture Importer directly selects the name of the atlas where the Sprite will be packed and so all Sprites with the same packing tag will be packed in the same atlas. Atlases are then further sorted by the Texture import settings so that they match whatever the user sets for the source textures. Sprites with the same Texture **compression** settings will be grouped into the same atlas where possible.

  * DefaultPackerPolicy will use rectangle packing by default unless “[TIGHT]” is specified in the **Packing Tag** (i.e. setting your packing tag to “[TIGHT]Character” will allow tight packing).
  * TightPackerPolicy will use tight packing by default if Sprite have tight meshes. If “[RECT]” is specified in the **Packing Tag** , rectangle packing will be done (i.e. setting your packing tag to “[RECT]UI_Elements” will force rect packing).
  * TightRotateEnabledSpritePackerPolicy will use tight packing by default if Sprite have tight meshes and will enable rotation of Sprites. If “[RECT]” is specified in the **Packing Tag** , rectangle packing will be done (i.e. setting your packing tag to “[RECT]UI_Elements” will force rect packing).

## Customizing the Sprite Packer

The **DefaultPackerPolicy** option is sufficient for most purposes but you can also implement your own custom packing policy if you need to. To do this, you need to implement the UnityEditor.Sprites.IPackerPolicy interface for a class in an editor script. This interface requires the following methods:

  * GetVersion - return the version value of your packer policy. Version should be bumped if modifications are done to the policy script and this policy is saved to **version control**.
  * OnGroupAtlases - implement your packing logic here. Define atlases on the PackerJob and assign Sprites from the given TextureImporters.

DefaultPackerPolicy uses rect packing (see SpritePackingMode) by default. This is useful if you’re doing texture-space effects or would like to use a different mesh for rendering the Sprite. Custom policies can override this and instead use tight packing.

  * Repack button is only enabled when a custom policy is selected. 
    * OnGroupAtlases will not be called unless TextureImporter metadata or the selected PackerPolicy version values change.
    * Use Repack button when working on your custom policy.
  * Sprites can be packed rotated with TightRotateEnabledSpritePackerPolicy automatically. 
    * SpritePackingRotation is a reserved type for future Unity versions.

## Other

  * Atlases are cached in Project\Library\AtlasCache. 
    * Deleting this folder and then launching Unity will force atlases to be repacked. Unity must be closed when doing so.
  * Atlas cache is not loaded at start. 
    * All textures must be checked when packing for the first time after Unity is restarted. This operation might take some time depending on the total number of textures in the project.
    * Only the required atlases are loaded.
  * Default maximum atlas size is 2048x2048.
  * When PackingTag is set, Texture will not be compressed so that the SpritePacker can grab original **pixel** values and then do compression on the atlas.

## DefaultPackerPolicy
    
    
    using System;
    using System.Linq;
    using UnityEngine;
    using UnityEditor;
    using System.Collections.Generic;
    
    
    public class DefaultPackerPolicySample : UnityEditor.Sprites.IPackerPolicy
    {
            protected class Entry
            {
                public Sprite            Sprite;
            public UnityEditor.Sprites.AtlasSettings settings;
                public string            atlasName;
                public SpritePackingMode packingMode;
                public int               anisoLevel;
            }
    
            private const uint kDefaultPaddingPower = 3; // Good for base and two mip levels.
    
            public virtual int GetVersion() { return 1; }
            protected virtual string TagPrefix { get { return "[TIGHT]"; } }
            protected virtual bool AllowTightWhenTagged { get { return true; } }
            protected virtual bool AllowRotationFlipping { get { return false; } }
    
        public static bool IsCompressedFormat(TextureFormat fmt)
        {
            if (fmt >= TextureFormat.DXT1 && fmt <= TextureFormat.DXT5)
                return true;
            if (fmt >= TextureFormat.DXT1Crunched && fmt <= TextureFormat.DXT5Crunched)
                return true;
            if (fmt >= TextureFormat.PVRTC_RGB2 && fmt <= TextureFormat.PVRTC_RGBA4)
                return true;
            if (fmt == TextureFormat.ETC_RGB4)
                return true;
            if (fmt >= TextureFormat.ATC_RGB4 && fmt <= TextureFormat.ATC_RGBA8)
                return true;
            if (fmt >= TextureFormat.EAC_R && fmt <= TextureFormat.EAC_RG_SIGNED)
                return true;
            if (fmt >= TextureFormat.ETC2_RGB && fmt <= TextureFormat.ETC2_RGBA8)
                return true;
            if (fmt >= TextureFormat.ASTC_RGB_4x4 && fmt <= TextureFormat.ASTC_RGBA_12x12)
                return true;
            if (fmt >= TextureFormat.DXT1Crunched && fmt <= TextureFormat.DXT5Crunched)
                return true;
            return false;
        }
    
        public void OnGroupAtlases(BuildTarget target, UnityEditor.Sprites.PackerJob job, int[] textureImporterInstanceIDs)
            {
                List<Entry> entries = new List<Entry>();
    
                foreach (int instanceID in textureImporterInstanceIDs)
                {
                    TextureImporter ti = EditorUtility.InstanceIDToObject(instanceID) as TextureImporter;
    
                    TextureFormat desiredFormat;
                    ColorSpace colorSpace;
                    int compressionQuality;
                    ti.ReadTextureImportInstructions(target, out desiredFormat, out colorSpace, out compressionQuality);
    
                    TextureImporterSettings tis = new TextureImporterSettings();
                    ti.ReadTextureSettings(tis);
    
                Sprite[] Sprites =
                    AssetDatabase.LoadAllAssetRepresentationsAtPath(ti.assetPath)
                        .Select(x => x as Sprite)
                        .Where(x => x != null)
                        .ToArray();
                    foreach (Sprite Sprite in Sprites)
                    {
                        Entry entry = new Entry();
                        entry.Sprite = Sprite;
                        entry.settings.format = desiredFormat;
                        entry.settings.colorSpace = colorSpace;
                        // Use Compression Quality for Grouping later only for Compressed Formats. Otherwise leave it Empty.
                    entry.settings.compressionQuality = IsCompressedFormat(desiredFormat) ? compressionQuality : 0;
                    entry.settings.filterMode = Enum.IsDefined(typeof(FilterMode), ti.filterMode)
                        ? ti.filterMode
                        : FilterMode.Bilinear;
                        entry.settings.maxWidth = 2048;
                        entry.settings.maxHeight = 2048;
                        entry.settings.generateMipMaps = ti.mipmapEnabled;
                        entry.settings.enableRotation = AllowRotationFlipping;
                        if (ti.mipmapEnabled)
                            entry.settings.paddingPower = kDefaultPaddingPower;
                        else
                            entry.settings.paddingPower = (uint)EditorSettings.SpritePackerPaddingPower;
                        #if ENABLE_ANDROID_ATLAS_ETC1_COMPRESSION
                            entry.settings.allowsAlphaSplitting = ti.GetAllowsAlphaSplitting ();
                        #endif //ENABLE_ANDROID_ATLAS_ETC1_COMPRESSION
    
                        entry.atlasName = ParseAtlasName(ti.SpritePackingTag);
                        entry.packingMode = GetPackingMode(ti.SpritePackingTag, tis.SpriteMeshType);
                        entry.anisoLevel = ti.anisoLevel;
    
                        entries.Add(entry);
                    }
    
                    Resources.UnloadAsset(ti);
                }
    
                // First split Sprites into groups based on atlas name
                var atlasGroups =
                    from e in entries
                    group e by e.atlasName;
                foreach (var atlasGroup in atlasGroups)
                {
                    int page = 0;
                    // Then split those groups into smaller groups based on texture settings
                    var settingsGroups =
                        from t in atlasGroup
                        group t by t.settings;
                    foreach (var settingsGroup in settingsGroups)
                    {
                        string atlasName = atlasGroup.Key;
                        if (settingsGroups.Count() > 1)
                            atlasName += string.Format(" (Group {0})", page);
    
                    UnityEditor.Sprites.AtlasSettings settings = settingsGroup.Key;
                        settings.anisoLevel = 1;
                        // Use the highest aniso level from all entries in this atlas
                        if (settings.generateMipMaps)
                            foreach (Entry entry in settingsGroup)
                                if (entry.anisoLevel > settings.anisoLevel)
                                    settings.anisoLevel = entry.anisoLevel;
    
                        job.AddAtlas(atlasName, settings);
                        foreach (Entry entry in settingsGroup)
                        {
                            job.AssignToAtlas(atlasName, entry.Sprite, entry.packingMode, SpritePackingRotation.None);
                        }
    
                        ++page;
                    }
                }
            }
    
            protected bool IsTagPrefixed(string packingTag)
            {
                packingTag = packingTag.Trim();
                if (packingTag.Length < TagPrefix.Length)
                    return false;
                return (packingTag.Substring(0, TagPrefix.Length) == TagPrefix);
            }
    
            private string ParseAtlasName(string packingTag)
            {
                string name = packingTag.Trim();
                if (IsTagPrefixed(name))
                    name = name.Substring(TagPrefix.Length).Trim();
                return (name.Length == 0) ? "(unnamed)" : name;
            }
    
            private SpritePackingMode GetPackingMode(string packingTag, SpriteMeshType meshType)
            {
                if (meshType == SpriteMeshType.Tight)
                    if (IsTagPrefixed(packingTag) == AllowTightWhenTagged)
                        return SpritePackingMode.Tight;
                return SpritePackingMode.Rectangle;
            }
    }
    

## TightPackerPolicy
    
    
    using System;
    using System.Linq;
    using UnityEngine;
    using UnityEditor;
    using UnityEditor.Sprites;
    using System.Collections.Generic;
    
    // TightPackerPolicy will tightly pack non-rectangle Sprites unless their packing tag contains "[RECT]".
    class TightPackerPolicySample : DefaultPackerPolicySample
    {
            protected override string TagPrefix { get { return "[RECT]"; } }
            protected override bool AllowTightWhenTagged { get { return false; } }
            protected override bool AllowRotationFlipping { get { return false; } }
    }
    

## TightRotateEnabledSpritePackerPolicy
    
    
    using System;
    using System.Linq;
    using UnityEngine;
    using UnityEditor;
    using UnityEditor.Sprites;
    using System.Collections.Generic;
    
    // TightPackerPolicy will tightly pack non-rectangle Sprites unless their packing tag contains "[RECT]".
    class TightRotateEnabledSpritePackerPolicySample : DefaultPackerPolicySample
    {
            protected override string TagPrefix { get { return "[RECT]"; } }
            protected override bool AllowTightWhenTagged { get { return false; } }
            protected override bool AllowRotationFlipping { get { return true; } }
    }
    

## Additional Resources

  * Prepare Sprite Packer Legacy packed assets to work after deprecation