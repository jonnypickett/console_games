import random
from Games.MonsterAttack.Characters.combat import Combat


class Monster(Combat):
    COLORS = ['yellow', 'red', 'blue', 'green']
    max_experience = 1
    max_hit_points = 1
    min_experience = 1
    min_hit_points = 1
    sound = 'roar'
    weapon = 'sword'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(self.COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hit_points,
                                              self.experience)

    def battlecry(self):
        return self.sound.upper()
