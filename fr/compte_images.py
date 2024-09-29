import os

def count_images_in_directory(directory):
    # Liste des extensions d'images
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    
    # Compteur d'images
    image_count = 0

    # Parcourir les sous-dossiers et fichiers
    for subdir, _, files in os.walk(directory):
        for filename in files:
            # Vérifier si le fichier a une extension d'image
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                image_count += 1

    print(f"Total d'images dans '{directory}': {image_count}")

# Remplace 'D:\\trie\\images\\icone' par ton répertoire
source_directory = 'D:\\trie\\images\\icone\\all_images'

# Compter les images
count_images_in_directory(source_directory)
