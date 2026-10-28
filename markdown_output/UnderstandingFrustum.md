---
title: "Understanding the View Frustum"
category: "General"
source_file: "UnderstandingFrustum.html"
doc_type: "manual"
---

# Understanding the View Frustum

The word **frustum** refers to a solid shape that looks like a pyramid with the top cut off parallel to the base. This is the shape of the region that can be seen and rendered by a perspective **camera**. The following thought experiment should help to explain why this is the case.

Imagine holding a straight rod (a broom handle or a pencil, for example) end-on to a camera and then taking a picture. If the rod were held in the centre of the picture, perpendicular to the camera lens, then only its end would be visible as a circle on the picture; all other parts of it would be obscured. If you moved it upward, the lower side would start to become visible but you could hide it again by angling the rod upward. If you continued moving the rod up and angling it further upward, the circular end would eventually reach the top edge of the picture. At this point, any object above the line traced by the rod in world space would not be visible on the picture.

The rod could just as easily be moved and rotated left, right, or down or any combination of horizontal and vertical. The angle of the “hidden” rod simply depends on its distance from the centre of the screen in both axes.

The meaning of this thought experiment is that any point in a camera’s image actually corresponds to a line in world space and only a single point along that line is visible in the image. Everything behind that position on the line is obscured.

The outer edges of the image are defined by the diverging lines that correspond to the corners of the image. If those lines were traced backwards towards the camera, they would all eventually converge at a single point. In Unity, this point is located exactly at the camera’s transform position and is known as the centre of perspective. The angle subtended by the lines converging from the top and bottom centres of the screen at the centre of perspective is called the field of view (often abbreviated to FOV).

As stated above, anything that falls outside the diverging lines at the edges of the image will not be visible to the camera, but there are also two other restrictions on what it will render. The near and far clipping planes are parallel to the camera’s XY plane and each set at a certain distance along its centre line. Anything closer to the camera than the near **clipping plane** and anything farther away than the **far clipping plane** will not be rendered.

The diverging corner lines of the image along with the two clipping planes define a truncated pyramid - the view frustum.

## The far clipping plane and floating point math

Objects, lights, and shadows might flicker if they’re far away. The flickering occurs because distances are too large to calculate positions precisely with floating point math. In each frame, the object, light, or shadow is at a slightly different position, so it moves in and out of the view frustum.

Minimise flickering using one of the following approaches:

  * Reduce the far clipping plane distance in the Camera component to avoid the distance of objects becoming too large for precise calculations.
  * Make everything in your **scene** smaller, to reduce distances across your whole scene.

Unity calculates lights and shadows with the world space position as the reference point, for example `0, 0, 0` in a 3D scene. Flickering occurs when lights and shadows are far away from the world space position. To minimise flickering, you can enable camera-relative culling, so Unity uses the camera position as the relative position for shadow calculations. See Culling settings in Graphics settings.

## Reduce tearing

Simulated example of tearing. The shift in the picture is visible in the magnified portion.

Updates in Unity aren’t synchronized with updates of the display device, so Unity might send a new frame while the display device is still rendering the previous frame. This results in a visible ‘tear’ at the position the frame changes.

To reduce tearing, go to **Edit** > **Project Settings** > **Quality** , then set **VSync Count** to one of the following:

  * **Every V Blank** to send frames only during the periods when the display device isn’t updating, which is called its vertical blank.
  * **Every Second V Blanks** to send frames during every other vertical blank. Use this value if your project takes longer than one update of the display device to render a frame.

## Additional resources

  * Quality settings