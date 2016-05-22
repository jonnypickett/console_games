from Games.game import Game


class WordGuessingGame(Game):
    """Manage Word Guessing Game game play"""
    ID = 4
    TITLE = "Word Guessing Game"

    def start(self):
        self.stop()
