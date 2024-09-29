import os

def count_images_in_directory(directory):
    # List of image extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    
    # Image counter
    image_count = 0

    # Traverse subdirectories and files
    for subdir, _, files in os.walk(directory):
        for filename in files:
            # Check if the file has an image extension
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                image_count += 1

    print(f"Total images in '{directory}': {image_count}")

# Replace 'D:\\trie\\images\\icone' with your directory
source_directory = 'D:\\trie\\images\\icone\\all_images'

# Count the images
count_images_in_directory(source_directory)
