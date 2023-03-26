from modules.utils import *

def show_menu(options, advanced_mode):
    """

    Affichage des options disponibles dans le terminal

    Args :
        - options (list[str]) : liste des options disponibles pour l'utilisateur
        - advanced_mode (bool) : mode d'affichage avancée ou non

    """

    clear_terminal()
    idx = 0

    print("================== OPTIONS ==================")
    print()

    if not advanced_mode:
        for idx, option in enumerate(options, 1):
            print(f"\t{idx} : {option}")
    else:
        advanced_options_count = 3
        basic_options = options[0:len(options) - advanced_options_count]
        advanced_options = options[len(options) - advanced_options_count:]

        print("Options basiques")
        for idx, option in enumerate(basic_options, 1):
            print(f"\t{idx} : {option}")

        print()
        print("Options avancés")
        for idx, option in enumerate(advanced_options, len(options) - advanced_options_count + 1):
            print(f"\t{idx} : {option}")

    print()