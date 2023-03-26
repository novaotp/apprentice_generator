import random
from modules.utils import *
from modules.config import *

def get_random_last_name(filename="./src/csv_files/noms.csv"):
    """

    Retourne un nom aléatoire depuis un fichier source

    Args :
        - filename (str) : fichier source (avec encodage utf-8) contenant les noms
            - par défaut : "./csv_files/noms.csv"

    Return :
        - last_name (str) : nom aléatoire généré

    """

    with open(file=filename, mode='r', encoding='utf-8') as source_file:
        last_names = source_file.readlines()

    last_name = random.choice(last_names).removesuffix('\n')

    return last_name


def get_random_first_name(filename="./src/csv_files/prenoms.csv"):
    """

    Retourne un prénom aléatoire depuis un fichier source

    Args :
        - filename (str) : fichier source (avec encodage utf-8) contenant les prénoms
            - par défaut : "./csv_files/prenoms.csv"

    Return :
        - first_name (str) : prénom aléatoire généré

    """

    with open(file=filename, mode='r', encoding='utf-8') as source_file:
        first_names = source_file.readlines()

    first_name = random.choice(first_names).removesuffix('\n')

    return first_name


def get_random_location_valais(filename="./src/csv_files/localites_suisses.csv"):
    """

    Retourne un npa + une localité aléatoirement depuis un fichier source

    Args :
        - filename (str) : fichier source (avec encodage utf-8) contenant les localités
            - par défaut : "./csv_files/localites_suisses.csv"

    Return :
        - npa (int) : npa aléatoire généré
        - locality (str) : localité correspondant au npa

    """

    # Localités valaisannes : TODO

    npa = 0  # Initialisé à 0

    with open(file=filename, mode='r', encoding='utf-8') as source_file:
        localities = source_file.readlines()

    complete_locality = random.choice(localities).removesuffix('\n')

    idx, npa, locality = complete_locality.split(';')

    return npa, locality


def assemble_apprentice(first_name, last_name, npa, locality):
    """

    Assemble et retourne un apprenti avec un nom, un prénom, un npa et une localité

    Args :
        - first_name (str) : prénom
        - last_name (str) : nom
        - npa (int) : npa
        - locality (str) : localité

    Return :
        - apprentice (str) : chaîne de caractères contenant le nom, prénom, npa et localité d'un apprenti

    """

    apprentice = f"{first_name};{last_name};{npa};{locality}"

    return apprentice



def get_apprentice_count():
    """

    Demande à l'utilisateur le nombre d'apprentis à générer

    Return :
        - apprentice_count (int) : nombre d'apprentis à générer

    """

    clear_terminal()

    print("================== GÉNÉRATION - DÉBUT ==================")
    print()

    min_apprentice_count = get_config_value("min_apprentice_count")
    max_apprentice_count = get_config_value("max_apprentice_count")
    prompt = "Entrer le nombre d'apprentis à générer : "

    apprentice_count = to_valid_positive_integer(prompt, min_apprentice_count, max_apprentice_count)

    return apprentice_count


def generate_apprentices(apprentice_count, show_message=True):
    """

    Génère une liste d'apprentis

    Args :
        - apprentice_count (int) : nombre d'apprentis à générer
        - show_message (bool) : affiche le message de fin (mettre False uniquement pour setup rapide)

    Return :
        - apprentices (list[str]) : liste d'apprentis générée

    """

    clear_terminal()

    apprentices = []

    for num in range(apprentice_count):
        first_name = get_random_first_name()
        last_name = get_random_last_name()
        npa, locality = get_random_location_valais()

        apprentice = assemble_apprentice(first_name, last_name, npa, locality)

        apprentices.append(apprentice)

    if show_message:
        print("================== GÉNÉRATION TERMINÉE ==================")
        print()
        print("Votre liste d'apprentis à été généré avec succès !")
        print()
        input("Appuyer sur un bouton pour revenir au menu principal : ")

    return apprentices

