import os
import sys


def read_config(config_file="./config/app.conf"):
    """
    
    Lis le fichier de configuration de l'application (DEVTOOLS)

    Args :
        - config_file (str) : nom du fichier de configuration

    Return :
        - config_lines (dict[str, str]) : dictionnaire des paramètres de l'application

    """

    if not os.path.isfile(config_file):
        sys.exit("app.conf not found in the config directory")

    with open(file=config_file, mode="r", encoding='utf-8') as cfg_file:
        lines = cfg_file.readlines()

    config_lines = {}
    type_map = {
        "int": int,
        "float": float,
        "bool": lambda x: x.lower() == "true",
        "str": str
    }

    try:
        for line in lines:
            line =  line.removesuffix('\n')
            key, value_type, value = line.split(";")

            mapped_type = type_map[value_type]

            config_lines[key] = mapped_type(value)
    except Exception as e:
        print(e)
        sys.exit("Missing or incorrect config file")

    if any(value is None for value in config_lines.values()):
        sys.exit("System error : missing or incorrect config values in app.conf")

    return config_lines

def get_config_value(key, config_file="./config/app.conf"):
    """
    
    Retourne la valeur correspondante à la clé dans le fichier de configuration

    Args :
        - key (str) : clé pour récupérer la valeur
        - config_file (str) : nom du fichier de configuration

    Return :
        - value (str | int| bool) : valeur recherchée
    
    """

    configs = read_config(config_file)

    value = configs.get(key)

    return value