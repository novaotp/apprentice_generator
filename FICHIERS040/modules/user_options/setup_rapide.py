import os
from modules.user_options.generer import *
from modules.user_options.sauvegarder import *
from modules.read_config_file import *

def fast_setup():
    """

    Setup rapide pour générer une liste d'apprentis + sauvegarder les données dans un fichier

    """

    configs = read_config()

    fast_setup_apprentice_generation_count = configs.get("fast_setup_apprentice_generation_count")
    fast_setup_filename = configs.get("fast_setup_filename")
    fast_setup_should_overwrite = configs.get("fast_setup_should_overwrite")

    csv_folder = configs.get("csv_folder")

    if fast_setup_apprentice_generation_count is None or fast_setup_filename is None or fast_setup_should_overwrite is None or csv_folder is None:
        sys.exit("System error : missing or incorrect config values")

    try:
        fast_setup_apprentice_generation_count = int(fast_setup_apprentice_generation_count)
    except:
        sys.exit("System error : missing or incorrect config values")

    if not os.path.isdir(csv_folder):
        os.mkdir(csv_folder)

    apprentices = generate_apprentices(fast_setup_apprentice_generation_count, show_message=False)

    save_data(apprentices, fast_setup_filename, fast_setup_should_overwrite, path=csv_folder, show_message=False)