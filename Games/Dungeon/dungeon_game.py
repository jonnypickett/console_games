from Games.game import Game
import logging
import random
import utilities


class DungeonGame(Game):
    """Manage Dungeon Game game play"""
    ID = 1
    TITLE = "Dungeon Game"
    LEFT_COMMAND = 'LEFT'
    RIGHT_COMMAND = 'RIGHT'
    UP_COMMAND = 'UP'
    DOWN_COMMAND = 'DOWN'
    QUIT_COMMAND = 'QUIT'
    CELLS = [(0, 0), (0, 1), (0, 2), (0, 3),
             (1, 0), (1, 1), (1, 2), (1, 3),
             (2, 0), (2, 1), (2, 2), (2, 3),
             (3, 0), (3, 1), (3, 2), (3, 3)]
    PLAY_AGAIN_RESPONSE = "Fantastic. Good luck! Don't get eaten!"
    QUIT_RESPONSE = "Too scared, eh? No problem. Thanks for playing! Come back once you've gained more courage!"

    def draw_map(self):
        """Draw the map with a, 'X' where the player is currently."""
        print(' _ _ _ _ ')
        tile = '|{}'

        for idx, cell in enumerate(self.CELLS):
            if idx in [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14]:
                if cell == self.player.location:
                    print(tile.format('X'), end='')
                else:
                    print(tile.format('_'), end='')
            else:
                if cell == self.player.location:
                    print(tile.format('X|'))
                else:
                    print(tile.format('_|'))

    def get_moves(self):
        """Get the player's available moves based on their current location"""
        moves = [self.LEFT_COMMAND, self.RIGHT_COMMAND, self.UP_COMMAND, self.DOWN_COMMAND]

        x, y = self.player.location

        if x == 0:
            moves.remove(self.UP_COMMAND)
        elif x == 3:
            moves.remove(self.DOWN_COMMAND)

        if y == 0:
            moves.remove(self.LEFT_COMMAND)
        elif y == 3:
            moves.remove(self.RIGHT_COMMAND)

        return moves

    def move_player(self, move):
        """Move player UP, DOWN, LEFT, or RIGHT based on their choice."""
        x, y = self.player.location

        if move == self.LEFT_COMMAND:
            y -= 1
        elif move == self.RIGHT_COMMAND:
            y += 1
        elif move == self.UP_COMMAND:
            x -= 1
        elif move == self.DOWN_COMMAND:
            x += 1

        self.player.location = x, y

    def set_locations(self):
        """Set the locations of the player, door, and monster."""
        self.monster = random.choice(self.CELLS)
        self.door = random.choice(self.CELLS)
        self.player.location = random.choice(self.CELLS)

        if self.monster == self.door or self.monster == self.player.location or self.door == self.player:
            return self.set_locations()

    def start(self):
        """Begin the game."""
        super().start()
        self.set_locations()
        logging.info("monster: {}; door: {}; player: {}".format(self.monster, self.door, self.player))
        utilities.clear_screen()
        print("Welcome to the dungeon! There's a monster in here with you. Find the door before you get eaten!")

        while self.playing:
            moves = self.get_moves()

            print("You're currently in room {}".format(self.player.location))
            self.draw_map()
            print("You can move {}".format(moves))
            print("Enter QUIT to quit")

            move = input("> ")
            move = move.upper()

            if move == self.QUIT_COMMAND:
                break

            if move in moves:
                self.move_player(move)
            else:
                print("You can't go that way! There's a wall there!")
                continue

            if self.player.location == self.door:
                print("You escaped! Great job!")
                self.stop()
            elif self.player.location == self.monster:
                print("You are a tasty treat for the monster. You lose!")
                self.stop()

        self.play_again_prompt()
