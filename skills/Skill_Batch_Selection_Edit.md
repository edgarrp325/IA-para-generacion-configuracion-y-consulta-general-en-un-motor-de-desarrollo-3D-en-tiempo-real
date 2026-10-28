SKILL: Skill_Batch_Selection_Edit
DESCRIPCION: Aplicar modificaciones simultáneas a múltiples GameObjects seleccionados en Unity Editor, incluyendo renombrado masivo, desplazamientos acumulativos y alineación por ejes.
Palabras clave: Selection.gameObjects, edición por lotes, Undo.RecordObjects, renombrar objetos, prefijos, sufijos, offset, alineación, Transform.position.

NAMESPACES: using UnityEngine; using UnityEditor;

APIS_VALIDAS:
- GameObject[] Selection.gameObjects
- void Undo.RecordObjects(Object[] objectsToUndo, string name)
- void EditorSceneManager.MarkSceneDirty(Scene scene)
- void EditorUtility.SetDirty(Object target)

REGLAS_CRITICAS:
- Obtener los objetivos mediante Selection.gameObjects y filtrar referencias nulas.
- Usar Undo.RecordObjects para registrar todos los objetos afectados en una sola llamada cuando sea apropiado.
- Registrar los objetos antes de modificar nombres o propiedades.
- Para cambios de posición, incluir los Transform en el arreglo de Undo.RecordObjects.
- No usar Undo.RecordObject dentro del bucle si todos los objetivos pueden registrarse previamente en lote.
- Marcar las escenas afectadas como modificadas cuando corresponda.
- No usar Undo.SetCurrentGroup(): esta API no existe.

EJEMPLO_CANONICO:
GameObject[] selected = Selection.gameObjects;
if (selected.Length == 0) return;
Undo.RecordObjects(selected, "Renombrar objetos");
for (int i = 0; i < selected.Length; i++)
{
    GameObject go = selected[i];
    if (go == null) continue;
    go.name = "Objeto_" + (i + 1);
    EditorSceneManager.MarkSceneDirty(go.scene);
}
