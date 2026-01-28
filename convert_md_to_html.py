import markdown
import os

# Configuration des fichiers
INPUT_FILE = 'REQUIREMENTS.md'
OUTPUT_FILE = 'REQUIREMENTS.html'

# CSS pour rendre le document joli (Style proche de GitHub)
CSS_STYLE = """
<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
        line-height: 1.6;
        color: #24292e;
        max-width: 900px;
        margin: 0 auto;
        padding: 40px 20px;
        background-color: #ffffff;
    }
    h1, h2, h3 {
        margin-top: 24px;
        margin-bottom: 16px;
        font-weight: 600;
        line-height: 1.25;
    }
    h1 { font-size: 2em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
    h2 { font-size: 1.5em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
    h3 { font-size: 1.25em; }
    
    /* Style des tableaux */
    table {
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 16px;
        display: block;
        overflow-x: auto;
    }
    th, td {
        padding: 6px 13px;
        border: 1px solid #dfe2e5;
    }
    tr {
        background-color: #fff;
        border-top: 1px solid #c6cbd1;
    }
    tr:nth-child(2n) {
        background-color: #f6f8fa;
    }
    th {
        font-weight: 600;
        background-color: #f6f8fa;
    }

    /* Style du code */
    code {
        padding: 0.2em 0.4em;
        margin: 0;
        font-size: 85%;
        background-color: #f6f8fa;
        border-radius: 3px;
        font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
    }
    pre {
        padding: 16px;
        overflow: auto;
        font-size: 85%;
        line-height: 1.45;
        background-color: #f6f8fa;
        border-radius: 3px;
    }
    pre code {
        background-color: transparent;
        padding: 0;
    }

    /* Listes et citations */
    blockquote {
        padding: 0 1em;
        color: #6a737d;
        border-left: 0.25em solid #dfe2e5;
        margin: 0;
    }
    hr {
        height: 0.25em;
        padding: 0;
        margin: 24px 0;
        background-color: #e1e4e8;
        border: 0;
    }
</style>
"""

def convert_markdown_to_html():
    # Vérifier si le fichier existe
    if not os.path.exists(INPUT_FILE):
        print(f"Erreur : Le fichier '{INPUT_FILE}' est introuvable.")
        return

    print(f"Lecture de {INPUT_FILE}...")
    
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        text = f.read()

    # Conversion avec extensions (pour gérer les tableaux et le code)`
    html_content = markdown.markdown(text, extensions=['tables', 'fenced_code'])

    # Construction du fichier HTML final
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Project Requirements</title>
        {CSS_STYLE}
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Écriture du fichier
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)

if __name__ == "__main__":
    convert_markdown_to_html()