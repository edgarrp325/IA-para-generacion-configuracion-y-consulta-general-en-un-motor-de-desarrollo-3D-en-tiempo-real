SKILL: Skill_Manage_Asset
DESCRIPCION: Cargar prefabs o modelos desde el proyecto e instanciarlos en la escena conservando su vínculo original de prefab.
Palabras clave: AssetDatabase, LoadAssetAtPath, PrefabUtility, InstantiatePrefab, Undo, instanciar prefab.

NAMESPACES: using UnityEngine; using UnityEditor; using UnityEngine.SceneManagement;

APIS_VALIDAS:
- T AssetDatabase.LoadAssetAtPath<T>(string assetPath)
- Object PrefabUtility.InstantiatePrefab(Object asset, Scene destinationScene)
- void Undo.RegisterCreatedObjectUndo(Object objectToUndo, string name)

REGLAS_CRITICAS:
- Prohibido usar Object.Instantiate para crear instancias que deban conservar el vínculo de prefab.
- Validar que el asset cargado no sea null antes de instanciar.
- Registrar obligatoriamente Undo.RegisterCreatedObjectUndo inmediatamente después de crear la instancia.
- No usar APIs inexistentes como Undo.SetCurrentGroup.
- Usar PrefabUtility.InstantiatePrefab para mantener la conexión con el prefab original.

EJEMPLO_CANONICO:
GameObject prefab = AssetDatabase.LoadAssetAtPath<GameObject>("Assets/Prefabs/MiObjeto.prefab");
if (prefab != null)
{
    GameObject instance = PrefabUtility.InstantiatePrefab(prefab, UnityEngine.SceneManagement.SceneManager.GetActiveScene()) as GameObject;
    if (instance != null)
    {
        Undo.RegisterCreatedObjectUndo(instance, "Instanciar Prefab");
        instance.transform.position = Vector3.zero;
    }
}