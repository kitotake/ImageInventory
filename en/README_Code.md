# Code Documentation

## Introduction

This document describes the different parts of the code for the "Image Counter" project. The project consists of Python scripts that manage counting and organizing images.

## Code Structure

### 1. Counting Images

The script `code.py` is responsible for counting images in a given directory. Here are the main functions:

- **count_images_in_directory(directory)**:
  - **Parameter**: `directory` - the path of the directory to analyze.
  - **Functionality**:
    - Traverses all subdirectories and files.
    - Counts the number of images based on specified extensions (JPG, JPEG, PNG, GIF, BMP, TIFF).
    - Displays the total number of images found.

### 2. Organizing Images

The same script `code.py` also handles moving images to folders based on their category.

- **gather_and_separate_images(source_directory, categories)**:
  - **Parameters**:
    - `source_directory`: the source directory where the images are located.
    - `categories`: a list of categories for organizing images.
  - **Functionality**:
    - Creates folders for each category if necessary.
    - Moves images based on their filename.
    - Handles duplicates by renaming files as needed.

## Conclusion

This project aims to make image management easier and more efficient. Users can quickly count and organize their images, allowing them to maintain a well-ordered collection.

## Links

To return to the project description, refer to [Project README](./README_Project.md).
