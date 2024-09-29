import os
import shutil

def gather_and_separate_images(source_directory, categories):
    # Create folders for each category
    for category in categories:
        category_folder = os.path.join(source_directory, category)
        os.makedirs(category_folder, exist_ok=True)

    # Counter for moved images
    moved_count = {category: 0 for category in categories}

    # Traverse subdirectories
    for subdir, _, files in os.walk(source_directory):
        for filename in files:
            file_path = os.path.join(subdir, filename)

            # Remove duplicates "(1)", "(2)", etc.
            base_filename, ext = os.path.splitext(filename)
            base_filename = base_filename.split(' (')[0]  # Remove parts in "(1)", "(2)", etc.

            # Check which category the file belongs to
            moved = False
            for category in categories:
                if category.lower() in filename.lower():
                    dst = os.path.join(source_directory, category, f"{base_filename}{ext}")
                    
                    # Handle duplicates
                    count = 1
                    while os.path.exists(dst):
                        dst = os.path.join(source_directory, category, f"{base_filename}_{count}{ext}")
                        count += 1

                    # Move the file
                    shutil.move(file_path, dst)
                    moved_count[category] += 1
                    print(f'Moved: {file_path} to {dst}')
                    moved = True
                    break
            
            # If no matching category, leave it in an "others" folder
            if not moved:
                other_folder = os.path.join(source_directory, 'others')
                os.makedirs(other_folder, exist_ok=True)
                dst = os.path.join(other_folder, f"{base_filename}{ext}")
                
                count = 1
                while os.path.exists(dst):
                    dst = os.path.join(other_folder, f"{base_filename}_{count}{ext}")
                    count += 1
                
                shutil.move(file_path, dst)
                print(f'Moved: {file_path} to {dst}')

    # Summary
    for category in moved_count:
        print(f"Total images '{category}' moved: {moved_count[category]}")

# Replace 'D:\\trie\\images\\icone' with your directory
source_directory = 'D:\\trie\\images\\icone\\all_images'

# List of categories based on ox_inventory and added
categories = [
    'ammo', 'weapon', 'food', 'ingredient', 'money', 'item', 'clothing', 
    'medkit', 'drink', 'furniture', 'tool', 'electronics', 'misc', 
    'vehicle', 'wood', 'metal', 'plastic', 'medicine', 'alcohol', 
    'jewelry', 'documents', 'hardware', 'books', 'keys', 'plants', 
    'seeds', 'gems', 'backpacks', 'cosmetics', 'art', 'sporting_goods', 
    'stationery', 'farming', 'fishing', 'camping_gear', 'luxury_items'
]

gather_and_separate_images(source_directory, categories)
