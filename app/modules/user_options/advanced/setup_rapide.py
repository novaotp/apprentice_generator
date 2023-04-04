import os
import modules.user_options.basic.generer as generer
import modules.user_options.basic.sauvegarder as sauvegarder
import modules.common.config as config
import modules.common.utils as utils

def fast_setup():
    """

    Setup rapide pour générer une liste d'apprentis + sauvegarder les données dans un fichier

    Les paramètres se trouvent dans le fichier app.conf

    Return :
        - apprentices (list[str]) : liste des apprentis générés

    """

    configs = config.read_config()

    fast_setup_apprentice_generation_count = config.get_config_value("fast_setup_apprentice_generation_count")
    fast_setup_filename = config.get_config_value("fast_setup_filename")
    fast_setup_should_overwrite = config.get_config_value("fast_setup_should_overwrite")
    csv_folder = config.get_config_value("csv_folder")
    
    utils.create_folder_if_not_exists(csv_folder)

    apprentices = generer.generate_apprentices(fast_setup_apprentice_generation_count, show_message=False)

    sauvegarder.save_data(apprentices, fast_setup_filename, fast_setup_should_overwrite, path=csv_folder, show_message=False)

    return apprentices