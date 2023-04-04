import modules.common.utils as utils
import modules.common.config as config

def settings():
    """

    Ouvre le menu de configuration des paramètres de l'application.

    """

    stop_showing_settings = False

    while not stop_showing_settings:
        utils.clear_terminal()

        configs = config.read_config()
        keys = list(configs.keys())

        show_settings(configs, keys)
        
        print()
        min_option = 1
        max_option = len(keys) + 1
        prompt = "Veuillez choisir une option : "

        option = utils.to_valid_positive_integer(prompt, min_option, max_option)

        if option == 13:
            stop_showing_settings = True
        else:
            check_user_setting_option(configs, keys, option)

    # Add logic later

def check_user_setting_option(configs, keys, option):
    """
    
    Vérifie le choix de l'utilisateur

    Args :
        - configs (dict[str, str | int | bool]) : le dictionnaire de configuration
        - keys (list[str]) : liste des clés
        - option (int) : n° du choix de l'utilisateur
    
    """

    choice = keys[option - 1]
    metadata = config.get_config_metadata(choice)
    value = metadata.get("value")
    
    value_type = metadata.get("type")

    utils.clear_terminal()

    print("============================ PARAMÈTRES SYSTÈME - MODIFICATION EN COURS ============================")
    print()

    new_value = get_new_value(choice, value, value_type)

    confirm_change = confirm_change_parameter(choice, value, new_value)

    if confirm_change == 'r':
        check_user_setting_option(configs, keys, option)
    else:
        is_successful = False

        if confirm_change == 'y':
            config.update_config(choice, new_value)
            is_successful = True
            
        show_change_status(is_successful, choice, value, new_value)

def get_new_value(choice, old_value, value_type):
    """
    
    Demande la nouvelle valeur à l'utilisateur avec un système de type checking pour éviter les erreurs de types

    Args :
        - choice (str) : clé correspondante au choix de l'utilisateur
        - old_value (str | int | bool) : la valeur actuelle à modifier
        - value_type (str) : type de valeur d'old_value et de la nouvelle valeur

    Return :
        - new_value (str | int | bool) : nouvelle valeur pour le paramètre 
    
    """

    type_map = utils.get_type_map()
    mapped_type = type_map[value_type]

    is_good_input = False

    while not is_good_input:
        new_value = input(f"Entrez une nouvelle valeur pour {choice} (valeur actuelle : {old_value}) : ")

        try:
            new_value = mapped_type(new_value)
        except Exception as e:
            print(f"Valeur invalide : la nouvelle valeur doit être de type <{value_type}>")
            continue

        is_good_input = True

    return new_value

def confirm_change_parameter(choice, old_value, new_value):
    """
    
    Confirme le changement de valeur du paramètre ou non

    Args :
        - choice (str) : clé correspondante au choix de l'utilisateur
        - old_value (str | int | bool) : la valeur actuelle à modifier
        - new_value (str | int | bool) : la nouvelle valeur pour remplacer old_value

    Return :
        - confirm_change (str) : si l'utilisateur confirme le changement ou non
    
    """

    is_change_confirmed = False

    utils.clear_terminal()

    print("============================ PARAMÈTRES SYSTÈME - CONFIRMATION ============================")
    print()

    while not is_change_confirmed:
        print(f"Modification de {choice}")
        print()
        print(f"\tAncienne valeur : {old_value} | Nouvelle valeur : {new_value}")
        print()
        print(f"Confirmer la modification ? ")
        print()
        print("\ty : confirmer")
        print("\tn : annuler")
        print("\tr : recommencer")
        print()

        confirm_change = input("Voitre choix : ")

        if confirm_change not in ['y', 'n', 'r']:
            print("Choix invalide... Choisissez entre 'y', 'n' et 'r'")
            continue

        is_change_confirmed = True

    return confirm_change

def show_change_status(is_successful, choice, old_value, new_value):
    """
    
    Affiche le statut du changement (réussite ou échec) dans le terminal

    Args :
        - is_successful (bool) : réussite ou non du changement
    
    """

    message = f"Échec... Confirmez les changements apportés pour modifier les paramètres !"

    if is_successful:
        message = f"Réussite ! Modifié {choice} de <{old_value}> à <{new_value}> !"

    utils.clear_terminal()

    print("================== PARAMÈTRES SYSTÈME - MODIFICATION TERMINÉE ==================")
    print()

    print(message)

    print()
    input("Appuyer sur un bouton pour revenir au menu principal : ")

def show_settings(configs, keys):
    """
    
    Affiche tous les paramètres modifiables à l'utilisateur.

    Args :
        - configs (dict) : dictionnaire contenant tous les paramètres modifiables de l'application
        - keys (list[str]) : liste des clés
    
    """

    print("============================ PARAMÈTRES SYSTÈME - PREVIEW ============================")
    print()

    category = configs.get(keys[0]).get("category")
    last_idx = len(keys) + 1

    for idx, key in enumerate(keys, 1):
        metadata = config.get_config_metadata(key)

        value = metadata.get("value")
        new_category = metadata.get("category")
        description = metadata.get("description")

        if category != new_category:
            print()
        
        category = new_category

        print(f"\t{idx:2}. [{category}] - {description} : {value}")

    print()
    print(f"\t{last_idx:2}. [quitter] - Retourner au menu principal")