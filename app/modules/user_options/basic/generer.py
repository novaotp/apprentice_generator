import random
import tqdm
import itertools

import modules.common.utils as utils
import modules.common.config as config

def get_random_last_name(filename="./src/assets/csv_files/noms.csv"):
    """

    Retourne un nom aléatoire depuis un fichier source

    Args :
        - filename (str) : fichier source (avec encodage utf-8) contenant les noms

    Return :
        - last_name (str) : nom aléatoire généré

    """

    filename = utils.try_default_file(filename, "./app/assets/csv_files/noms.csv", "System error : noms.csv not found")

    with open(file=filename, mode='r', encoding='utf-8') as source_file:
        last_names = source_file.readlines()

    last_name = random.choice(last_names).rstrip('\n')

    return last_name


def get_random_first_name(filename="./src/assets/csv_files/prenoms.csv"):
    """

    Retourne un prénom aléatoire depuis un fichier source

    Args :
        - filename (str) : fichier source (avec encodage utf-8) contenant les prénoms

    Return :
        - first_name (str) : prénom aléatoire généré

    """

    filename = utils.try_default_file(filename, "./app/assets/csv_files/prenoms.csv", "System error : prenoms.csv not found")

    with open(file=filename, mode='r', encoding='utf-8') as source_file:
        first_names = source_file.readlines()

    first_name = random.choice(first_names).rstrip('\n')

    return first_name


def get_random_location(only_valais, filename="./src/assets/csv_files/localites_suisses.csv"):
    """

    Retourne un npa + une localité aléatoirement depuis un fichier source

    Args :
        - filename (str) : fichier source (avec encodage utf-8) contenant les localités

    Return :
        - npa (int) : npa aléatoire généré
        - locality (str) : localité correspondant au npa

    """

    filename = utils.try_default_file(filename, "./app/assets/csv_files/localites_suisses.csv", "System error : localites_suisses.csv not found")

    with open(file=filename, mode='r', encoding='utf-8') as source_file:
        localities = source_file.readlines()

    localities.pop(0)

    if only_valais:
        is_location_valid = False

        while not is_location_valid:
            complete_locality = random.choice(localities).rstrip('\n')

            idx, npa, locality = complete_locality.split(';')

            # Check if npa is valid
            npa = int(npa)
            if (npa >= 1868 and npa <= 1997) or (npa >= 3900 and npa <= 3999): # Source des npa : https://fr.wikipedia.org/wiki/Num%C3%A9ro_postal_d%27acheminement
                is_location_valid = True
    else:
        complete_locality = random.choice(localities).rstrip('\n')

        idx, npa, locality = complete_locality.split(';')

    return npa, locality

def get_last_names(filename="./src/assets/csv_files/noms.csv"):
    """

    Retourne la liste de noms depuis un fichier source

    Args :
        - filename (str) : fichier source (avec encodage utf-8) contenant les noms

    Return :
        - last_name (str) : nom aléatoire généré

    """

    filename = utils.try_default_file(filename, "./app/assets/csv_files/noms.csv", "System error : noms.csv not found")

    with open(file=filename, mode='r', encoding='utf-8') as source_file:
        last_names = source_file.readlines()

    return last_names


