from Games.game import Game
import random
import utilities


class NumberGuessingGame(Game):
    """Manage Number Guessing Game game play"""
    ID = 3
    TITLE = "Number Guessing Game"
    DIFFICULTIES = {
        'e': {'guesses_allowed': 8, 'max_number': 10, 'min_number': 1},
        'm': {'guesses_allowed': 5, 'max_number': 20, 'min_number': 1},
        'h': {'guesses_allowed': 2, 'max_number': 50, 'min_number': 1},
    }
    game_difficulty = None
    guess = None
    guesses = []
    guesses_allowed = None
    max_number = None
    min_number = None
    secret_number = None

    def cleanup(self):
        """Clean up the game to prepare for another."""
        self.guesses = []

    def get_guess(self):
        """Get player guess"""
        self.guess = input("Guess a number between {0.min_number} and {0.max_number}: ".format(self))

    def set_difficulty(self):
        """Set the game difficulty"""
        difficulty = input("Would you like this to be [E]asy, [M]edium, or [H]ard? ").lower()

        if not difficulty in self.DIFFICULTIES:
            print("I didn't quite get that. Let's try again.")
            self.set_difficulty()

        self.game_difficulty = difficulty

    def setup(self):
        """Set up the game"""
        self.set_difficulty()
        self.guesses_allowed = self.DIFFICULTIES[self.game_difficulty]['guesses_allowed']
        self.max_number = self.DIFFICULTIES[self.game_difficulty]['max_number']
        self.min_number = self.DIFFICULTIES[self.game_difficulty]['min_number']
        self.secret_number = random.randint(self.min_number, self.max_number)

    def start(self):
        """Start and manage the game."""
        super(NumberGuessingGame, self).start()
        utilities.clear_screen()
        print("Welcome to the {0.TITLE}!".format(self))
        self.setup()
        print("I'm thinking of a number between {0.min_number} and {0.max_number}.".format(self))
        print("Can you guess what it is with {0.guesses_allowed} guesses?".format(self))
        print("Let's see.")

        while self.playing and len(self.guesses) < self.guesses_allowed:
            self.get_guess()
            try:
                self.guess = int(self.guess)
            except ValueError:
                print("{} isn't a number!".format(self.guess))
            else:
                # add guess to guesses
                self.guesses.append(self.guess)

                # compare guess to secret number
                if self.guess == self.secret_number:
                    print("Wow! You got it! My number was {}. You are pretty amazing.".format(self.secret_number))
                    break
                # print hit/miss
                elif self.guess < self.secret_number:
                    print("Nope. Think higher.")
                else:
                    print("Nope. Lower.")


        else:
            print("I win! You didn't guess it! My number was {}. Try again if you think you can beat me.".format(
                self.secret_number))

        self.play_again_prompt()
