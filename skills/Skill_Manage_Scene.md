SKILL: Skill_Manage_Scene
DESCRIPCION: Gestionar objetos y componentes de la escena desde Unity Editor, consultar selecciones del usuario y localizar componentes mediante APIs modernas de Unity 2022.3.
Palabras clave: Selection.gameObjects, Selection.activeGameObject, FindObjectsByType, FindObjectsSortMode.None, MarkSceneDirty, escena modificada, búsqueda de componentes.

NAMESPACES: using UnityEngine; using UnityEditor; using UnityEditor.SceneManagement;

APIS_VALIDAS:
- GameObject[] Selection.gameObjects
- GameObject Selection.activeGameObject
- T[] Object.FindObjectsByType<T>(FindObjectsSortMode sortMode) where T : Object
- void EditorSceneManager.MarkSceneDirty(Scene scene)
- Scene GameObject.scene { get; }

REGLAS_CRITICAS:
- Prohibido usar Object.FindObjectsOfType: está obsoleto en Unity 2022.3.
- Usar Object.FindObjectsByType<T>(FindObjectsSortMode.None) cuando no se requiera ordenamiento.
- Validar referencias nulas antes de acceder a objetos seleccionados.
- Marcar la escena afectada con EditorSceneManager.MarkSceneDirty(obj.scene) después de cambios que deban persistir.
- No marcar escenas como modificadas si no hubo cambios efectivos.
- Para modificaciones reversibles, registrar Undo.RecordObject antes de alterar objetos o componentes.

EJEMPLO_CANONICO:
GameObject[] selected = Selection.gameObjects;
GameObject active = Selection.activeGameObject;
foreach (GameObject go in selected)
{
    if (go == null) continue;
    Undo.RecordObject(go.transform, "Mover objeto");
    go.transform.position += Vector3.up;
    EditorSceneManager.MarkSceneDirty(go.scene);
}
MeshRenderer[] renderers =
    Object.FindObjectsByType<MeshRenderer>(
        FindObjectsSortMode.None);
Debug.Log($"Activo: {active?.name}, renderers: {renderers.Length}");