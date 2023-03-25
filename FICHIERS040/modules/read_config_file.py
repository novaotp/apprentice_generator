def read_config(config_file="./config/app.conf"):
    """
    
    Lis le fichier de configuration de l'application (DEVTOOLS)

    Args :
        - config_file (str) : nom du fichier de configuration

    Return :
        - config_lines (dict) : dictionnaire des paramètres de l'application

    """

    with open(file=config_file, mode="r", encoding='utf-8') as cfg_file:
        lines = cfg_file.readlines()

    config_lines = {}

    for line in lines:
        line =  line.removesuffix('\n')
        key, value = line.split(";")
        config_lines[key] = value

    return config_lines