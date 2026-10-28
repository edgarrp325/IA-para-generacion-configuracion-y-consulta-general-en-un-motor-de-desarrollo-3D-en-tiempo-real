SKILL: Skill_Manage_Material
DESCRIPCION: Crear y configurar materiales desde Unity Editor usando shaders básicos, modificar colores y asignarlos a objetos de la escena mediante Renderer.
Palabras clave: Material, Shader.Find, Standard shader, color, sharedMaterial, Renderer, Undo.RecordObject, AssetDatabase.

NAMESPACES: using UnityEngine; using UnityEditor;

APIS_VALIDAS:
- Shader Shader.Find(string name)
- Material Material(Shader shader)
- void Undo.RegisterCreatedObjectUndo(Object objectToUndo, string name)
- void Undo.RecordObject(Object objectToUndo, string name)
- Material Renderer.sharedMaterial { get; set; }
- void EditorUtility.SetDirty(Object target)

REGLAS_CRITICAS:
- PROHIBIDO usar renderer.material en Editor: instancia materiales implícitamente y puede causar memory leaks.
- Usar obligatoriamente renderer.sharedMaterial para consultar o asignar materiales.
- Ejecutar Undo.RecordObject(renderer, "Asignar material") antes de cambiar sharedMaterial.
- Registrar materiales nuevos con Undo.RegisterCreatedObjectUndo.
- Verificar que Shader.Find("Standard") no devuelva null.
- No modificar sharedMaterial existente si se pretende aislar cambios; crear un material nuevo.
- Para persistencia entre sesiones, guardar el material como asset mediante AssetDatabase.

EJEMPLO_CANONICO:
Shader shader = Shader.Find("Standard");
if (shader == null) return;
Material mat = new Material(shader);
Undo.RegisterCreatedObjectUndo(mat, "Crear material");
mat.color = Color.red;
Renderer renderer = Selection.activeGameObject
    ?.GetComponent<Renderer>();
if (renderer == null) return;
Undo.RecordObject(renderer, "Asignar material");
renderer.sharedMaterial = mat;
EditorUtility.SetDirty(renderer);