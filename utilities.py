import os


def clear_screen():
    """Clear the console screen"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
