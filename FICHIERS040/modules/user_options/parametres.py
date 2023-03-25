from modules.utils import *

def show_settings(fast_setup_apprentice_generation_count, fast_setup_filename, fast_setup_should_overwrite):
    """

    Affiche certains paramètres modifiables à l'utilisateur

    """

    clear_terminal()

    print("================== PARAMÈTRES ==================")
    print()

    print(f"[Rapide] Nombre d'apprentis générés : {fast_setup_apprentice_generation_count}")
    print(f"[Rapide] Nom du fichier (sans extension) : {fast_setup_filename}")
    print(f"[Rapide] Écraser automatiquement : {fast_setup_should_overwrite}")
    
    print()
    input("Appuyer sur un bouton pour revenir au menu principal : ")