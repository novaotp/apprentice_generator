import os
from modules.utils import *


def get_save_filename():
    """

    Demande à l'utilisateur le nom du fichier à enregistrer (sans l'extension)

    Return :
        - filename (str) : nom du fichier

    """

    clear_terminal()

    print("================== ENREGISTREMENT DES DONNÉES - DÉBUT ==================")
    print()

    filename = input(
        "Entrez le nom du fichier dans lequel enregistrer vos données (sans extension) : ")

    return filename


def should_overwrite_file():
    """

    Vérifie si un fichier existe déjà

    Args :
        - filename (str) : nom du fichier

    Return :
        - should_overwrite (bool) : écraser le fichier ou non

    """

    should_overwrite = False
    is_valid_input = False

    while not is_valid_input:
        should_overwrite = input(
            "Ce fichier existe déjà... Écraser le fichier (y/n) ? ")

        if should_overwrite != 'y' and should_overwrite != 'n':
            print("Choix invalide...")
            continue

        is_valid_input = True

    if should_overwrite == 'n':
        should_overwrite = False

    return should_overwrite


def save_data(apprentices, filename, should_overwrite, path="./tests", show_message=True):
    """

    Enregistre les données des apprentis dans un fichier .csv

    Args :
        - apprentices (list[str]) : liste des apprentis
        - filename (str) : nom du fichier dans lequel sauvegarder les données des apprentis
        - should_overwrite (bool) : écraser le fichier ou non
        - path (str) : chemin du dossier
            - par défaut : ./tests
        - show_message (bool) : afficher le message de fin (mettre False uniquement pour setup rapide)

    """

    clear_terminal()

    is_successful = True

    if should_overwrite:
        write_file(path, filename, apprentices)
    else:
        is_successful = False

    if show_message:
        print()
        show_write_status(is_successful)
        print()
        input("Appuyer sur un bouton pour revenir au menu principal : ")


def show_write_status(is_successful):
    """

    Affiche le status de l'écriture dans un terminal

    Args :
        - is_successful (bool) : réussite ou échec de l'écriture

    """

    clear_terminal()

    print("================== ENREGISTREMENT DES DONNÉES - TERMINÉ ==================")
    print()

    if is_successful:
        message = "Réussite ! Votre fichier se trouve dans le dossier <tests>."
    else:
        message = "Échec... Choisissez un autre nom..."

    print(message)


def write_file(path, filename, apprentices):
    """

    Écrit les données des apprentis dans un fichier

    Args :
        - path (str) : chemin du dossier
        - filename (str) : fichier dans lequel écrire
        - apprentices (list[str]) : liste des apprentis

    """

    with open(file=f"{path}/{filename}.csv", mode='w+', encoding='utf-8') as destination_file:
        destination_file.write("Prénom;Nom;Npa;Localité\n")

        for apprentice in apprentices:
            destination_file.write(f"{apprentice}\n")

def save_manager(apprentices):
    clear_terminal()

    if not empty_apprentice_list(apprentices):
        filename = get_save_filename()
        should_overwrite = True

        if os.path.isfile(f"./tests/{filename}.csv"):
            should_overwrite = should_overwrite_file()

        save_data(apprentices, filename, should_overwrite)