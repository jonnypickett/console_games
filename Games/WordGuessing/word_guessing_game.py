import random

from Games.game import Game
import utilities


class WordGuessingGame(Game):
    """Manage Word Guessing Game game play"""
    ID = 4
    TITLE = "Word Guessing Game"
    DIFFICULTIES = {
        'e': {
            'bad_guesses_allowed': 5,
            'words': [
                'apple',
                'baby',
                'banana',
                'book',
                'cake',
                'cat',
                'dog',
                'good',
                'going',
                'green',
                'hair',
                'like',
                'love',
                'red',
                'stop',
            ]
        },
        'm': {
            'bad_guesses_allowed': 4,
            'words': [
                'gross',
                'happy',
                'house',
                'monkey',
            ]
        },
        'h': {
            'bad_guesses_allowed': 3,
            'words': [
                'baseball',
                'basketball',
                'hamburger',
                'president',
            ]
        },
    }
    game_difficulty = None
    bad_guesses = []
    good_guesses = []
    bad_guesses_allowed = None
    secret_word = None

    def cleanup(self):
        """Prepare for a new game."""
        self.bad_guesses = []
        self.good_guesses = []
        self.secret_word = None
        self.bad_guesses_allowed = None

    def draw(self):
        """Draw out the current status of the game.
        Show the bad guesses and the good guesses
        grouped together as the secret word.
        """
        print("Strikes: {}/{}".format(len(self.bad_guesses), self.bad_guesses_allowed))
        print("")

        for letter in self.bad_guesses:
            print(letter, end=" ")
        print("\n\n")

        for letter in self.secret_word:
            if letter in self.good_guesses:
                print(letter, end='')
            else:
                print('_', end='')

        print("")

    def get_guess(self):
        """Get and return player guess."""
        while True:
            guess = input("Guess a letter: ").lower()

            if len(guess) == 0:
                print("You didn't guess anything!")
            elif len(guess) > 1:
                print("You can only guess one letter at a time!")
            elif guess in self.bad_guesses or guess in self.good_guesses:
                print("You've already guessed that letter!")
            elif not guess.isalpha():
                print("You can only guess letters!")
            else:
                return guess

    def print_secret_word(self):
        """Print out the secret word."""
        print("The secret word was {0.secret_word}".format(self))

    def setup(self):
        """Set up the game."""
        self.set_difficulty()
        self.bad_guesses_allowed = self.DIFFICULTIES[self.game_difficulty]['bad_guesses_allowed']
        self.secret_word = random.choice(self.DIFFICULTIES[self.game_difficulty]['words'])

    def start(self):
        """Begin the game."""
        super().start()
        utilities.clear_screen()
        self.show_welcome()
        self.setup()

        while self.playing:
            utilities.clear_screen()
            print("I'm thinking of a word. Can you guess what it is letter by letter?")
            print("You can guess wrong only {0.bad_guesses_allowed} times. Good luck!".format(self))
            self.draw()
            guess = self.get_guess()

            if guess in self.secret_word:
                self.good_guesses.append(guess)
                found = True
                for letter in self.secret_word:
                    if letter not in self.good_guesses:
                        found = False
                if found:
                    print("You win!")
                    self.print_secret_word()
                    self.playing = False

            else:
                self.bad_guesses.append(guess)
                if len(self.bad_guesses) == self.bad_guesses_allowed:
                    self.draw()
                    print("You lost!")
                    self.print_secret_word()
                    self.playing = False

        self.play_again_prompt()
