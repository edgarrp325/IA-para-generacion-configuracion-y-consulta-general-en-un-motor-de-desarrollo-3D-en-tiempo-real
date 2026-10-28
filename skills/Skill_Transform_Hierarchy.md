SKILL: Skill_Transform_Hierarchy
DESCRIPCION: Gestionar jerarquías de GameObjects en Unity Editor mediante creación de objetos padre, asignación de parent e iteración de hijos para organizar estructuras de escena y prefabs.
Palabras clave: Transform.SetParent, worldPositionStays, jerarquía, objetos padre, childCount, GetChild, localPosition, localRotation, localScale, Undo.RecordObject.

NAMESPACES: using UnityEngine; using UnityEditor;

APIS_VALIDAS:
- void Transform.SetParent(Transform parent, bool worldPositionStays)
- Transform GetChild(int index)
- int childCount { get; }
- void Undo.RecordObject(Object objectToUndo, string name)
- GameObject(string name)
- void Undo.RegisterCreatedObjectUndo(Object objectToUndo, string name)

REGLAS_CRITICAS:
- Registrar Undo.RecordObject(transform, "Descripción") antes de modificar localPosition, localRotation o localScale.
- Usar SetParent(parent, false) cuando se requiera conservar los valores locales relativos al nuevo padre.
- Registrar objetos padre nuevos con Undo.RegisterCreatedObjectUndo.
- No modificar jerarquías mediante asignaciones directas de matrices para sustituir SetParent.
- Iterar hijos por índice desde 0 hasta childCount - 1; evitar cambios estructurales durante la iteración que alteren los índices.
- No usar Undo.SetCurrentGroup: esta API no existe.

EJEMPLO_CANONICO:
GameObject parent = new GameObject("Organizador");
Undo.RegisterCreatedObjectUndo(parent, "Crear organizador");
Transform child = Selection.activeTransform;
if (child != null && child != parent.transform)
{
    Undo.RecordObject(child, "Reorganizar objeto");
    child.SetParent(parent.transform, false);
    Undo.RecordObject(child, "Ajustar posición local");
    child.localPosition = Vector3.zero;
    Undo.RecordObject(child, "Ajustar escala local");
    child.localScale = Vector3.one;
}