import os
import re
from pathlib import Path
import chromadb
from chromadb.utils import embedding_functions

# 1. Configuración de rutas y cliente
SKILLS_DIR = Path("./skills")
MANUAL_DIR = Path("./markdown_output")
CHROMA_PATH = "./chroma_unity_db"
BATCH_SIZE = 100  # Tamaño de lote para no saturar la memoria ni la API de Ollama

# Inicializar el cliente persistente sobre el directorio local
client = chromadb.PersistentClient(path=CHROMA_PATH)

# Configurar función de embedding mediante Ollama
embedding_fn = embedding_functions.OllamaEmbeddingFunction(
    url="http://localhost:11434/api/embeddings",
    model_name="nomic-embed-text"
)

# Inicializar ambas colecciones
col_skills = client.get_or_create_collection(
    name="unity_skills",
    embedding_function=embedding_fn
)
col_manual = client.get_or_create_collection(
    name="unity_manual",
    embedding_function=embedding_fn
)

def parse_frontmatter(content: str):
    """Extrae el frontmatter YAML y devuelve metadatos junto con el cuerpo."""
    metadata = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            raw_meta = parts[1]
            body = parts[2].strip()
            for line in raw_meta.strip().splitlines():
                if ":" in line:
                    key, val = line.split(":", 1)
                    metadata[key.strip()] = val.strip().strip('"\'')
    return metadata, body

def chunk_text(text: str, max_chars: int = 1500, overlap: int = 200):
    """Divide documentos extensos en bloques manteniendo solapamiento para no perder contexto."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + max_chars
        chunks.append(text[start:end])
        if end >= len(text):
            break
        start += (max_chars - overlap)
    return chunks

# 2. Indexación de Skills
def index_skills():
    if not SKILLS_DIR.exists():
        print(f"[!] Directorio no encontrado: {SKILLS_DIR}")
        return

    print("Indexando Skills en 'unity_skills'...")
    skill_files = list(SKILLS_DIR.glob("*.md"))
    
    ids, docs, metas = [], [], []
    for f in skill_files:
        content = f.read_text(encoding="utf-8")
        # El nombre de la skill se usa como ID único
        skill_id = f.stem
        ids.append(skill_id)
        docs.append(content)
        metas.append({"name": skill_id, "type": "skill", "filename": f.name})

    if ids:
        # Usar upsert para actualizar si ya existen o insertar si son nuevos
        col_skills.upsert(ids=ids, documents=docs, metadatas=metas)
        print(f"-> {len(ids)} skills indexadas con éxito.")
    else:
        print("[!] No se encontraron archivos .md en la carpeta de skills.")

# 3. Indexación del Manual
def index_manual():
    if not MANUAL_DIR.exists():
        print(f"[!] Directorio no encontrado: {MANUAL_DIR}")
        return

    print("Indexando Manual en 'unity_manual'...")
    manual_files = list(MANUAL_DIR.rglob("*.md"))
    
    ids, docs, metas = [], [], []
    total_chunks = 0

    for file_path in manual_files:
        raw_text = file_path.read_text(encoding="utf-8")
        parsed_meta, body = parse_frontmatter(raw_text)

        # Parametrización aplicada sobre el cuerpo depurado del manual
        chunks = chunk_text(body, max_chars=1800, overlap=250)
        
        for idx, chunk in enumerate(chunks):
            chunk_id = f"{file_path.stem}_{idx}"
            chunk_meta = {
                "title": parsed_meta.get("title", file_path.stem),
                "category": parsed_meta.get("category", "General"),
                "source_file": file_path.name,
                "chunk_index": idx
            }
            
            ids.append(chunk_id)
            docs.append(chunk)
            metas.append(chunk_meta)

            # Eviar por lotes para optimizar llamadas y memoria
            if len(ids) >= BATCH_SIZE:
                col_manual.upsert(ids=ids, documents=docs, metadatas=metas)
                total_chunks += len(ids)
                print(f"   -> Insertados {total_chunks} fragmentos...")
                ids, docs, metas = [], [], []

    # Insertar los fragmentos residuales
    if ids:
        col_manual.upsert(ids=ids, documents=docs, metadatas=metas)
        total_chunks += len(ids)

    print(f"-> Manual indexado con éxito. Total fragmentos: {total_chunks}")

if __name__ == "__main__":
    index_skills()
    index_manual()
    print("\n[OK] Base de datos ChromaDB configurada e indexada por completo.")