from modules.utils import *
from modules.read_config_file import *

def show_settings():
    """

    Affiche certains paramètres modifiables à l'utilisateur

    """

    clear_terminal()

    configs = read_config()

    fast_setup_apprentice_generation_count = configs.get("fast_setup_apprentice_generation_count")
    fast_setup_filename = configs.get("fast_setup_filename")
    fast_setup_should_overwrite = configs.get("fast_setup_should_overwrite")

    if fast_setup_apprentice_generation_count is None or fast_setup_filename is None or fast_setup_should_overwrite is None or csv_folder is None:
        sys.exit("System error : missing or incorrect config values")

    try:
        fast_setup_apprentice_generation_count = int(fast_setup_apprentice_generation_count)
    except:
        sys.exit("System error : missing or incorrect config values")

    print("================== PARAMÈTRES ==================")
    print()

    print(f"[Rapide] Nombre d'apprentis générés : {fast_setup_apprentice_generation_count}")
    print(f"[Rapide] Nom du fichier (sans extension) : {fast_setup_filename}")
    print(f"[Rapide] Écraser automatiquement : {fast_setup_should_overwrite}")
    
    print()
    input("Appuyer sur un bouton pour revenir au menu principal : ")