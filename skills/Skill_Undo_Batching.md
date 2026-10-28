SKILL: Skill_Undo_Batching
DESCRIPCION: Agrupar múltiples operaciones del Unity Editor en una sola entrada del historial de deshacer para que Ctrl+Z revierta toda la acción como una unidad.
Palabras clave: Undo batching, Undo group, Ctrl+Z, IncrementCurrentGroup, SetCurrentGroupName, CollapseUndoOperations.

NAMESPACES: using UnityEngine; using UnityEditor;

APIS_VALIDAS:
- int Undo.GetCurrentGroup()
- void Undo.IncrementCurrentGroup()
- void Undo.SetCurrentGroupName(string name)
- void Undo.CollapseUndoOperations(int groupIndex)
- void Undo.RecordObject(Object objectToUndo, string name)
- void Undo.RegisterCreatedObjectUndo(Object objectToUndo, string name)

REGLAS_CRITICAS:
- PROHIBIDO usar Undo.SetCurrentGroup(): es una API inexistente.
- Capturar el índice del grupo con Undo.GetCurrentGroup() antes de registrar operaciones.
- Usar Undo.IncrementCurrentGroup() para iniciar un nuevo grupo cuando corresponda.
- Asignar un nombre descriptivo mediante Undo.SetCurrentGroupName().
- Colapsar las operaciones con Undo.CollapseUndoOperations(groupIndex) al finalizar.
- Registrar cada modificación o creación con la API Undo correspondiente.
- Usar try/finally si se necesita garantizar el colapso ante excepciones.

EJEMPLO_CANONICO:
Undo.IncrementCurrentGroup();
int groupIndex = Undo.GetCurrentGroup();
Undo.SetCurrentGroupName("Crear y posicionar objetos");
try
{
    GameObject a = new GameObject("A");
    Undo.RegisterCreatedObjectUndo(a, "Crear A");
    Undo.RecordObject(a.transform, "Posicionar A");
    a.transform.position = Vector3.one;
}
finally
{
    Undo.CollapseUndoOperations(groupIndex);
}