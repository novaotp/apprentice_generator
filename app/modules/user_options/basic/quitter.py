import modules.common.utils as utils


def quit_program():
    """

    Quitte le programme avec un message de fin

    """

    utils.clear_terminal()

    print("================== FIN ==================")
    print()
    print("Merci d'avoir utilisé le programme.")
    print()
    input("Appuyer sur un bouton pour quitter : ")