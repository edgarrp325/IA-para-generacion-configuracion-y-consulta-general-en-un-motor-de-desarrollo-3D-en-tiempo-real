using UnityEngine;
using UnityEditor;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;
using System.IO;
using System.Text.RegularExpressions;

public class LLMAssistant : EditorWindow
{
    public enum AssistantMode
    {
        Accion,
        Consulta
    }

    // Configuración Ollama y Backend
    private string modelName = "qwen3.5";
    private string ragUrl = "http://127.0.0.1:8000/rag";
    private static readonly HttpClient client = new HttpClient()
    {
        Timeout = System.TimeSpan.FromMinutes(5)
    };

    private AssistantMode currentMode = AssistantMode.Accion;
    private string userPrompt = "";
    private string queryResponse = "";
    private string log = "Listo (Ollama Local).";
    private bool isProcessing = false;
    private Vector2 scrollPos;

    // Contador del tiempo de respuesta de LLM
    private readonly System.Diagnostics.Stopwatch responseTimer =
    new System.Diagnostics.Stopwatch();

    private double responseSeconds = 0;
    private bool isWaitingForResponse = false;

    // Estilos personalizados
    private GUIStyle richTextStyle;
    private GUIStyle codeBlockStyle;
    private GUIStyle headerStyle;

    const string TempFilePath = "Assets/OllamaTempCommand.cs";
    bool TempFileExists => File.Exists(TempFilePath);

    [MenuItem("LLMTools/LLM Assistant")]
    public static void ShowWindow() => GetWindow<LLMAssistant>("LLM Assistant");

    void InitializeStyles()
    {
        if (richTextStyle == null)
        {
            richTextStyle = new GUIStyle(EditorStyles.label)
            {
                richText = true,
                wordWrap = true,
                fontSize = 12
            };
        }

        if (codeBlockStyle == null)
        {
            codeBlockStyle = new GUIStyle(EditorStyles.helpBox)
            {
                font = EditorStyles.miniFont,
                fontSize = 11,
                wordWrap = true,
                padding = new RectOffset(10, 10, 8, 8)
            };
        }

        if (headerStyle == null)
        {
            headerStyle = new GUIStyle(EditorStyles.boldLabel)
            {
                richText = true,
                fontSize = 13,
                margin = new RectOffset(0, 0, 8, 4)
            };
        }
    }

    void OnGUI()
    {
        InitializeStyles();

        GUILayout.Label("Asistente Local", EditorStyles.boldLabel);

        // Selector de modo
        EditorGUILayout.Space(4);
        currentMode = (AssistantMode)EditorGUILayout.EnumPopup("Modo de uso:", currentMode);
        EditorGUILayout.Space(6);

        if (currentMode == AssistantMode.Accion)
        {
            EditorGUILayout.LabelField("Instrucción para la escena (crear objetos, modificar, etc.):");
        }
        else
        {
            EditorGUILayout.LabelField("Pregunta / Consulta técnica sobre Unity o C#:");
        }

        userPrompt = EditorGUILayout.TextArea(userPrompt, GUILayout.Height(60));

        EditorGUI.BeginDisabledGroup(isProcessing || string.IsNullOrWhiteSpace(userPrompt));
        string buttonText = currentMode == AssistantMode.Accion ? "Ejecutar Acción en Escena" : "Consultar";
        if (GUILayout.Button(buttonText, GUILayout.Height(28)))
        {
            _ = RunGenerator();
        }
        EditorGUI.EndDisabledGroup();

        // Contador del tiempo de respuesta del LLM
        GUILayout.Space(5);

        double elapsedSeconds = isWaitingForResponse
            ? responseTimer.Elapsed.TotalSeconds
            : responseSeconds;

        EditorGUILayout.LabelField(
            "Tiempo de respuesta:",
            $"{elapsedSeconds:F2} segundos"
        );

        GUILayout.Space(10);
        GUILayout.Label("Estado:", EditorStyles.boldLabel);
        EditorGUILayout.HelpBox(log, MessageType.Info);

        // Área de respuesta estilizada para el modo Consulta
        if (currentMode == AssistantMode.Consulta && !string.IsNullOrEmpty(queryResponse))
        {
            GUILayout.Space(10);
            GUILayout.Label("Respuesta:", EditorStyles.boldLabel);

            scrollPos = EditorGUILayout.BeginScrollView(scrollPos, EditorStyles.helpBox, GUILayout.MinHeight(220));
            RenderStyledMarkdown(queryResponse);
            EditorGUILayout.EndScrollView();
        }
    }

