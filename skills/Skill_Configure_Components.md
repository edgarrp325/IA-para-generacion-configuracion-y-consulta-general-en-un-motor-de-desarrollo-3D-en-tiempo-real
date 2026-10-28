SKILL: Skill_Configure_Components
DESCRIPCION: Añadir y configurar componentes en GameObjects existentes desde Unity Editor, incluyendo colliders, rigidbodies y luces, con soporte completo para deshacer mediante Undo.
Palabras clave: AddComponent, Undo.AddComponent, BoxCollider, Rigidbody, Light, color, intensity, mass, configuración de componentes.

NAMESPACES: using UnityEngine; using UnityEditor;

APIS_VALIDAS:
- T Undo.AddComponent<T>(GameObject go) where T : Component
- Component Undo.AddComponent(GameObject go, Type type)
- void Undo.RecordObject(Object objectToUndo, string name)
- void Undo.RegisterCreatedObjectUndo(Object objectToUndo, string name)

REGLAS_CRITICAS:
- Preferir Undo.AddComponent<T>(gameObject) para añadir componentes reversibles.
- No usar GameObject.AddComponent directamente cuando se requiera deshacer la operación.
- Registrar Undo.RecordObject(component, "Configurar componente") antes de modificar propiedades de componentes existentes.
- Validar que el GameObject objetivo no sea null.
- No registrar con Undo.RegisterCreatedObjectUndo un componente añadido mediante Undo.AddComponent: la operación ya queda registrada.
- No usar Undo.SetCurrentGroup(): esta API no existe.

EJEMPLO_CANONICO:
GameObject go = Selection.activeGameObject;
if (go == null) return;
BoxCollider box = Undo.AddComponent<BoxCollider>(go);
Rigidbody rb = Undo.AddComponent<Rigidbody>(go);
Undo.RecordObject(rb, "Configurar Rigidbody");
rb.mass = 2f;
Light light = Undo.AddComponent<Light>(go);
Undo.RecordObject(light, "Configurar luz");
light.color = Color.white;
light.intensity = 3f;