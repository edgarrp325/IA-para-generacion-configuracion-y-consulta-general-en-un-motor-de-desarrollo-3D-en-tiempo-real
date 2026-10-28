---
title: "Custom fall-off"
category: "General"
source_file: "ProgressiveLightmapper-CustomFallOff.html"
doc_type: "manual"
---

# Custom fall-off

In the real world, light fades over distance, and dim lights have a lower range than bright lights. The term “fall-off” refers to the rate at which light fades. Alongside Unity’s default fall-off lighting behaviour, you can also use custom fall-off settings.

Progressive **Lightmapper** provides custom fall-off presets, which you can implement via script. See the image below the table for a visual representation of how these work, and the code sample below the image for an example of how to use this functionality.

**Property** | **Function**  
---|---  
`InverseSquared` | Apply an inverse-squared distance fall-off model. This means the light intensity decreases inversely proportional to the square of location’s distance to the light source. For more information , see Wikipedia: Inverse-square law. This option is the most physically accurate.  
`InverseSquaredNoRangeAttenuation` | Apply an inverse-squared distance fall-off model with no smooth range attenuation. This works in the same way as `InverseSquared`, but the lighting system does not take into account the attenuation for the range parameter of punctual lights (that is, point lights and spot lights).  
`Legacy` | Apply a quadratic fall-off model. This model bases the light attenuation on the range of the light source. The intensity diminishes as the light gets further away from the source, but there is a very sharp and unnatural drop in the attenuation, and the visual effect is not realistic.  
`Linear` | Apply a linear fall-off model. In this model, attenuation is inversely proportional to the distance from the light, and the fall-off diminishes at a fixed rate from its source.  
An example of the visual effect of each custom fall-off preset

**Note** : The code example below only works with the Progressive Lightmapper when you use Baked or Mixed lights. To use the code example with **realtime lights** , use Enlighten Realtime Global Illumination. 
    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Experimental.GlobalIllumination;
    using UnityEngine.SceneManagement;
    [ExecuteInEditMode]
    public class ExtractFalloff : MonoBehaviour
    {
        public void OnEnable()
        {
            Lightmapping.RequestLightsDelegate testDel = (Light[] requests, Unity.Collections.NativeArray<LightDataGI> lightsOutput) =>
            {
                DirectionalLight dLight = new DirectionalLight();
                PointLight point = new PointLight();
                SpotLight spot = new SpotLight();
                RectangleLight rect = new RectangleLight();
                DiscLight disc = new DiscLight();
                Cookie cookie = new Cookie();
                LightDataGI ld = new LightDataGI();
                
                for (int i = 0; i < requests.Length; i++)
                {
                    Light l = requests[i];
                    switch (l.type)
                    {
                        case UnityEngine.LightType.Directional: LightmapperUtils.Extract(l, ref dLight); LightmapperUtils.Extract(l, out cookie); ld.Init(ref dLight, ref cookie); break;
                        case UnityEngine.LightType.Point: LightmapperUtils.Extract(l, ref point); LightmapperUtils.Extract(l, out cookie); ld.Init(ref point, ref cookie); break;
                        case UnityEngine.LightType.Spot: LightmapperUtils.Extract(l, ref spot); LightmapperUtils.Extract(l, out cookie); ld.Init(ref spot, ref cookie); break;
                        case UnityEngine.LightType.Area: LightmapperUtils.Extract(l, ref rect); LightmapperUtils.Extract(l, out cookie); ld.Init(ref rect, ref cookie); break;
                        case UnityEngine.LightType.Disc: LightmapperUtils.Extract(l, ref disc); LightmapperUtils.Extract(l, out cookie); ld.Init(ref disc, ref cookie); break;
                        default: ld.InitNoBake(l.GetInstanceID()); break;
                    }
    
                    if (l.cookie != null)
                    {
                        ld.cookieID = l.cookie.GetInstanceID();
                    }
                    else
                    {
                        ld.cookieID = 0;
                    }
                    
                    ld.falloff = FalloffType.InverseSquared;
                    lightsOutput[i] = ld;
                }
            };
            Lightmapping.SetDelegate(testDel);
        }
        void OnDisable()
        {
            Lightmapping.ResetDelegate();
        }
    }
    

**Note** : All code in the example above is necessary for the custom falloff to work; however, you can change `InverseSquared` in the line `ld.falloff = FalloffType.InverseSquared;` to use any of the presets described above.

* * *

Progressive Lightmapper added in 2018.1 NewIn20181

2018–03–28 Page published