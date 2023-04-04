import modules.common.utils as utils

def show_description(options_descriptions):
    """

    Affichage d'une description du programme dans le terminal

    Args :
        - options_descriptions (dict[str, str]) : liste des options + descriptions disponibles pour l'utilisateur

    """

    utils.clear_terminal()

    print("================== DESCRIPTION ==================")
    print()
    print("Ce programme est un générateur aléatoire d'apprentis.")
    print()
    print("Vous avez accès à plusieurs options :")

    show_formatted_options(options_descriptions)

    input("Appuyer sur un bouton pour revenir au menu principal : ")

def show_formatted_options(options_descriptions):
    """

    Affichage des options d'une manière formattée et ergonomique dans le terminal

    Args :
        - options_descriptions (dict[str, str]) : liste des options + descriptions disponibles pour l'utilisateur

    """
    options = list(options_descriptions.keys())

    for idx, option in enumerate(options, 1):
        print(f"\t{idx}. {option}")
        print(f"\t\t{options_descriptions[option]}")
        print()
