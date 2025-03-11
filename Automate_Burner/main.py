from bs4 import BeautifulSoup

def read_html_file(file_path):
    """Lire le contenu d'un fichier HTML local."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_style_content(html_content):
    """Extraire le contenu entre les balises <style> et </style>."""
    soup = BeautifulSoup(html_content, 'html.parser')
    style_content = soup.style
    if style_content:
        return style_content.decode_contents()
    return ""

def extract_body_content(html_content):
    """Extraire le contenu entre les balises <body> et </body>."""
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return body_content.decode_contents()
    return ""

def save_content_to_file(content, output_file_path):
    """Sauvegarder le contenu dans un nouveau fichier."""
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def insert_content_into_template(style_content, body_content, template_path, output_path):
    """Insérer le contenu extrait dans le template HTML."""
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()

    # Insérer le contenu extrait dans le template et supprimer le commentaire
    updated_content = template_content.replace('/* INSERT YOUR CSS HERE */', style_content)
    updated_content = updated_content.replace('/* INSERT YOUR BODY HERE */', body_content)

    # Sauvegarder le contenu mis à jour dans un nouveau fichier
    save_content_to_file(updated_content, output_path)

def extract_links_from_body(html_content):
    """Extraire tous les liens dans le <body>."""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.body.find_all('a') if soup.body else []
    return [link.get('href') for link in links]

def create_link_files(links, template_path):
    """Créer des fichiers pour chaque lien en remplaçant 'INSERER LIEN ICI'."""
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()

    for index, link in enumerate(links, start=1):
        updated_content = template_content.replace('INSERER LIEN ICI', link)
        # Générer un nom de fichier valide basé sur le lien
        output_path = f'output/index_link_{index}.php'
        save_content_to_file(updated_content, output_path)

def main():
    # Chemin vers le fichier HTML local
    file_path = 'source/index.html'

    # Lire le contenu du fichier HTML
    html_content = read_html_file(file_path)

    # Extraire le contenu du <body>
    body_content = extract_body_content(html_content)

    # Extraire le contenu du <style>
    style_content = extract_style_content(html_content)

    # Chemin vers le fichier template HTML
    template_path = 'template/index_traitement.html'

    # Chemin vers le fichier de sortie
    output_path = 'output/mail.php'

    # Insérer le contenu extrait dans le template HTML
    insert_content_into_template(style_content, body_content, template_path, output_path)

    # Extraire tous les liens dans le <body>
    links = extract_links_from_body(html_content)

    # Créer des fichiers pour chaque lien
    create_link_files(links, 'template/index_link_.php')

    # Afficher les liens
    for link in links:
        print(link)

if __name__ == "__main__":
    main()