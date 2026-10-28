SKILL: Skill_Create_Runtime_Script_Asset
DESCRIPCION: Generar scripts C# de tiempo de ejecución para Unity, guardarlos dentro de Assets/ y actualizar el Asset Database para iniciar su importación y compilación.
Palabras clave: MonoBehaviour, Start, Update, generar script C#, File.WriteAllText, Directory.CreateDirectory, Application.dataPath, AssetDatabase.Refresh, Domain Reload.

NAMESPACES: using System.IO; using UnityEngine; using UnityEditor;

APIS_VALIDAS:
- string Application.dataPath
- bool Directory.Exists(string path)
- Directory.CreateDirectory(string path)
- void File.WriteAllText(string path, string contents)
- void AssetDatabase.Refresh()
- string AssetDatabase.GenerateUniqueAssetPath(string path)
- bool AssetDatabase.IsValidFolder(string path)

REGLAS_CRITICAS:
- Guardar scripts únicamente en rutas validadas dentro de Assets/, evitando rutas absolutas arbitrarias fuera del proyecto.
- Usar Application.dataPath para construir rutas absolutas o validar rutas relativas mediante AssetDatabase.
- Crear directorios inexistentes con Directory.CreateDirectory antes de escribir.
- La clase MonoBehaviour debe coincidir exactamente con el nombre del archivo .cs, respetando mayúsculas y minúsculas.
- Invocar AssetDatabase.Refresh() después de escribir el archivo para iniciar su importación.
- La compilación de Unity es asíncrona: no añadir inmediatamente el nuevo tipo mediante AddComponent en el mismo frame. Esperar a que finalice la compilación y el Domain Reload, y comprobar que el tipo ya está disponible.
- Evitar sobrescribir scripts existentes sin autorización explícita.
- No inventar APIs como Undo.SetCurrentGroup(); AssetDatabase.Refresh() no garantiza compilación inmediata.

EJEMPLO_CANONICO:
string folder = "Assets/Scripts";
if (!AssetDatabase.IsValidFolder(folder))
    Directory.CreateDirectory(Path.Combine(Application.dataPath, "Scripts"));
string className = "PlayerController";
string path = $"{folder}/{className}.cs";
if (File.Exists(path)) return;
string code = "using UnityEngine;\\npublic class " + className +
    " : MonoBehaviour { void Start() {} void Update() {} }";
File.WriteAllText(Path.Combine(Application.dataPath, "Scripts", className + ".cs"), code);
AssetDatabase.Refresh();