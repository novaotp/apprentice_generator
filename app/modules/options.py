import modules.common.utils as utils

import modules.user_options.basic.description as description
import modules.user_options.basic.generer as generer
import modules.user_options.basic.lister as lister
import modules.user_options.basic.quitter as quitter
import modules.user_options.basic.sauvegarder as sauvegarder

import modules.user_options.advanced.parametres as parametres
import modules.user_options.advanced.setup_rapide as setup_rapide
import modules.user_options.advanced.mode as mode


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

    user_option = utils.to_valid_positive_integer(prompt, 1, len(options))

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
        description.show_description(options_descriptions)
    elif choice == "Générer":
        apprentice_count = generer.get_apprentice_count()
        apprentices = generer.generate_apprentices(apprentice_count)
    elif choice == "Setup rapide":
        apprentices = setup_rapide.fast_setup()
    elif choice == "Lister":
        lister.list_apprentices(apprentices)
    elif choice == "Sauvegarder":
        sauvegarder.save_manager(apprentices)
    elif choice == "Paramètres":
        parametres.settings()
    elif choice == "Mode avancé" or choice == "Mode basique":
        options_descriptions, advanced_mode = mode.switch_mode(advanced_mode)
    else:
        quitter.quit_program()
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
