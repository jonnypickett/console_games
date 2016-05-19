import os


def clear():
    """Clear the console screen"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
