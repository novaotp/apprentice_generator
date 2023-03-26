def activate_advanced_mode():
    """
    
    Retourne les options pour le mode avancé.
    
    """

    advanced_options_descriptions = {"Description": "Décrit l'utilité du programme et ce que vous pouvez faire.",
                                        "Générer": "Génère des apprentis. Vous pouvez définir la quantité.",
                                        "Lister": "Liste les apprentis par block de x. Vous pouvez choisir x.",
                                        "Sauvegarder": "Sauvegarde les données des apprentis dans un fichier csv nommé par vous.",
                                        "Quitter": "Permet à l'utilisateur de quitter le programme.",
                                        "Setup rapide": "[IN DEVELOPMENT] Option rapide pour générer des apprentis + sauvegarder les données. Vous pouvez définir les variables dans l'onglet Paramètres.",
                                        "Paramètres": "Quelques paramètres modifiables.",
                                        "Mode basique": "Passer au mode basique."}

    return advanced_options_descriptions

def deactivate_advanced_mode():
    """
    
    Retourne les options pour le mode basique.
    
    """

    options_descriptions = {"Description": "Décrit l'utilité du programme et ce que vous pouvez faire.",
                            "Générer": "Génère des apprentis. Vous pouvez définir la quantité.",
                            "Lister": "Liste les apprentis par block de x. Vous pouvez choisir x.",
                            "Sauvegarder": "Sauvegarde les données des apprentis dans un fichier csv nommé par vous.",
                            "Quitter": "Permet à l'utilisateur de quitter le programme.",
                            "Mode avancé": "Passer au mode avancé."}

    return options_descriptions

def switch_mode(advanced_mode):
    """
    
    Switch le mode actuel à l'autre mode.

    Args :
        - advanced_mode (bool): True si le mode avancé est activé, False sinon.
    
    """

    if advanced_mode:
        options_descriptions = deactivate_advanced_mode()
        advanced_mode = False
    else:
        options_descriptions = activate_advanced_mode()
        advanced_mode = True
    
    return options_descriptions, advanced_mode

