from Characters.character import Character
from Characters.dragon import Dragon
from Games.game import Game
from Characters.goblin import Goblin
from Characters.troll import Troll
import utilities


class MonsterAttackGame(Game):
    """Manage Monster Attack Game game play"""
    ID = 2
    TITLE = "Monster Attack Game"
    ATTACK_COMMAND = 'a'
    QUIT_COMMAND = 'q'
    REST_COMMAND = 'r'

    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.character.experience += self.monster.experience
            print("You killed {}!".format(self.monster))
            self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        """Handle the monster turn."""
        if self.monster.attack():
            print("{} is attacking!".format(self.monster))

            if input("Dodge? Y/N ").lower() == 'y':
                if self.player.character.dodge():
                    print("You dodged the attack!")
                else:
                    print("You got hit anyway!")
                    self.player.character.hit(1)
            else:
                print("{} hit you for 1 point!".format(self.monster))
                self.player.character.hit(1)
        else:
            print("{} isn't attacking this turn.".format(self.monster))

    def player_turn(self):
        """Handle the player turn."""
        player_choice = input("[A]ttack, [R]est, [Q]uit? ").lower()

        if player_choice == self.ATTACK_COMMAND:
            print("You're attacking {}!".format(self.monster))

            if self.player.character.attack():
                if self.monster.dodge():
                    print("{} dodged your attack!".format(self.monster))
                else:
                    if self.player.character.leveled_up():
                        self.monster.hit(2)
                    else:
                        self.monster.hit(1)

                    print("You hit {} with your {}!".format(self.monster, self.player.character.weapon))
            else:
                print("You missed!")
        elif player_choice == self.REST_COMMAND:
            self.player.character.rest()
        elif player_choice == self.QUIT_COMMAND:
            self.stop()
        else:
            self.player_turn()

    def setup(self):
        """Set up the game character and monsters."""
        self.player.character = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()

    def start(self):
        """Begin the game."""
        super(MonsterAttackGame, self).start()
        self.setup()
        print(self.player.character)

        while self.playing and self.player.character.hit_points and (self.monster or self.monsters):
            utilities.hard_break()
            print(self.player.character)
            self.monster_turn()
            print('-' * 20)
            self.player_turn()
            self.cleanup()
            utilities.hard_break()

        if self.player.character.hit_points:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")

        self.play_again_prompt()