    void RenderStyledMarkdown(string rawText)
    {
        string[] parts = rawText.Split(new string[] { "```" }, System.StringSplitOptions.None);

        for (int i = 0; i < parts.Length; i++)
        {
            string part = parts[i];
            if (string.IsNullOrWhiteSpace(part)) continue;

            // Bloques de código (impares)
            if (i % 2 != 0)
            {
                string cleanCode = part.Trim();

                int firstNewline = cleanCode.IndexOf('\n');
                if (firstNewline > 0 && firstNewline < 15 && !cleanCode.Substring(0, firstNewline).Contains(" "))
                {
                    cleanCode = cleanCode.Substring(firstNewline + 1).Trim();
                }

                EditorGUILayout.BeginVertical(codeBlockStyle);
                EditorGUILayout.BeginHorizontal();
                GUILayout.Label("<b>Código:</b>", richTextStyle);
                GUILayout.FlexibleSpace();
                if (GUILayout.Button("Copiar", EditorStyles.miniButton, GUILayout.Width(60)))
                {
                    EditorGUIUtility.systemCopyBuffer = cleanCode;
                }
                EditorGUILayout.EndHorizontal();

                EditorGUILayout.TextArea(cleanCode, EditorStyles.miniLabel);
                EditorGUILayout.EndVertical();
                EditorGUILayout.Space(4);
            }
            else
            {
                string[] lines = part.Replace("\r", "").Split('\n');
                foreach (string rawLine in lines)
                {
                    string line = rawLine;
                    if (string.IsNullOrWhiteSpace(line))
                    {
                        EditorGUILayout.Space(2);
                        continue;
                    }

                    // Títulos
                    if (line.StartsWith("### "))
                    {
                        GUILayout.Label("<size=13><b>" + ConvertInlineMarkdown(line.Substring(4)) + "</b></size>", headerStyle);
                    }
                    else if (line.StartsWith("## "))
                    {
                        GUILayout.Label("<size=14><b>" + ConvertInlineMarkdown(line.Substring(3)) + "</b></size>", headerStyle);
                    }
                    else if (line.StartsWith("# "))
                    {
                        GUILayout.Label("<size=15><b>" + ConvertInlineMarkdown(line.Substring(2)) + "</b></size>", headerStyle);
                    }
                    else
                    {
                        // Detectar viñetas de lista (* elemento o - elemento)
                        Match listMatch = Regex.Match(line, @"^\s*[\*\-]\s+(.*)$");
                        if (listMatch.Success)
                        {
                            line = "  • " + listMatch.Groups[1].Value;
                        }

                        GUILayout.Label(ConvertInlineMarkdown(line), richTextStyle);
                    }
                }
            }
        }
    }

    
    string ConvertInlineMarkdown(string input)
    {
        if (string.IsNullOrEmpty(input)) return "";

        string result = input;
        string codeColor = EditorGUIUtility.isProSkin ? "#9CDCFE" : "#00569E";

        // 1. Código inline `codigo`
        result = Regex.Replace(
            result,
            @"`([^`]+)`",
            "<color=" + codeColor + "><b>$1</b></color>"
        );

        // 2. Negrita **texto** o __texto__
        result = Regex.Replace(result, @"\*\*(.+?)\*\*", "<b>$1</b>");
        result = Regex.Replace(result, @"__(.+?)__", "<b>$1</b>");

        // 3. Cursiva *texto* o _texto_
        result = Regex.Replace(
            result,
            @"(?<![<b><i>])\*(?!\s)([^*]+?)(?<!\s)\*",
            "<i>$1</i>"
        );

        result = Regex.Replace(
            result,
            @"(?<![<b><i>])_(?!\s)([^_]+?)(?<!\s)_",
            "<i>$1</i>"
        );

        return result;
    }


