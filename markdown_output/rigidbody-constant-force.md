---
title: "Apply constant force to a Rigidbody"
category: "General"
source_file: "rigidbody-constant-force.html"
doc_type: "manual"
---

# Apply constant force to a Rigidbody

To apply a constant linear or rotational force to a **GameObject** ’s **Rigidbody** ’s **Rigidbody** , add the **Constant Force** , add the **Constant Force** component (represented by the API class `ConstantForce`) to your GameObject. See Constant Force component reference for details on how to configure the properties on the component.

## Set maximum velocity limitations

Constant force is not the same as constant speed. When you apply a constant force, the speed of movement accelerates over time based on the value of the force. In real life, this acceleration continues indefinitely. By default in Unity’s physics simulation, linear acceleration continues indefinitely, and angular acceleration continues until the Rigidbody reaches a max velocity of 50 rad/s. You can change these maximum velocities in code, via the properties `Rigidbody.maxLinearVelocity` and `Rigidbody.maxAngularVelocity`.

## Configure constant forward acceleration

To make a GameObject constantly accelerate forward (for example, to make it behave like a rocket), do the following:

  1. Add a Constant Force component to the GameObject.
  2. On the Constant Force component, set the **Relative Force** Z axis to a positive value.
  3. On the Rigidbody, disable **Use Gravity**. This ensures that there is no competing gravitational force acting upon the GameObject.
  4. On the Rigidbody component, set the **Drag** property so that the Rigidbody does not exceed your preferred maximum velocity (the higher the drag, the lower the maximum velocity will be). This might require some trial and error to get the effect you want.