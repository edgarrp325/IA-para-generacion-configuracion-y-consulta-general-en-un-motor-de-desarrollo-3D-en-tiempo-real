SKILL: Skill_Build_And_Player_Settings
DESCRIPCION: Configurar escenas de compilación, plataforma activa y metadatos del proyecto Unity desde herramientas de Editor, validando rutas y actualizando identificadores de aplicación.
Palabras clave: EditorBuildSettings.scenes, EditorBuildSettingsScene, SwitchActiveBuildTarget, PlayerSettings, companyName, productName, bundleVersion, SetApplicationIdentifier.

NAMESPACES: using UnityEditor; using UnityEditor.Build; using UnityEditor.Build.Reporting; using UnityEngine;

APIS_VALIDAS:
- EditorBuildSettingsScene[] EditorBuildSettings.scenes { get; set; }
- EditorBuildSettingsScene(string path, bool enabled)
- bool EditorUserBuildSettings.SwitchActiveBuildTarget(BuildTargetGroup targetGroup, BuildTarget target)
- string PlayerSettings.companyName { get; set; }
- string PlayerSettings.productName { get; set; }
- string PlayerSettings.bundleVersion { get; set; }
- void PlayerSettings.SetApplicationIdentifier(NamedBuildTarget buildTarget, string identifier)
- bool AssetDatabase.LoadAssetAtPath<T>(string path) where T : UnityEngine.Object

REGLAS_CRITICAS:
- PROHIBIDO usar .Add() o .Remove() directamente en EditorBuildSettings.scenes; obtener el arreglo, modificar una lista y reasignar el arreglo completo.
- Validar que cada escena exista y su ruta sea válida, por ejemplo "Assets/Scenes/Main.unity".
- No inventar APIs como Undo.SetCurrentGroup().
- Usar NamedBuildTarget para SetApplicationIdentifier en Unity 2022.3.
- Comprobar el resultado de SwitchActiveBuildTarget; el cambio puede fallar o requerir módulos instalados.
- Estas configuraciones del proyecto no deben tratarse como modificaciones de objetos de escena con Undo.

EJEMPLO_CANONICO:
var scenes = new System.Collections.Generic.List<EditorBuildSettingsScene>(EditorBuildSettings.scenes);
string path = "Assets/Scenes/Main.unity";
if (AssetDatabase.LoadAssetAtPath<SceneAsset>(path) != null)
{
    scenes.Add(new EditorBuildSettingsScene(path, true));
    EditorBuildSettings.scenes = scenes.ToArray();
}
PlayerSettings.companyName = "MiEmpresa";
PlayerSettings.productName = "MiJuego";
PlayerSettings.bundleVersion = "1.0.0";
PlayerSettings.SetApplicationIdentifier(NamedBuildTarget.Standalone, "com.miempresa.mijuego");