def get_first_names(filename="./src/assets/csv_files/prenoms.csv"):
    """

    Retourne un prénom aléatoire depuis un fichier source

    Args :
        - filename (str) : fichier source (avec encodage utf-8) contenant les prénoms

    Return :
        - first_name (str) : prénom aléatoire généré

    """

    filename = utils.try_default_file(filename, "./app/assets/csv_files/prenoms.csv", "System error : prenoms.csv not found")

    with open(file=filename, mode='r', encoding='utf-8') as source_file:
        first_names = source_file.readlines()

    return first_names

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

    utils.clear_terminal()

    no_duplicates = config.get_config_value("no_duplicates")
    max_apprentice_without_duplicates = utils.get_max_combinations()

    print("================== GÉNÉRATION - DÉBUT ==================")
    print()

    min_apprentice_count = config.get_config_value("min_apprentice_count")
    max_apprentice_count = config.get_config_value("max_apprentice_count")

    is_not_valid = True

    while is_not_valid:
        prompt = f"Entrer le nombre d'apprentis à générer (entre {min_apprentice_count} et {max_apprentice_count}) : "

        apprentice_count = utils.to_valid_positive_integer(prompt, min_apprentice_count, max_apprentice_count)

        if no_duplicates and apprentice_count > max_apprentice_without_duplicates:
            print(f"Génération impossible : sans duplication, la génération se limite à {max_apprentice_without_duplicates}")
            print(f"Désactivez la duplication dans les paramètres si vous souhaitez en générer plus")
        else:
            is_not_valid = False

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

    utils.clear_terminal()

    apprentices = []

    no_duplicates = config.get_config_value("no_duplicates")
    only_valais = config.get_config_value("only_valais")

    print("================== GÉNÉRATION - EN COURS ==================")
    print()

    show_warnings(no_duplicates, only_valais)

    print()

    with tqdm.tqdm(total=apprentice_count) as progress_bar: # Cette ligne permet d'afficher une barre de progression lors de la génération des apprentis
        if no_duplicates:
            generate_unique_apprentices(apprentice_count, apprentices, only_valais, progress_bar)
        else:
            generate_generic_apprentices(apprentice_count, apprentices, only_valais, progress_bar)

    if show_message:
        show_success_message()
        
    input("Appuyer sur un bouton pour revenir au menu principal : ")

    return apprentices

def generate_unique_apprentices(apprentice_count, apprentices, only_valais, progress_bar):
    """
    
    Génère une liste d'apprentis avec une paire de (prénom + nom) unique

    Args :
        - apprentice_count (int) : nombre d'apprentis à générer
        - apprentices (list[str]) : liste d'apprentis générée
        - only_valais (bool) : génère uniquement les apprentis avec une localité valaisanne ou non
    
    """

    first_names = get_first_names()
    last_names = get_last_names()
    combined_names = set(itertools.product(first_names, last_names)) # Cette ligne permet de générer une liste de paires (prénom + nom) unique. Utile également pour accélérer le processus en pré-générant la liste.

    while len(apprentices) < apprentice_count and combined_names:
        combined_name = combined_names.pop()
        first_name, last_name = [name.rstrip('\n') for name in combined_name]
        npa, locality = get_random_location(only_valais)

        apprentice = assemble_apprentice(first_name, last_name, npa, locality)
        apprentices.append(apprentice)

        progress_bar.update(1)

def generate_generic_apprentices(apprentice_count, apprentices, only_valais, progress_bar):
    """
    
    Génère une liste d'apprentis avec une paire de (prénom + nom) unique

    Args :
        - apprentice_count (int) : nombre d'apprentis à générer
        - apprentices (list[str]) : liste d'apprentis générée
        - only_valais (bool) : génère uniquement les apprentis avec une localité valaisanne ou non
    
    """

    while len(apprentices) < apprentice_count:
        first_name = get_random_first_name()
        last_name = get_random_last_name()
        npa, locality = get_random_location(only_valais)

        apprentice = assemble_apprentice(first_name, last_name, npa, locality)

        apprentices.append(apprentice)
            
        progress_bar.update(1)

def show_success_message():
    """
    
    Affiche un message si la génération est effectuée avec succès
    
    """

    utils.clear_terminal()

    print("================== GÉNÉRATION TERMINÉE ==================")
    print()
    print("Votre liste d'apprentis à été généré avec succès !")
    print()

def show_warnings(no_duplicates, only_valais):
    """
    
    Affiche des messages d'avertissement par rapport aux paramètres actuels

    Args :
        - no_duplicates (bool) : affiche un message lié aux doublons des apprentis
        - only_valais (bool) : affiche un message lié à la localité des apprentis
    
    """

    if no_duplicates:
        print("INFO : La génération risque de prendre plus de temps car les doublons ne sont pas générés")
    else:
        print("INFO : La génération risque de contenir des doublons")

    if only_valais:
        print("INFO : Les localités seront uniquement valaisannes")
    else:
        print("INFO : Les localités ne seront pas uniquement valaisannes")