    async Task RunGenerator()
    {
        isProcessing = true;
        isWaitingForResponse = true;
        responseSeconds = 0;
        responseTimer.Restart();

        log = "Consultando a FastAPI + RAG + LLM...";
        Repaint();

        try
        {
            string modeStr = currentMode == AssistantMode.Accion
                ? "Accion"
                : "Consulta";

            // Esperar la respuesta del backend
            string responseText = await CallRAG(userPrompt, modeStr);

            // Detener el contador al recibir la respuesta
            responseTimer.Stop();
            responseSeconds = responseTimer.Elapsed.TotalSeconds;
            isWaitingForResponse = false;

            if (!string.IsNullOrEmpty(responseText))
            {
                if (currentMode == AssistantMode.Accion)
                {
                    string code = responseText
                        .Replace("```csharp", "")
                        .Replace("```", "")
                        .Trim();

                    log = "Código recibido. Compilando...";
                    CreateScriptAsset(code);
                }
                else
                {
                    queryResponse = responseText.Trim();
                    log = "Respuesta recibida.";
                }
            }
        }
        catch (System.Exception e)
        {
            responseTimer.Stop();
            responseSeconds = responseTimer.Elapsed.TotalSeconds;
            isWaitingForResponse = false;

            log = "Error: " + e.Message;
            Debug.LogError(e);
        }

        isProcessing = false;
        Repaint();
    }

    async Task<string> CallRAG(string prompt, string mode)
    {
        string jsonPayload = "{" +
            "\"prompt\": \"" + EscapeJson(prompt) + "\"," +
            "\"mode\": \"" + mode + "\"" +
            "}";

        var content = new StringContent(jsonPayload, Encoding.UTF8, "application/json");

        try
        {
            var response = await client.PostAsync(ragUrl, content);
            string result = await response.Content.ReadAsStringAsync();

            if (!response.IsSuccessStatusCode)
            {
                log = "Error en FastAPI. ¿Está corriendo el backend?\n" + response.StatusCode;
                return null;
            }

            return ExtractOllamaText(result);
        }
        catch (System.Exception e)
        {
            log = "Error de conexión: " + e.Message;
            return null;
        }
    }

    void CreateScriptAsset(string code)
    {
        var flags = BindingFlags.Static | BindingFlags.NonPublic;
        var method = typeof(ProjectWindowUtil).GetMethod("CreateScriptAssetWithContent", flags);

        if (method != null)
            method.Invoke(null, new object[] { TempFilePath, code });
        else
        {
            File.WriteAllText(TempFilePath, code);
            AssetDatabase.ImportAsset(TempFilePath);
        }
    }

    void OnEnable()
    {
        AssemblyReloadEvents.afterAssemblyReload += OnAfterAssemblyReload;
        EditorApplication.update += OnEditorUpdate;
    }

    void OnDisable()
    {
        AssemblyReloadEvents.afterAssemblyReload -= OnAfterAssemblyReload;
        EditorApplication.update -= OnEditorUpdate;
    }

    void OnAfterAssemblyReload()
    {
        if (!TempFileExists) return;

        bool success = EditorApplication.ExecuteMenuItem("Edit/Do AI Task");
        if (success)
        {
            AssetDatabase.DeleteAsset(TempFilePath);
            log = "Tarea completada con éxito por Qwen.";
        }
    }

    string EscapeJson(string text) => text.Replace("\\", "\\\\").Replace("\"", "\\\"").Replace("\n", "\\n").Replace("\r", "\\r");

    [System.Serializable]
    public class OllamaResponse { public string response; }

    string ExtractOllamaText(string json)
    {
        try
        {
            return JsonUtility.FromJson<OllamaResponse>(json).response;
        }
        catch { return ""; }
    }

    void OnEditorUpdate()
    {
        if (isWaitingForResponse)
        {
            Repaint();
        }   
    }
}