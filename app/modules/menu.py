import modules.common.utils as utils

def show_menu(options, advanced_mode):
    """

    Affichage des options disponibles dans le terminal

    Args :
        - options (list[str]) : liste des options disponibles pour l'utilisateur
        - advanced_mode (bool) : mode d'affichage avancée ou non

    """

    utils.clear_terminal()
    idx = 0

    print("================== OPTIONS ==================")
    print()

    if not advanced_mode:
        show_basic_menu(options)
    else:
        show_advanced_menu(options)

    print()

def show_basic_menu(options):
    """

    Affichage du menu basique dans le terminal

    Args :
        - options (list[str]) : liste des options disponibles pour l'utilisateur

    """
    
    for idx, option in enumerate(options, 1):
        print(f"\t{idx} : {option}")

def show_advanced_menu(options):
    """

    Affichage du menu avancé dans le terminal

    Args :
        - options (list[str]) : liste des options disponibles pour l'utilisateur

    """

    advanced_options_count = 3
    basic_options = options[0:len(options) - advanced_options_count]
    advanced_options = options[len(options) - advanced_options_count:len(options)]
    advanced_start_idx = len(options) - advanced_options_count + 1

    print("Options basiques")
    for idx, option in enumerate(basic_options, 1):
        print(f"\t{idx} : {option}")

    print()
    print("Options avancés")
    for idx, option in enumerate(advanced_options, advanced_start_idx):
        print(f"\t{idx} : {option}")
