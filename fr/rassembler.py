import os
import shutil

def gather_and_separate_images(source_directory, categories):
    # Créer les dossiers pour chaque catégorie
    for category in categories:
        category_folder = os.path.join(source_directory, category)
        os.makedirs(category_folder, exist_ok=True)

    # Compteur d'images déplacées
    moved_count = {category: 0 for category in categories}

    # Parcourir les sous-dossiers
    for subdir, _, files in os.walk(source_directory):
        for filename in files:
            file_path = os.path.join(subdir, filename)

            # Retirer les duplicatas "(1)", "(2)", etc.
            base_filename, ext = os.path.splitext(filename)
            base_filename = base_filename.split(' (')[0]  # Supprime les parties en "(1)", "(2)", etc.

            # Vérifier à quelle catégorie appartient le fichier
            moved = False
            for category in categories:
                if category.lower() in filename.lower():
                    dst = os.path.join(source_directory, category, f"{base_filename}{ext}")
                    
                    # Gestion des duplicatas
                    count = 1
                    while os.path.exists(dst):
                        dst = os.path.join(source_directory, category, f"{base_filename}_{count}{ext}")
                        count += 1

                    # Déplacer le fichier
                    shutil.move(file_path, dst)
                    moved_count[category] += 1
                    print(f'Déplacé: {file_path} vers {dst}')
                    moved = True
                    break
            
            # Si aucune catégorie correspondante, laisser dans un dossier "autres"
            if not moved:
                other_folder = os.path.join(source_directory, 'others')
                os.makedirs(other_folder, exist_ok=True)
                dst = os.path.join(other_folder, f"{base_filename}{ext}")
                
                count = 1
                while os.path.exists(dst):
                    dst = os.path.join(other_folder, f"{base_filename}_{count}{ext}")
                    count += 1
                
                shutil.move(file_path, dst)
                print(f'Déplacé: {file_path} vers {dst}')

    # Résumé
    for category in moved_count:
        print(f"Total d'images '{category}' déplacées: {moved_count[category]}")

# Remplace 'D:\\trie\\images\\icone' par ton répertoire
source_directory = 'D:\\trie\\images\\icone\\all_images'

# Liste des catégories basées sur ox_inventory et ajoutées
categories = [
    'ammo', 'weapon', 'food', 'ingredient', 'money', 'item', 'clothing', 
    'medkit', 'drink', 'furniture', 'tool', 'electronics', 'misc', 
    'vehicle', 'wood', 'metal', 'plastic', 'medicine', 'alcohol', 
    'jewelry', 'documents', 'hardware', 'books', 'keys', 'plants', 
    'seeds', 'gems', 'backpacks', 'cosmetics', 'art', 'sporting_goods', 
    'stationery', 'farming', 'fishing', 'camping_gear', 'luxury_items'
]

gather_and_separate_images(source_directory, categories)
