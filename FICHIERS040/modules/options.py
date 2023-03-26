from modules.utils import *
from modules.user_options.description import *
from modules.user_options.generer import *
from modules.user_options.setup_rapide import *
from modules.user_options.lister import *
from modules.user_options.parametres import *
from modules.user_options.quitter import *
from modules.user_options.sauvegarder import *
from modules.user_options.mode_avance import *


def get_user_option(options):
    """

    Demande le choix de l'utilisateur concernant ce qu'il veut faire

    Args :
        - options (list[str]) : liste des options disponibles pour l'utilisateur

    Return :
        - user_option (int) : n° de l'option choisie par l'utilisateur

    """

    prompt = "Veuillez choisir une option : "
    error_message = "Choix invalide..."

    user_option = to_valid_positive_integer(prompt, 1, len(options))

    return user_option


def check_user_option(user_option, options, apprentices, options_descriptions, advanced_mode):
    """

    Dirige l'utilisateur vers la fonction choisie

    Args :
        - user_option (int) : choix de l'utilisateur
        - options (list[str]) : liste des options disponibles pour l'utilisateur
        - apprentices (list[str]) : liste des apprentis
        - options_descriptions (dict[str, str]) : liste des (options + descriptions) disponibles pour l'utilisateur
        - advanced_mode (bool) : afficher le mode avancé ou non

    """

    choice = options[user_option - 1]
    should_continue = True

    if choice == "Description":
        show_description(options_descriptions)
    elif choice == "Générer":
        apprentice_count = get_apprentice_count()
        apprentices = generate_apprentices(apprentice_count)
    elif choice == "Setup rapide":
        fast_setup()
    elif choice == "Lister":
        list_apprentices(apprentices)
    elif choice == "Sauvegarder":
        save_manager(apprentices)
    elif choice == "Paramètres":
        settings()
    elif choice == "Mode avancé" or choice == "Mode basique":
        options_descriptions, advanced_mode = switch_mode(advanced_mode)
    else:
        quit_program()
        should_continue = False

    return should_continue, apprentices, options_descriptions, advanced_mode

def update_options(options_descriptions):
    """
    
    Met à jour les options disponibles pour l'utilisateur

    Args :
        - options_descriptions (dict[str, str]) : liste des (options + descriptions) disponibles pour l'utilisateur
    
    """

    options = list(options_descriptions.keys())

    return options
