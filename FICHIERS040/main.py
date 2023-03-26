#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
#           EPTM - Ecole professionnelle technique et des métiers
#
# Nom du projet / nom du module      : [Insert project name here]
# Nom du fichier source              : fichier040.py
#
# Auteur (Nom, Prénom)               : Rahman Sajidur
# Classe                             : EM-IN 1B
# Module                             : PR_PROG
# Date de création                   : 22.03.2023
#
# Description succincte du programme :
#   [Insert text here]
# ----------------------------------------------------------------------------

from modules.introduction import *
from modules.menu import *
from modules.options import *

def main():
    """

    Programme principal

    """

    options_descriptions = {"Description": "Décrit l'utilité du programme et ce que vous pouvez faire.",
                            "Générer": "Génère des apprentis. Vous pouvez définir la quantité.",
                            "Lister": "Liste les apprentis par block de x. Vous pouvez choisir x.",
                            "Sauvegarder": "Sauvegarde les données des apprentis dans un fichier csv nommé par vous.",
                            "Quitter": "Permet à l'utilisateur de quitter le programme.",
                            "Mode avancé": "Passer au mode avancé."}
    
    should_continue = True
    advanced_mode = get_config_value("default_advanced_mode")
    apprentices = None  # Initialement vide

    show_introduction()

    while should_continue:
        options = update_options(options_descriptions)

        show_menu(options, advanced_mode)

        user_option = get_user_option(options)

        should_continue, apprentices, options_descriptions, advanced_mode = check_user_option(
            user_option, options, apprentices, options_descriptions, advanced_mode)


if __name__ == '__main__':
    main()
