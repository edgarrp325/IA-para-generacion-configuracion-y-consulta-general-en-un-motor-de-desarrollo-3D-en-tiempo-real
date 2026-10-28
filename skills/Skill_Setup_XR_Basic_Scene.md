SKILL: Skill_Setup_XR_Basic_Scene
DESCRIPCION: Construir la jerarquía base de una escena VR en Unity 2022.3 con XR Interaction Toolkit, incluyendo origen XR, cámara rastreada y controladores izquierdo/derecho.
Palabras clave: XR Origin, XROrigin, XR Interaction Origin, Camera Offset, Main Camera, TrackedPoseDriver, XRRayInteractor, ActionBasedController, Undo.

NAMESPACES: using UnityEngine; using UnityEditor; using Unity.XR.CoreUtils; using UnityEngine.XR.Interaction.Toolkit; using UnityEngine.InputSystem.XR;

APIS_VALIDAS:
- GameObject(string name)
- T Undo.AddComponent<T>(GameObject go) where T : Component
- void Undo.RegisterCreatedObjectUndo(Object objectToUndo, string name)
- void Undo.RecordObject(Object objectToUndo, string name)
- void Transform.SetParent(Transform parent, bool worldPositionStays)
- T Object.FindFirstObjectByType<T>() where T : Object
- Component Undo.AddComponent(GameObject go, System.Type type)

REGLAS_CRITICAS:
- Registrar cada GameObject creado con Undo.RegisterCreatedObjectUndo inmediatamente.
- Reutilizar la Main Camera existente o crear una sola; nunca dejar cámaras duplicadas etiquetadas MainCamera.
- Usar XROrigin en versiones modernas de XR Core Utils; no asumir que XRInteractionOrigin existe en la versión instalada.
- Añadir TrackedPoseDriver solo si está disponible y configurar sus acciones de posición/rotación según el Input System del proyecto.
- Crear controladores hijos bajo Camera Offset o el origen XR y añadir XRRayInteractor y ActionBasedController solo si los paquetes instalados exponen esos tipos.
- No inventar referencias de Input Actions ni asumir que los bindings están configurados.
- PROHIBIDO usar APIs inexistentes como Undo.SetCurrentGroup().

EJEMPLO_CANONICO:
GameObject rig = new GameObject("XR Rig");
Undo.RegisterCreatedObjectUndo(rig, "Crear XR Rig");
Undo.AddComponent<XROrigin>(rig);
GameObject offset = new GameObject("Camera Offset");
Undo.RegisterCreatedObjectUndo(offset, "Crear Camera Offset");
offset.transform.SetParent(rig.transform, false);
GameObject cam = GameObject.FindWithTag("MainCamera");
if (cam == null) {
    cam = new GameObject("Main Camera");
    Undo.RegisterCreatedObjectUndo(cam, "Crear Main Camera");
    cam.tag = "MainCamera";
}
cam.transform.SetParent(offset.transform, false);
GameObject left = new GameObject("Left Controller");
Undo.RegisterCreatedObjectUndo(left, "Crear controlador izquierdo");
left.transform.SetParent(rig.transform, false);
Undo.AddComponent<XRRayInteractor>(left);
