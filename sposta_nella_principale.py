import os
import shutil

# definire il percorso della cartella principale e delle sottocartelle
parent_folder = "/media/michelangelo/7E9264A192645F9F/data/gta5-tracking/val/image"

# iterare attraverso tutte le sottocartelle nella cartella principale
for root, dirs, files in os.walk(parent_folder):
    for file in files:
        # creare il percorso completo del file corrente
        current_file_path = os.path.join(root, file)

        # creare il percorso del nuovo file nella cartella principale
        new_file_path = os.path.join(parent_folder, file)

        # spostare il file nella cartella principale
        shutil.move(current_file_path, new_file_path)
