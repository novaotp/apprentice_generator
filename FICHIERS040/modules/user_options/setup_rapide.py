import os
from modules.user_options.generer import *
from modules.user_options.sauvegarder import *
from modules.config import *

def fast_setup():
    """

    Setup rapide pour générer une liste d'apprentis + sauvegarder les données dans un fichier

    Les paramètres se trouvent dans le fichier app.conf

    """

    configs = read_config()

    fast_setup_apprentice_generation_count = get_config_value("fast_setup_apprentice_generation_count")
    fast_setup_filename = get_config_value("fast_setup_filename")
    fast_setup_should_overwrite = get_config_value("fast_setup_should_overwrite")
    csv_folder = get_config_value("csv_folder")
    
    create_folder_if_not_exists(csv_folder)

    apprentices = generate_apprentices(fast_setup_apprentice_generation_count, show_message=False)

    save_data(apprentices, fast_setup_filename, fast_setup_should_overwrite, path=csv_folder, show_message=False)