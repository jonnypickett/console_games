import utilities


class Game:
    """Base Game class"""
    TITLE = "Base Game"
    PLAY_AGAIN_RESPONSE = "Great! Have fun!"
    QUIT_RESPONSE = "No worries. Thanks for playing!"
    player = None
    playing = False

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def cleanup(self):
        """Handle game clean up."""

    def play_again_prompt(self):
        """Ask player if they'd like to play the game again.
        If yes, start the game again.
        If no, quit the game.
        """
        play_again = input("Do you want to play again? Y/n ")
        if play_again.lower() != 'n':
            print("{0.PLAY_AGAIN_RESPONSE}".format(self))
            self.cleanup()
            self.start()
        else:
            print("{0.QUIT_RESPONSE}".format(self))
            self.quit()

    def quit(self):
        """Quit game and return to menu"""
        utilities.clear_screen()
        print(
            "Welcome back. I hope you had a great time playing {0.TITLE}. Would you like to play another game?".format(
                self))

    def start(self):
        """Start the game"""
        self.playing = True

    def stop(self):
        """Stop the game"""
        self.playing = False
