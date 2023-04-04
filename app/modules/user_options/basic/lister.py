import modules.common.utils as utils
import modules.common.config as config

def get_apprentice_per_block():
    """

    Demande le nombre d'apprentis par bloc à l'utilisateur

    Return :
        - apprentice_per_block (int) : nombre d'apprentis par bloc

    """

    utils.clear_terminal()

    print("================== LISTE DES APPRENTIS - DÉBUT ==================")
    print()

    min_apprentice_per_block = config.get_config_value("min_apprentice_per_block")
    max_apprentice_per_block = config.get_config_value("max_apprentice_per_block")
    prompt = "Entrer le nombre d'apprentis par bloc : "

    apprentice_per_block = utils.to_valid_positive_integer(prompt, min_apprentice_per_block, max_apprentice_per_block)

    return apprentice_per_block


def list_apprentices(apprentices):
    """

    Affiche les apprentis dans le terminal

    Args :
        - apprentices (list[str]) : liste des apprentis

    """

    utils.clear_terminal()

    if not utils.empty_apprentice_list(apprentices):
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
    max_block_idx = len(apprentice_blocks)

    while continue_listing and block_idx < max_block_idx:
        utils.clear_terminal()

        show_apprentice_block(block_idx, apprentice_blocks[block_idx], apprentice_per_block, max_block_idx)

        command = input("Continuer (enter to continue, r to restart, q to quit) : ")

        if command == "q":
            continue_listing = False
        elif command == "r":
            block_idx = 0
        else:
            block_idx += 1
            

def show_apprentice_block(block_idx, apprentice_block, apprentice_per_block, max_block_idx):
    """
    
    Affiche le bloc d'apprentis dans le terminal

    Args :
        - block_idx (int) : index du bloc
        - apprentice_block (list[str]) : liste des apprentis
        - apprentice_per_block (int) : nombre d'apprentis par bloc
        - max_block_idx (int) : nombre total de blocs
    
    """

    print(f"================== LISTE DES APPRENTIS EN COURS - BLOC {block_idx + 1}/{max_block_idx} ==================")
    print()

    for idx, apprentice in enumerate(apprentice_block, 1):
        apprentice_idx = apprentice_per_block * block_idx + idx
        print(f"{apprentice_idx:5} : {apprentice}")

    print()

