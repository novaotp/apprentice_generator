from modules.utils import *

def show_description(options_descriptions):
    """

    Affichage d'une description du programme dans le terminal

    Args :
        - options_descriptions (dict[str, str]) : liste des options + descriptions disponibles pour l'utilisateur

    """

    clear_terminal()

    options = list(options_descriptions.keys())

    print("================== DESCRIPTION ==================")
    print()
    print("Ce programme est un générateur aléatoire d'apprentis.")
    print()
    print("Vous avez accès à plusieurs options :")

    for idx, option in enumerate(options, 1):
        print(f"\t{idx}. {option}")
        print(f"\t\t{options_descriptions[option]}")
        print()

    input("Appuyer sur un bouton pour revenir au menu principal : ")