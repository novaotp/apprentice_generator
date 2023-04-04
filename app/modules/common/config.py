import sys
import modules.common.utils as utils


def read_config(config_file="./src/config/app.conf"):
    """

    Lis le fichier de configuration de l'application (DEVTOOLS)

    Args :
        - config_file (str) : nom du fichier de configuration

    Return :
        - config_lines (dict[str, str]) : dictionnaire des paramètres de l'application

    """

    config_file = utils.try_default_file(
        config_file, "./app/config/app.conf", "System error : missing or invalid config file")

    with open(file=config_file, mode="r", encoding='utf-8') as cfg_file:
        lines = cfg_file.readlines()

    config_lines = config_data(lines)

    if any(value is None for value in config_lines.values()):
        sys.exit("System error : missing or incorrect config values in app.conf")

    return config_lines


def config_data(lines):
    config_lines = {}
    type_map = utils.get_type_map()

    try:
        for line in lines:
            line = line.rstrip('\n')
            category, key, description, value_type, value = line.split(";")

            mapped_type = type_map[value_type]

            config_lines[key] = {"value": mapped_type(
                value), "category": category, "description": description, "type": value_type}
    except Exception as e:
        print(e)
        sys.exit("Missing or incorrect config file")

    return config_lines


def update_config(key, new_value, config_file="./src/config/app.conf"):
    """
    
    Met à jour le fichier de configuration de l'application

    Args :
        - key (str) : clé du paramètre à mettre à jour
        - new_value (str) : nouvelle valeur de la clé
        - config_file (str) : nom du fichier de configuration
    
    """

    config_file = utils.try_default_file(
        config_file, "./app/config/app.conf", "System error : missing or invalid config file")

    with open(config_file, 'r') as cfg_file:
        lines = cfg_file.readlines()

    substitute_config_line(key, lines, new_value)

    # Write the updated list back to the config file
    with open(config_file, 'w') as f:
        f.writelines(lines)


def substitute_config_line(key, lines, new_value):
    """
    
    Remplace l'ancienne valeur de la configuration de l'application par la nouvelle valeur

    Modification de la liste "lines"

    Args :
        - key (str) : clé pour récupérer la valeur
        - lines (list[str]) : liste des lignes de configuration
        - new_value (str) : nouvelle valeur de la clé
    
    """

    for i, line in enumerate(lines):
        category, old_key, description, value_type, old_value = line.split(";")

        if key == old_key:
            # Replace the line with the new value
            lines[i] = assemble_config_line(
                category, old_key, description, value_type, new_value)

def assemble_config_line(category, key, description, type, value):
    """
    
    Assemble des valeurs pour former une nouvelle ligne de configuration

    Args :
        - category (str) : catégorie du paramètre
        - key (str) : nom de clé du paramètre
        - description (str) : description du paramètre
        - type (str) : type du paramètre
        - value (str | int | bool) : valeur du paramètre
    
    """

    config_line = f'{category};{key};{description};{type};{value}\n'

    return config_line


def get_config_value(key):
    """

    Retourne la valeur correspondante à la clé dans le fichier de configuration

    Args :
        - key (str) : clé pour récupérer la valeur

    Return :
        - value (str | int | bool) : valeur de la clé

    """

    configs = read_config()

    value = configs.get(key).get("value")

    return value


def get_config_metadata(key):
    """

    Retourne les métadonnées de la clé dans le fichier de configuration

    Args :
        - key (str) : clé pour récupérer la valeur

    Return :
        - metadata (dict[str, str | int | bool]) : métadonnées de la clé

    """

    configs = read_config()

    metadata = configs.get(key)

    return metadata


def restore_config(config_file="./src/config/"):
    """
    
    Restaure le fichier de configuration de l'application

    Args :
        - config_file (str) : nom du fichier de configuration
    
    """

    config_file = utils.try_default_file(
        config_file, "./app/config/", "System error : missing or invalid config file")

    lines = ["fs;fast_setup_apprentice_generation_count;Nombre d'apprentis générés;int;20000\n",
             "fs;fast_setup_filename;Nom du fichier (sans extension);str;fs_auto\n",
             "fs;fast_setup_should_overwrite;Écraser automatiquement;bool;True\n",
             "strict;only_valais;Générer des apprentis avec des localités uniquement valaisannes;bool;True\n",
             "strict;no_duplicates;Générer des apprentis avec une paire (nom, prénom) unique;bool;True\n",
             "storage;csv_folder;Dossier de sauvegarde des fichiers .csv;str;./tests\n",
             "limit;min_apprentice_count;Nombre minimum d'apprentis;int;1\n",
             "limit;max_apprentice_count;Nombre maximum d'apprentis;int;31374\n",
             "limit;min_apprentice_per_block;Nombre minimum d'apprentis par bloc;int;1\n",
             "limit;max_apprentice_per_block;Nombre maximum d'apprentis par bloc;int;5000\n",
             "default;default_basic_mode;Activer le mode basique par défaut;bool;True\n",
             "default;default_filename;Nom du fichier par défaut (si nom du fichier vide);str;auto"]

    with open(file=f"{config_file}/app.conf", mode='w+', encoding="utf-8") as cfg_file:
        for line in lines:
            cfg_file.write(line)
