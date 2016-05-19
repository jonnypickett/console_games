class Game:
    """Base Game class"""
    TITLE = "Base Game"
    def start(self):
        print("You are starting the {}".format(self.TITLE))