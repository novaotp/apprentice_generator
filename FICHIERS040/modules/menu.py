from modules.utils import *

def show_menu(options):
    """

    Affichage des options disponibles dans le terminal

    Args :
        - options (list[str]) : liste des options disponibles pour l'utilisateur

    """

    clear_terminal()
    idx = 0

    print("================== OPTIONS ==================")
    print()

    for idx, option in enumerate(options, 1):
        print(f"\t{idx} : {option}")

    print()