import os
import re
import sys

def barre_progression(fichiers_traites, total_fichiers):
    """
    Affiche une barre de progression pour indiquer l'avancement du traitement des fichiers.
    :param fichiers_traites: le nombre de fichiers déjà traités
    :param total_fichiers: le nombre total de fichiers à traiter
    """
    # Calculer le pourcentage d'avancement
    pourcentage = (fichiers_traites / total_fichiers) * 100

    # Définir la longueur de la barre de progression
    longueur_barre = 50

    # Calculer le nombre de caractères à afficher pour la barre de progression
    nb_caracteres = int((pourcentage / 100) * longueur_barre)

    # Afficher la barre de progression
    barre = "#" * nb_caracteres + "-" * (longueur_barre - nb_caracteres)
    sys.stdout.write(f"\rProgression : [{barre}] {int(pourcentage)}%")
    sys.stdout.flush()


# Directory containing the scripts
directory = os.path.dirname(os.path.realpath(__file__))

script_files = []
# Get all the script files in the directory
for folder in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, folder)):
        for file in os.listdir(os.path.join(directory, folder)):
            if file.endswith(".py"):
                script_files.append(os.path.join(folder, file))

errors = False
compteur = 0
# Loop through each script file
for script_file in script_files:
    script_path = os.path.join(directory, script_file)
    
    try:
        with open(script_path, 'r') as file:
            script_content = file.read()

            # Modify the script content to comment out print statements
            modified_content = re.sub(r'print\((.*?)\)', r'# print(\1)', script_content)
            # Execute the script
            exec(modified_content)

        # No error raised, print success message
        # print(f"{script_file} executed successfully.")
        
    except Exception as e:
        # Error raised, print error message
        print(f"Error executing {script_file}: {str(e)}")
        errors = True
    
    barre_progression(compteur + 1, len(script_files))
    compteur += 1

if not errors:
    print("\n\nTous les sujets d'ECE ont été executés sans erreur.\nFélicitations !")
