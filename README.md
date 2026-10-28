# IA para generación, configuración y consulta general en un motor de desarrollo 3D en tiempo real
Asistente local para Unity 2022.3 con RAG (FastAPI, ChromaDB, Ollama y Qwen 3.5). Resuelve consultas técnicas del manual y ejecuta acciones en escena (crear objetos y configurar componentes) mediante skills atómicas y compilación dinámica en el editor, asegurando privacidad total.


### Software y Entornos
* **Sistema Operativo:** Windows 10/11 (64-bit).
* **Motor 3D:** [Unity 2022.3 LTS (recomendado 2022.3.62f3)](https://unity.com/)
* **Python:** Versión 3.10 o 3.11.
* **Servidor de Modelos:** [Ollama](https://ollama.com/)

---

## 📁 Estructura del Directorio

```text
rag_unity/
├── html_docs/                 # Carpeta receptora de archivos HTML del Manual de Unity
├── markdown_output/           # Salida Markdown depurada del manual (generada automáticamente)
├── skills/                    # Colección curada de habilidades atómicas (*.md)
│   ├── Skill_Manage_GameObject.md
│   ├── Skill_Transform_Hierarchy.md
│   └── ...
├── chroma_db/                 # Base de datos vectorial persistente (generada automáticamente)
├── convertir_html.py          # Script de extracción, limpieza y parseo de HTML a Markdown
├── index_doc.py               # Script de indexación y generación de embeddings en ChromaDB
├── main.py                    # Servidor API FastAPI / Uvicorn (Orquestador RAG)
└── Assets/                    # Archivos para copiar dentro de tu proyecto de Unity
    └── Editor/
        └── LLMAssistant.cs    # Ventana nativa del asistente y controlador de hot-reloading
```

---

## 🛠️ Instalación y Configuración Inicial

### 1. Entorno de Inferencia Local (Ollama)
Descarga e instala Ollama desde su sitio oficial. Abre una terminal (PowerShell o CMD) y descarga los modelos requeridos:

```powershell
# 1. Modelo de incrustaciones vectoriales (Embeddings)
ollama pull nomic-embed-text

# 2. Modelo de lenguaje generativo
ollama pull qwen3.5
```

Puedes verificar su correcta instalación ejecutando:
```powershell
ollama list
```

---

### 2. Preparación del Entorno Backend (Python)
Crea y activa un entorno virtual en la raíz del proyecto para evitar conflictos de dependencias:

```powershell
cd ruta/a/rag_unity
python -m venv venv
.\venv\Scripts\activate
```

Instala las bibliotecas requeridas:
```powershell
pip install fastapi uvicorn requests langchain langchain-community chromadb beautifulsoup4 html2text pydantic
```

---

### 3. Indexación en ChromaDB
Ejecuta el script de cálculo de vectores y almacenamiento persistente:
```powershell
python index_doc.py
```
*Esto generará la base de datos `chroma_db/` con dos colecciones independientes:*
* `unity_manual`: Segmentada mediante ventana deslizante (1,800 caracteres con 14% de solapamiento).
* `unity_skills`: Indexación atómica de plantillas canónicas en C#.

---

### 4. Integración en el Editor de Unity
1. Abre tu proyecto en **Unity 2022.3**.
2. Asegúrate de tener una carpeta llamada `Editor` dentro de `Assets/` (ruta: `Assets/Editor/`).
3. Copia el archivo `LLMAssistant.cs` dentro de `Assets/Editor/`.
4. Unity compilará el script automáticamente y creará una nueva entrada en la barra superior:
   **LLMTools > LLM Assistant**.

---

## Guía de Uso Diario (Flujo de Ejecución)

Para utilizar el asistente en tu sesión de trabajo, sigue esta secuencia en 3 pasos:

### Paso 1: Iniciar Ollama
Abre una terminal y ejecuta el modelo:
```powershell
ollama run qwen3.5
```
*(Una vez cargado en memoria, puedes minimizar o cerrar esta ventana; el servicio permanecerá activo en el puerto `11434`).*

---

### Paso 2: Iniciar el Servidor Orquestador (FastAPI)
Abre otra terminal en la carpeta `rag_unity`, activa el entorno virtual y corre el backend:
```powershell
.\venv\Scripts\activate
python main.py
```
*El servidor levantará en `http://127.0.0.1:8000`. Mantén esta terminal abierta durante tu sesión de desarrollo.*

*(Opcional: puedes probar el servicio abriendo `http://127.0.0.1:8000/docs` en tu navegador).*

---

### Paso 3: Abrir y Usar el Asistente en Unity
1. En Unity Editor, haz clic en el menú superior: **LLMTools > LLM Assistant**.
2. Acopla la ventana interactiva donde prefieras dentro de la interfaz.
3. Selecciona el **Modo de uso** según tu necesidad:

#### A. Modo Consulta (Resolución Conceptual y Teórica)
* **Propósito:** Resolver dudas técnicas sobre componentes, arquitectura o APIs basándose en el manual oficial.
* **Respuesta:** Texto técnico estructurado en Markdown con fragmentos de código y botón rápido de copiado.
* **Ejemplos de prompts:**
  * *"¿Qué es un Prefab y cuáles son sus ventajas?"*
  * *"¿Cómo agrego un Rigidbody a un objeto y qué precauciones debo tener?"*
  * *"¿Qué restricciones existen al usar Coroutines en scripts?"*

#### B. Modo Acción (Automatización y Manipulación en Escena)
* **Propósito:** Modificar directamente la jerarquía, instanciar primitivas, aplicar materiales o configurar el proyecto.
* **Mecanismo:** El asistente genera un script C# temporal (`Assets/OllamaTempCommand.cs`), dispara el ciclo de *hot-reloading* de Unity, ejecuta la acción registrándola en el sistema `Undo` (Ctrl+Z) y limpia el archivo temporal.
* **Ejemplos de prompts:**
  * *"Crea un cubo rojo en la posición (0, 1, 0) con un Rigidbody."*
  * *"Genera una escalera de 5 escalones usando cubos."*
  * *"Agrupa todos los objetos seleccionados bajo un nuevo GameObject padre llamado 'Escenario'."*
  * *"En Player Settings, configura el Company Name como 'MiEstudio'."*

---

## Configuración del Modo Razonamiento (Thinking)

En el script `main.py`, en el payload enviado a Ollama, puedes controlar el comportamiento de inferencia modificando el parámetro `"think"`:

* `"think": False` **(Modo Rápido / Sin Pensamiento):**
  * Latencia contenida (~9.6 s de respuesta).
  * Ideal para consultas técnicas del día a día y tareas atómicas.
* `"think": True` **(Modo Razonamiento Profundo):**
  * Mayor tiempo de cálculo (~50 s de respuesta).
  * Recomendado para tareas procedurales complejas, cálculos geométricos o transformaciones múltiples en escena.

---

## Solución de Problemas Frecuentes

* **Error de conexión en Unity (`Error en FastAPI` o `Error de conexión`):**
  Verifica que `python main.py` esté corriendo y que la dirección `http://127.0.0.1:8000` responda en el navegador.
* **Ollama no responde o tiempo de espera agotado (Timeout):**
  Verifica que el servicio esté activo accediendo a `http://127.0.0.1:11434/` (debe mostrar el mensaje *"Ollama is running"*).
* **Objetos creados con componentes duplicados (ej. doble BoxCollider):**
  Las primitivas de Unity (`GameObject.CreatePrimitive`) incluyen colisionadores por defecto. Si pides agregar un colisionador a una primitiva en el prompt, el modelo podría inyectar uno adicional. Puedes deshacer la acción con `Ctrl+Z` o especificar en el prompt: *"sin agregar colisionadores extra"*.




