---
title: "Master and Variant Sprite Atlases"
category: "General"
source_file: "MasterVariantAtlases.html"
doc_type: "manual"
---

# Master and Variant Sprite Atlases

The **Type** property defines whether a **Sprite** Atlas is a ‘**Master** ’ or a ‘**Variant** ’. Sprite Atlases are created as Master types by default. Set their Type to ‘Variant’ to create a **Variant Atlas**.

A Variant Atlas requires a Master type **Sprite Atlas** to be set in its **Master Atlas** property. The Variant Atlas receives a copy of the Master Atlas’s contents to use as its own. Refer to documentation on Variant Sprite Atlas for more details about how to create and use Variant Sprite Atlases.

When the Sprite Atlas Type is set to ‘Variant’, the following properties appear:

Property | Description  
---|---  
**Type** | Set the Atlas’s Type to **Variant** to reveal the following properties.  
**Master Atlas** | A Variant Atlas receives a copy of its Master Atlas’ contents to use as its own. Assign a Sprite Atlas to this property to make it the **Master** Atlas of the currently selected **Variant** Atlas. The Master Atlas cannot be a Variant Atlas itself.  
**Include in Build** | Check this box to include the Sprite Atlas in the current build. This option is enabled by default.  
**Scale** | Set the scale factor of the Variant Sprite Atlas that can range from 0.1 to 1. The size of the Variant Atlas Texture is the result of the Master Atlas’ Texture multiplied by the **Scale** value. The default and maximum Scale value is 1, where the Variant Atlas Texture remains identical to its Master Atlas’ Texture.