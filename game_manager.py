from utilities import clear
from dungeon_game import DungeonGame
from monster_attack_game import MonsterAttackGame
from number_guessing_game import NumberGuessingGame
from player import Player
from word_guessing_game import WordGuessingGame


class GameManager:
    """A class to manage player game choices"""
    available_games = {}
    dungeon_game = None
    monster_attack_game = None
    number_guessing_game = None
    word_guessing_game = None

    def __init__(self):
        """Set up games and start main function"""
        self.setup()
        self.main()

    def choose_game(self):
        """Show games menu then calls get_choice"""
        print("Which game would you like to play today?")
        self.show_game_menu()
        return self.get_choice()

    def get_choice(self):
        """Get game id choice from player.
        If choice is not an int, ask player to choose again.
        If choice is not an available game id, ask player to choose again.
        """
        try:
            choice = int(input("Enter the number for the game you'd like to play: "))
        except ValueError:
            print("You must enter a number.")
            return self.get_choice()
        else:
            if not choice in self.available_games:
                print("That's not one of the choices. Please choose one of the available games.")
                return self.get_choice()
            return choice

    def main(self):
        """Welcomes player to Console Games then calls choose_game"""
        clear()
        self.show_welcome()
        self.show_help()
        choice = self.choose_game()
        self.start_game(choice)

    def setup(self):
        """Set up game play"""
        self.player = Player()

        self.dungeon_game = DungeonGame(player=self.player)
        self.monster_attack_game = MonsterAttackGame(player=self.player)
        self.number_guessing_game = NumberGuessingGame(player=self.player)
        self.word_guessing_game = WordGuessingGame(player=self.player)
        self.available_games.update(
            {self.dungeon_game.ID: self.dungeon_game.TITLE,
             self.monster_attack_game.ID: self.monster_attack_game.TITLE,
             self.number_guessing_game.ID: self.number_guessing_game.TITLE,
             self.word_guessing_game.ID: self.word_guessing_game.TITLE})

    def show_game_menu(self):
        """Prints out game menu from available games"""
        for id, game in self.available_games.items():
            print("{}. {}".format(id, game))

    def show_help(self):
        """Show help menu"""
        print("Help menu stuff.")

    def show_welcome(self):
        """Display welcome message"""
        print("Welcome to Console Games, {}!".format(self.player.name))
        print("""
        There are a few games to choose from,
        and we're always adding more games,
        so remember to come back and play regularly!
        """)

    def start_game(self, choice):
        """Start game of choice. If player choice isn't in available game choices,
        have player choose again
        """
        if self.dungeon_game.ID == choice:
            self.dungeon_game.start()
        elif self.monster_attack_game.ID == choice:
            self.monster_attack_game.start()
        elif self.number_guessing_game.ID == choice:
            self.number_guessing_game.start()
        elif self.word_guessing_game.ID == choice:
            self.word_guessing_game.start()
        else:
            print("It seems like there was a problem finding the game you selected. Let's try again.")
            self.choose_game()
