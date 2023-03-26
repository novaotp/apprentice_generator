import os
import sys


def clear_terminal():
    """
    
    Vide le terminal
    
    """

    os.system('cls' if sys.platform == "win32" else 'clear')

def is_between(value, lower_bound, upper_bound):
    """

    Vérifie si la valeur est entre deux valeurs

    Args :
        - value (int) : la valeur à vérifier
        - lower_bound (int) : la valeur de début
        - upper_bound (int) : la valeur de fin

    Return :
        - is_between (bool) : True si la valeur est entre les deux valeurs, False sinon

    """

    is_between = False

    if not (value < lower_bound or value > upper_bound):
        is_between = True

    return is_between

def to_valid_positive_integer(prompt, lower_bound, upper_bound):
    """

    Invite l'utilisateur à entrer une valeur entière positive dans les bornes spécifiées jusqu'à ce qu'une saisie valide soit fournie
    
    Args:
    - prompt (str): le message affiché à l'utilisateur pour demander une saisie
    - lower_bound (int): la borne inférieure pour la saisie valide (inclus)
    - upper_bound (int): la borne supérieure pour la saisie valide (inclus)
    
    Returns:
    - value (int): la saisie de l'utilisateur sous forme d'entier positif valide dans les bornes spécifiées

    """

    is_good_input = False

    while not is_good_input:
        value = input(prompt)

        if not is_positive_integer(value):
            print("Ceci n'est pas un nombre positif...")
            continue

        # Safe to cast to int
        value = int(value)

        if not is_between(value, lower_bound, upper_bound):
            print(f"Choisissez une valeur entre {lower_bound} et {upper_bound}...")
            continue
        
        is_good_input = True

    return value

def is_positive_integer(value):
    """

    Vérifie si la valeur est un nombre positif

    """

    is_positive_int = False

    if value.isdigit():
        is_positive_int = True

    return is_positive_int

def create_folder_if_not_exists(folder_path):
    """

    Crée un dossier s'il n'existe pas

    Args :
        - folder_path (str) : le chemin du dossier à créer si il n'existe pas

    """

    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)

def empty_apprentice_list(apprentices):
    """
    
    Vérifie si la liste de apprentices est vide ou non

    Args :
        - apprentices (list[str]) : la liste de apprentices à vérifier
    
    """

    is_empty = False

    if apprentices == None:
        print("================== LISTE DES APPRENTIS DÉBUT ==================")
        print()
        print("Vous devez générer une liste d'apprentis (option 2) avant de lister les apprentis !")
        print()
        input("Appuyer sur un bouton pour continuer : ")

        is_empty = True

    return is_empty