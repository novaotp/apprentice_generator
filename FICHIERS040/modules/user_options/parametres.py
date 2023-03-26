from modules.utils import *
from modules.config import *

def settings():
    """

    Affiche certains paramètres modifiables à l'utilisateur

    """

    clear_terminal()

    configs = read_config()

    fast_setup_apprentice_generation_count = configs.get("fast_setup_apprentice_generation_count")
    fast_setup_filename = configs.get("fast_setup_filename")
    fast_setup_should_overwrite = configs.get("fast_setup_should_overwrite")
    only_valais = configs.get("only_valais")
    no_duplicates = configs.get("no_duplicates")
    csv_folder = configs.get("csv_folder")
    min_apprentice_count = configs.get("min_apprentice_count")
    max_apprentice_count = configs.get("max_apprentice_count")
    
    parameters = [f"[Rapide] Nombre d'apprentis générés : {fast_setup_apprentice_generation_count}",
                    f"[Rapide] Nom du fichier (sans extension) : {fast_setup_filename}",
                    f"[Rapide] Écraser automatiquement : {fast_setup_should_overwrite}\n",
                    f"[Strict] Générer des apprentis avec des localités uniquement valaisannes : {only_valais}",
                    f"[Strict] Générer des apprentis avec une paire (nom, prénom) unique : {no_duplicates}\n",
                    f"[Storage] Dossier dans lequel enregistre les apprentis : {csv_folder}\n",
                    f"[Limite] Nombre minimum d'apprentis : {min_apprentice_count}",
                    f"[Limite] Nombre maximum d'apprentis : {max_apprentice_count}\n",
                    "[Quitter] Retourner au menu principal"]

    show_settings(parameters)
    
    print()
    min_option = 1
    max_option = len(parameters)
    prompt = "Veuillez choisir une option : "

    option = to_valid_positive_integer(prompt, 1, max_option)

    # Add logic later

def show_settings(parameters):
    print("============================ PARAMÈTRES SYSTÈME ============================")
    print()

    for idx, parameter in enumerate(parameters, 1):
        print(f"\t{idx} : {parameter}")