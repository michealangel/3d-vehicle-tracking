import os

# definire il percorso della cartella contenente i file .json
folder_path = "/media/michelangelo/7E9264A192645F9F/data/gta5-tracking/val/label"

# iterare attraverso tutti i file nella cartella
for filename in os.listdir(folder_path):
    if filename.endswith("bdd.json"): # controllare se il file finisce con "bdd.json"
        # aprire il file e leggere il contenuto
        with open(os.path.join(folder_path, filename), "r") as f:
            content = f.read()

        # sostituire tutte le occorrenze di "./data/gta5_tracking/val/label/" con " /media/michelangelo/7E9264A192645F9F/data/gta5-tracking/val/label"
        new_content = content.replace(" /media", "/media")

        # scrivere il nuovo contenuto nel file
        with open(os.path.join(folder_path, filename), "w") as f:
            f.write(new_content)