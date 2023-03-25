from modules.utils import *
from modules.user_options.description import *
from modules.user_options.generer import *
from modules.user_options.setup_rapide import *
from modules.user_options.lister import *
from modules.user_options.parametres import *
from modules.user_options.quitter import *
from modules.user_options.sauvegarder import *


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

    user_option = to_valid_positive_integer(prompt, error_message, 1, len(options))

    return user_option


def check_user_option(user_option, options, apprentices, options_descriptions):
    """

    Dirige l'utilisateur vers la fonction choisie

    Args :
        - user_option (int) : choix de l'utilisateur
        - options (list[str]) : liste des options disponibles pour l'utilisateur
        - apprentices (list[str]) : liste des apprentis
        - options_descriptions (dict[str, str]) : liste des (options + descriptions) disponibles pour l'utilisateur
        - fast_setup_apprentice_generation_count (int) : [RAPIDE] nombre d'apprentis à générer par défaut
        - fast_setup_filename (str) : [RAPIDE] nom du fichier par défaut
        - fast_setup_should_overwrite (bool) : [RAPIDE] écraser le fichier sans demander ou pas

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
        clear_terminal()

        if apprentices == None:
            print("================== ENREGISTREMENT DES DONNÉES ==================")
            print()
            print("Vous devez générer une liste d'apprentis (option 2) avant d'enregistrer les apprentis dans un fichier !")
            input("Appuyer sur un bouton pour continuer : ")
        else:
            filename = get_save_filename()
            should_overwrite = True

            if os.path.isfile(f"./tests/{filename}.csv"):
                should_overwrite = should_overwrite_file()

            save_data(apprentices, filename, should_overwrite)
    elif choice == "Paramètres":
        show_settings(fast_setup_apprentice_generation_count,
                      fast_setup_filename, fast_setup_should_overwrite)
    else:
        quit_program()
        should_continue = False

    return should_continue, apprentices
