from modules.utils import *
from modules.config import *

def get_apprentice_per_block():
    """

    Demande le nombre d'apprentis par bloc à l'utilisateur

    Return :
        - apprentice_per_block (int) : nombre d'apprentis par bloc

    """

    clear_terminal()

    print("================== LISTE DES APPRENTIS - DÉBUT ==================")
    print()

    min_apprentice_per_block = get_config_value("min_apprentice_per_block")
    max_apprentice_per_block = get_config_value("max_apprentice_per_block")
    prompt = "Entrer le nombre d'apprentis par bloc : "

    apprentice_per_block = to_valid_positive_integer(prompt, min_apprentice_per_block, max_apprentice_per_block)

    return apprentice_per_block


def list_apprentices(apprentices):
    """

    Affiche les apprentis dans le terminal

    Args :
        - apprentices (list[str]) : liste des apprentis

    """

    clear_terminal()

    if not empty_apprentice_list(apprentices):
        apprentice_per_block = get_apprentice_per_block()
        show_apprentices_per_block(apprentice_per_block, apprentices)
        input("Appuyer sur un bouton pour revenir au menu principal : ")


def create_apprentices_block(apprentice_per_block, apprentices):
    """

    Crée les blocs d'apprentis

    Args :
        - apprentice_per_block (int) : nombre d'apprentis par bloc
        - apprentices (list[str]) : liste des apprentis

    Return :
        - apprentice_blocks (list(list[str])) : liste des blocs

    """

    apprentice_blocks = []

    for idx in range(0, len(apprentices), apprentice_per_block):
        apprentice_block = apprentices[idx:idx+apprentice_per_block]

        apprentice_blocks.append(apprentice_block)

    return apprentice_blocks


def show_apprentices_per_block(apprentice_per_block, apprentices):
    """

    Affiche tous les apprentis dans le terminal avec des inputs pour continuer ou revenir au menu principal

    Args :
        - apprentice_per_block (int) : nombre d'apprentis par bloc
        - apprentices (list[str]) : liste des apprentis

    """

    apprentice_blocks = create_apprentices_block(
        apprentice_per_block, apprentices)

    continue_listing = True
    block_idx = 0

    while continue_listing and block_idx < len(apprentice_blocks):
        clear_terminal()

        show_apprentice_block(block_idx, apprentice_blocks[block_idx], apprentice_per_block)

        command = input("Continuer (enter to continue, q to quit) : ")

        if command == "q":
            continue_listing = False

        block_idx += 1
            

def show_apprentice_block(block_idx, apprentice_block, apprentice_per_block):
    """
    
    Affiche le bloc d'apprentis dans le terminal

    Args :
        - block_idx (int) : index du bloc
        - apprentice_block (list[str]) : liste des apprentis
        - apprentice_per_block (int) : nombre d'apprentis par bloc
    
    """

    print(f"================== LISTE DES APPRENTIS EN COURS - BLOC {block_idx + 1} ==================")
    print()

    for idx, apprentice in enumerate(apprentice_block, 1):
        print(f"{apprentice_per_block*block_idx + idx} : {apprentice}")

    print()
