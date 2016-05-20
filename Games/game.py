from utilities import clear_screen


class Game:
    """Base Game class"""
    TITLE = "Base Game"
    player = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def start(self):
        """Start the game"""
        clear_screen()
        print("Welcome to the {0.TITLE}, {0.player.name}!".format(self))
        self.quit()

    def quit(self):
        """Quit game and return to menu"""
        clear_screen()
        print("Welcome back. I hope you had a great time playing {0.TITLE}. Would you like to play another game?".format(self))