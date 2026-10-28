---
title: "2D joints"
category: "General"
source_file: "Joints2D.html"
doc_type: "manual"
---

# 2D joints

2D joints are the 2D counterparts of the 3D **joint** physics components, and are made to work only with 2D GameObjects. You can only attach 2D joints to GameObjects which have an attached **Rigidbody** physics components, and are made to work only with 2D GameObjects. You can only attach 2D joints to GameObjects which have an attached **Rigidbody** 2D component, or to a fixed position in world space. A 2D joint connects a Rigidbody 2D **GameObject** 2D component, or to a fixed position in world space. A 2D joint connects a Rigidbody 2D **GameObject** to another Rigidbody 2D GameObject. 2D joints can apply forces that move Rigidbody GameObjects, and joint limits can restrict that movement.

You can tell a 2D joint from its 3D counterpart in the Component browser by its name ending in ‘2D’.

There are many different types of 2D joints available. Refer to each joint’s respective page for detailed information about their properties and uses.

**Topic** | **Description**  
---|---  
**Constraints of 2D joints** | Understand the constraints of using 2D joints.  
**Distance Joint 2D** | Attach two GameObjects controlled by Rigidbody physics together while keeping them a set distance apart.  
**Fixed Joint 2D** | Keep two objects in a certain position relative to each other, so that the objects are always offset at a set position and angle. This is useful for objects that need to react as if they’re rigidly connected. You can also use this joint to create a less rigid connection with some flexibility.  
**Friction Joint 2D** | Reduce both the linear and angular velocities between two GameObjects controlled by Rigidbody physics to zero (i.e. it slows them down and stops them). For example, use this joint to create a rotating platform that still resists the rotation.  
**Hinge Joint 2D** | Allow a GameObject controlled by Rigidbody physics to be attached to a point in space around which it can rotate. For example, use this joint as the pivot on a pair of scissors.  
**Relative Joint 2D** | Allow two GameObjects controlled by Rigidbody physics to maintain a position based on each other’s location. Use this joint to keep two objects at a certain offset from each other. For example, use this joint to attach two additional guns to a spaceship which follows its position.  
**Slider Joint 2D** | Allow a GameObject controlled by Rigidbody physics to slide along a line in space. For example, use this joint to create a sliding door object.  
**Spring Joint 2D** | Allow two GameObjects controlled by Rigidbody physics to react as if they were attached together by a spring.  
**Target Joint 2D** | connects to a specified target, rather than another Rigidbody object, as other joints do. It’s a spring type joint, which you could use for picking up and moving an object acting under gravity, for example.  
**Wheel Joint 2D** | simulates the behavior of a rolling wheel, with a suspension ‘spring’ maintaining its distance from the main body of the ‘vehicle’.  
  
## Additional resources

  * 3D joints
  * API documentation on Joint2D