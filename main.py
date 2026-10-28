from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import traceback
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

app = FastAPI(title="Unity RAG Engine")

CHROMA_DIR = "./chroma_unity_db"
OLLAMA_BASE_URL = "http://127.0.0.1:11434"
OLLAMA_GENERATE_URL = f"{OLLAMA_BASE_URL}/api/generate"
MODEL_NAME = "qwen3.5"

# 1. Configurar embeddings apuntando a Ollama
embeddings = OllamaEmbeddings(
    base_url=OLLAMA_BASE_URL,
    model="nomic-embed-text"
)

# 2. Inicializar ambas colecciones por separado en la misma base de datos
skills_db = Chroma(
    persist_directory=CHROMA_DIR,
    collection_name="unity_skills",
    embedding_function=embeddings
)
skills_retriever = skills_db.as_retriever(search_kwargs={"k": 2})

manual_db = Chroma(
    persist_directory=CHROMA_DIR,
    collection_name="unity_manual",
    embedding_function=embeddings
)
manual_retriever = manual_db.as_retriever(search_kwargs={"k": 3})

class RAGRequest(BaseModel):
    prompt: str
    mode: str = "Consulta"  # "Accion" o "Consulta"

@app.post("/rag")
async def rag_endpoint(req: RAGRequest):
    try:
        if req.mode == "Accion":
            # 1. Recuperar únicamente de la colección de Skills
            docs = skills_retriever.invoke(req.prompt)
            context = "\n\n".join([f"--- [Skill: {d.metadata.get('name', d.metadata.get('filename', 'Skill'))}] ---\n{d.page_content}" for d in docs])

            temperature = 0.1
                
            system_prompt = (
                "Eres un generador determinista de scripts para Unity Editor 2022.3 "
                "usando C#.\n\n"

                "CONTEXTO RAG (Skills):\n"
                f"{context}\n\n"

                "OBJETIVO:\n"
                "Genera un archivo C# completo, compilable y funcional que resuelva la instrucción del usuario utilizando las Skills proporcionadas.\n\n"

                "REGLAS OBLIGATORIAS DE SALIDA:\n"
                "1. La primera línea del archivo debe ser un using válido.\n"
                "2. Incluye SIEMPRE, como mínimo:\n"
                "   using UnityEngine;\n"
                "   using UnityEditor;\n"
                "3. Incluye todos los using adicionales que requieran las APIs utilizadas. Por ejemplo, si usas EditorSceneManager, incluye using UnityEditor.SceneManagement;.\n"
                "4. Después de los using, declara exactamente la clase pública estática: public static class OllamaTempCommand.\n"
                "5. Dentro de la clase, declara el método estático que resuelve la tarea y que contiene [MenuItem(\"Edit/Do AI Task\")].\n"
                "6. El archivo debe contener todas las llaves, métodos y declaraciones necesarios para compilar. No omitas los using ni el código auxiliar necesario.\n"
                "7. Utiliza exclusivamente APIs válidas de Unity 2022.3 y respeta las prohibiciones de las Skills. NUNCA uses Undo.SetCurrentGroup.\n"
                "8. Prioriza las APIs de Undo apropiadas para cada modificación del Editor. No inventes métodos ni firmas.\n"
                "9. No supongas que los using ya existen en otro archivo. Cada respuesta debe ser un archivo independiente y completo.\n\n"

                "FORMATO DE RESPUESTA:\n"
                "- Devuelve únicamente código fuente C#.\n"
                "- No uses bloques Markdown ni delimitadores de código.\n"
                "- No incluyas explicaciones antes ni después del código.\n"
                "- No sustituyas declaraciones necesarias por puntos suspensivos.\n\n"

                "VERIFICACIÓN FINAL OBLIGATORIA:\n"
                "Antes de responder, comprueba que el archivo comienza con los namespaces 'using UnityEngine;' y 'using UnityEditor;', que contiene la clase "
                "OllamaTempCommand y el atributo [MenuItem(\"Edit/Do AI Task\")], y que se agregaron todos los namespaces adicionales necesarios \n"
                "Si falta alguno de estos elementos, corrige el código antes de devolverlo."
            )
            stop_tokens = ["Explicación:", "Nota:"]

        else:
            # 1. Recuperar únicamente del Manual conceptual
            docs = manual_retriever.invoke(req.prompt)
            context = "\n\n".join([f"--- [Sección: {d.metadata.get('title', 'Manual')}] ---\n{d.page_content}" for d in docs])

            temperature = 0.5
            system_prompt = (
                "Eres un asistente técnico experto en Unity 2022.3 y C#.\n"
                "Responde de forma concisa, estructurada y directa a la duda basándote en el contexto del manual.\n"
                "Usa formato Markdown para títulos (###), listas y bloques breves de código (```csharp ... ```).\n\n"
                f"Contexto disponible del Manual:\n{context}"
            )
            stop_tokens = []

        # 2. Petición al endpoint de Ollama
        payload = {
            "model": MODEL_NAME,
            "system": system_prompt,
            "prompt": req.prompt,
            "stream": False,
            "think": False,
            "options": {
                "temperature": temperature,
                "num_ctx": 8192,
                "num_predict": -1,
                "stop": stop_tokens
            }
        }
        res = requests.post(OLLAMA_GENERATE_URL, json=payload, timeout=500)
        res.raise_for_status()

        ollama_data = res.json()
        return {"response": ollama_data.get("response", "")}

    except Exception as e:
        print("\n--- ERROR DETALLADO EN FASTAPI ---")
        traceback.print_exc()
        print("----------------------------------\n")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)