---
title: "Frame Debugger event information"
category: "General"
source_file: "frame-debugger-window-event-information.html"
doc_type: "manual"
---

# Frame Debugger event information

The Event Information Panel in the Frame Debugger window displays information about the event such as geometry details and the **shader**

The event information panel **Label** | **Description**  
---|---  
|  **Render target selector** : When rendering into multiple render targets (such as multiple RenderTextures or when also rendering to depth), this specifies which render target to display in the Game view. This is useful for example to view individual render targets in a G-buffer.  
|  **Color channel selector** : Specifies which color channels of the render target to display.  
|  **Levels** : Controls the black and white intensity. Use this to isolate areas of the Game view based on light intensity.  
|  **Output /**Mesh** Preview**: Displays a preview of the selected event output as well as the mesh geometry in the event. For more information, see Preview.  
|  **Event properties** : Contains further information about the selected event. For more information, see Event properties.  
  
## Preview

The preview section consists of two tabs:

  * The **Output** tab displays a preview of the selected event output.
  * The **Mesh Preview** tab displays the mesh geometry Unity rendered in the event.

The mesh preview tab displaying the power jigsaw mesh from the URP sample scene. **Label** | **Description**  
---|---  
|  **Preview** : A preview of the mesh geometry Unity rendered during the event.  
|  **Mesh name** : The name of the mesh asset in the preview. Click on the mesh name to take see the mesh asset in the **Project window**. If the geometry was procedural and there is no mesh asset associated, this is empty (Unity displays **-**).  
|  **Preview mode** : Specifies how the preview renders the mesh. The options are:  
• **Shaded** : Renders the mesh using its material and a basic light.  
• **UV Checker** : Applies a checkerboard texture to the mesh to visualize how the mesh’s UV map applies textures..  
• **UV Layout** : Displays how the vertices of the mesh are organized in the unwrapped UV map. This view disables the Wireframe toggle.  
• **Vertex Color** : Visualizes any vertex colors that the vertices in this mesh have. If no vertices have a vertex color, this option is unavailable.  
• **Normals** : Visualizes the relative directions of the normals in the mesh with color.  
• **Tangents** : Visualizes the tangent data in the mesh with color.  
• **Blendshapes** : Visualizes blend shape deformations on the mesh. If the mesh has no blend shapes, this option is unavailable.  
|  **Wireframe toggle** : Toggles the mesh wireframe on and off. When enabled, the preview displays the mesh vertices and edges.  
  
## Event properties

The event properties section contains properties and values for the selected event. It has a **Details** fold-out section that contains information about the event itself and then a fold-out section for each type of shader property. If the fold-out section is grayed-out, it means that the shader in the event didn’t contain any properties of that type. For more information on the information that each section displays, see:

  * Details
  * Keywords
  * Textures
  * Ints
  * Floats
  * Vectors
  * Matrices
  * Buffers
  * Constant Buffers

**Note** : When using OpenGL and GLSL shaders, this panel displays all shader properties as being part of the vertex stage.

### Details

The **Details** section displays information about the rendering event, such as the number of draw calls as well as the meshes that Unity rendered and the shader it used to render them.

The Details section of the Event Information Panel **Property** | **Description**  
---|---  
**RenderTarget** | The name of the render target  
**Size** | The size of the render target.  
**Format** | The TextureFormat for the render target.  
**Color Actions** | Shows which actions to perform on the color target when:  
• The GPU first loads the color target. For more information, see RenderBufferLoadAction.  
• The GPU finishes rendering to the color target. For more information, see RenderBufferStoreAction.  
**Depth Actions** | Shows which actions to perform on the depth target when:  
• The GPU first loads the depth target. For more information, see RenderBufferLoadAction.  
• The GPU finishes rendering to the depth target. For more information, see RenderBufferStoreAction.  
**Memoryless** | The **render texture** memoryless mode mode. For more information, see memoryless.  
**ColorMask** | The color channel mask used for the render target. For more information, see ColorMask.  
**Blend Color** | The color blending method Unity used during the selected event.  
**Blend Alpha** | The alpha blending method Unity used during the selected event.  
**BlendOp Color** | The color blending operation Blend Color used.  
**BlendOp Alpha** | The alpha blending operation Blend Alpha used.  
**Draw Calls** | The number of draw calls Unity processed during the selected event.  
**Vertices** | The number of vertices Unity processed during the select event.  
**Indices** | The number of indices Unity processed during the select event.  
**Clear Color** | The color Unity used to clear the render target during the selected event. If Unity didn’t clear the render target, the display doesn’t show a color here.  
**Clear Depth** | The color Unity used to clear the **depth buffer** during the selected event. If Unity didn’t clear the depth buffer, the display doesn’t show a color here.  
**Clear Stencil** | The color Unity used to clear the **stencil buffer** during the selected event. If Unity didn’t clear the stencil buffer, the display doesn’t show a color here.  
**Batch cause** | The reason why the SRP Batcher was unable to batch the selected rendering event with the previous rendering event.   
This is only relevant if your application uses the SRP Batcher.  
**Meshes** | The list of meshes that Unity rendered during the selected event.  
**Pass** | The shader Pass Unity used.  
**LightMode** | The LightMode pass tag Unity used during the selected event.  
**Used Shader** | The shader asset Unity used during the selected event. This can sometimes be different than the original shader, for example when the original shader uses a fallback shader or USEPASS.  
**Original Shader** | The original shader Unity used with the pass.  
**ZClip** | The shader’s depth clip mode.  
**ZTest** | The shader’s depth test mode.  
**ZWrite** | The shader’s depth clip mode.  
**Cull** | The shader’s cull mode.  
**Conservative** | Indicates whether the shader used conservative rasterization.  
**Offset** | The depth bias on the GPU that Unity used during the selected event.  
**Stencil** | Indicates whether Stencil is enabled in the selected event. For more information, see Stencil.  
**Stencil Ref** | The stencil reference value.  
**Stencil ReadMask** | The stencil readmask value Unity used to perform the stencil test.  
**Stencil WriteMask** | The stencil writemask value Unity used to write to the stencil buffer.  
**Stencil Comp** | The operation that the GPU performed for the stencil test for all **pixels**.  
**Stencil Pass** | The operation that the GPU performed on the stencil buffer for pixels that passed both the stencil test and the depth test.  
**Stencil Fail** | The operation that the GPU performed on the stencil buffer for pixels that failed the stencil test.  
**Stencil ZFail** | The operation that the GPU performed on the stencil buffer for pixels that passed the stencil test but failed the depth test.  
  
### Keywords

This section displays information about the enabled shader keywords Unity used in the rendering event.

The Keywords section of the Event Information Panel **Property** | **Description**  
---|---  
**Name** | The name of the shader keyword.  
**Stage** | The shader stage that Unity used the shader keyword in. The possible values are:  
• **vs** : Vertex Shader  
• **fs** : Fragment Shader  
• **gs** : Geometry Shader  
• **hs** : Hull Shader  
• **ds** : Domain Shader  
**Scope** | Indicates whether the scope of the keyword is global or local. For more information, see Declaring keywords.  
**Dynamic** | Indicates whether the keyword is dynamic or not. For more information, see Declaring and using shader keywords in HLSL.  
  
### Textures

The **Texture** section displays information about the named textures Unity used during the rendering event.

The Textures section of the Event Information Panel **Property** | **Description**  
---|---  
**Name** | The property name for the texture.  
**Stage** | The shader stage that Unity used the texture in. The possible values are:  
• **vs** : Vertex Shader  
• **fs** : Fragment Shader  
• **gs** : Geometry Shader  
• **hs** : Hull Shader  
• **ds** : Domain Shader  
**Size** | The size of the texture. This is the width and height for 2D textures and width, height, and depth for 3D textures,  
**Sampler Type** | Indicates type of a Texture (such as 2D Texture, cubemap, or 3D volume texture).  
**Color Format** | The color format that the texture uses. For more information on RenderTexture formats, see GraphicsFormat. For more information on formats for other texture types, see TextureFormat.  
**Depth Stencil Format** | The depth stencil format for the RenderTexture. For more information, see RenderTexture.depthStencilFormat.   
**Note** : If the texture isn’t a RenderTexture, Unity doesn’t display a graphics format here.  
**Texture** | The texture name.  
  
### Ints

The **Ints** section displays information about the named int values Unity used during the rendering event.

The Ints section of the Event Information Panel **Property** | **Description**  
---|---  
**Name** | The name of the int property in the shader.  
**Stage** | The shader stage that Unity used the int property in. The possible values are:  
• **vs** : Vertex Shader  
• **fs** : Fragment Shader  
• **gs** : Geometry Shader  
• **hs** : Hull Shader  
• **ds** : Domain Shader  
**Value** | The value of the int property.  
  
### Floats

The **Floats** section displays information about the named float values Unity used during the rendering event.

The Floats section of the Event Information Panel **Property** | **Description**  
---|---  
**Name** | The name of the float property in the shader.  
**Stage** | The shader stage that Unity used the float property in. The possible values are:  
• **vs** : Vertex Shader  
• **fs** : Fragment Shader  
• **gs** : Geometry Shader  
• **hs** : Hull Shader  
• **ds** : Domain Shader  
**Value** | The value of the float property.  
  
### Vectors

The Vectors section of the Event Information Panel **Property** | **Description**  
---|---  
**Name** | The name of the vector property in the shader.  
**Stage** | The shader stage that Unity used the vector property in. The possible values are:  
• **vs** : Vertex Shader  
• **fs** : Fragment Shader  
• **gs** : Geometry Shader  
• **hs** : Hull Shader  
• **ds** : Domain Shader  
**Value(R)** | The R component of the vector.  
**Value(G)** | The G component of the vector.  
**Value(B)** | The B component of the vector.  
**Value(A)** | The A component of the vector.  
  
### Matrices

The **Matrices** section displays information about the named matrix values Unity used during the rendering event.

The Matrices section of the Event Information Panel **Property** | **Description**  
---|---  
**Name** | The name of the matrix property in the shader.  
**Stage** | The shader stage that Unity used the matrix property in. The possible values are:  
• **vs** : Vertex Shader  
• **fs** : Fragment Shader  
• **gs** : Geometry Shader  
• **hs** : Hull Shader  
• **ds** : Domain Shader  
**Column 0** | The values in the first column of the matrix.  
**Column 1** | The values in the second column of the matrix.  
**Column 2** | The values in the third column of the matrix.  
**Column 3** | The values in the fourth column of the matrix.  
  
### Buffers

The **Buffers** section displays information about the named  buffers Unity used during the rendering event.

The Buffers section of the Event Information Panel **Property** | **Description**  
---|---  
**Name** | The name of the buffer in the shader.  
**Stage** | The shader stage that Unity used the buffer in. The possible values are:  
• **vs** : Vertex Shader  
• **fs** : Fragment Shader  
• **gs** : Geometry Shader  
• **hs** : Hull Shader  
• **ds** : Domain Shader  
  
### Constant Buffers

This **Constant Buffers** section displays information about the named constant buffers Unity used during the rendering event.

The Constant Buffers section of the Event Information Panel **Property** | **Description**  
---|---  
**Name** | The name of the constant buffer in the shader.  
**Stage** | The shader stage that Unity used the constant buffer in. The possible values are:  
• **vs** : Vertex Shader  
• **fs** : Fragment Shader  
• **gs** : Geometry Shader  
• **hs** : Hull Shader  
• **ds** : Domain Shader  
  
## Share event information

To help you share information for a particular event, the Frame Debugger window can copy the information in the user interface to the clipboard. It can copy information for a single property, for all the properties in a properties section, or for an entire event. This means you don’t need to take one or multiple screenshots to share the results of a frame capture. 

To copy a single property and its values to the clipboard, right-click the property and select **Copy Property**.

The Copy Property option.

To copy all the properties and their values from a properties section, right-click the properties section header and select **Copy** **All <property type> Properties**.

To copy all the information from the rendering event, right-click the event header and select **Copy** **Event Info**.