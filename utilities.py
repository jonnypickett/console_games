import os


def clear_screen():
    """Clear the console screen"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def hard_break(length=20):
    """Print out a hard break line to the console of varying length
    depending on an argument. Defaults to a length of 20."""
    try:
        length = int(length)
    except ValueError:
        length = 20
    print('\n' + '=' * length)