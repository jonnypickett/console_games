class Game:
    """Base Game class"""
    TITLE = "Base Game"

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def start(self):
        """Start the game"""
        print("Welcome to the {0.TITLE}, {0.player.name}!".format(self))