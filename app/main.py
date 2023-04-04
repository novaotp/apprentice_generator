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

import modules.introduction as introduction
import modules.menu as menu
import modules.options as mod_options
import modules.common.config as config
import modules.user_options.advanced.mode as mode

def main():
    """

    Programme principal

    """
    
    should_continue = True
    apprentices = None  # Initialement vide

    try:
        options_descriptions, advanced_mode = mode.switch_mode(advanced_mode=config.get_config_value("default_basic_mode"))
    except:
        config.restore_config() # Tenter de restaurer le fichier de configuration
        options_descriptions, advanced_mode = mode.switch_mode(advanced_mode=config.get_config_value("default_basic_mode"))

    introduction.show_introduction()

    while should_continue:
        print(options_descriptions)
        options = mod_options.update_options(options_descriptions)

        menu.show_menu(options, advanced_mode)

        user_option = mod_options.get_user_option(options)

        should_continue, apprentices, options_descriptions, advanced_mode = mod_options.check_user_option(
            user_option, options, apprentices, options_descriptions, advanced_mode)


if __name__ == '__main__':
    main()
