# Documentation du Code

## Introduction

Ce document décrit les différentes parties du code du projet "Compteur d'Images". Le projet comprend des scripts Python qui gèrent le comptage et l'organisation des images.

## Structure du Code

### 1. Comptage des Images

Le script `code.py` est responsable du comptage des images dans un répertoire donné. Voici les principales fonctions :

- **count_images_in_directory(directory)** : 
  - **Paramètre** : `directory` - le chemin du répertoire à analyser.
  - **Fonctionnalité** : 
    - Parcourt tous les sous-dossiers et fichiers.
    - Compte le nombre d'images en fonction des extensions spécifiées (JPG, JPEG, PNG, GIF, BMP, TIFF).
    - Affiche le total d'images trouvées.

### 2. Organisation des Images

Le même script `code.py` s'occupe également de déplacer les images vers des dossiers en fonction de leur catégorie.

- **gather_and_separate_images(source_directory, categories)** :
  - **Paramètres** :
    - `source_directory` : le répertoire source où se trouvent les images.
    - `categories` : une liste de catégories pour organiser les images.
  - **Fonctionnalité** : 
    - Crée des dossiers pour chaque catégorie si nécessaire.
    - Déplace les images en fonction de leur nom de fichier.
    - Gère les doublons en renommer les fichiers si nécessaire.

## Conclusion

Ce projet vise à rendre la gestion des images plus facile et plus efficace. Les utilisateurs peuvent rapidement compter et organiser leurs images, ce qui leur permet de garder une collection bien rangée.

## Liens

Pour revenir à la description du projet, consultez [README du projet](./README_Project.md).

