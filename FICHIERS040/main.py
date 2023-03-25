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
                            "Setup rapide": "[IN DEVELOPMENT] Option rapide pour générer des apprentis + sauvegarder les données. Vous pouvez définir les variables dans l'onglet Paramètres.",
                            "Lister": "Liste les apprentis par block de x. Vous pouvez choisir x.",
                            "Sauvegarder": "Sauvegarde les données des apprentis dans un fichier csv nommé par vous.",
                            "Paramètres": "Quelques paramètres modifiables",
                            "Quitter": "Permet à l'utilisateur de quitter le programme."}

    options = list(options_descriptions.keys())
    
    should_continue = True
    apprentices = None  # Initialement vide

    show_introduction()

    while should_continue:
        show_menu(options)

        user_option = get_user_option(options)

        should_continue, apprentices = check_user_option(
            user_option, options, apprentices, options_descriptions)


if __name__ == '__main__':
    main()
