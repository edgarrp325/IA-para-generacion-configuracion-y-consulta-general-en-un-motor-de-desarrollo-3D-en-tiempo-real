SKILL: Skill_Manage_GameObject
DESCRIPCION: Crear, configurar y eliminar GameObjects en escenas de Unity mediante scripts de Editor, incluyendo primitivas (Cube, Sphere, Capsule, Cylinder, Plane, Quad), objetos vacíos, nombres y posiciones.
Palabras clave: crear GameObject, GameObject.CreatePrimitive, objeto vacío, posicionar objeto, renombrar, eliminar con Undo, gestión de escena.
NAMESPACES: using UnityEngine; using UnityEditor;

APIS_VALIDAS:
- GameObject.CreatePrimitive(PrimitiveType type)
- new GameObject(string name)
- Undo.RegisterCreatedObjectUndo(Object objectToUndo, string name)
- Undo.DestroyObjectImmediate(Object objectToUndo)
- Undo.RecordObject(Object objectToUndo, string name)
- EditorUtility.SetDirty(Object target)

REGLAS_CRITICAS:
- Toda creación debe registrarse con Undo.RegisterCreatedObjectUndo.
- Toda eliminación reversible debe usar Undo.DestroyObjectImmediate, nunca Object.DestroyImmediate directamente.
- No añadir MeshFilter ni MeshRenderer manualmente después de GameObject.CreatePrimitive.
- Registrar cambios de propiedades existentes con Undo.RecordObject antes de modificarlas.
- No usar Undo.SetCurrentGroup: esta API no existe.
- Evitar suscripciones permanentes a eventos del Editor sin retirar los callbacks en OnDisable.

EJEMPLO_CANONICO:
// Crear una primitiva y registrar Undo.
GameObject go = GameObject.CreatePrimitive(PrimitiveType.Cube);
Undo.RegisterCreatedObjectUndo(go, "Crear cubo");
go.name = "Cubo";
go.transform.position = Vector3.zero;

// Crear un objeto vacío.
GameObject empty = new GameObject("ObjetoVacio");
Undo.RegisterCreatedObjectUndo(empty, "Crear objeto vacío");
empty.transform.position = new Vector3(2, 0, 0);

// Eliminar de forma reversible.
Undo.DestroyObjectImmediate(go);