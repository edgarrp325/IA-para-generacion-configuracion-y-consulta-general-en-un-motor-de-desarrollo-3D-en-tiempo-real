import os
import re
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from bs4 import BeautifulSoup
import html2text

def clean_html_to_markdown(html_content: str):
    """
    Limpia el HTML del manual, extrae el título real y devuelve el texto Markdown limpio.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # 1. Extraer título descriptivo
    page_title = ""
    h1_tag = soup.find('h1')
    if h1_tag:
        page_title = h1_tag.get_text().strip()
    elif soup.title:
        page_title = soup.title.get_text().split('-')[0].strip()

    # 2. Localizar el contenedor principal
    main_section = (
        soup.find('div', class_='section') or 
        soup.find('div', class_='content-block') or 
        soup.find('div', id='content-wrap') or 
        soup.find('div', class_='content') or
        soup
    )

    # 3. Eliminar menús, cabeceras, footers y scripts
    noise_selectors = [
        'nav', 'footer', 'script', 'style', 'header', 'aside',
        '.breadcrumbs', '.nextprev', '.lang-switcher', '.toolbar', 
        '.sidebar', '#_leavefeedback', '.footer-wrapper', '.suggest', 
        '.scrollToFeedback', '.mobileLogo', '#_content', '.otherversionscontent',
        '.toc', '.search-form', '.feedbackbox'
    ]
    for selector in noise_selectors:
        for tag in main_section.select(selector):
            tag.decompose()

    # 4. Eliminar tooltips emergentes que duplican texto
    for tooltip in main_section.find_all('span', class_='tooltiptext'):
        tooltip.decompose()

    # 5. Formatear bloques de código
    for pre in main_section.find_all('pre', class_='codeExampleCS'):
        code_text = pre.get_text()
        pre.string = f"\n```csharp\n{code_text.strip()}\n```\n"

    # 6. Convertir a Markdown limpio
    h = html2text.HTML2Text()
    h.ignore_links = True     
    h.ignore_images = True         
    h.ignore_emphasis = False      
    h.body_width = 0              
    h.mark_code = False
    
    markdown_output = h.handle(str(main_section)).strip()
    
    # Reducir saltos de línea excesivos
    markdown_output = re.sub(r'\n{3,}', '\n\n', markdown_output)

    return page_title, markdown_output

def process_single_file(file_info):
    """Procesa solo archivos del Manual y descarta la Scripting API."""
    file_path, input_path, output_path = file_info
    try:
        relative_path = file_path.relative_to(input_path)
        path_str_lower = str(relative_path).lower()

        # Descartar Scripting API
        if "scriptreference" in path_str_lower or "scripting" in path_str_lower or "api" in path_str_lower:
            return "skipped_scripting_api"

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            raw_html = f.read()

        title, md_body = clean_html_to_markdown(raw_html)

        # Descartar archivos vacíos o páginas índice con menos de 150 caracteres.
        if len(md_body) < 150:
            return "skipped_empty"

        final_title = title if title else file_path.stem

        # Extraer carpeta temática para categorizar en metadatos
        category = relative_path.parts[0] if len(relative_path.parts) > 1 else "General"

        # Encabezado estructurado YAML
        frontmatter = (
            f"---\n"
            f"title: \"{final_title}\"\n"
            f"category: \"{category}\"\n"
            f"source_file: \"{file_path.name}\"\n"
            f"doc_type: \"manual\"\n"
            f"---\n\n"
        )
        
        full_content = frontmatter + md_body

        target_file = (output_path / relative_path).with_suffix('.md')
        target_file.parent.mkdir(parents=True, exist_ok=True)

        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(full_content)

        return True
    except Exception as e:
        return f"Error en {file_path.name}: {e}"

def process_all_html(input_dir: str = "./html_docs", output_dir: str = "./markdown_output"):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    if not input_path.exists():
        print(f"[!] Error: La carpeta '{input_dir}' no existe.")
        return

    html_files = list(input_path.rglob("*.html")) + list(input_path.rglob("*.htm"))
    total_files = len(html_files)
    print(f"Total de archivos HTML encontrados: {total_files}")
    
    if total_files == 0:
        return

    print("Procesando Manual de Unity en paralelo...")
    tasks = [(f, input_path, output_path) for f in html_files]

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(process_single_file, tasks))

    successes = sum(1 for r in results if r is True)
    skipped_api = sum(1 for r in results if r == "skipped_scripting_api")
    skipped_empty = sum(1 for r in results if r == "skipped_empty")
    errors = [r for r in results if isinstance(r, str) and r.startswith("Error")]

    print(f"\nResumen:")
    print(f"- Manual procesado con éxito: {successes}")
    print(f"- Scripting API ignorada (sustituida por Skills): {skipped_api}")
    print(f"- Páginas vacías/índices descartadas: {skipped_empty}")
    if errors:
        print(f"- Errores: {len(errors)} (primeros: {errors[:3]})")

if __name__ == "__main__":
    process_all_html(input_dir="./html_docs", output_dir="./markdown_output")